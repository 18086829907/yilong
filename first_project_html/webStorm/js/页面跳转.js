function toBlue(){
    window.location.href = 'blue.html';
}

function toGreen(){
    window.location.assign('green.html');
}

function toRed(){
    window.location.assign('red.html');
    // window.location.replace('red.html'); 无历史记录的加载
}

//上一页
function toBack(){
    window.history.back();
}

//下一页
function toForWard(){
    window.history.forward();
}

//回到主页
function toMainPage(){
    window.history.go(-(window.history.length - 1));
}

function printLenHistory(){
    console.log(window.history.length);
}

//打开或跳转新窗口网页
//参数
//  url/.html
//  openMode打开方式
//      'self'/'blank'
//  大小位置
//      'width=400px, height=400px, top=20px, left=20px'
function openNewWindow(url, openMode, sizePosition){
    window.open(url, openMode, sizePosition);
}

//关闭窗口
function closeWindow(){
    window.close();
}