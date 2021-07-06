from accounts.models import User
from accounts.serializers import UserSerializer
from rest_framework.response import Response
from django.http import JsonResponse
from .serializers import StatusSerializer
import jwt
import math
from django.db.models import Q
from rest_framework.views import APIView
from .models import *
# Create your views here.

def verify_token(request):
    if not (request.headers['Authorization'] == "null"):
            token = request.headers['Authorization']
    # if not (request.COOKIES.get('token') == "null"):
    #     token = request.COOKIES.get('token')
    #     print(token)
    else:
        context = {
            "success":False,
            "error":"Not Authorized",
            "message":"",
            }
        payload = JsonResponse(context)
    try:
        payload = jwt.decode(token, 'secret', algorithm=['HS256'])
    except :
        context = {
                "success":False,
                "error":"UnAuthenticated",
                "message":"",
            }
        payload =  JsonResponse(context)
    print(payload)
    return payload

class AddStatus(APIView):
    serializer_class = StatusSerializer
    def post(self, request):
        payload = verify_token(request)
        try:
            user = User.objects.filter(id=payload['id']).first()
        except:
            return payload
        if user.status_add and user.is_enabled:
            serializer = StatusSerializer(data=request.data)
            if not serializer.is_valid():
                #print(serializer.errors)
                return Response({
                "success":False,
                "error":'Status already exists',
                "message":"",
                "data": user.email
                })

            serializer.save()
            return Response({
                "success":True,
                "error":"",
                "message":"Status added successfully",
                "data":serializer.data
                })
        else:
            return Response({
                "success":False,
                "error":"Not authorized to Add status",
                "message":"",
                "data":{
                    "email":user.email
                }
            })
        
    
class EditStatus(APIView):
    serializer_class = StatusSerializer
    def put(self, request, status):
        
        payload = verify_token(request)
        try:
            user = User.objects.filter(id=payload['id']).first()
        except:
            return payload
        if user.status_edit and user.is_enabled:
            try:
                requeststatus = Status.objects.get(status=status)
            except Status.DoesNotExist:
                return Response({
                    'success':False,
                    'error':'Status does not exists',
                    'message':''})
            serializer = StatusSerializer(requeststatus,data=request.data)
            if not serializer.is_valid():
                return Response({
                    'success':False,
                    'error':'Some error occured',
                    'message':''})
            serializer.save()
            return Response({
                'success':True,
                'error':'',
                'message':'Status Edited successfully'})
        return Response({
            'success':False,
            'error':'You are not allowed to edit status',
            'message':''})            


class GetStatus(APIView):
    def get(self, request):
        payload = verify_token(request)
        #print(payload)
        try:
            user = User.objects.filter(id=payload['id']).first()
        except:
            return payload
        if(user.is_enabled):
            search = request.GET.get('search')
            page = int(request.GET.get('currentPage', 1))
            per_page = int(request.GET.get('pageSize', 8))
            queryset = Status.objects.all()
            if search:
                queryset = queryset.filter(Q(status__icontains=search))
            total = queryset.count()
            start = (page - 1) * per_page
            end = page * per_page
            serializer = StatusSerializer(queryset[start:end], many=True)
            return Response({
                'success': True,
                'error': "",
                'data': serializer.data,
                'totalItems': total,
                'currentPage': page,
                'totalPage': math.ceil(total / per_page)
            })             