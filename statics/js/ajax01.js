
$(function(){
    $("#username").bind("focus",function() {
        $("#username").bind("blur",function(){
            if($("#username").val()==""){
                $("#reg_submit").css("display","none");
                $("#icon01").removeClass();
                $("#icon01").addClass("error");
                $("#error_info").empty();
                $("#error_info").html("请输入用户名");
            }
            else {
                // 与后台交互
                $.ajax({
                    url: "/reg_data/",
                    type: "POST",
                    data: {username: $("#username").val()},
                    success: function (data) {
                        if (data == 1) {
                            $("#icon01").removeClass();
                            $("#icon01").addClass("tick");
                            $("#error_info").empty();
                            Password();
                        }
                        else {
                            $("#reg_submit").css("display","none");
                            $("#icon01").removeClass();
                            $("#icon01").addClass("error");
                            $("#error_info").html("该用户已存在!");
                        }
                    }
                });
            }
        });
    });
    function Password() {
        $("#password").bind("focus", function () {
            $("#password").bind("blur", function () {
                if ($("#password").val() == "") {
                    $("#reg_submit").css("display","none");
                    $("#icon02").removeClass();
                    $("#icon02").addClass("error");
                    $("#error_info").empty();
                    $("#error_info").html("请输入密码");
                }
                else if ($("#password").val().length < 6) {
                    $("#submit01").css("display","none");
                    $("#icon02").removeClass();
                    $("#icon02").addClass("error");
                    $("#error_info").empty();
                    $("#error_info").html("密码长度小于6位");
                }
                else {
                    $("#error_info").empty();
                    $("#icon02").removeClass();
                    $("#icon02").addClass("tick");
                    Confirm_Password();
                }
            });
        });
    }

    function Confirm_Password() {
        if ($("#confirm_password").val() != $("#password").val()) {
            $("#reg_submit").css("display","none");
            $("#icon03").removeClass();
            $("#icon03").addClass("error");
            $("#error_info").empty();
            $("#error_info").html("两次密码输入不一致");
        }
        $("#confirm_password").bind("focus", function () {
            $("#confirm_password").bind("blur", function () {
                if ($("#confirm_password").val() != $("#password").val()) {
                    $("#reg_submit").css("display","none");
                    $("#icon03").removeClass();
                    $("#icon03").addClass("error");
                    $("#error_info").empty();
                    $("#error_info").html("两次密码输入不一致");
                }
                else {
                    $("#error_info").empty();
                    $("#icon03").removeClass();
                    $("#icon03").addClass("tick");
                    $("#reg_submit").css("display","");
                }
            });
        });
    }
});
