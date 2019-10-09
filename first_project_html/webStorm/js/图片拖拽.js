var jsD1 = document.getElementById('d1');
var jsD2 = document.getElementById('d2');
var jsImg = document.getElementById('img');

jsImg.ondragstart = function(e){ //图片开始拖拽时开始触发此事件
    var data = e.dataTransfer; //获取图片数据
    data.setData('text/plain', this.id); //将数据设置成文本并加上id
};

jsD2.ondragover = function(e){ //有元素被拖拽进入时，触发此事件
    e.preventDefault() //阻止div的默认行为——不让其他模块放置
};

jsD2.ondrop = function(e){ //元素被拖拽到此并放下时触发此事件
    var data = e.dataTransfer; //获取图片数据
    var text = data.getData('text/plain'); //获取文本格式的数据的id
    e.target.appendChild(document.getElementById(text)) //e.target为进入目标dom，给其添加id为text的dom
};

jsD1.ondragover = function(e){ //有元素被拖拽进入时，触发此事件
    e.preventDefault() //阻止div的默认行为——不让其他模块放置
};

jsD1.ondrop = function(e){ //元素被拖拽到此并放下时触发此事件
    var data = e.dataTransfer; //获取图片数据
    var text = data.getData('text/plain'); //获取文本格式的数据的id
    e.target.appendChild(document.getElementById(text)); //e.target为进入目标dom，给其添加id为text的dom
};