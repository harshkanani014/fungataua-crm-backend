from accounts.models import User
from accounts.serializers import UserSerializer
from rest_framework.response import Response
from django.http import JsonResponse
from .serializers import CategorySerializer, StatusSerializer, ServiceSerializer, SubCategorySerializer, CategorySerializer
import jwt
import math
from django.db.models import Q
from rest_framework.views import APIView
from .models import *
# Create your views here.
def get_error(serializerErr):
    err = ''
    for i in serializerErr:
        err = serializerErr[i][0]
        break    
    return err


def verify_token(request):
    if not (request.headers['Authorization'] == "null"):
        token = request.headers['Authorization']
    # if not (request.COOKIES.get('token') == "null"):
    #     token = request.COOKIES.get('token')
    #     print(token)
    else:
        context = {
            "success": False,
            "error": "Not Authorized",
            "message": "",
        }
        payload = JsonResponse(context)
    try:
        payload = jwt.decode(token, 'secret', algorithm=['HS256'])
    except:
        context = {
            "success": False,
            "error": "UnAuthenticated",
            "message": "",
        }
        payload = JsonResponse(context)
    print(payload)
    return payload

# Status page starts from here


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
                # print(serializer.errors)
                return Response({
                    "success": False,
                    "error": get_error(serializer.errors),
                    "message": "",
                    "data": user.email
                })

            serializer.save()
            return Response({
                "success": True,
                "error": "",
                "message": "Status added successfully",
                "data": serializer.data
            })
        else:
            return Response({
                "success": False,
                "error": "Not authorized to Add status",
                "message": "",
                "data": {
                    "email": user.email
                }
            })


class EditStatus(APIView):
    serializer_class = StatusSerializer

    def put(self, request, id):

        payload = verify_token(request)
        try:
            user = User.objects.filter(id=payload['id']).first()
        except:
            return payload
        if user.status_edit and user.is_enabled:
            try:
                requeststatus = Status.objects.get(id=id)
            except Status.DoesNotExist:
                return Response({
                    'success': False,
                    'error': 'Status does not exists',
                    'message': ''})
            serializer = StatusSerializer(requeststatus, data=request.data)
            if not serializer.is_valid():
                return Response({
                    'success': False,
                    'error': get_error(serializer.errors),
                    'message': ''})
            serializer.save()
            return Response({
                'success': True,
                'error': '',
                'message': 'Status Edited successfully'})
        return Response({
            'success': False,
            'error': 'You are not allowed to edit status',
            'message': ''})


class GetStatus(APIView):
    def get(self, request):
        payload = verify_token(request)
        # print(payload)
        try:
            user = User.objects.filter(id=payload['id']).first()
        except:
            return payload
        if user.is_enabled:
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
                'data': {
                    'data': serializer.data,
                    'totalItems': total,
                    'currentPage': page,
                    'totalPage': math.ceil(total / per_page)
                }
                
            })


# Service Page start from here
class AddService(APIView):
    serializer_class = ServiceSerializer

    def post(self, request):
        payload = verify_token(request)
        try:
            user = User.objects.filter(id=payload['id']).first()
        except:
            return payload
        if user.services_add and user.is_enabled:
            serializer = ServiceSerializer(data=request.data)
            if not serializer.is_valid():
                # print(serializer.errors)
                return Response({
                    "success": False,
                    "error": get_error(serializer.errors),
                    "message": "",
                    "data": user.email
                })

            serializer.save()
            return Response({
                "success": True,
                "error": "",
                "message": "Service added successfully",
                "data": serializer.data
            })
        else:
            return Response({
                "success": False,
                "error": "Not authorized to Add service",
                "message": "",
                "data": {
                    "email": user.email
                }
            })


class EditService(APIView):
    serializer_class = ServiceSerializer

    def put(self, request, id):

        payload = verify_token(request)
        try:
            user = User.objects.filter(id=payload['id']).first()
        except:
            return payload
        if user.services_edit and user.is_enabled:
            try:
                requestservice = Services.objects.get(id=id)
            except Services.DoesNotExist:
                return Response({
                    'success': False,
                    'error': 'Service does not exists',
                    'message': ''})
            serializer = ServiceSerializer(requestservice, data=request.data)
            if not serializer.is_valid():
                return Response({
                    'success': False,
                    'error': get_error(serializer.errors),
                    'message': ''})
            serializer.save()
            return Response({
                'success': True,
                'error': '',
                'message': 'Service Edited successfully'})
        return Response({
            'success': False,
            'error': 'You are not allowed to edit service',
            'message': ''})


class GetService(APIView):
    def get(self, request):
        payload = verify_token(request)
        # print(payload)
        try:
            user = User.objects.filter(id=payload['id']).first()
        except:
            return payload
        if(user.is_enabled):
            search = request.GET.get('search')
            page = int(request.GET.get('currentPage', 1))
            per_page = int(request.GET.get('pageSize', 8))
            orderBy = request.GET.get('orderBy')
            queryset = Services.objects.all()
            if search:
                queryset = queryset.filter(Q(service_name__icontains=search))
            if (orderBy == 'is_enabled'):
                queryset = queryset.order_by('is_enabled').reverse()
            elif (orderBy == 'disabled'):
                queryset = queryset.order_by('is_enabled')

            total = queryset.count()
            start = (page - 1) * per_page
            end = page * per_page
            serializer = ServiceSerializer(queryset[start:end], many=True)
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


# subcategory page starts

class AddSubCategory(APIView):
    serializer_class = SubCategorySerializer

    def post(self, request):
        payload = verify_token(request)
        try:
            user = User.objects.filter(id=payload['id']).first()
        except:
            return payload
        if user.services_add and user.is_enabled:
            serializer = SubCategorySerializer(data=request.data)
            if not serializer.is_valid():
                # print(serializer.errors)
                return Response({
                    "success": False,
                    "error": get_error(serializer.errors),
                    "message": "",
                    "data": user.email
                })

            serializer.save()
            return Response({
                "success": True,
                "error": "",
                "message": "subcategory added successfully",
                "data": serializer.data
            })
        else:
            return Response({
                "success": False,
                "error": "Not authorized to Add subcategory",
                "message": "",
                "data": {
                    "email": user.email
                }
            })


class EditSubCategory(APIView):
    serializer_class = SubCategorySerializer

    def put(self, request, id):

        payload = verify_token(request)
        try:
            user = User.objects.filter(id=payload['id']).first()
        except:
            return payload
        if user.services_edit and user.is_enabled:
            try:
                requestservice = SubCategory.objects.get(id=id)
            except Services.DoesNotExist:
                return Response({
                    'success': False,
                    'error': 'Sub-category does not exists',
                    'message': ''})
            serializer = SubCategorySerializer(requestservice, data=request.data)
            if not serializer.is_valid():
                return Response({
                    'success': False,
                    'error': get_error(serializer.errors),
                    'message': ''})
            serializer.save()
            return Response({
                'success': True,
                'error': '',
                'message': 'Sub-category Edited successfully'})
        return Response({
            'success': False,
            'error': 'You are not allowed to edit Sub-category',
            'message': ''})




class GetSubCategory(APIView):
    def get(self, request):
        payload = verify_token(request)
        # print(payload)
        try:
            user = User.objects.filter(id=payload['id']).first()
        except:
            return payload
        if(user.is_enabled):
            search = request.GET.get('search')
            page = int(request.GET.get('currentPage', 1))
            per_page = int(request.GET.get('pageSize', 8))
            orderBy = request.GET.get('orderBy')
            queryset = SubCategory.objects.all()
            if search:
                queryset = queryset.filter(
                    Q(subcategory_name__icontains=search))
            if (orderBy == 'is_enabled'):
                queryset = queryset.order_by('is_enabled').reverse()
            elif (orderBy == 'disabled'):
                queryset = queryset.order_by('is_enabled')

            total = queryset.count()
            start = (page - 1) * per_page
            end = page * per_page
            serializer = SubCategorySerializer(queryset[start:end], many=True)
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


# category start from

class AddCategory(APIView):
    serializer_class = CategorySerializer

    def post(self, request):
        payload = verify_token(request)
        try:
            user = User.objects.filter(id=payload['id']).first()
        except:
            return payload
        if user.category_add and user.is_enabled:
            serializer = CategorySerializer(data=request.data)
            if not serializer.is_valid():
                return Response({
                    "success": False,
                    # "error": serializer.errors,
                    "error":get_error(serializer.errors),
                    "message": "",
                    "data": user.email
                })

            serializer.save()
            return Response({
                "success": True,
                "error": "",
                "message": "Category added successfully",
                "data": serializer.data
            })
        else:
            return Response({
                "success": False,
                "error": "Not authorized to Add category",
                "message": "",
                "data": {
                    "email": user.email
                }
            })

class EditCategory(APIView):
    serializer_class = CategorySerializer

    def put(self, request, id):

        payload = verify_token(request)
        try:
            user = User.objects.filter(id=payload['id']).first()
        except:
            return payload
        if user.services_edit and user.is_enabled:
            try:
                requestservice = Category.objects.get(id=id)
            except Services.DoesNotExist:
                return Response({
                    'success': False,
                    'error': 'category does not exists',
                    'message': ''})
            serializer = CategorySerializer(requestservice, data=request.data)
            if not serializer.is_valid():
                return Response({
                    'success': False,
                    'error': get_error(serializer.errors),
                    'message': ''})
            serializer.save()
            return Response({
                'success': True,
                'error': '',
                'message': 'category Edited successfully'})
        return Response({
            'success': False,
            'error': 'You are not allowed to edit category',
            'message': ''})




class GetCategory(APIView):
    def get(self, request):
        payload = verify_token(request)
        # print(payload)
        try:
            user = User.objects.filter(id=payload['id']).first()
        except:
            return payload
        if(user.is_enabled):
            search = request.GET.get('search')
            page = int(request.GET.get('currentPage', 1))
            per_page = int(request.GET.get('pageSize', 8))
            orderBy = request.GET.get('orderBy')
            queryset = Category.objects.all()
            if search:
                queryset = queryset.filter(
                    Q(category_name__icontains=search))
            if (orderBy == 'is_enabled'):
                queryset = queryset.order_by('is_enabled').reverse()
            elif (orderBy == 'disabled'):
                queryset = queryset.order_by('is_enabled')

            total = queryset.count()
            start = (page - 1) * per_page
            end = page * per_page
            serializer = CategorySerializer(queryset[start:end], many=True)
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




