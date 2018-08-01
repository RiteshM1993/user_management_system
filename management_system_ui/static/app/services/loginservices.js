angular.module('loginService',[])

.service('loginService',['$http', function($http){

    var  login = {}

    login.User = function(loginuser,success,failure){
        $http.post('api/login/',{
            'email' : loginuser.email,
            'password' : loginuser.password,
        }).then(success, failure)

    }

        return login


 }])