$(function(){
    //给导航标签增加抬起事件
    $('ul:first li').on('touchend',function(e){
        var label = e.changedTouches[0].target.innerHTML;
        if (label === '娱乐八卦'){
            console.log($('.con li:eq(0)')[0].offsetLeft);
        }
        else if (label === '军事'){
            // $('.con li:eq(1)')[0].offsetLeft;
            // console.log($('.con li:eq(1)')[0].style.transform='translate(100px)');
            $('.con').css('transform','translate(-100px)')
        }
    });

    $('.con li:eq(1)').on('touchmove',function(e){
        e.changedTouches[0].pageX = 0;
    });

    // $('.con').on('touchmove',function(e){
    //     // console.log($('.con')[0]);
    //     console.log(e.changedTouches[0].pageX = 100);
    // });
});