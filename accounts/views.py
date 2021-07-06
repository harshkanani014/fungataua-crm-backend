from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.decorators import api_view
from .models import *
from .serializers import UserSerializer
import jwt, datetime
import random
import time
from django.http import JsonResponse
from twilio.rest import Client

def send_sms(otp):

    # Your Account SID from twilio.com/console
    account_sid = "ACb92105d6cb505863a13e05bef39dc8bd"
    # Your Auth Token from twilio.com/console
    auth_token  = "44705a3ce65f65f5c7bffc47e398311e"

    client = Client(account_sid, auth_token)
    
    message = client.messages.create(
        to="+919874307594", 
        from_="+12512903658",
        body="Your otp is " + str(otp)  + " only valid for 05 mins ")


# def verify_token(request):
#     # if not (request.headers['Authorization'] == "null"):
#     #         token = request.headers['Authorization']
#     if not (request.COOKIES.get('token') == "null"):
#         token = request.COOKIES.get('token')
#         #print(token)
#     else:
#         context = {
#             "success":False,
#             "error":"Not Authorized",
#             "message":"",
#             }
#         return JsonResponse(context)
#     try:
#         payload = jwt.decode(token, 'secret', algorithm=['HS256'])
#     except :
#         context = {
#                 "success":False,
#                 "error":"UnAuthenticated",
#                 "message":"",
#             }
#         return JsonResponse(context)
#     return payload


            

class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            context = {
                "success":False,
                "error":"User not found",
                "message":"",
                "data":
                {
                    "email":email,
                    "is_active":False
                
                }
            }
            return JsonResponse(context)
            #raise AuthenticationFailed('User not found!') remove comment after auth level done

        if not user.check_password(password):
            context = {
                "success":False,
                "error":"In correct password",
                "message":"",
                "data":
                {
                    "email":email,
                    "is_active":False
                
                }
            }
            return JsonResponse(context)
            # raise AuthenticationFailed('Incorrect password!') remove comment after auth level done
        
        otp = random.randint(1000, 9999)
                #login(request, user)
        print("otp :",  otp)
        send_sms(otp)
        expire_at = time.time() + 300


        if user.is_enabled==True:
            new_login = loginDetails()
            try:
                new_login.email = email
                new_login.otp = otp
                new_login.exp = expire_at
                new_login.is_active = True
                new_login.save()
            except:
                new_login = loginDetails.objects.get(email=email)
                new_login.otp = otp
                new_login.exp = expire_at
                new_login.is_active = True
                new_login.save()
            context = {
                "success":True,
                "error":"",
                "message":"OTP sent successully",
                "data":
                {
                    "email":email,
                    "is_active":True
                
                }
            }
            return JsonResponse(context)
        else:
            context = {
                "success":False,
                "error":"user has disabled your account Please contact administrator",
                "message":"",
                "data":
                {
                    "email":email,
                    "is_active":False
                
                }
            }
            return JsonResponse(context)

        
        

        # payload = {
        #     'id': user.id,
        #     'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=600),
        #     'iat': datetime.datetime.utcnow()
        # }

        # token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')

        # response = Response()

        # response.set_cookie(key='jwt', value=token, httponly=True)
        # response.data = {
        #                 "success":True,
        #                 "error":"",
        #                 "message":"OTP sent successully",
        #                 "token":token 
            
        #             }
        # return response

class OtpVerify(APIView):
    #authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    def post(self, request):
        email = request.data['email']
        otp = request.data['otp']
        current_req = loginDetails.objects.get(email=email)
        if current_req.is_active==True:
                if time.time() > float(current_req.exp):
                    context = {
                    "success":False,
                    "error":"OTP was expired!",
                    "message":"",
                    "data":
                        {
                        "email":email,
                        }
                    }
                    return Response(context)
                elif int(current_req.otp)==int(otp):
                    user = User.objects.get(email=email)
                    current_req.is_active = False
                    current_req.save()
                    payload = {
                    'id': user.id,
                    'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=600),
                    'iat': datetime.datetime.utcnow()
                    }

                    token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')

                    response = Response()
                    response.set_cookie(key='token', value=token, httponly=True)
                   
                    response.data = {
                        "success":True,
                        "error":"",
                        "message":"User login successfully",
                        "token":token,
                        "data":
                            {
                            "email":user.email,
                            "phone_number":user.phone_number,
                            "is_superadmin": user.is_superadmin,
                            "client_add": user.client_add,
                            "client_edit":user.client_edit ,
                            "services_add":user.services_add,
                            "services_edit":user.services_edit,
                            "category_add" : user.category_add,
                            "category_edit": user.category_edit,
                            "status_add": user.status_add,
                            "status_edit": user.status_edit,
                            "is_enabled": user.is_enabled,
                            }
                        }
                    return response
                else:
                    context = {
                        "success":False,
                        "error":"OTP was wrong",
                        "message":"",
                        "data":
                        {
                            "email":email
                        }
                    }
                    return Response(context)
        else:
            context = {
                "success":False,
                "error":"no data",
                "message":"",
                "data":""
            }
            return Response(context) 


# class OtpVerify(APIView):
#     def post(self, request):
#         otp = request.data['otp']
#         email = request.data['email']
#         current_req = loginDetails.objects.get(email=email)
#         if(int(current_req.otp)==int(otp)):
#             user = User.objects.filter(email=email).first()
#             payload = {
#             'id': user.id,
#             'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=600),
#             'iat': datetime.datetime.utcnow()
#             }

#             token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')

#             response = Response()

#             response.set_cookie(key='token', value=token, httponly=True)
#             response.data = {
#                         "success":True,
#                         "error":"",
#                         "message":"login successful",
#                         "token":token,
#                         "data":{ 
#                             "email":email
#                             }
            
#                     }
#             return response
#         context = {
#                 "success":False,
#                 "error":"OTP not matching",
#                 "message":"",
#             }
#         return JsonResponse(context)
        
        

@api_view(["GET"])
def resend_otp(request):
    email = request.data['email']
    current_req = loginDetails.objects.get(email=email)
    if current_req.is_active:
        # checks if OTP expired or not
        if time.time()> float(current_req.exp):
            otp = random.randint(1000,9999)
            print("otp", otp)
            send_sms(otp)
            current_req.otp = otp
            expire_at = time.time() + 300
            current_req.otp = otp
            current_req.save()
            # send_sms(otp)
            print(otp)
            context = {
                    "success":True,
                    "error":"",
                    "message":"OTP resend successfully",
                    "data":
                    {
                            "email":email
                    }
                }
            return Response(context)
        else:
            context = {
                    "success":False,
                    "error":"OTP already exist",
                    "message":"",
                    "data":
                    {
                            "email":email
                    }
                }
            return Response(context)
    else:
        context = {
                "success":False,
                "error":"no data",
                "message":"",
                "data":""
            }
        return Response(context) 



# class UserView(APIView):

#     def get(self, request):
#         # token = request.COOKIES.get('token')
#         # print(type(request.headers['Authorization']))
#         if not (request.headers['Authorization'] == "null"):
#             token = request.headers['Authorization']
#         else:
#             context = {
#                 "success":False,
#                 "error":"Not Authorized",
#                 "message":"",
#             }
#             return JsonResponse(context)
#         # print(token)
        
#         # print(token)

#         try:
#             payload = jwt.decode(token, 'secret', algorithm=['HS256'])
#         except :
#             context = {
#                 "success":False,
#                 "error":"UnAuthenticated",
#                 "message":"",
#             }
#             return JsonResponse(context)
            

#         user = User.objects.filter(id=payload['id']).first()
#         serializer = UserSerializer(user)
#         return Response(serializer.data)


class LogoutView(APIView):
    def get(self, request):
        response = Response()
        response.delete_cookie('token')
        response.data = {
            "error":"",
            'message': "success"
        }
        return response
