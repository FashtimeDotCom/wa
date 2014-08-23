//终端浏览器内核判断
//function browserRedirect() {
//    var sUserAgent = navigator.userAgent.toLowerCase();
//    var bIsIpad = sUserAgent.match(/ipad/i) == "ipad";
//    var bIsIphoneOs = sUserAgent.match(/iphone os/i) == "iphone os";
//    var bIsMidp = sUserAgent.match(/midp/i) == "midp";
//    var bIsUc7 = sUserAgent.match(/rv:1.2.3.4/i) == "rv:1.2.3.4";
//    var bIsUc = sUserAgent.match(/ucweb/i) == "ucweb";
//    var bIsAndroid = sUserAgent.match(/android/i) == "android";
//    var bIsCE = sUserAgent.match(/windows ce/i) == "windows ce";
//    var bIsWM = sUserAgent.match(/windows mobile/i) == "windows mobile";
//    if (!(bIsIpad || bIsIphoneOs || bIsMidp || bIsUc7 || bIsUc || bIsAndroid || bIsCE || bIsWM) ){
//        window.location.href="www.baidu.com";
//    }
//}
//browserRedirect();

$(document).ready(function(){

    //响应式
    window.onresize = function(){
        var w=window.innerWidth
            || document.documentElement.clientWidth
            || document.body.clientWidth;
        var li_sum_width = 0;
        var li_width = 0;
        $("#nav-wrapper .nav ul li").each(function(){
            li_width = $(this).width();
            li_sum_width = li_width+li_sum_width;
        })
        var empty_width = w - li_sum_width;
        var li_length = $("#nav-wrapper .nav ul li").length;
        var li_empty_width = empty_width/li_length;
        var min_li_empty_width = (w-$("#nav-wrapper .nav ul li").eq(0).width()-$("#nav-wrapper .nav ul li").eq(1).width()-$("#nav-wrapper .nav ul li").eq(2).width()-$("#nav-wrapper .nav ul li").eq(3).width())/4;
        $("#nav-wrapper .nav ul").css("width",w);
        if(li_empty_width < min_li_empty_width){
            li_empty_width = min_li_empty_width;
        };
        //logo文字大小
        if((w-150) >= $(".logo span").width()){
            $(".logo span").css("width",w-150);
            $(".logo span").css("font-size","30px");
            $(".logo span").css("line-height","78px");
        }
        if((w-150) < $(".logo span").width()){
            $(".logo span").css("width",w-150);
            $(".logo span").css("font-size","20px");
            $(".logo span").css("line-height","39px");
        };
        //导航大小
        $("#nav-wrapper .nav ul li").each(function(){
            $("#nav-wrapper .nav ul li").css("padding-left",li_empty_width/2);
            $("#nav-wrapper .nav ul li").css("padding-right",li_empty_width/2);
        });
        //轮播图片大小
        $(".slider ul li").each(function(){
            $(this).find("img").css("width",w);
        });
        //搜索框大小
        $(".search_modal input").css("width",w-152);
        //文章图片大小的限制
        $(".article_box .article img").css("max-width",w-50);
    };
    window.onresize();
    $(window).resize(function(){
        window.onresize();
    });

    //搜索引擎
    var thisHOST=document.location.host;
    $("button#search_btn").click(function(){
        var search_val=$("input#search_val").val();
        window.open("http://www.baidu.com/s?wd=" + search_val + "+site%3A" + self.location.origin);
    });
    $("#search_icon").click(function(){
        $("em.square").slideToggle();
        $("div.search_modal").slideToggle();
    });

    //页面最后一个模块组件样式
    $("#main div.index_box:last").addClass("last_box map");
    $("#main div.introduction_box:last").addClass("last_box");

    //内容页图片的缩镜
    $(".article_box .article p img").parent().css("text-indent","0px");
});