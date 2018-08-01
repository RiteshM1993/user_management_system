angular.module('registerController', [])

.controller('registerController', ['userRegisterService','$scope','$rootScope', function(userRegisterService,$scope,$rootScope){

//  var loginCtrl  = this

  var registerScope = this

  registerScope.userRegister = function(){

     Registeruser={
           'email' : registerScope.email,
           'password' : registerScope.password,
     }


     var success = function(response){
            console.log(response)
            console.log('success')
            registerScope.successmsg = true
            registerScope.errormsg = false
        }


        var failure = function(response){
            console.log(response)
            console.log('failure')
            registerScope.successmsg = false
            registerScope.errormsg = true
        }

         userRegisterService.addUser(Registeruser,password,success,failure)


  }
  return registerScope;

}]);