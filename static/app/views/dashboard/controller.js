'use strict';
var debug = {};

angular.module('cloudColony')
.controller('DashboardController',
    ['$cookieStore', 'config',
    function ($scope, $cookieStore, config, $http) {
    	$scope.mouse={}
    	$scope.mouse.name='fuck off';
    	debug=$scope;
	}
]);
