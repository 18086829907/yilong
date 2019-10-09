//加载完毕触发事件
window.onload = function(){alert('页面加载完毕')};

//滚轮滚动触发事件
window.onscroll = function(){
    console.log('发生了滚动事件');
    var scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
    console.log('滚动条的高度：%d', scrollTop);
};

//窗口大小改变触发事件
window.onresize = function(){
    var w = document.documentElement.clientWidth || document.body.clientWidth || window.innerWidth;
    var h = document.documentElement.clientHeight || document.body.clientWidth || window.innerWidth;
    console.log('宽：%dpx 高：%d',w,h)
};

//间歇式定时器
var time;
function myTimerIntermittent(){
    time = window.setInterval(function(){
        console.log('justin')
    }, 2000);
}

//定时器清除
function myClearTime(){
    window.clearInterval(time)
}

//延时定时器
function myTimerDelay(){
    window.setTimeout(function(){
        console.log('justin');
    },3000);
}
