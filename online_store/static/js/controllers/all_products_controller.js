'use strict';

angular.module('App').controller(
    'AllProductsController',
    function($scope, $http) {

	$http.get(
   		"/products"
   	).success(
   	    function(products_json, status, headers, config) {
   	    $scope.products = products_json
   	    debugger;
    });
});