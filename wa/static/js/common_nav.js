
/**
 * JS 常量配置对象
 * */
var CONFIG = {};


var urlCompostion = {
    protocol: /([^\/]+:)\/\/(.*)/i,
    host: /(^[^\:\/]+)((?:\/|:|$)?.*)/,
    port: /\:?([^\/]*)(\/?.*)/,
    pathname: /([^\?#]+)(\??[^#]*)(#?.*)/
};

var Common = {
    /**
     * 判断是否IE6,7,8系列浏览器
     * */
    IsIE678: function(){
        if ($.browser.msie){
            return true
        } else{
            return false;
        }
    }(),

    /*
     * 解析URL，获得URL各个部分对应的值
     * */
    parseURL: function(url) {
        var tmp, res = {};
        res['href'] = url;
        for(p in urlCompostion) {
            tmp = urlCompostion[p].exec(url);
            res[p] = tmp[1];
            url = tmp[2];
            if (url === ""){
                url = "/";
            }
            if (p === "pathname") {
                res["pathname"] = tmp[1];
                res["search"]   = tmp[2];
                res["hash"]     = tmp[3];
            }
        }
        if(CONFIG.DEBUG && !this.IsIE678){
        }
        return res;
    },

    /*
    * 网站导航条加背景色
    * */
    addClassOnNavigation: function(url) {
        var res = this.parseURL(url);
        var pathname = res['pathname'] + res['search'];
        var news_patt1=/\/aboutme\?cate_id=1&news_id=\d*/;
        var news_patt2=/\/aboutme\?cate_id=2&news_id=\d*/;
        var news_patt3=/\/aboutme\?cate_id=\d*$/;
        var navs = USER_NAVS;
        if(pathname.match(news_patt3)){
            $(".menu ul li:first").addClass("active");
        }
        if (pathname.match(news_patt1)){
            $("#title1").addClass("active");
        }
        if (pathname.match(news_patt2)){
            $("#title2").addClass("active");
        } else {
            if(pathname != "" || pathname != undefined){
                for(var i=0; i< navs.length; i++){
                    var path = navs[i];
                    if (path[0] == pathname) {
                        path[1]();
                        break;
                    }
                }
            }
        }
    }
};

