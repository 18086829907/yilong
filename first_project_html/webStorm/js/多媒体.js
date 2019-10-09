$(function(){
    var video = $('video');
    var playButton = $('#someButton input:eq(0)');
    var pauseButton = $('#someButton input:eq(1)');
    var muteButton = $('#someButton input:eq(2)');
    var fullScreenButton = $('#someButton input:eq(3)');
    var pro = $('#someButton progress');
    var ran = $('#someButton input:eq(4)');

//播放
    playButton.on('click', function(){
        video[0].play();
        playButton.attr('disabled',true);
        pauseButton.attr('disabled',false);
        setInterval(function(){
            pro.attr('max',video[0].duration);
            pro.attr('value',video[0].currentTime);
        },100)
    });

//暂停
    pauseButton.attr('disabled',true);
    pauseButton.on('click', function(){
        video[0].pause();
        playButton.attr('disabled',false);
        pauseButton.attr('disabled',true)
    });

//静音
    var vol;
    muteButton.on('click',function(){
        if (video[0].muted === false){
            vol = ran.val();
            ran.val(0);
            video[0].muted = true;

        }else{
            video[0].muted = false;
            ran.val(vol);

        }
    });

//全屏
    fullScreenButton.on('click',function(){
        video[0].webkitRequestFullScreen()
    });

//音量设置
    video[0].volume = ran.val()/100;
    ran.on('change',function(){
        video[0].volume = ran.val()/100;
        console.log(ran.val())
    });
});