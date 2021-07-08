from time import ctime
from accounts.models import User
from accounts.serializers import UserSerializer
from rest_framework.response import Response
from django.http import JsonResponse
from .serializers import CategorySerializer, ClientSerializer, StatusSerializer, ServiceSerializer, SubCategorySerializer, CategorySerializer, client_service_records_serializer
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
    try:
        if not (request.headers['Authorization'] == "null"):
            token = request.headers['Authorization']
    except:
        if not (request.COOKIES.get('token') == "null"):
            token = request.COOKIES.get('token')
            print(token)
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
        if user.category_add and user.is_enabled:
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
        if user.category_edit and user.is_enabled:
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
            tot_subcat = SubCategory.objects.all()
            search = request.GET.get('search')
            page = int(request.GET.get('currentPage', 1))
            per_page = request.GET.get('pageSize', len(tot_subcat))
            if(per_page=="max"):
                per_page = len(tot_subcat)
            else:
                per_page = int(per_page) 
               
            
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
            start = (page - 1) * int(per_page)
            end = page * per_page
            serializer = SubCategorySerializer(queryset[start:end], many=True)
            try:
                var = math.ceil(total / per_page)
            except:
                var = 0
            return Response({
                'success': True,
                'error': "",
                'data': {
                    'data': serializer.data,
                    'totalItems': total,
                    'currentPage': page,
                    'totalPage': var
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
            category_name = request.data['category_name']
            try:
                var = Category.objects.filter(category_name=category_name)
                if len(var)==0: 
                    is_enabled = request.data['is_enabled']         
                    subcategory = request.data['sub_category']
                    for i in subcategory:
                        new_cat = Category()
                        new_cat.category_name = category_name
                        new_cat.is_enabled = is_enabled
                        new_cat.subcategory = SubCategory.objects.get(id=i['id'])
                        new_cat.save()
                    return Response({
                        "success": True,
                        "error": "",
                        "message": "Category added successfully",
                        "data": request.data
                    })
                else:
                    return Response({
                        "success": False,
                        "error": "Category with same sub-category already exists",
                        "message": "",
                        "data": request.data
                    })
            except:
                 return Response({
                        "success": False,
                        "error": "Category with same sub-category already exists",
                        "message": "",
                        "data": request.data
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
        if user.category_add and user.is_enabled:
            name = Category.objects.get(id=id)
            var = Category.objects.filter(category_name=name.category_name)
            print(var)
            var.delete()
            category_name = request.data['category_name']
            try:
                var = Category.objects.filter(category_name=category_name)
                if len(var)==0: 
                    is_enabled = request.data['is_enabled']         
                    subcategory = request.data['sub_category']
                    for i in subcategory:
                        new_cat = Category()
                        new_cat.category_name = category_name
                        new_cat.is_enabled = is_enabled
                        new_cat.subcategory = SubCategory.objects.get(id=i['id'])
                        new_cat.save()
                    return Response({
                        "success": True,
                        "error": "",
                        "message": "Category Edited successfully",
                        "data": request.data
                    })
                else:
                    return Response({
                        "success": False,
                        "error": "Category with same sub-category already exists",
                        "message": "",
                        "data": request.data
                    })
            except:
                 return Response({
                        "success": False,
                        "error": "Category with same sub-category already exists",
                        "message": "",
                        "data": request.data
                    })

        else:
            return Response({
                "success": False,
                "error": "Not authorized to Edit category",
                "message": "",
                "data": {
                    "email": user.email
                }
            })




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
            categories=dict()
            for i in queryset:
                var = SubCategory.objects.filter(id=i.subcategory_id)
                if(i.category_name not in categories):
                    cat={
                            "id":i.id,                             
                            "category_name":i.category_name,
                            "is_enabled":i.is_enabled,
                            "sub_category":[]
                    }
                else:
                    cat=categories[i.category_name]
                for j in var:
                    # temp = {
                    #     "id":i.id,
                    #     "category_name":i.category_name,
                    #     "is_enabled":i.is_enabled,
                    #     "subcategory":{
                    #         "id":j.id,
                    #         "subcategory_name":j.subcategory_name,
                    #         "is_enabled":j.is_enabled
                    #     }
                    # }
                    sub = {
                            "id":j.id,
                            "subcategory_name":j.subcategory_name,
                            "is_enabled":j.is_enabled
                    }
                    cat["sub_category"].append(sub)
                categories.update({i.category_name:cat})
            
            cats=[]
            for i in categories:
                cats.append(categories[i])
            #print(cats)    
            # print(categories)
            # cat = dict()
            # serializer = SubCategorySerializer(subcat, many=True)
            # print(serializer.data)
            if search:
                queryset = queryset.filter(Q(category_name__icontains=search))
            if (orderBy == 'is_enabled'):
                queryset = queryset.order_by('is_enabled').reverse()
            elif (orderBy == 'disabled'):
                queryset = queryset.order_by('is_enabled')
            total = len(cats)
            start = (page - 1) * per_page
            end = page * per_page
            serializer = CategorySerializer(queryset[start:end], many=True)
            return Response({
                'success': True,
                'error': "",
                'data': {
                    'data': cats,
                    'totalItems': total,
                    'currentPage': page,
                    'totalPage': math.ceil(total / per_page)
                }
            })

# client view starts from here

class AddClient(APIView):
    serializer_class = ClientSerializer

    def post(self, request):
        payload = verify_token(request)
        try:
            user = User.objects.filter(id=payload['id']).first()
        except:
            return payload
        if user.client_add and user.is_enabled:
            serializer = ClientSerializer(data=request.data)
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
                "message": "Client added successfully",
                "data": serializer.data
            })
        else:
            return Response({
                "success": False,
                "error": "Not authorized to Add client",
                "message": "",
                "data": {
                    "email": user.email
                }
            })


class EditClient(APIView):
    serializer_class = ClientSerializer

    def put(self, request, id):

        payload = verify_token(request)
        try:
            user = User.objects.filter(id=payload['id']).first()
        except:
            return payload
        if user.client_edit and user.is_enabled:
            try:
                requestservice = Client.objects.get(id=id)
            except Client.DoesNotExist:
                return Response({
                    'success': False,
                    'error': 'client does not exists',
                    'message': ''})
            serializer = ClientSerializer(requestservice, data=request.data)
            if not serializer.is_valid():
                return Response({
                    'success': False,
                    'error': get_error(serializer.errors),
                    'message': ''})
            serializer.save()
            return Response({
                'success': True,
                'error': '',
                'message': 'client Edited successfully'})
        return Response({
            'success': False,
            'error': 'You are not allowed to edit client',
            'message': ''})

class GetClient(APIView):
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
            queryset = Client.objects.all()
            if search:
                queryset = queryset.filter(
                    Q(first_name__icontains=search) | Q(last_name__icontains=search) | Q(email__icontains=search) | Q(phone_number__icontains=search) | Q(city__icontains=search) | Q(state__icontains=search))
            if (orderBy == 'first_name'):
                queryset = queryset.order_by('first_name')
            elif (orderBy == 'last_name'):
                queryset = queryset.order_by('last_name')
            elif (orderBy == 'gender'):
                queryset = queryset.order_by('gender')

            total = queryset.count()
            start = (page - 1) * per_page
            end = page * per_page
            serializer = ClientSerializer(queryset[start:end], many=True)
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


# get specific client

class GetEachClient(APIView):
    def get(self, request, id):
        payload = verify_token(request)
        # print(payload)
        try:
            user = User.objects.filter(id=payload['id']).first()
        except:
            return payload
        if(user.is_enabled):
            queryset = Client.objects.filter(id=id)
            serializer = ClientSerializer(queryset, many=True)
            return Response({
                'success': True,
                'error': "",
                'data': serializer.data,
            })


# client records starts from here

class AddClientService(APIView):
    serializer_class = client_service_records_serializer
                                                             
    def post(self, request):                                 
        payload = verify_token(request)
        try:
            user = User.objects.filter(id=payload['id']).first()
        except:
            return payload
        if user.client_add and user.is_enabled:
            serializer = client_service_records_serializer(data=request.data)
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
                "message": "Client record added successfully",
                "data": serializer.data
            })
        else:
            return Response({
                "success": False,
                "error": "Not authorized to Add client record",
                "message": "",
                "data": {
                    "email": user.email
                }
            })


class EditClientService(APIView):
    serializer_class = client_service_records_serializer

    def put(self, request, id):

        payload = verify_token(request)
        try:
            user = User.objects.filter(id=payload['id']).first()
        except:
            return payload
        if user.client_edit and user.is_enabled:
            try:
                requestservice = client_service_records.objects.get(id=id)
            except Client.DoesNotExist:
                return Response({
                    'success': False,
                    'error': 'client/service does not exists',
                    'message': ''})
            serializer = client_service_records_serializer(requestservice, data=request.data)
            if not serializer.is_valid():
                return Response({
                    'success': False,
                    'error': get_error(serializer.errors),
                    'message': ''})
            serializer.save()
            return Response({
                'success': True,
                'error': '',
                'message': 'client/service Edited successfully'})
        return Response({
            'success': False,
            'error': 'You are not allowed to edit client/service',
            'message': ''})



class GetClientService(APIView):
    def get(self, request, id):
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
            queryset = client_service_records.objects.filter(email_id = id)  # email_id is foreign key 
            client_email = Client.objects.get(id=id).email
            #print(client_email)
            client_services=dict()
            for i in queryset:
                added_by_var = User.objects.filter(id=i.added_by.id)
                services_var = Services.objects.filter(id=i.services.id)
                category_var = Category.objects.filter(id=i.category.id)
                subcategory_var = SubCategory.objects.filter(id=i.subcategory.id)
                status_var = Status.objects.filter(id=i.status.id)
                
                if(i.email.email not in client_services):
                    single = {
                        "email":i.email.email,
                        "services":[]                      
                    }
                else:
                    single = client_services[i.email.email]
                single_service = dict()
                single_service.update({"id":i.id})
                single_service.update({"date_of_visit":i.date_of_visit})
                for j in added_by_var:
                    single_service.update({"added_by":j.email})
                for j in services_var:
                    single_service.update({"service_name":j.service_name})
                                    
                for j in category_var:
                    single_service.update({"category":j.category_name})  

                for j in subcategory_var:
                    single_service.update({"subcategory":j.subcategory_name})  
                    
                for j in status_var:
                    single_service.update({"status":j.status}) 
                single_service.update({"remarks":i.remarks})
                single["services"].append(single_service)
                client_services.update({i.email.email:single})
            
            
            client_service_arr=[]
            for i in client_services:
                client_service_arr.append(client_services[i])
            res = client_service_arr
            if(len(res)==0):
                res = {
                        "email":client_email,
                        "services":[]                      
                    }
            else:
                res=client_service_arr[0]
            # print(client_service_arr)    
            # print(categories)
            # cat = dict()
            # serializer = SubCategorySerializer(subcat, many=True)
            # print(serializer.data)
            
            if search:
                queryset = queryset.filter(Q(category_name__icontains=search))
            if (orderBy == 'is_enabled'):
                queryset = queryset.order_by('is_enabled').reverse()
            elif (orderBy == 'disabled'):
                queryset = queryset.order_by('is_enabled')
            total = len(client_service_arr)
            start = (page - 1) * per_page
            end = page * per_page
            # print("debug")
            #serializer = client_service_records_serializer(queryset[start:end], many=True)
            return Response({
                'success': True,
                'error': "",
                'data': {
                    'data': res,
                    'totalItems': total,
                    'currentPage': page,
                    'totalPage': math.ceil(total / per_page)
                }
            })           




