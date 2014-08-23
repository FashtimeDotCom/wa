Common.addClassOnNavigation(window.location);
$(document).ready(function(){
    $(".lightbox b a").lightbox({
        fitToScreen: false,
        imageClickClose: false
    });

   //tab切换
    $("#tab_li ul li").click(function(){
        $(this).addClass("active").siblings().removeClass();
        var li_num = $(this).index();
        $("#list_zoom").children("div").eq(li_num).addClass("table_con active").siblings().removeClass("active");
    });
});
