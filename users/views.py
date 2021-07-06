from django.shortcuts import render
from accounts.models import User
from accounts.serializers import UserSerializer
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.views import APIView
import jwt
import math
from django.db.models import Q
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
        
    if not token:
        context = {
                "success":False,
                "error":"UnAuthenticated",
                "message":"",
            }
        payload =  JsonResponse(context)
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

class AddUserView(APIView):
    def post(self, request):
    #     payload = verify_token(request)
    #     print(payload)
    #     try:
    #         user = User.objects.filter(id=payload['id']).first()
    #     except:
    #         return payload
    #     if user.is_superadmin:            
            serializer = UserSerializer(data=request.data)
            if not serializer.is_valid():
                #print(serializer.errors)
                return Response({
                "success":False,
                "error":'user with this email already exists',
                "message":"",
                # "data": user.email
                })

            serializer.save()
            return Response({
                "success":True,
                "error":"",
                "message":"User added successfully",
                "data":serializer.data
                })
        # else:
        #     return Response({
        #         "success":False,
        #         "error":"Not authorized to access this page",
        #         "message":"",
        #         "data":{
        #             "email":user.email
        #         }
        #     })


class EditUser(APIView):
    # authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    serializer_class = UserSerializer
    def put(self, request,email):
        payload = verify_token(request)
        try:
            user = User.objects.filter(id=payload['id']).first()
        except:
            return payload
        if email==user.email:
            return Response({
                'success':False,
                'error':'User cannot change his own mail',
                'message':''
            })
        if user.is_superadmin:
            try:
                print(email)
                requestuser = User.objects.get(email=email)
                
            except User.DoesNotExist:
                return Response({
                    'success':False,
                    'error':'User does not exists',
                    'message':''})
            serializer = UserSerializer(requestuser,data=request.data)
            if not serializer.is_valid():
                return Response({
                    'success':False,
                    'error':serializer.errors,
                    'message':''})
            serializer.save()
            return Response({
                'success':True,
                'error':'',
                'message':'User Edited successfully'})
        return Response({
            'success':False,
            'error':'Subadmins are not allowed',
            'message':''})


class GetUser(APIView):
    # queryset = User.objects.all()
    # serializer_class = UserSerializerWithoutPass
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['username', 'email','phone_number']
    # permission_classes = [IsAuthenticated, ]
    
    def get(self, request):
        payload = verify_token(request)
        #print(payload)
        try:
            user = User.objects.filter(id=payload['id']).first()
        except:
            return payload
        if(user.is_superadmin):
            search = request.GET.get('search')
            orderBy = request.GET.get('orderBy')
            page = int(request.GET.get('currentPage', 1))
            per_page = int(request.GET.get('pageSize', 8))
            queryset = User.objects.all().exclude(is_superuser=True)
            if search:
                queryset = queryset.filter(Q(name__icontains=search) | Q(email__icontains=search) |  Q(phone_number__icontains=search)).exclude(is_superuser=True)
            if orderBy == 'superadmin':
                queryset = queryset.order_by('is_superadmin').reverse()
            elif orderBy == 'admin':
                queryset = queryset.order_by('is_superadmin')
            total = queryset.count()
            start = (page - 1) * per_page
            end = page * per_page

            serializer = UserSerializer(queryset[start:end], many=True)
            return Response({
                'success': True,
                'error': "",
                'data': serializer.data,
                'totalItems': total,
                'currentPage': page,
                'totalPage': math.ceil(total / per_page)
            }) 
        else:
            context = {
                "success":False,
                "error":"Only superadmins are allowed",
                "message":"",
                "data":
                {
                    "email":user.email
                }
            }
            return JsonResponse(context)  