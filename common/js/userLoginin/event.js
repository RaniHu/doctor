/**
 * Created by Administrator on 2016/4/30 0030.
 */

//获取双字节的字符长度
function getLength(str) {
    return str.replace(/[^\x00-\xff]/g, "xx").length;                                         // \x00-xff代表单字节字符。
}

var nameReg = /[^\u4e00-\u9fa5]/g;                                                            //用户名为非中文的正则表达式
var emailReg = /^\w+((-\w+)|(\.\w+))*\@[A-Za-z0-9]+((\.|-)[A-Za-z0-9]+)*\.[A-Za-z0-9]+$/;     //正确邮箱正则表达式
var chineseReg = /[\u4e00-\u9fa5]/g;                       //密码为中文的正则表达式;
var pwdReg = /[^A-Za-z0-9]/g;                              //密码不是大小写字母加数字的正则表达式
var regL = /^[a-zA-Z]+$/g;                                 //密码为纯字母的正则表达式
var regN = /^[0-9]+$/g;                                    //密码为纯数字的正则表达式


$(function () {

    //获取用户页面可视高度
    var H=$(window).height();
    $(".main").css("height",H);
    $(document.body).css("overflow","hidden");

    //注册验证
    var username = $("input#name");                           //真实姓名
    var email = $("input#email");                             //邮箱
    var pwd1 = $("input#pwd1");                               //初次密码
    var pwd2 = $("input#pwd2");                               //确认密码
    var msg = $("div.msg");                                   //提示框
    var msgTxt = $(".msg .msgTxt");                           //提示文字
    var msgIcon = $(".msg .msg-icon");                        //错误提示图标
    var correctIcon = $(".input-filed .correct-icon");        //正确提示图标

    //提示信息
    function prompt() {
        msg.slideDown(500);
        msgIcon.attr("src", "/static/image/userLoginin/prompt-icon.png");
    }
    //错误信息
    function error(obj) {
        msg.slideDown(500);
        msgIcon.attr("src", "/static/image/userLoginin/error.png");
        obj.css("border", "1px red solid");

    }
    //正确信息
    function correct(obj) {
        msg.slideUp(500);
        obj.css("border", "1px silver solid");

    }


    //用户名验证
    //得到焦点
    username.focus(function () {
        prompt();
        msgTxt.html("真实姓名必须为2-4个中文字符");
    });

    //失去焦点
    username.blur(function () {
        //真实姓名为空
        if (username.val() == "") {
            error(username);
            msgTxt.html("真实姓名不能为空");
            correctIcon.css("display","none");

        }
        //真实姓名不是中文
        else if (nameReg.test(username.val())) {
            error(username);
            msgTxt.html("含有非法字符");
            correctIcon.css("display","none");

        }
        //姓名长度超过4位或小于2位
        else if (getLength(username.val()) > 8 || getLength(username.val()) < 4) {
            error(username);
            msgTxt.html("真实姓名长度应为2-4个字符");
            correctIcon.css("display","none");

        }
        //输入合法
        else {
            correct(username);
            correctIcon.eq(0).attr("src", "/static/image/userLoginin/correct.png");
            correctIcon.css("display","block");

        }

    });


    //邮箱验证
    //纯数字，纯字母，带下划线_，带点.，带连接线-,邮箱域至少一个.和两个单词，不得特殊字符开头
    //失去焦点
    email.blur(function () {
        var emailOk = emailReg.test($(this).val());
        //邮箱为空
        if (email.val() == "") {
            error(email);
            msgTxt.html("邮箱不能为空");
            correctIcon.css("display","none");

        }
        //邮箱格式错误
        else if (!emailOk) {
            error(email);
            msgTxt.html("请输入有效的邮箱");
            correctIcon.css("display","none");

        }
        //邮箱正确
        else {
            correct(email);
            correctIcon.eq(1).attr("src", "/static/image/userLoginin/correct.png");
            correctIcon.css("display","block");

        }
    });


    //密码验证
    //离开键盘
    pwd1.keyup(function () {
        prompt();
        msgTxt.html("6至16个字符,大小写字母和数字组成");
    });

    //失去焦点
    pwd1.blur(function () {
        //密码为空
        if (pwd1.val() == "") {
            error(pwd1);
            msgTxt.html("密码不能为空");
            correctIcon.css("display","none");

        }
        //密码不符合大小写加数字
        else if (pwdReg.test(pwd1.val())) {
            error(pwd1);
            msgTxt.html("密码应由大写、小写字母和数字组成");
            correctIcon.css("display","none");

        }
        //密码不能全为数字
        else if (regN.test(pwd1.val())) {
            error(pwd1);
            msgTxt.html("密码不能全为数字");
            correctIcon.css("display","none");

        }
        //密码不能全为字母
        else if (regL.test(pwd1.val())) {
            error(pwd1);
            msgTxt.html("密码不能全为字母");
            correctIcon.css("display","none");

        }
        //密码不能包含中文
        else if (chineseReg.test(pwd1.val())) {
            error(pwd1);
            msgTxt.html("密码不能使用中文字符");
        }
        //密码长度少于6位或超过16位
        else if (getLength(pwd1.val()) > 16 || getLength(pwd1.val()) < 6) {
            error(pwd1);
            msgTxt.html("密码长度应在6-16位之间");
            correctIcon.css("display","none");

        }
        //密码正确
        else {
            correct(pwd1);
            correctIcon.eq(2).attr("src", "/static/image/userLoginin/correct.png");
            correctIcon.css("display","block");

        }

    });


    //再次确认密码
    //失去焦点
    pwd2.blur(function () {
        //两次密码不一致
        if (pwd2.val() != pwd1.val()) {
            error(pwd2);
            msgTxt.html("两次密码不一致");
            correctIcon.css("display","none");

        }
        //密码长度少于6位或超过16位/密码为空
        else if (getLength(pwd2.val()) > 16 || getLength(pwd2.val()) < 6||pwd2.val()=="") {
            error(pwd2);
            msgTxt.html("密码长度应在6-16位之间");
            correctIcon.css("display","none");
        }
        else if(regN.test(pwd2.val())||regL.test(pwd2.val())||chineseReg.test(pwd2.val())){
            error(pwd2);
            msgTxt.html("密码不能相同");
            correctIcon.css("display","none");
        }

        //输入正确
        else {
            correct(pwd2);
            correctIcon.eq(3).attr("src", "/static/image/userLoginin/correct.png");
            correctIcon.css("display","block");

        }
    });
});

//提交表单时检查
function checkForm(){
    var username = $("input#name");                           //真实姓名
    var email = $("input#email");                             //邮箱
    var pwd1 = $("input#pwd1");                               //初次密码
    var pwd2 = $("input#pwd2");                               //确认密码
    var msg = $("div.msg");                                   //提示框
    var emailOk = emailReg.test(email.val());
    if(username.val()==""||nameReg.test(username.val())||getLength(username.val()) > 8 || getLength(username.val()) < 4){
       username.css("border", "1px red solid");
        return false;
    }
    if(email.val()==""||!emailOk){
        email.css("border", "1px red solid");
        return false;
    }
    if(pwd1.val()==""||getLength(pwd1.val()) > 16 || getLength(pwd1.val()) < 6||pwdReg.test(pwd1.val())||regN.test(pwd1.val())||regL.test(pwd1.val())||chineseReg.test(pwd1.val())){
        pwd1.css("border", "1px red solid");
        return false;
    }
    if(pwd2.val()==""||pwd2.val() != pwd1.val()||getLength(pwd2.val()) > 16 || getLength(pwd2.val()) < 6||pwdReg.test(pwd2.val())||regN.test(pwd2.val())||regL.test(pwd2.val())||chineseReg.test(pwd2.val())){
        pwd2.css("border", "1px red solid");
        return false;
    }
}



