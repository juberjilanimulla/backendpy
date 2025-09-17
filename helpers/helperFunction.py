import bcrypt
import jwt
import os 
import uuid
import secrets
from datatime import datetime,timedelta
from helpers.serverResponse import error_response


SECRET_KEY = os.getenv("JWT_SECRET",secrets.token_hex(48))
sessions = {}

# generate tokens
def generate_access_token(userid,email,role):
    session_id =create_session(user_id)

    encoded_payload = {"id":user_id,"email":email,"role":role,"exp":datetime.utcnow()+timedelta(minutes=1)}

    public_payload = {"id":user_id,"email":email,"role":role,"sessionid":session_id,"exp":datetime.utcnow()+timedelta(minutes=1)}

    encoded_token =jwt.encode(encoded_payload,SECRET_KEY,algorithm="HS256")
    public_token =jwt.encode(public_payload,SECRET_KEY,algorithm="HS256")

    return {"encoded_token":encoded_token,"public_token":public_token}

def validate_token(token):
    try:
        return jwt.decode(token,SECRET_KEY,algorithm="HS256")
    except Exception as e:
        raise e
    

    # middleware  (Flask-style decorator)
    def auth_middleware(f):
        from functools import wraps
        from flask import request,g

  @wraps(f)
       def wrapper(*args, **kwargs):
        auth_header = request.headers.get("Authorization") or request.args.get("token")
        if not auth_header:
            return error_response(401, "token not found")
        
        encoded_token = auth_header.split(" ")[1] if " " in auth_header else auth_header
        try:
            decoded = validate_token(encoded_token)
            g.user_id = decoded.get("id")
            g.role = decoded.get("role")
            g.email = decoded.get("email")
        except Exception:
            return error_response(401, "user not authorized")
        
        return f(*args, **kwargs)
    return wrapper


# Password hashing
def bcrypt_password(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

def compare_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode("utf-8"), hashed.encode("utf-8"))

# Sessions
def create_session(user_id):
    session_id = str(uuid.uuid4())
    sessions[user_id] = session_id
    return session_id

def get_session_data(user_id):
    return sessions.get(user_id)

def delete_session(user_id):
    return sessions.pop(user_id, None)

# Seed admin (like Admin() in JS)
def seed_admin():
    admin_emails = os.getenv("ADMIN", "").split(",")
    for email in admin_emails:
        if not UserModel.find_by_email(email):
            UserModel.create_user({
                "firstname": "admin",
                "lastname": "admin",
                "email": email,
                "role": "admin",
                "mobile": "9966470788",
                "password": bcrypt_password("Drkhizarraoof0832#*")
            })