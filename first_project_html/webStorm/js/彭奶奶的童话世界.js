//创建促销信息节点
var aNewTagNode = document.createElement('a');
aNewTagNode.id = 'promotion';
aNewTagNode.innerHTML = '今日大促销：全场5折，点击查看爆促商品';
aNewTagNode.href = '#';

//插入节点
var logoColumnTagNode = document.getElementById('logoColumn');
var searchTagNode = document.getElementById('searchColumn');
logoColumnTagNode.insertBefore(aNewTagNode, searchTagNode);

//定时器
var colorArray = ['#ccc400','#3ab053','#3f9ad5','#e73441'];
window.setInterval(function(){
    var color = colorArray[parseInt(Math.random()*3)];
    aNewTagNode.style.backgroundColor = color;
},500);