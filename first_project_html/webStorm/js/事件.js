//1、事件添加

//box2
//导入事件函数
function func2(){
    alert('触发事件2')
}

//box3
//this作为实参传入函数，目的是定位属性函数，接收的形参指代this标记的标签节点
function func3(tagNode){
    console.log(this);
    alert('触发事件3');
    tagNode.style.backgroundColor = 'yellow';
}

//box4
//设置事件函数
var box4 = document.getElementById('box4');
box4.onclick = function(){
    this.style.backgroundColor = 'red'; //在事件函数中指代获取的标签节点
    alert('触发事件4')
};
//清除事件
// box4.onclick = null;

//box5
//添加事件函数监听
var box5 = document.getElementById('box5');
function event_1(){
    this.style.backgroundColor = 'green'; //this在事件监听函数体中指代获取的标签本身
}
function event_2(){
    this.style.borderRadius = '90px'; //this在事件监听函数体中指代获取的标签本身
}
//添加第一个事件
box5.addEventListener('click', event_1, false);
//添加第二个事件
box5.addEventListener('click', event_2, false);
//清除事件
// box5.removeEventListener('click', event1, false);


//2、具体事件

//聚焦事件
var inputTagNode = document.getElementById('target1');
function event1(){
    this.style.border='2px solid red'; //事件函数中的this指代的添加事件函数的标签节点本身
    console.log('聚焦事件');
}
function event2(){
    this.style.border='2px solid green';
    console.log('离焦事件');
}
inputTagNode.addEventListener('focus', event1, false);
inputTagNode.addEventListener('blur', event2, false);

//单击与双击同时作用于一个标签节点对象
var target2 = document.getElementById('target2');
var time;
function event3(){
    clearTimeout(time);
    time = window.setTimeout(function(){console.log('单击')},300);
}
function event4(){
    clearTimeout(time);
    console.log('双击');
}
target2.addEventListener('click', event3, false);
target2.addEventListener('dblclick', event4,false);

//鼠标事件
var target3 = document.getElementById('target3');
var target4 = document.getElementById('target4');
var target5 = document.getElementById('target5');
var target6 = document.getElementById('target6');
var target7 = document.getElementById('target7');

function event5(){
    this.style.backgroundColor='#567939';
}
function event6(){
    this.style.fontSize = '20px';
}
function event7(){
    this.style.fontSize = '14px';
}
function event8(e){
    console.log(e);
    // console.log(e.pageX, e.pageY, e.screenX, e.screenY, e.clientX, e.clientY, e.offsetX, e.offsetY);
    console.log('鼠标移动事件');
}

target3.addEventListener('mouseover', event5, false);
target4.addEventListener('mouseout', event5, false);
target5.addEventListener('mousedown', event6, false);
target6.addEventListener('mouseup', event7, false);
target7.addEventListener('mousemove', event8,false);

//键盘事件
function event9(e){
    console.log(e.key, e.keyCode, e.ctrlKey, e.altKey, e.shiftKey);
}
document.addEventListener('keydown', event9,false);
document.addEventListener('keyup', event9,false);
document.addEventListener('keypress', event9,false);

//验证事件流顺序
var target8 = document.getElementById('target8');
var target9 = document.getElementById('target9');
var target10 = document.getElementById('target10');

function event10(){
    console.log('一')}
function event11(){
    console.log('二')}
function event12(){
    console.log('三')}

target8.addEventListener('click', event10, true);
target9.addEventListener('click', event11, true);
target10.addEventListener('click', event12, true);

//阻止事件流

document.body.onclick = function(){this.style.backgroundColor = 'yellow'};
document.getElementById('target11').onclick = function(e){
    e.stopPropagation(); //屏蔽冒泡
    this.style.backgroundColor = '#178494';
};
document.getElementById('target13').onclick = function(e){
    e.stopPropagation();
    var info = window.confirm('您浏览的页面存在风险，是否继续？');
    if (info === false){
        //屏蔽跳转的默认行为
        e.preventDefault();
    }};