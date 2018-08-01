from management_system.models import Authentication


class registerUserService:


    def registeruser(self, email, password):
        try:
            saveqry = Authentication(email=email, password=password)
            saveqry.save()
            saveqrysuccessobj = {
                'response': "success"
            }
            return saveqrysuccessobj

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }
            return saveqryfailureobj


















