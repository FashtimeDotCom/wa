var thisHOST=document.location.host;
var thisHREF=document.location.href;
Common.addClassOnNavigation(window.location);
$(document).ready(function() {
    //搜索引擎
    $("#search_btn").click(function(){
        var search_val=$("#search_val").val();
        window.open("http://www.baidu.com/s?wd=" + search_val + "+site%3A" + self.location.origin);
    });


    //文章页面左侧导航列表样式更换
    var news_li_url = $(".menu ul").children("li").children("a");
    var news_li_length = news_li_url.length;
    for(var a=0;a<news_li_length;a++){
        if(thisHREF.indexOf(news_li_url[a]) == 0){
            $(".menu ul").children("li").eq(a).addClass("active");
        }
    }
});
