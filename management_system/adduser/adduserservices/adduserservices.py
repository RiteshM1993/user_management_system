from management_system.models import User,UserAddress,Authentication



class Management_User:


    def addUser(self,salutation,firstname,lastname,email,dob,relationshipstatus,gender, address):
        try:
            authentication_object = Authentication.objects.get(email=email)
            user_object= User(authentication=authentication_object, salutation=salutation,first_name=firstname,last_name=lastname,date_of_birth=dob,relationship_status=relationshipstatus,gender=gender,email=email)
            #
            user_object.save()

            if address:
                for add in address:
                    if len(add.keys()) > 0:
                        user_address = UserAddress(user=user_object, name=add['name'], label=add['label'], nearest_landmark=add['landmark'])
                        user_address.save()

            saveqrysuccessobj = {
                'response': "success"
            }
            return saveqrysuccessobj

        except Exception, err:
            saveqryfailureobj = {

                'response': "Failure"
            }
            return saveqryfailureobj

    #
    # def listUser(self,id):
    #     try:
    #         listqry = UserAddress.objects.all()















