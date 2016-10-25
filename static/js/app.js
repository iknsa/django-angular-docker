/**
 * Created by philippe on 24/10/2016.
 */

app = angular.module('gwapitApp', ['ngSanitize']);

app.controller('helloCtrl', function ($scope, $http) {
        $http.get('http://rest-service.guides.spring.io/greeting').then(function (response) {
            $scope.greeting = response.data;
            console.log($scope.greeting);
        });
    });


app.controller('gmailCtrl', function ($scope, $http) {

        req = 'https://www.googleapis.com/gmail/v1/users/'
                + 'bazard.philippe@gmail.com'
                + '/messages?key='
                + 'ya29.Ci-GAzgyXr1D4LWA6wZq54hFtejHdESLOWrMJ1sTdCWhU3xdTspRBf2MhoEgPNlNCQ';

        $http.get(req).then(function (response) {
            $scope.res = response.data;
            console.log($scope.res);
        });
    });