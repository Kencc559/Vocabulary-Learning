var log = {
    startday: "2021-12-7",
    endday: "2021-12/21",
    updateday: "",
    anchor: "Ken"
}
// var clr ={
//     cancle : "clr1"
// }

log.submit = {
    check: function(result){
        var _result = (result == "") ? true : false;
        return _result;
    },
    autohide: function(obj){
        setTimeout(function(){
            obj.hide();
            },2000
        )
    }

}
function check_login(){
    var $username = $("#username");
    var $password = $("#password");
    var $error1 = $("#error1");
    var $error2 = $("#error2");


    if (!log.submit.check($username.val()) && !log.submit.check($password.val())){
        return true;
    }else{
        if ($username.val() == ""){
            $error1.show();
            log.submit.autohide($error1);
            $username.focus();
            return false;
        }else{
            $error2.show();
            log.submit.autohide($error2);
            $password.focus();
            return false;
        }
    }
}

function clr_login(){
    // window.alert(123);
    $("#username").val("");
    $("#password").val("");
    $("#error3").text("");
    $("#username").focus();
}

function clr_register(){
    document.location.href="/t1/user/login";

}

function check_register(){
    var $username = $("#username");
    var $password = $("#password");
    var $username_error = $("#username_error");
    var $user_pwd_error =$(".user_pwd_error");

    if (!log.submit.check($username.val())){
        return true;
    }else{
        $username_error.text("用戶名不能空白 !!");
        $username_error.show();
        log.submit.autohide($username_error);
        $username.focus();
        return false;
    }
}
function clr_error_reg(){
    var $user_pwd_error = $(".user_pwd_error");
    $user_pwd_error.css("display","none");
}

function clr_infor(){
    document.location.href="/t1";
}

function rePage(){
    document.location.href="review_list.html";
   
}

function review_words(){
//     window.alert(123);
    $("#review_words").attr("href","review_word/");
}


function btn_edit_learnWeb(){
    $("#website_add").css('display', 'none');
    $("#website_modify").css('display','inline');
    $("#website_del").css('display', 'inline');
    $("#web_list_cancle").css('display', 'inline');
    $("#web_list_edit").css('background', '#ccc');
    $("#web_list_edit").css('border', 'none'); 
    $(".saved_webname").css('border', 'solid #ccc 3px');
    editdata();

}

function btn_cancle_learnWeb(){ 
    $("#website_add").css('display', 'inline');
    $("#website_modify").css('display','none');
    $("#website_del").css('display', 'none');
    $("#web_list_cancle").css('display', 'none');
    $("#web_list_edit").css('display', 'inline');
    $("#web_list_edit").css('background', 'none');
    $("#web_list_edit").css('border', 'solid #005ab5 2px'); 
    $(".saved_webname").css('border', 'solid #005ab5 2px');
    origindata();

}
var edit_website = {
        site:function(numb, name, web){
            var _html = "" ;
            _html +='<ul>';
            _html +='<li id="webName" class="webName" onclick="showWord_learn('+numb+')"><span><u>'+name+'</u></span></li>';
            _html += '<li class="webAddr" onclick="showWord_learn('+numb+')"><span><u>'+web+'</u></span></li>';
            _html += '</ul>';
            return _html;
        }
}

var origin_website = {
    site:function(numb,name, web){
        var _html = "" ;
        _html +='<ul>';
        _html +='<li class="webName"><a href="'+web+'" target="_blank">'+name+'</a></li>';
        _html += '<li class="webAddr">'+web+'</li>';
        _html += '</ul>';
        return _html;
    }
}

var arrwebsite = [
    {
        name : "聽力練習",
        web : "https://www.esl-lab.com/easy/"
    },
    {
        name: "單字查詢",
        web: "https://dictionary.cambridge.org/us/dictionary/english-chinese-traditional"
    },
    // {
    //     name: "單字查詢ireoireowpow",
    //     web: "https://dictionary.cambridge.org/us/dictionary/english-chinese-traditional"
    // },
    // {
    //     name: "單字查詢",
    //     web: "https://dictionary.cambridge.org/us/dictionary/english-chinese-traditional"
    // },
    // {
    //     name: "單字查詢",
    //     web: "https://dictionary.cambridge.org/us/dictionary/english-chinese-traditional"
    // },
    // {
    //     name: "單字查詢",
    //     web: "https://dictionary.cambridge.org/us/dictionary/english-chinese-traditional"
    // },
    // {
    //     name: "單字查詢",
    //     web: "https://dictionary.cambridge.org/us/dictionary/english-chinese-traditional"
    // },
    // {
    //     name: "單字查詢",
    //     web: "https://dictionary.cambridge.org/us/dictionary/english-chinese-traditional"
    // },
    // {
    //     name: "單字查詢",
    //     web: "https://dictionary.cambridge.org/us/dictionary/english-chinese-traditional"
    // },
    // {
    //     name: "單字查詢",
    //     web: "https://dictionary.cambridge.org/us/dictionary/english-chinese-traditional"
    // },
]

function editdata(){
    $(".saved_webname").text("");
    for( var j=0; j<arrwebsite.length; j++ ){
        var _HTML=edit_website.site(j, arrwebsite[j].name, arrwebsite[j].web);
        $(".saved_webname").append(_HTML);
    }
}

function origindata(){
    $(".saved_webname").text("");
    $("#website_web_name").val(""); 
    $("#website_web_addr").val(""); 
    for( var j=0; j<arrwebsite.length; j++ ){
        var _HTML=origin_website.site(j, arrwebsite[j].name, arrwebsite[j].web);
        $(".saved_webname").append(_HTML);
    }
}

function showWord_learn(numb){
    for( var j=0; j<arrwebsite.length; j++ ){
        console.log('before',numb, j);
        if (numb == j){
            console.log('after',numb, j);
            $("#website_web_name").val(arrwebsite[j].name); 
            $("#website_web_addr").val(arrwebsite[j].web); 

            return true;
        }
        else{
            $("#website_web_name").val('Nan');
            $("#website_web_addr").val('Nan');
        }

    }
}