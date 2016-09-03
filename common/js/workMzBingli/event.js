$(function(){

    //当前页面主导航位置高亮显示
    var index = window.location.href.split('/').length - 2;                 //当前页面的href位置
    var href = window.location.href.split('/')[index];                      //当前页面的href值
    $(".main-nav-li a[href^='" + href + "']").addClass("main-nav-on");
    

    //鼠标划入主导航栏下级子导航出现
    var mainNavLis = $(".main-nav .main-nav-li ");
    mainNavLis.hover(function () {
        $(this).find(".sub-nav").stop().slideDown();
    }, function () {
        $(this).find(".sub-nav").stop().slideUp();
    });


    //点击菜单显示相应的基本资料/病历类/非病历类详情
    var mainMenu = $(".main-menu ul li");
//    var detailInfo = $(".detail-info>div");

//    mainMenu.eq(1).addClass("on");                                 //基本资料菜单栏添加下划线样式
//    detailInfo.eq(1).show();                                       //基本资料详情显示
    mainMenu.click(function () {
//        var index = $(this).index();                                 //将菜单栏的索引值赋给具体详情
        $(this).addClass("on").siblings().removeClass("on");         //给点击的菜单栏添加下划线样式并移除同胞元素的样式
//        detailInfo.eq(index).show().siblings().hide();
    });


    //鼠标滑过预约信息框，出现查看详情
    var reserveBox=$(".detail-info .reserve-box");
    reserveBox.hover(function(){
        $(this).find(".reserve-status").css("display","block");
        $(this).find(".user-name").css("visibility","hidden");      //visibility为隐藏时元素位置仍然保留
        $(this).find(".recep-time").css("visibility","hidden");
       
    },function(){
        $(this).find(".reserve-status").css("display","none");
        $(this).find(".user-name").css("visibility","visible");
        $(this).find(".recep-time").css("visibility","visible");
        
    });
    
    
    //用户未上传病历时删除翻页按钮
    var blBox=$(".bl-box");
    if(blBox.length<=0){
    	$("div#pagination").remove();
        $(".bingli").text("此用户尚未上传病历!")

    }
    
    //上传图片
    $(".uploadBtn").click(function () {
        $(".uploadInput").click();
    });


   /* var commentBtn=$("ul.comment .comment-btn");
    var comentInput=$(".comment-input");
    alert(comentInput.length)
    commentBtn.click(function () {
        var index=$(this).index();
        comentInput.eq(index).slideDown(500)
    })*/



});

//验证输入页数
function checkGoBtn(){
	var goPage=$("input.goPage");
	var numReg=/^[0-9]+$/g;							//纯数字正则表达式							
	var numRegOk=numReg.test(goPage.val());			
    if(goPage.val()==""||goPage.val()==0||!numRegOk){
    	return false;
    }
}

