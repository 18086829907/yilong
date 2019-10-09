//1、获取标签节点

//a id获取标签
var div1TagNode = document.getElementById('div1');
console.log(div1TagNode);
console.log([div1TagNode]); //对象形式打印
console.log(typeof(div1TagNode));

//b class获取标签
var div2TagNodeArray = document.getElementsByClassName('div2');
console.log(div2TagNodeArray);
console.log(typeof(div2TagNodeArray));

//c name获取标签
var inputTagNodeArray = document.getElementsByName('inputText');
console.log(inputTagNodeArray);

//d tagName获取标签
var jsAllDivsArray = document.getElementsByTagName('div');
console.log(jsAllDivsArray);

//2、获取属性节点


//获取属性节点
//标签节点.getAttributeNode('属性名')
var inputTagNode = document.getElementById('in');
var attributeNode = inputTagNode.getAttributeNode("type");

//a 获得官方属性的值
//标签节点.属性名
var typeNode = inputTagNode.type;
var placeholderNode = inputTagNode.placeholder;

//修改值
function changeAttributeValue(){
    inputTagNode.placeholder = '我是世界上最帅的人'
}

//b 获取自定义属性值
//标签节点.getAttribute(自定义属性名)
var selfNode = inputTagNode.getAttribute('my');
console.log(selfNode);
//修改值
inputTagNode.setAttribute('my','我是最帅的人');


//c 移除属性
//标签节点.removeAttribute('属性名')
inputTagNode.removeAttribute('my');


//3、获取文本节点
//标签节点.innerHTML
var jsDivBox = document.getElementById('innerHTML');
console.log(jsDivBox.innerHTML);
console.log(jsDivBox.outerHTML);
console.log(jsDivBox.innerText);
jsDivBox.innerHTML = '<h1>我是盒子它兄弟</h1>';

//4、获取修改样式
//a 改变行间样式
function changeInnerStyle(){
    var divLineStyleTagNode = document.getElementById('lineStyle');
    var colorCode = randColorCode();
    divLineStyleTagNode.style.backgroundColor = '#' + colorCode;
    divLineStyleTagNode.style.width = "200px";
    divLineStyleTagNode.style.height = "200px";
}

//b 获取外部样式
var outerStyleTabNode = document.getElementById('outerStyle');
var wbc = window.getComputedStyle(outerStyleTabNode, null).backgroundColor;
var ww = window.getComputedStyle(outerStyleTabNode, null).width;
var wh = window.getComputedStyle(outerStyleTabNode, null).height;

//c 改变外部样式
function changeOuterStyle(){
    var divOuterStyleTagNode = document.getElementById('outerStyle');
    var colorCode = randColorCode();
    divOuterStyleTagNode.style.backgroundColor = '#' + colorCode;
    divOuterStyleTagNode.style.width = "200px";
    divOuterStyleTagNode.style.height = "200px";
    }

//随机颜色编号
function randColorCode(){
    var colorCode = '';
    for (var i = 0; i < 6; i++){
        var code = parseInt(Math.random()*10).toString();
        colorCode += code;
    }
    return colorCode;
}

//随机数字符串
function randNumStr(count){
    var randNumStr = parseInt(Math.random()*9 + 1).toString();
    for (var i = 0; i < count - 1; i++){
        var numStr = parseInt(Math.random()*10).toString();
        randNumStr += numStr;
    }
    return randNumStr;
}

//节点的常用属性
var inputComAttTagNode = document.getElementById('comAtt');
var inputComAttAttributeNode = inputComAttTagNode.getAttributeNode('placeholder');
console.log(inputComAttTagNode.nodeName, inputComAttTagNode.nodeType, inputComAttTagNode.nodeValue);
console.log(inputComAttAttributeNode.nodeName, inputComAttAttributeNode.nodeType, inputComAttAttributeNode.nodeValue);

//层次关系属性
var tagNode = document.getElementById('parent');
var allChildNode = tagNode.childNodes;
var fristChildNode = tagNode.firstChild;
var lastChildNode = tagNode.lastChild;
var rootNode = tagNode.ownerDocument;
var parentNode = tagNode.parentNode;
var previousNode = tagNode.previousSibling;
var nextNode = tagNode.nextSibling;
var allAttribuleNodeArray = inputComAttTagNode.attributes;
console.log(allAttribuleNodeArray[3]);

//动态操作
//创建节点
var newPTagNode = document.createElement('p');
newPTagNode.id = 'idPStyle';
newPTagNode.className = 'pStyle';
newPTagNode.style.backgroundColor = '#224455';
newPTagNode.innerHTML = '我是被动态加载的';
console.log(newPTagNode);

//获取TagNode
var divDynamicTagNode = document.getElementById('dynamic');
var p1TagNode = document.getElementById('p1');
var p2TagNode = document.getElementById('p2');

//添加节点
// divDynamicTagNode.appendChild(newPTagNode); //插入到最后一个子节点

//插入节点
// divDynamicTagNode.insertBefore(newPTagNode, p2TagNode);

//替换节点
divDynamicTagNode.replaceChild(newPTagNode, p2TagNode);




