var log = {
    startday: "2021-12-7",
    endday: "2021-12/21",
    updateday: "",
    anchor: "Ken",
    arr: "",
    arr2: "",
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
    document.location.href="/t1/vocab/review_list.html";
   
}

//function review_words(word){
////     window.alert(123);
//    $("#review_words").attr("href","review_word/word");
//        console.log(word)
//}


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
            _html +='<li id="webName'+numb+'" class="webName" onclick="showWord_learn('+numb+')"><span><u>'+name+'</u></span></li>';
            _html += '<li id="webAddr'+numb+'" class="webAddr" onclick="showWord_learn('+numb+')"><span><u>'+web+'</u></span></li>';
            _html += '</ul>';
            return _html;
        }
}

var origin_website = {
    site:function(numb,name, web){
        numb += 1;
        var _html = "" ;
        _html +='<ul>';
        _html +='<li id="webName'+numb+'" class="webName"><a href="'+web+'" target="_blank">'+name+'</a></li>';
        _html += '<li id="webAddr'+numb+'" class="webAddr">'+web+'</li>';
        _html += '</ul>';
        return _html;
    }
}

var arrwebsite = [
//    {
//        name : "聽力練習",
//        web : "https://www.esl-lab.com/easy/"
//     },
//        data = {
//            name : webName,
//            addr : webAddr
//        };
]

function editdata(){
//    $(".saved_webname").text("");
    var $webdata = $(".webdata");
//    var $webName = $(".webdata #webName a");
//    var $webAddr = $(".webdata #webAddr");

//    console.log($webname.html());
    for(var j=1; j<$webdata.length+1; j++){
        var $webName = $("#webName"+j+" a").text();
        var $webAddr = $("#webAddr"+j ).text();
//        console.log(webName);
//        console.log(webAddr);
        var data = {
            name : $webName,
            addr : $webAddr
        };
        arrwebsite.push(data);
    }
//    console.log(arrwebsite);
    $(".saved_webname").text("");
    for( var j=0; j<arrwebsite.length; j++ ){
        var _HTML=edit_website.site(j, arrwebsite[j].name, arrwebsite[j].addr);
        $(".saved_webname").append(_HTML);
    }
}

function origindata(){
    $(".saved_webname").text("");
    $("#website_web_name").val(""); 
    $("#website_web_addr").val("");
//    var $webname = $(".saved_webname");
//    console.log(log.arr);
//    $webname.html(log.arr);
    for( var j=0; j<arrwebsite.length; j++ ){
        var _HTML=origin_website.site(j, arrwebsite[j].name, arrwebsite[j].addr);
        $(".saved_webname").append(_HTML);
    }
}

function showWord_learn(numb){
    for( var j=0; j<arrwebsite.length; j++ ){
//        console.log('before',numb, j);
        if (numb == j){
//            console.log('after',numb, j);
            $("#website_web_name").val(arrwebsite[j].name); 
            $("#website_web_addr").val(arrwebsite[j].addr);
            $('#website_del').focus();
            return true;
        }
        else{
            $("#website_web_name").val('Nan');
            $("#website_web_addr").val('Nan');
        }

    }
}

function btn_website_del_learn(){
    var $webname = $("#website_web_name");
    var $webaddr = $("#website_web_addr");
    var $website_del = $('#website_del');
//    console.log($webname);
//    console.log($webaddr);
    $.ajax({
        url:'/t1/vocab/learn/del_website',
        type:'post',
        datatype:'json',
        async: true,
        data : {
            webname : $webname.val(),
            webaddr : $webaddr.val(),
        },
        success: function(data){
            del_list($webname.val());
            console.log(data.result);
            $webname.val(data.rwebname);
            $webaddr.val(data.rwebaddr);
            editdata();
            $website_del.css({'background':'#efefef'});
        },
        beforeSend: function(data){
//              console.log('beforSend')
            $website_del.css({'background':'#ccc'});
        },

    })
}

function del_list(webname){
    console.log(webname)
    for(var j=0 ; j < arrwebsite.length ; j++ ){
        console.log(arrwebsite[j].name)
        if (webname == arrwebsite[j].name){
            arrwebsite.splice(j,1);
        };
    };
}

function btn_website_modify_learn(){
    var $webname = $("#website_web_name");
    var $webaddr = $("#website_web_addr");
//    var $website_modify = $('#website_modify');

    $.ajax({
        url: '/t1/vocab/learn/mod_website',
        type: 'post',
        datatype: 'json',
        async: true,
        data : {
            webname : $webname.val(),
            webaddr : $webaddr.val(),
        },
        success: function(data){
            mod_list($webname.val(),$webaddr.val());
//            console.log(data.result);
            $webname.val(data.rwebname);
            $webaddr.val(data.rwebaddr);
            editdata();
        },
    })
}

function mod_list(webname,webaddr){
    console.log('mod');
    for( j=0 ; j < arrwebsite.length ; j++){
        if (webname == arrwebsite[j].name) {
            arrwebsite[j].addr = webaddr;

        };
        console.log(arrwebsite);
    };
}

//function btn_search_index(){
//    $('#save_ok').text()="";
//    $('#rWord').text("");
//    $('#audio_path').text("");
//    $('#chinese_dic').text("");
//    $('#chinese_dic_empty').text("");
//    $('#show_pic').text("");
//
//}

function searching_index(){
    if (($('#search_word').val() == '') || ($('#search_word').val() == 'Please input your vocabulary...')){
        $('#search_word').css({'color':'#FF60AF'});
        $('#search_word').val('Please input your vocabulary...');
        return false
    }else{
//        $('#show_result').text('');

        $('#show_result').text('');
//        $('#save_ok').text('');
//        $('#rWord').text('');
//        $('.chinese_dic').text('');
        $('#btn_save_word').css({'display': 'none'});
        $('#show_pic').text('');
//        $('.imgs').text('');
        $('#search_icon').css('background','#ccc');
        $('#loading').show();
        return true
    }
}

function searchword(){
    var $search_word = $('#search_word');
        $search_word.css({'color':'black'});
        $search_word.val('');
        $search_word.attr('placeholder','');
}

function save_index(){
        //var $saveword = $("#btn_save_word");
        var $rword = $('#rWord');
        var $saveok = $('#save_ok span');
        var $chinese_dic =$('#chinese_dic li');
        var $audio_path = $('#show_result a');
        var $imgs1_path = $('#imgs1_1 img')
//        var $imgs2_path = $('#imgs1_2 img')
//        var $imgs3_path = $('#imgs2_1 img')
//        var $imgs4_path = $('#imgs2_2 img')

//        console.log($imgs1_path.attr('src'));
//        console.log($imgs2_path.attr('src'));
//        console.log($imgs3_path.attr('src'));
//        console.log($imgs4_path.attr('src'));
//        console.log($chinese_dic.text());
        $.ajax({
            url:'/t1/index/save/',
            type:'post',
            datatype:'json',
            async: true,
            data: {
                word : $rword.text(),
                audio_path : $audio_path.attr('href'),
                imgs_path : $imgs1_path.attr('src'),
            },
            success: function(data){

//                console.log(data.word);
//                console.log(data.audio_path);
//                console.log(data.imgs_path);
//                console.log(data.chinese);
//                console.log(data.mesg);
                $saveok.text(data.mesg);
                $saveok.show();
                log.submit.autohide($saveok);
//                $saveok.text('查詢結果:')
            },
//            beforeSend: function(){
//                $saveok.text();
//            },
        })
//        $saveok.text("Save OK !!");
}
function btn_reg_login(){
    document.location.href='/t1/user/register'
}

//function onSignIn(googleUser){
//        var id_token = googleUser.getAuthResponse().id_token;
//        var profile = googleUser.getBasicProfile();
//        console.log('ID: ' + profile.getId()); // Do not send to your backend! Use an ID token instead.
//        console.log('Name: ' + profile.getName());
//        console.log('Image URL: ' + profile.getImageUrl());
//        console.log('Email: ' + profile.getEmail()); // This is null if the 'email' scope is not present.
//        $.ajax({
//          type: "POST",
//          url: '/t1/user/google_sign_in',
//          data: JSON.stringify({'id_token': id_token}),
//          success: function() {
//            console.log('login success')
//          },
//          dataType: 'json',
//          contentType:"application/json",
//        });
//}