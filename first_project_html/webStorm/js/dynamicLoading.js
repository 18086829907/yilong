$('#button1').bind('click', function(){
   //点击按钮发送网络请求
    $.ajax({type:'get',
        data:{a:'1', b:'2'},
        url:'http://192.168.0.102:8090/json/caidanJson.json',
        success:function (data, textStatus) {
            var caiDanArray = data['breakfast_menu']['food'];
            console.log(caiDanArray);
            for (var i=0; i<caiDanArray.length; i++){
                $('#d'+(i+1)).append($('<h1>' + caiDanArray[i]['name'] + '</h1>')).fadeIn(1000);
                $('#d'+(i+1)).append($('<p>' + caiDanArray[i]['description'] + '</p>')).fadeIn(1000);
                $('#d'+(i+1)).append($('<p>' + caiDanArray[i]['calories'] + '</p>')).fadeIn(1000);
                $('#d'+(i+1)).append($('<p>' + caiDanArray[i]['price'] + '</p>')).fadeIn(1000);
            }
        }
    })
});