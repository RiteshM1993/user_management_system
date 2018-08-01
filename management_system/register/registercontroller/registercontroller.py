import json
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from ..registerservice.registerservice import registerUserService

@api_view(['POST'])
def registerUser(request):
    email = request.data['email']
    password = request.data.get('password')
    register_User_obj = registerUserService()
    result = register_User_obj.registeruser(email, password)
    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)