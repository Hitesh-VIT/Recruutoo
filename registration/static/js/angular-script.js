var app = angular.module('app', []);

app.config(function($interpolateProvider){
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});

app.controller('loginController', function($scope){
  $scope.login = true;
  $scope.changeLogin = function(changeTo){
    $scope.login = changeTo;
  }
});

app.controller('detailsController', function($scope){
  
})
