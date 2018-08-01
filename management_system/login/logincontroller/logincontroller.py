import json
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder



from management_system.login.loginservices.loginservices import UserManagementLogin

@api_view(['POST'])
def login(request):
    email_id = request.data['email']
    password = request.data['password']
    user_management_obj = UserManagementLogin()
    result = user_management_obj.login(email_id,password)
    dataobj = {'data': result}
    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)


@api_view(['GET'])
def getUserDetails(request):
    email = request.GET['email']
    user_management_obj = UserManagementLogin()
    result= user_management_obj.listUserDetails(email=email)
    dataobj = {'data': result}
    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)



