
from management_system.models import Authentication,User,UserAddress

class UserManagementLogin:

    @classmethod
    def login(cls, email_id,password):
        try:
            getqry = Authentication.objects.filter(email=email_id,password=password)

            if getqry:
                succesresplist= []
                succesresplist.append({
                    'emailid': getqry[0].email,
                    'password': getqry[0].password,
                })
                return {'data': succesresplist,
                        'success': True}

            else:
                return {'success': False}



        except Exception, err:
            failureobj = {
                'response': "Failure"
            }
            return failureobj

    def listUserDetails(self, email):
        try:
            listqry= User.objects.filter(email=email)
            userdatalist= []
            for values in listqry:
                addresses = []
                address_data = UserAddress.objects.filter(user=values.id)
                for addess in address_data:
                    addresses.append({
                        "id": addess.id,
                        "name": addess.name,
                        "label": addess.label,
                        "landmark": addess.nearest_landmark
                    })
                userdatalist.append({
                    "salutation": values.salutation,
                    "firstName": values.first_name,
                    "lastName": values.last_name,
                    "email": values.email,
                    "dob": values.date_of_birth,
                    "status": values.relationship_status,
                    "gender": values.gender,
                    "address": addresses
                })
            if userdatalist:
                userdatalist = userdatalist[0]
            else:
                userdatalist = {}
            return userdatalist

        except Exception, err:
            failureobj = {
                'response': "Failure"
            }
            return failureobj










