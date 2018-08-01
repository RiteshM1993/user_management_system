angular.module('userRegisterService',[])

.service('userRegisterService',['$http', function($http){

    var register = {}

    register.addUser = function(Registeruser,success,failure){
        $http.post('/api/register/',{
            'email' : Registeruser.email,
            'password' : Registeruser.password,
        }).then(success, failure)

    }

        return register


 }])