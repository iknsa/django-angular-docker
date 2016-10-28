/**
 * Created by philippe on 24/10/2016.
 */

app = angular.module('gwapitApp', ['ngSanitize']);

app.controller('gmailCtrl', function ($scope, $http) {
        $http.get('http://localhost:8000/test').then(function (response) {
            $scope.records = response.data;
            console.log($scope.records);
        });
    });