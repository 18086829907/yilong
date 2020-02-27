//创建一个标签节点
var spanTagNode = document.createElement('span');
spanTagNode.innerHTML = '输出城市名即可';
spanTagNode.style.position = 'absolute';
spanTagNode.style.border = 'solid 2px #000';
spanTagNode.style.borderRadius = '20px';
spanTagNode.style.left = '900px';
spanTagNode.style.top = '260px';
spanTagNode.style.backgroundColor = '#234525';
spanTagNode.style.padding = '0 10px';
spanTagNode.style.display = 'none';

//插入标签节点
var fomr1 = document.getElementById('form1');
var s3_in1 = document.getElementById('s3_in1');
fomr1.insertBefore(spanTagNode, s3_in1);

//设置聚焦和离焦事件
function event1(){
    spanTagNode.style.display = 'inline-block';
}
function event2(){
    spanTagNode.style.display = 'none';
}
s3_in1.addEventListener('focus', event1,false);
s3_in1.addEventListener('blur', event2, false);
