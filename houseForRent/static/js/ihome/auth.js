function showSuccessMsg() {
    $('.popup_con').fadeIn('fast', function() {
        setTimeout(function(){
            $('.popup_con').fadeOut('fast',function(){}); 
        },1000) 
    });
}

$(document).ready(function(){
   // e.preventDefault();
    alert("form-auth");
   $('#form-auth').submit(function(e){ // 注意空格不能多打，尤其是.与其他部分之间（不能打）
      alert("auth-submit");
      e.preventDefault();  // 不加该句会提交两次  第二次real_id_card值为空  且键为id-card,而非real_id_card
      real_name = $('#real-name').val();
      real_id_card = $('#id-card').val();
      alert(real_name);
      alert(real_id_card);
      $.ajax({
         url:'/user/auth/',
         type:'POST',
         dataType:'json',
         data:{'real_name':real_name,'real_id_card':real_id_card},
         success:function (data) {
             alert(data.code);
            if(data.code=='200'){
                alert("成功了成功了！！");
                 $('.error-msg').hide();
                showSuccessMsg();
                location.href = "/user/my/";
            }else if(data.code=='1008'){
                alert("信息不全信息不全");
                $('.error-msg').show();
                // location.href = "/user/auth/"
            }else if(data.code=='1009'){
                alert("身份证参数错误");
                 $('.error-msg').hide();  //除了信息不全，其他地方需隐藏红色提示字
                // location.href = "/user/auth/"
            }
         },
         error:function (data) {
             alert("实名认证失败")
         }
      });
   });
});

