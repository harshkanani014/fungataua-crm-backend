from django.urls import path
from .views import *


urlpatterns = [
    path('get-card-info', GetDasbaordCardsInfo.as_view()),

    path('get-client-visits', ClientChart.as_view()),

    path('download-client-report', DownloadClientReport, name="download_report"),

    path('download-client-service-report', DownloadClientServiceReport, name="client_service_report"),

    path('download-client-service-report/<int:id>', DownloadEachClientServiceReport, name="client_service_report"),

    path('download-client-service-report-datewise', DownloadClientServiceReportDatewise, name="client_service_report_datewise"),

    path('get-referral-pie-chart', ReferralPieChart.as_view())
]