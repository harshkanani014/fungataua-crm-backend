from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from accounts.models import User
from rest_framework.response import Response
from django.http import JsonResponse
import math
from django.db.models import Q
from rest_framework.views import APIView
from client.models import *
from client.views import verify_token
import io
from datetime import timedelta
from django.utils import timezone
import tablib


# Dash-board cards api
class GetDasbaordCardsInfo(APIView):

    def get(self, request):

        payload = verify_token(request)

        try:
            user = User.objects.filter(id=payload['id']).first()
        except:
            return payload
        
        no_of_clients = Client.objects.all().count()                         # This is number of client (served clients + present clients)
        no_of_services = Services.objects.filter(is_enabled=True).count()    # This is number of enabled services
        no_of_visits = client_service_records.objects.all().count()
        no_of_category = Category.objects.all().count()

        return Response({
            'success': True,
            'error': "",
            'data': [
                { 
                "title": "dashboards.no-of-clients", 
                "icon":"iconsminds-business-mens", 
                "value": no_of_clients },
                {
                "title": "dashboards.no-of-services",
                 "icon": "iconsminds-consulting",
                 "value": no_of_services,
                },
                {
                "title": "dashboards.no-of-visits",
                "icon": "simple-icon-calendar",
                "value": no_of_visits,
                },
                {
                "title": "dashboards.no-of-category",
                "icon": "simple-icon-drawer",
                "value": no_of_category,
                },
               ]
        }) 





# API for plotting graph on Dashboard
class ClientChart(APIView):

    def get(self, request):

        some_day_last_week = timezone.now().date() - timedelta(days=7)    # Taking records of past 7 days
        today = timezone.now().date()
        all_data = client_service_records.objects.filter(date_of_visit__gte=some_day_last_week, date_of_visit__lt=today)
        d =  {}

        for i in range(7):
            temp = timezone.now().date() - timedelta(days=7) + timedelta(days=i)
            d.update({str(temp):0})
        
        for j in all_data:
            d[str(j.date_of_visit)] += 1
       
        lables = []
        dataset = []
        for i in d:
            lables.append(i)
            dataset.append(d[i])


        return Response({
                'success': True,
                'error': "",
                'data': {
                    "labels":lables,
                    "data": dataset,

                }
            })


# API for generating Pie Chart
class ReferralPieChart(APIView):
    def get(self, request):
        all_services = client_service_records.objects.all()
        d=dict()
        for i in all_services:
            if (i.services.service_name not in d):
                d[i.services.service_name]=1
            else:
                d[i.services.service_name]+=1
        lables=[]
        dataset=[]
        for i in d:
            lables.append(i)
            dataset.append(d[i])
        return Response({
                'success': True,
                'error': "",
                'data': {
                    "labels":lables,
                    "data": dataset,

                }
            })

# API for downloading client report
def DownloadClientReport(request):


            headers = ('First Name', 'Last Name', 'E-mail', 'Date of Birth', 'Phone Number', "Gender", "Address", "State", "City")
            data = []
            data = tablib.Dataset(*data, headers=headers)
            clients = Client.objects.all()

            for i in clients:
                data.append((i.first_name, i.last_name, i.email, i.date_of_birth, i.phone_number, i.gender, i.address, i.state, i.city))

            response = HttpResponse(data.csv, content_type='application/vnd.ms-excel;charset=utf-8')
            response['Content-Disposition'] = "attachment; filename=client_report_export.csv"

            return response
        
 

# API for downloading service report for all clients
def DownloadClientServiceReportDatewise(request):

        from_date= request.GET.get('from')
        to_date = request.GET.get('to')
        headers = ('Date of Visit', 'Added By', 'E-mail', 'Services', 'Category', 'Subcategory', 'Status', 'Remarks')
        data = []
        data = tablib.Dataset(*data, headers=headers)
        client_records = client_service_records.objects.filter(date_of_visit__gte = from_date, date_of_visit__lte = to_date )

        for i in client_records:
            data.append((i.date_of_visit, i.added_by, i.email, i.services, i.category, i.subcategory, i.status, i.remarks))
        
        response = HttpResponse(data.csv, content_type='application/vnd.ms-excel;charset=utf-8')
        response['Content-Disposition'] = "attachment; filename=client_service_report.csv"

        return response
 


# API for downloading service report for all clients
def DownloadClientServiceReport(request):

        headers = ('Date of Visit', 'Added By', 'E-mail', 'Services', 'Category', 'Subcategory', 'Status', 'Remarks')
        data = []
        data = tablib.Dataset(*data, headers=headers)
        client_records = client_service_records.objects.all()

        for i in client_records:
            data.append((i.date_of_visit, i.added_by, i.email, i.services, i.category, i.subcategory, i.status, i.remarks))
        
        response = HttpResponse(data.csv, content_type='application/vnd.ms-excel;charset=utf-8')
        response['Content-Disposition'] = "attachment; filename=client_service_report.csv"

        return response



# Function to download service records for EACH client
def DownloadEachClientServiceReport(request, id):

        headers = ('Date of Visit', 'Added By', 'E-mail', 'Services', 'Category', 'Subcategory', 'Status', 'Remarks')
        data = []
        data = tablib.Dataset(*data, headers=headers)
        client_records = client_service_records.objects.filter(email_id=id)
    
        for i in client_records:
            data.append((i.date_of_visit, i.added_by, i.email, i.services, i.category, i.subcategory, i.status, i.remarks))
        
        # Return excel file as response to client side
        response = HttpResponse(data.csv, content_type='application/vnd.ms-excel;charset=utf-8')
        response['Content-Disposition'] = "attachment; filename=each_client_service_report_export.csv"
        return response





