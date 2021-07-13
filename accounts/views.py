from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
import jwt, datetime
import random
import time
from django.http import JsonResponse
from twilio.rest import Client
from django.core.mail import EmailMultiAlternatives
from client.views import verify_token


# Function for sending OTP via email
def send_email(otp, email_1):
    
    email = EmailMultiAlternatives('2FA OTP for FUNGATAUA trust', ' Your OTP is :' + otp)
    email.to = [email_1]
    email.send()

    


# Function for sending sms
def send_sms(otp):

    # Your Account SID from twilio.com/console
    account_sid = "ACb92105d6cb505863a13e05bef39dc8bd"
    # Your Auth Token from twilio.com/console
    auth_token  = "44705a3ce65f65f5c7bffc47e398311e"

    client = Client(account_sid, auth_token)
    
    message = client.messages.create(
        to="+917048475675", 
        from_="+12512903658",
        body="Your otp is " + str(otp)  + " only valid for 05 mins ")


# API for login 
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

        if not user.check_password(password):
            context = {
                "success":False,
                "error":"In-correct password",
                "message":"",
                "data":
                {
                    "email":email,
                    "is_active":False
                }
            }
            return JsonResponse(context)
        
        otp = random.randint(1000, 9999)      
        print("otp :", otp)
        try:
            send_email(str(otp), email)
        except:
            context = {
                "success":False,
                "error":"Unable to send otp to given E-Mail",
                "message":"",
                "data":
                {
                    "email":email,
                    "is_active":False
                }
            }
            return JsonResponse(context)

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


#API for checkiing otp and verifying it
class OtpVerify(APIView):

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
                    'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=500),
                    'iat': datetime.datetime.utcnow()
                    }

                    token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8') #generating token
                    response = Response()
                    response.set_cookie(key='token', value=token, httponly=True)
                   
                    response.data = {
                        "success":True,
                        "error":"",
                        "message":"User login successfully",
                        "token":token,
                        "data":
                            {
                            "id":user.id,
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


# API for resending otp to user after expiring.            
@api_view(["POST"])
def resend_otp(request):

    email = request.data['email']
    current_req = loginDetails.objects.get(email=email)

    if current_req.is_active:
        # checks if OTP expired or not
        if time.time()> float(current_req.exp):
            otp = random.randint(1000,9999)
            print("otp", otp)
            # send_sms(otp)

            try:
                send_email(str(otp), email)
            except:
                context = {
                    "success":False,
                    "error":"Unable to send otp to given E-Mail",
                    "message":"",
                    "data":
                    {
                        "email":email,
                        "is_active":False
                    }
                }
                return JsonResponse(context)

            expire_at = time.time() + 300
            current_req.otp = otp
            current_req.exp = expire_at
            current_req.save()
            
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


class ResetPassword(APIView):
     def put(self, request):
        payload = verify_token(request)
        
        try:
            user = User.objects.filter(id=payload['id']).first()
        except:
            return payload
        
        old_password = request.data['old_password']
        new_password = request.data['new_password']
        conf_password = request.data['confirm_password']
        if not user.check_password(old_password):
            context = {
                "success":False,
                "error":"Old password does not match",
                "message":"",
                "data":""
            }
            return Response(context)
        
        if new_password==conf_password:
            user.set_password(new_password)
            user.save()
            context = {
                "success":True,
                "error":"",
                "message":"Password Reset Successfully",
                "data":""
            }
            return Response(context)
        else:
            context = {
                "success":False,
                "error":"Password does not match",
                "message":"",
                "data":""
            }
            return Response(context)


# API for logout
class LogoutView(APIView):

    def get(self, request):
        
        response = Response()
        response.delete_cookie('token') #delete the token
        
        response.data = {
            "error":"",
            'message': "success"
        }
        return response
