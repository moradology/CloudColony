'use strict';

angular.module('CloudColony', [
    'ngAnimate',
    'ngCookies',
    'ngResource',
    'ui.router',
    'angularFileUpload',
    'pascalprecht.translate',
    'ui.bootstrap',
    'ui.utils',
    'angular-spinkit'
]).config(['$stateProvider', '$urlRouterProvider', '$locationProvider', 'config', '$httpProvider',
        function ($stateProvider, $urlRouterProvider, $locationProvider, config, $httpProvider) {

    $httpProvider.interceptors.push('authInterceptor');
    $httpProvider.interceptors.push('logoutInterceptor');

    $urlRouterProvider.when('', '/');
    $urlRouterProvider.otherwise('/');

    $stateProvider
        .state('root', {
            abstract: true,
            templateUrl: '/controllers/root/root-partial.html',
            controller: 'RootController'
        })
        .state('login', {
            url: '/login',
            templateUrl: '/controllers/auth/login-partial.html',
            controller: 'AuthController'
        })
        .state('settings', {
            parent: 'root',
            url: '/settings',
            templateUrl: '/controllers/settings/settings-partial.html',
            controller: 'SettingsController'
        });

        /*
         * config.settingsView view objects are:
         * {
         *      id: '<unique string>',
         *      label: '<sidebar display string>'
         * }
         * URL matches to /settings/<view.id>
         * To add a new entry in the settings sidebar:
         *  1) Add new 'view' object to config.settingsView in config.js with
         *     id and label properties
         *  2) Add controller and partial files to the path:
         *     controllers/<view.id>/<view.id>-controller.js
         *     controllers/<view.id>/<view.id>-partial.html
         *  3) Ensure controller has the name OTI<view.id>Controller where the first letter of
         *     view.id is capitalized, e.g. for view.id == upload, name is OTIUploadController
         *  4) Add <script> tag for your controller in ../index.html
         */
        _.each(config.settingsViews, function (view) {
            var viewId = view.id;
            var capsId = viewId.charAt(0).toUpperCase() + viewId.slice(1);
            $stateProvider.state(view.id, {
                parent: 'settings',
                url: '/' + viewId,
                templateUrl: '/controllers/settings/' + viewId + '/' + viewId + '-partial.html',
                controller: capsId + 'Controller'
            });
        });

        _.each(config.scenarioViews, function (view) {
            var viewId = view.id;
            var nodash = viewId.replace('-', '');
            var capsId = nodash.charAt(0).toUpperCase() + nodash.slice(1);
            $stateProvider.state(view.id, {
                parent: 'scenarios',
                url: '/' + viewId,
                templateUrl: '/controllers/scenarios/' + viewId + '/' + viewId + '-partial.html',
                controller: capsId + 'Controller',
                resolve: {

                }
            });
        });

}]).config(['$translateProvider', 'config', function($translateProvider, config) {
    $translateProvider.useStaticFilesLoader({
       prefix: 'i18n/',
       suffix: '.json'
    });
    // Log untranslated tokens to console
    $translateProvider.useMissingTranslationHandlerLog();
    // Use browser's set language if one of our supported languages; otherwise, English
    var languageActual = (navigator.language || navigator.userLanguage).substring(0,2);
    /** list of IANA language tags used by browsers here:
    * http://www.iana.org/assignments/language-subtag-registry/language-subtag-registry
    *
    * zh -> Chinese (macrolanguage tag)
    * vi -> Vietnamese
    * lha -> Laha (Viet Nam)
    * nut -> Nung (Viet Nam)
    */
    var languageUsing = (_.contains(_.values(config.languages), languageActual) ? languageActual : config.defaultLanguage);
    $translateProvider.preferredLanguage(languageUsing);
    $translateProvider.fallbackLanguage('en');
}]).config(['$logProvider', function($logProvider) {
    $logProvider.debugEnabled(true);
}]).run(['$rootScope', '$state', '$cookies', '$http', 'authService', 'OTIEvents', 'OTIUserService',
    function($rootScope, $state, $cookies, $http, authService, OTIEvents, OTIUserService) {
}]);
