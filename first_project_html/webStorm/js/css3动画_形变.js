$(function(){
    $('html').css('font-size',parseInt($('html').css('width'))/10 + 'px');
    var n,rotateX,rotateY,rotateZ,zoomX,zoomY,zoomZ,forwardX,forwardY,forwardZ,T,recovery,rotateInterval,zoomInterval,forwardInterval;
    T = $('#d1');
    rotateX = $('#someButton input:eq(0)');
    rotateY = $('#someButton input:eq(1)');
    rotateZ = $('#someButton input:eq(2)');
    zoomX = $('#someButton input:eq(3)');
    zoomY = $('#someButton input:eq(4)');
    zoomZ = $('#someButton input:eq(5)');
    forwardX = $('#someButton input:eq(6)');
    forwardY = $('#someButton input:eq(7)');
    forwardZ = $('#someButton input:eq(8)');
    recovery = $('#someButton input:eq(9)');

    rotateX.on('click',function(){
        clearInterval(rotateInterval);
        n = 0;
        rotateInterval = setInterval(function(){
            n += 1;
            T.css('transform','rotateX({0}deg)'.format(n));
            if (n === 180){
                clearInterval(rotateInterval)
            }
        },10)
    });

    rotateY.on('click',function(){
        clearInterval(rotateInterval);
        n = 0;
        rotateInterval = setInterval(function(){
            n += 1;
            T.css('transform','rotateY({0}deg)'.format(n));
            if (n === 180){
                clearInterval(rotateInterval)
            }
        },10)
    });

    rotateZ.on('click',function(){
        clearInterval(rotateInterval);
        n = 0;
        rotateInterval = setInterval(function(){
            n += 1;
            T.css('transform','rotateZ({0}deg)'.format(n));
            if (n === 180){
                clearInterval(rotateInterval)
            }
        },10)
    });

    zoomX.on('click', function(){
        clearInterval(zoomInterval);
        n = 1;
        zoomInterval = setInterval(function(){
            n -= 0.01;
            T.css('transform','scaleX({0})'.format(n));
            if (n < 0.5){
                clearInterval(zoomInterval);
            }
        },10)
    });

    zoomY.on('click', function(){
        clearInterval(zoomInterval);
        n = 1;
        zoomInterval = setInterval(function(){
            n -= 0.01;
            T.css('transform','scaleY({0})'.format(n));
            if (n < 0.5){
                clearInterval(zoomInterval);
            }
        },10)
    });

    zoomZ.on('click', function(){
        clearInterval(zoomInterval);
        n = 1;
        zoomInterval = setInterval(function(){
            n -= 0.01;
            T.css('transform','scaleZ({0})'.format(n));
            if (n < 0.5){
                clearInterval(zoomInterval);
            }
        },10)
    });

    forwardX.on('click', function(){
        clearInterval(zoomInterval);
        n = 0;
        forwardInterval = setInterval(function(){
            n += 0.1;
            T.css('transform','translateX({0}rem)'.format(n));
            if (n > 5){
                clearInterval(forwardInterval);
            }
        },10)
    });

    forwardY.on('click', function(){
        clearInterval(zoomInterval);
        n = 0;
        forwardInterval = setInterval(function(){
            n += 0.1;
            T.css('transform','translateY({0}rem)'.format(n));
            if (n > 6){
                clearInterval(forwardInterval);
            }
        },10)
    });

    forwardZ.on('click', function(){
        console.log('1');
        clearInterval(zoomInterval);
        n = 0;
        forwardInterval = setInterval(function(){
            n -= 0.1;
            T.css('transform','translateZ({0}rem)'.format(n));
            if (n < 0.01){
                clearInterval(forwardInterval);
            }
        },10)
    });

    recovery.on('click',function(){
        clearInterval(rotateInterval);
        clearInterval(zoomInterval);
        T.css('transform','rotateX(0deg) rotateY(0deg) rotateZ(0deg)');
        T.css('transform', 'scaleX(1)').css('transform', 'scaleY(1)').css('transform', 'scaleZ(1)')
    })
});