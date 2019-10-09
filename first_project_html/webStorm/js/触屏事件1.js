$(function(){
    //按下事件
    $('#d1').on('touchstart',function(e){
        console.log('按下事件');


    });
    //抬起事件
    $('#d1').on('touchend',function(){
        console.log('抬起事件')
    });
    //移动事件
    $('#d2').on('touchmove',function(e){
        console.log('手指移动');
        console.log(e.changedTouches)
    });
    //跟踪小球
    $(document).on('touchstart',function(e){
        $('#d3').css('display','block');
        var touch = e.touches[0];
        $('#d3').css('left',touch.pageX - $('#d3')[0].offsetWidth/2 + 'px');
        $('#d3').css('top',touch.pageY - $('#d3')[0].offsetHeight/2 + 'px');
    });
    $(document).on('touchmove',function(e){
        var touch = e.touches[0];
        $('#d3').css('left',touch.pageX - $('#d3')[0].offsetWidth/2 + 'px');
        $('#d3').css('top',touch.pageY - $('#d3')[0].offsetHeight/2 + 'px');
    });
    $(document).on('touchend', function(){
       $('#d3').css('display','none')
    })
});