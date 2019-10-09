var jsRotationChart = document.getElementById('rotationChart');
var jsPic = document.getElementById('pic');
var jsLeft = document.getElementById('left1');
var jsRight = document.getElementById('right1');
var jsList = document.getElementById('list1');
var jsListAllArr = jsList.childNodes;

//获得ul中的所有li
var jsListArr = [];
for (i in jsListAllArr){
    if (jsListAllArr[i].nodeType === 1){
        jsListArr.push(jsListAllArr[i])
    }
}

//进入后第一个li的背景为红色
jsListArr[0].style.backgroundColor = 'red';

//轮播图动起来及红点跟随
var currentPage = 1;
function changePage(){
    if (currentPage === 9){
        currentPage = 1;}
    else if (currentPage === 0){
        currentPage = 8;
    }
    jsPic.src = "img/童装店/轮播图/" + currentPage + ".jpg";
    for (var i = 0; i < jsListArr.length; i++){
        jsListArr[i].style.backgroundColor = '#aaa';
    }
    jsListArr[currentPage - 1].style.backgroundColor = 'red';
}
function rotationStart(){
    currentPage++;
    changePage();
}
var timer = window.setInterval(rotationStart,1000);


//鼠标进入停止轮播及显示按钮
function rotationStop(){
    clearInterval(timer);
    jsLeft.style.display = 'block';
    jsRight.style.display = 'block';
}
jsRotationChart.addEventListener('mouseover', rotationStop, false);

//鼠标离开继续轮播
function rotationReStart(){
    timer = window.setInterval(rotationStart,1000);
    jsLeft.style.display = 'none';
    jsRight.style.display = 'none';
}
jsRotationChart.addEventListener('mouseout', rotationReStart, false);

//进入按钮颜色加深
function deepColor(){
    this.style.backgroundColor = 'rgba(0,0,0,0.6)'
}
jsLeft.addEventListener('mouseover', deepColor,false);
jsRight.addEventListener('mouseover', deepColor,false);
//离开按钮颜色变浅
function shallowColor(){
    this.style.backgroundColor = 'rgba(0,0,0,0.2)'
}
jsLeft.addEventListener('mouseout', shallowColor,false);
jsRight.addEventListener('mouseout', shallowColor,false);
//点击jsRight显示下一页
function nextPage(){
    currentPage++;
    changePage()
}
jsRight.addEventListener('click', nextPage,false);

//点击jsLeft显示上一页
function previousPage(){
    currentPage--;
    changePage()
}
jsLeft.addEventListener('click', previousPage,false);

//进入哪个红点切换哪张图片
function modifyPage(){
    currentPage = this.index;
    changePage()
}

for (var i=0; i<jsListArr.length; i++){
    jsListArr[i].index = i + 1; //新增自定义属性
    jsListArr[i].addEventListener('mouseover', modifyPage, false);
}