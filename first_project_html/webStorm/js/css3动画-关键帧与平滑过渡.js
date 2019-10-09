$(function(){
    $('#box input:eq(0)').on('click', function(){
        $('#d2').css('animation','myColor 5s linear 0s infinite alternate')
    });

    $('#box input:eq(1)').on('click',function(){
       $('#d3').css('animation','myMove 5s linear 0s 2 alternate')
    })


});