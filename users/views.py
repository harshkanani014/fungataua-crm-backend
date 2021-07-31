from accounts.models import User
from accounts.serializers import UserSerializer
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.views import APIView
import jwt
import math
from django.db.models import Q


# This function verify token 
def verify_token(request):

    try:
        if not (request.headers['Authorization'] == "null"):
            token = request.headers['Authorization']
    except:
        if not (request.COOKIES.get('token') == "null"):
            token = request.COOKIES.get('token')

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
    return payload


# function getting error from serializer
def get_error(serializerErr):

    err = ''
    for i in serializerErr:
        err = serializerErr[i][0]
        break    
    return err


# API to add user
# request : POST
class AddUserView(APIView):
    def post(self, request):
        # Verify token i.e checks user is authenticated or not
        payload = verify_token(request)
        try:
            user = User.objects.filter(id=payload['id']).first()
        except:
            return payload
        
        #checks user is superadmin or not
        if user.is_superadmin:            
            serializer = UserSerializer(data=request.data)
            if not serializer.is_valid():
                return Response({
                "success":False,
                "error":get_error(serializer.errors),
                "message":"",
                "data": user.email
                })

            serializer.save()
            return Response({
                "success":True,
                "error":"",
                "message":"User added successfully",
                "data":serializer.data
                })

        else:
            return Response({
                "success":False,
                "error":"Not authorized to access this page",
                "message":"",
                "data":{
                    "email":user.email
                }
            })


# Function to Edit User Details
# request : PUT
class EditUser(APIView):

    serializer_class = UserSerializer

    def put(self, request, id):

        payload = verify_token(request)

        try:
            user = User.objects.filter(id=payload['id']).first()
        except:
            return payload

        if user.is_superadmin:
            try:
                requestuser = User.objects.get(id=id)
            except User.DoesNotExist:
                return Response({
                    'success':False,
                    'error':'User does not exists',
                    'message':''})
            serializer = UserSerializer(requestuser,data=request.data)

            # Validate Data
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


# Get User Details
# request : GET
class GetUser(APIView):
    def get(self, request):
        payload = verify_token(request)

        try:
            user = User.objects.filter(id=payload['id']).first()
        except:
            return payload

        if user.is_superadmin:
            search = request.GET.get('search')
            orderBy = request.GET.get('orderBy')
            page = int(request.GET.get('currentPage', 1))
            per_page = int(request.GET.get('pageSize', 8))
            queryset = User.objects.all().exclude(is_superuser=True)

            # Logic for searching and ordering
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
                'data': {
                    'data': serializer.data,
                    'totalItems': total,
                    'currentPage': page,
                    'totalPage': math.ceil(total / per_page)
                }
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