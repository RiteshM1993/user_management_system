angular.module('loginController', [])

.controller('loginController', ['loginService','$scope','$rootScope','$state', function(loginService,$scope,$rootScope,$state){

     var loginScope = this


     var loggedIn = localStorage.getItem('loggedIn')

     if(loggedIn){
        var email = localStorage.getItem('email')
        $state.go('dashboard', {email: email})

     }

     console.log(loggedIn)


     loginScope.userLogin = function(){

     loginuser = {
           'email' : loginScope.email,
           'password' : loginScope.password,
     }

     var success = function(response){
            console.log(response)
            console.log('success')
            loginScope.successmsg = true
            loginScope.errormsg = false
            if (response.data.data.success){
               localStorage.setItem("loggedIn", true);
               localStorage.setItem("email", loginScope.email);
               $state.go('dashboard', {email: response.data.data.data[0].emailid})
            }
            else{
                alert('Invalid Login Password')
            }
        }


        var failure = function(response){
            console.log(response)
            console.log('failure')
            loginScope.successmsg = false
            loginScope.errormsg = true
        }

         loginService.User(loginuser,success,failure)


  }




  return loginScope;

}]);