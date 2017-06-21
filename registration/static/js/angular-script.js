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
  $scope.urlRegex = '[-a-zA-Z0-9@:%._\\+~#=]{2,256}\.[a-z]{2,6}\\b([-a-zA-Z0-9@:%_\\+.~#?&//=]*)';
})

app.controller('addJobController', function($scope){

})

app.controller('jobDashboardController', function($scope){

});

app.controller('jobListController', function($scope, $http){
  $scope.categories = [];
  $scope.getJobs = function(){
    $http.get('http://demo-fiverr.herokuapp.com/companylist/git/').then(function(response){
      $scope.jobs = response.data;
      $scope.jobs.forEach(function(e){
        if($scope.categories.lastIndexOf(e.category) == -1){
          $scope.categories.push(e.category);
        }
      });
    });
  }
});

app.controller('singleJobController', function($scope){

});

app.controller('jobApplyController', function($scope){

});
