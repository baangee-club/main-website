import os
import time
import json
import logging
import hashlib
from reprlib import repr
import requests
from lxml import etree

logger = logging.getLogger("app.epos.helper")
FPS_ID = 123300100909
DIST_CODE = 233


def get_temp_file(url, data):
    md5 = hashlib.md5()
    md5.update((url + json.dumps(data, sort_keys=True)).encode())
    return md5.hexdigest()


def fetch_content(url, data, fresh=False):
    filename = os.path.join("data", get_temp_file(url, data))
    logger.info(f"temp file {filename}")
    content = ""
    if fresh or not os.path.exists(filename):
        logger.info(f"fetching {url} from network")
        try:
            res = requests.post(url, data=data)
        except Exception as ex:
            logger.exception(ex)
        else:
            content = res.text
            with open(filename, "w") as f:
                f.write(content)
    if os.path.exists(filename):
        with open(filename, "r") as f:
            content = f.read()
    return content


def get_sales_data(month, year, fresh=False):
    data = dict(dist_code=DIST_CODE, fps_id=FPS_ID, month=month, year=year)
    sales_html = fetch_content(
        "http://epos.bihar.gov.in/fps_transactions.action", data, fresh
    )
    if not sales_html:
        raise Exception("No data received ")
    html = etree.HTML(sales_html)
    table = html.findall("body/table")
    if table is None:
        raise Exception("Table tag not found in HTML response")
    table = table[0]

    def get_header(table):
        rows = list(table.findall("thead/tr"))
        # 0 has a table title
        # 1 has headers but with some columnspan
        # 2 has columns spanned headers
        headers = []
        for col in rows[1].findall("th"):
            text = col.text and col.text.strip()
            colspan = col.get("colspan")
            if colspan:
                spanned_cols = list(rows[2].findall("th"))
                for scol in spanned_cols:
                    headers.append(text + "(" + scol.text + ")")
            else:
                headers.append(text)
        return headers

    def get_content(headers, table):
        rows = table.findall("tbody/tr")
        content = [dict(zip(headers, [col.text for col in row])) for row in rows[1:]]
        return content

    headers = get_header(table)
    content = get_content(headers, table)
    return content


def get_rc_details(rc_number, month, year, fresh=False):
    data = dict(src_no=rc_number, month=5, year=2020)
    url = "http://epos.bihar.gov.in/SRC_Trans_Details.jsp"
    rc_html = fetch_content(url, data, fresh)
    if not rc_html:
        raise Exception("No data received ")
    html = etree.HTML(rc_html)
    table = html.findall("body/table")
    if table is None:
        raise Exception("No table tag not found in HTML response")
    first_table = table[0]
    trs = list(first_table.findall("tr"))
    if not trs:
        raise Exception("No tr in table")

    headers = [th.text for th in trs[2].findall("th")]
    content = [
        dict(zip(headers, [td.text for td in tr.findall("td")])) for tr in trs[3:]
    ]
    return content


def fetch_data(month, year, fresh=False):
    logger.info("fetching sales data")
    sales_data = get_sales_data(month, year, fresh)

    logger.info("fetching rc details")
    rc_details = {}
    for sd in sales_data[:10]:
        try:
            rc_num = sd.get("RC No")
            rc_detail = get_rc_details(rc_num, month, year, fresh)
            rc_details[rc_num] = rc_detail
        except Exception as ex:
            logger.error(str(ex))
    return sales_data, rc_details


class SRC_COL:
    SL_NO = "Sl No"
    RC_NO = "RC No"
    SCHEME = "Scheme"
    AVAIL_TYPE = "Avail Type"
    RECEIPT_NO = "Receipt No"
    DATE_TIME = "Date Time"
    QTY_IN_KGS_WHEAT = "Qty in Kgs(Wheat)"
    QTY_IN_KGS_RICE = "Qty in Kgs(Rice)"
    AMOUNT = "Amount"
    PORTABILITY = "Portability"
    DRAWN = "Drawn"
    AUTH_TRANS_TIME = "Auth Trans Time"


class DST_COL:
    SR_NO = "Sr No"
    NAME = "Name"
    SCHEME = "Scheme"
    RC_CARD_NUMBER = "RC Card Number"
    MEMBERS = "member"
    PHH_WHEAT = "PHH Wheat"
    PHH_RICE = "PHH Rice"
    AAY_WHEAT = "AAY Wheat"
    AAY_RICE = "AAY Rice"
    TOTAL_QUANTITY = "Total Quantity"
    PMGKAY_RICE = "PMGKAY Rice"
    PMGKAY_DAAL = "PMGKAY Daal"


def transform_to_sales(fetch_sales_data, rc_details):
    rows = []
    column_mapping = [
        (SRC_COL.SL_NO, DST_COL.SR_NO),
        # (SRC_COL. ,DST_COL.NAME)
        (SRC_COL.SCHEME, DST_COL.SCHEME),
        (SRC_COL.RC_NO, DST_COL.RC_CARD_NUMBER),
        # (SRC_COL. ,DST_COL.MEMBERS)
        # (SRC_COL. ,DST_COL.PHH_WHEAT)
        # (SRC_COL. ,DST_COL.PHH_RICE)
        # (SRC_COL. ,DST_COL.AAY_WHEAT)
        # (SRC_COL. ,DST_COL.AAY_RICE)
        # (SRC_COL. ,DST_COL.TOTAL_QUANTITY)
        # (SRC_COL. ,DST_COL.PMGKAY_RICE)
        # (SRC_COL. ,DST_COL.PMGKAY_DAAL)
    ]
    for sale in fetch_sales_data:
        row = {}
        for col_from, col_to in column_mapping:
            row[col_to] = col_from

        rc_number = sale.get(SRC_COL.SL_NO)
        rc_details = rc_details.get(rc_number)
        row[DST_COL.NAME] = next(rc_details, {}).get("Member")
        row[DST_COL.MEMBERS] = len(rc_details)
        wheat = sale.get(SRC_COL.QTY_IN_KGS_WHEAT)
        rice = sale.get(SRC_COL.QTY_IN_KGS_RICE)
        if row.get(DST_COL.RC_CARD_NUMBER) == "PHH":
            row[DST_COL.PHH_WHEAT] = wheat
            row[DST_COL.PHH_RICE] = rice
        else:
            row[DST_COL.AAY_WHEAT] = wheat
            row[DST_COL.AAY_RICE] = rice
        rows.append(row)
    return rows
