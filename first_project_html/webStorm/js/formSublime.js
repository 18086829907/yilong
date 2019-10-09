//非序列化表单提交
    // $(function () {
    //    $('#button').bind('click', function(){
    //        $.ajax({
    //            type:'post',
    //            url:'#',
    //            data:{
    //                username:$('#username').val(),
    //                sex:$('#sex').val(),
    //                age:$('#age').val(),
    //                email:$('#email').val(),
    //                address:$('#address').val(),
    //                content:$('#content').val()
    //            },
    //            dataType:'json',
    //            success:function(data,textStatus){
    //                console.log(textStatus);
    //                var html = '';
    //                html += '用户名：' + data.username + '<br>';
    //                html += '性别' + data.sex + '<br>';
    //                html += '年龄' + data.age + '<br>';
    //                html += '邮箱' + data.email + '<br>';
    //                html += '内容' + data.content + '<br>';
    //                $('#responseText').html(html);
    //
    //            }
    //        })
    //    })
    // });

//序列化提交表单
$(document).ajaxStart(function(){
    $('#msg').html('正在获取数据...').slideDown(1000)
});

$(document).ajaxStop(function(){
    $('#msg').html('数据已经加载完毕').slideUp(2000)
});

$(function () {
    $('#button').bind('click', function(){
        $.ajax({
            type:'post',
            url:'#',
            data:$('#testForm').serialize(),
            dataType:'json',
            success:function(data,textStatus){
                console.log(textStatus);
                var html = '';
                html += '用户名：' + data.username + '<br>';
                html += '性别' + data.sex + '<br>';
                html += '年龄' + data.age + '<br>';
                html += '邮箱' + data.email + '<br>';
                html += '内容' + data.content + '<br>';
                $('#responseText').html(html);

            }
        })
    })
});