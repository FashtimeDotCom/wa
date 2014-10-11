/**
 * Created by apple on 14-10-10.
 */


function HeadController($scope) {
    $scope.site = {
        title :'test test',
        logo : 'http://offlintab.firefoxchina.cn/static/img/search/baidu_web.png'
    }
}

function HeaderController($scope) {
    HeadController($scope)
}


function SidebarController($scope, $http) {
/*    $scope.menu = [
        {
            href:'http://baidu.com',
            name:'baidu'
        }
    ]
*/
    $http.get('./menu').success(function (data, status, headers, config) {
        $scope.menu = angular.fromJson(data)
    })
}

function ContainerController($scope) {

}

function FooterController($scope) {

}
