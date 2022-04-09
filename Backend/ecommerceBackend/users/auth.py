from wsgiref import headers
import jwt
from google.auth import jwt as jt
from django.conf import settings
import datetime
from ecommerceBackend.utils import Validation
import jwt
from rest_framework import status

from django.conf import settings
# Collections
Users = settings.DB['users']

Validator = Validation()
UserCollection = settings.DB['users']

def getExpTime(exp_time):
    if exp_time:
        exp = datetime.datetime.now() + datetime.timedelta(seconds=exp_time)
    else:
        exp = datetime.datetime.now() + settings.JWT_DEFAULT.get('TOKEN_LIFETIME')
        return exp

def createJWT(payload, exp=None, *args, **kwargs):
    now = datetime.datetime.timestamp(datetime.datetime.now())
    if not exp:
        print("yoo")
        exp = getExpTime(exp)
        exp = (datetime.datetime.timestamp(exp))
    print(now)
    print(exp)
    
    times = {'iat': now, 'exp': int(exp)}
    payload.update(times)
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
    return token

def get_user(username):
    user = UserCollection.find_one({"username": username})
    return user

def create_raw_user(**kwargs):
    fields = ['username',
               "email",
               "phone",
               "phone2",
               "password",
               "address",
               "role",
               "wallet",
               ]
    user={}

    # validate email, phone or password exist
    if not (kwargs.get("email") or kwargs.get("phone")):
        return {"status": False, "message": "Email or Phone no. required!"}
    if not kwargs.get("password"):
        return {"status": False, "message": "Password required!"}
  
    for i in fields:
        if i == "password":
            passwd = Validator.generate_password(kwargs.get(i))
            user[i] = passwd
            continue
        if i == "address":
            user[i] = list()
            continue
        user[i] = kwargs.get(i) or ""

    user['username'] = kwargs.get("email") or kwargs.get("phone")
    user['fullname'] = kwargs.get("full_name")
    user['created_at'] = datetime.datetime.now()
    user['updated_at'] = datetime.datetime.now()
    user["auth_type"] = "password",
    # check user existance
    existed_user = get_user(user.get("username"))
    if existed_user:
        return {"status": True,"message": "User already exists!"}
    
    UserCollection.insert_one(user) # insert user data to database
    created_user = get_user(user.get("username")) # get created user
    payload = {
        "user_id": str(user.get("_id")),
        "email": created_user.get("email"),
        "phone": created_user.get("phone"),
        "picture": created_user.get("picture"),
        "role": created_user.get("role"),
        "full_name": existed_user.get("fullname")
    }
    # encoded_jwt = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
    encoded_jwt = createJWT(payload)

    return {"status": True,"message": "User created", "user": payload, "token": encoded_jwt}


def athenticate_social_user(token):
    user_data = jt.decode(token, verify=False)
    print(user_data)
    if  user_data.get('email_verified')==True and user_data.get('aud')==settings.GOOGLE_CLIENT_ID:
        existed_user = get_user(user_data.get("email"))
        if existed_user:
            payload = {
                "user_id": str(existed_user.get("_id")),
                "email": existed_user.get("email"),
                "phone": existed_user.get("phone"),
                "picture": existed_user.get("picture"),
                "role": existed_user.get("role"),
                "full_name": existed_user.get("fullname")
            }

            # encoded_jwt = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
            encoded_jwt = createJWT(payload)

            return {
                "message": "Succesfully logged in!",
                "token": encoded_jwt,
                "user": payload,
                "status_code": 200 
            }

        else:
            new_user = {"username": user_data.get("email"),
                        "email": user_data.get("email"),
                        "fullname": f"{user_data.get('given_name')} {user_data.get('family_name')}",
                        "picture": user_data.get('picture'),
                        "address": "",
                        "role": "",
                        "auth_type": "social",
                        "wallet": 0,
                        "created_at": datetime.datetime.now(),
                        "updated_at": datetime.datetime.now()
                        }
            
            UserCollection.insert_one(new_user) # insert user data to database
            created_user = get_user(new_user.get("username")) # get created user
            payload = {
                "user_id": str(new_user.get("_id")),
                "email": created_user.get("email"),
                "phone": created_user.get("phone"),
                "picture": created_user.get("picture"),
                "role": created_user.get("role"),
                "full_name": existed_user.get("fullname")
            }
            encoded_jwt = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")

            return {"status": True,"message": "User created","user": payload, "token": encoded_jwt}
        
    else:
        result="Email not verified"

        return result


def authenticate_user(username, password):
    print(username)
    print(password)
    user_data = Users.find_one({'username': username})
    if user_data:  
        is_matched = Validator.match_paassword(user_data.get('password'), password)

        if is_matched:
            # created_user = get_user(user.get("username")) # get created user
            payload = {
                "user_id": str(user_data.get("_id")),
                "email": user_data.get("email"),
                "phone": user_data.get("phone"),
                "picture": user_data.get("picture"),
                "role": user_data.get("role"),
                "full_name": user_data.get("fullname")
            }
            print(payload)
            encoded_jwt = createJWT(payload)

            return {
                "message": "Succesfully logged in!",
                "token": encoded_jwt,
                "user": payload,
                "status_code": 200 
            }   

        else:
            return {
                "message": "Wrong password!",
                "status_code": 401
            }
    
    else:
        return {
                "message": "User not found!",
                "status_code": 404
            }

