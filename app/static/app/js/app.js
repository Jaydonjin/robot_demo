/**
 * Created by jj51 on 2017/4/22.
 */
angular.module('myApp', [])
    .factory('dfisSimpleURL', function () {
        var BASE_URL = "http://st01nbx01/api_ai_backend/api";

        return {
            base: BASE_URL
        }
    })
    .factory('dfisSimpleCenter', function ($http, $q, dfisSimpleHTTP, dfisSimpleURL) {
        var send_message = function (body) {
            return dfisSimpleHTTP.send(dfisSimpleURL.base, dfisSimpleHTTP.POST, body)

        };
        return {
            send_message: send_message
        }
    })
    .directive('ngEnter', function () {
        return function (scope, element, attrs) {
            element.bind("keyup", function (event) {
                if (event.which === 13) {
                    scope.$apply(function () {
                        scope.$eval(attrs.ngEnter);
                    });
                    event.preventDefault();
                }
            });
        };
    })
    .factory('dfisSimpleHTTP', function ($http, $timeout, $q, dfisSimpleURL) {
        var HTTP_DELETE = 'DELETE';
        var HTTP_GET = 'GET';
        var HTTP_POST = 'POST';
        var HTTP_PUT = 'PUT';

        function TaskPump() {
            this.tasks = new Array();
        }

        TaskPump.prototype.push = function (task) {
            this.tasks.push(task)
        };
        TaskPump.prototype.pop = function () {
            return this.tasks.pop();
        };

        var pump = new TaskPump();

        function loop() {
            var task = pump.pop();
            if (task === undefined) {
                $timeout(loop, 1000);
                return;
            }
            $http(task.params)
                .then(function successCallback(response) {
                    $timeout(loop, 1);
                    return task.deferred.resolve(response);
                }, function failedCallback(response) {
                    $timeout(loop, 1);
                    return task.deferred.resolve(response);
                });
        }

        // start event poll
        $timeout(loop, 1);

        var send_http = function (url, method, data, hideloading) {
            data = data && JSON.parse(JSON.stringify(data));
            method = method || HTTP_GET;
            if (hideloading == undefined) {
                hideloading = true
            }
            else {
                hideloading = hideloading;
            }
            var base = dfisSimpleURL.base;
            //url = [base, encodeURI(url)].join('');
            var deferred = $q.defer();
            pump.push({params: {method: method, url: url, data: data, hideLoading: hideloading}, deferred: deferred});
            return deferred.promise;
        };
        return {
            GET: HTTP_GET,
            POST: HTTP_POST,
            PUT: HTTP_PUT,
            DELETE: HTTP_DELETE,
            send: send_http
        }
    })
    .controller('SimpleCtrl', function ($scope, dfisSimpleCenter) {
        $scope.message = "";
        var hello_message = "hello";
        $scope.source = [{"message": hello_message}];
        var session_id = "";
        $scope.on_send_message = function () {
            if ($scope.input_message) {
                if ($scope.source.length % 2 === 1) {
                    var current_message = {"message": $scope.input_message};
                    $scope.source.push(current_message);
                    var body;
                    if ($scope.source.length > 1) {
                        body = {"query_string": $scope.input_message, "session_id": session_id};
                    } else {
                        body = {"query_string": $scope.input_message, "session_id": null}
                    }
                    dfisSimpleCenter.send_message(body)
                        .then(function (response) {
                            if (response.status == 200) {
                                var tmp = {"message": response.data.response_string};
                                session_id = response.data.session_id;
                                $scope.source.push(tmp)
                            }
                        });
                }
                else {
                    //negAlert.info("Please wait for me to answer the last question !", 5)
                }
            } else {
                //negAlert.info("Please tell me what you want to know !", 5)
            }
            $scope.input_message = "";
        };
    });