//创建挡板
var barTagNode = document.getElementById('bar');
function bar(e){
    barTagNode.style.left = e.clientX - 50 + 'px';
    barTagNode.style.top = e.clientY + 'px';}
document.addEventListener('mousemove', bar,false);//鼠标移动事件

//控制按钮
var speed = 0;
function control(e){
    if (e.key === 'd'){
        speed += 1;
    }
    if (e.key === 'a'){
        if (speed > 0){
            speed -= 1;
        }
        else{
            speed = 0;
        }
    }
    if (e.key === 's'){
        var num1 = 0;
        var num2 = 0;
        window.setInterval(function(){
            var barLeft = parseInt(window.getComputedStyle(barTagNode,null).left);
            var barTop = parseInt(window.getComputedStyle(barTagNode, null).top);
            console.log(barTop);
            var ball = document.getElementById('ball');
            var ballLeft = parseFloat(window.getComputedStyle(ball, null).left);
            var ballTop = parseFloat(window.getComputedStyle(ball, null).top);
            console.log(ballTop);
            //left
            //控制left反弹
            if (ballLeft >= 1503 || ballLeft <= 0){
                num1 += 1;}
            //修改left
            if (num1 % 2 === 0){
                ball.style.left = ballLeft + speed + 'px';}
            else{
                ball.style.left = ballLeft - speed + 'px';}
            //top
            //控制top反弹
            if (ballTop >= 880 || ballTop <= 0 || (ballTop + 100 > barTop && (ballLeft > barLeft - 100 && ballLeft < barLeft + 100))){
                num2 += 1;}
            //修改top
            if (num2 % 2 === 0){
                ball.style.top = ballTop + speed + 'px';}
            else{
                ball.style.top = ballTop - speed + 'px';}
            if (ballTop >= 870){
                alert('游戏结束');
                return 0
            }
        },10);

    }
}
document.addEventListener('keydown', control, false);

//随机颜色编码
function randColorCode(){
    var colorCode = '';
    for (var i = 0; i < 6; i++){
        var code = parseInt(Math.random()*10);
        colorCode += code;
    }
    return colorCode;
}

