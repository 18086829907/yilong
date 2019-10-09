//获取滚动高度
function $scrollTop(){
    return document.documentElement.scrollTop || document.body.scrollTop;
}

//根据id获取标签节点
function $(idName){
    return document.getElementById(idName);
}

//获取可视化窗口的宽度
function $w(){
    return document.body.width || document.documentElement.width || window.innerWidth;
}

function $h(){
    return document.body.height || document.documentElement.height || window.innerHeight;
}

//随机颜色
function randomColor(alph){
    //rgba(255,255,255,0.1)
    var r = parseInt(Math.random()*256);
    var g = parseInt(Math.random()*256);
    var b = parseInt(Math.random()*256);
    var a = alph;
    return 'rgba(' + r + ',' + g + ',' + b + ',' + a + ')'
}

//获取样式
function getStyle(tagNode, style){
    if (tagNode.currentStyle){
        //ie
        return tagNode.currentStyle[style];
    }else{
        return window.getComputedStyle(tagNode, null)[style];
    }
}
