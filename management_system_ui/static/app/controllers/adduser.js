angular.module('addUserController', [])

.controller('addUserController', ['adduserService','$scope','$rootScope','$state', function(adduserService,$scope,$rootScope,$state){

  var addUserScope = this;

  var addEditCall = $state.params.status;
  addUserScope.email = $state.params.email;
//  var dob = employeeeducationScope.dateOfComplete.replace(/(\d\d)\/(\d\d)\/(\d{4})/, "$3-$1-$2");
//  addUserScope.dob = dob.replace(/(\d\d)\/(\d\d)\/(\d{4})/, "$3-$1-$2");
  addUserScope.userDetails = {
    'salutation' : null,
    'firstName' : null,
    'lastName' : null,
    'email' : addUserScope.email,
    'dob' : null,
    'status' : null,
    'gender':null,
    'address': [{
        name: '',
        label: '',
        landmark: ''
    }]
  }

  var loggedIn = localStorage.getItem('loggedIn')

 if(!loggedIn){
    $state.go('login')

 }

  addUserScope.addRow = function(){

    addUserScope.userDetails.address.push({})

  }

  addUserScope.removeRow = function(index){

    addUserScope.userDetails.address.splice(index, 1);

  }

  addUserScope.adduser = function(){

     var success = function(response){
            console.log(response)
            console.log('success')
            addUserScope.successmsg = true
            addUserScope.errormsg = false

        }


        var failure = function(response){
            console.log(response)
            console.log('failure')
            addUserScope.successmsg = false
            addUserScope.errormsg = true
        }

         adduserService.user(addUserScope.userDetails,success,failure)


  }

    addUserScope.getUserlist = function(){

        var success = function(response){
            var userData = response.data.data
            if (( 'dob' in userData)){
               userData.dob = new Date( userData.dob);
            }
            addUserScope.userDetails = userData
            addUserScope.userDetails['email'] = addUserScope.email;
            if (!( 'address' in addUserScope.userDetails)){
                addUserScope.userDetails['address'] = [{
                    name: '',
                    label: '',
                    landmark: ''
                }];
            }
            console.log('success')

        }

        var failure = function(response){
            console.log(response)
            console.log('failure')
        }

        adduserService.listuser(addUserScope.email, success, failure)
    }

  if (addEditCall == "true"){
    addUserScope.getUserlist();
  }



    addUserScope.logout = function(){

        localStorage.removeItem("loggedIn");
        localStorage.removeItem("email");
        $state.go('login');

    }


  return addUserScope;

}]);