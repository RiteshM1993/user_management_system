angular.module('adduserService',[])

.service('adduserService',['$http', function($http){

    var  userdata = {}

    userdata.user = function(data,success,failure){
        $http.post('/api/user/',data
        ).then(success, failure)

    }

    userdata.listuser = function(email, success, failure){
        $http.get('/api/listuser/?email='+email).then(success, failure)
    }

        return userdata


 }])