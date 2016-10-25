/**
 * Created by philippe on 24/10/2016.
 */

app = angular.module('gwapitApp', ['ngSanitize']);

/**
 * Test
 */
app.controller('helloCtrl', function ($scope, $http) {
        $http.get('http://rest-service.guides.spring.io/greeting').then(function (response) {
            $scope.greeting = response.data;
            console.log($scope.greeting);
        });
    });