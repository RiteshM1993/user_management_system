var routerApp = angular.module('userManagementApp',[
    'ui.router',
    'registerController',
    'loginController',
    'userRegisterService',
    'loginService',
    'addUserController',
    'adduserService',
    ]);



routerApp.config(function($stateProvider, $urlRouterProvider) {

    $urlRouterProvider.otherwise('/login');

    $stateProvider
        .state('login', {
            url: '/login',
            views: {
                "mainContent@" : {
                    templateUrl: '/static/views/login.html',
                    controller: 'loginController',
                    controllerAs: 'loginScope'
                }
            }

         })

         .state('register', {
             url: '/register',
             views: {
                "mainContent@" : {
                    templateUrl: '/static/views/register.html',
                    controller: 'registerController',
                    controllerAs: 'registerScope'
                }
            }

         })

         .state('dashboard', {
             url: '/dashboard/:email',
             views: {
                "mainContent@" : {
                    templateUrl: '/static/views/dashboard.html',
                    controller: 'addUserController',
                    controllerAs: 'addUserScope'
                },
            }

         })

          .state('adduserdetails', {
             url: '/adduserdetails/:email/:status',
             views: {
                "mainContent@" : {
                    templateUrl: '/static/views/adduserdetails.html',
                    controller: 'addUserController',
                    controllerAs: 'addUserScope'
                }
            }

         })


});
