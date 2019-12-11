
from rest_framework.response import Response

def is_admin(func):
    def decorator(*args, **kwargs):

        if args[0].META['HTTP_X_ADMIN'] =='1':
            return func(*args, **kwargs)
        else:
            return Response({'message':'not_allow_to_access'},403)
    return decorator

