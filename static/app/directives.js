"use strict";
angular.module('cloudColony').directive('addForm', function ($state, $http) {
	return {
		restrict: 'E',
		scope: {
  			data:'='
		},
		templateUrl: 'directives/addForm.html',
		link: function(scope, element, attrs) {

		}
	}
});