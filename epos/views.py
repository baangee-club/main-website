from django.shortcuts import render
import logging
from .helper import fetch_data

logger = logging.getLogger("app.epos")


def index(request):
    return render(request, "epos/index.html")


def report(request, scheme, type, month, year):
    """
    scheme: PPH/AAY
    type: stock/sales
    month: month 1-12
    year: year in yyyy format
    """
    fresh = request.GET.get("fresh", False)
    sales_data, rc_details = fetch_data(month, year, fresh)
    return render(
        request,
        "epos/report.html",
        {"sales_data": sales_data, "rc_details": rc_details},
    )
