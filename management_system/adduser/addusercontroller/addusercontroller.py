import json
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder


from management_system.adduser.adduserservices.adduserservices import Management_User



@api_view(['POST'])
def userData(request):
    salutation = request.data['salutation']
    firstname = request.data['firstName']
    lastname = request.data['lastName']
    email = request.data['email']
    dob = request.data['dob']
    relationshipstatus = request.data['status']
    gender = request.data['gender']
    address = request.data.get('address')


    Management_User_obj = Management_User()
    result = Management_User_obj.addUser(salutation, firstname, lastname, email, dob, relationshipstatus, gender, address)
    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)



