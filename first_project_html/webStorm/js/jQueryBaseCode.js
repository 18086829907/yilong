//DOM对象转JQ对象
var jsD1 = document.getElementById('d1');
var jqD1 = $(jsD1);

//JQ对象集转DOM对象
var jqD2 = $('#d2');
var jsD2 = jqD2[0];
console.log(jqD2);

//选择器
//id选择器
var jqBox = $('#d1');
jqBox.attr('class','c1');

//元素选择器
var jqDivs = $('div');

//类名选择器
var jqdivs = $('.c3');

//复合选择器
var jqFhs = $('.c3,p,div');

//通配符
var jqall = $('*');

//后代选择器
var jqP = $('#d3 p');

//子代选择器
var jqChild = $('#d3>p');

//弟弟选择器
var jqYB = $('#p1+span');

//弟弟们选择器
var jqYBs = $('#p1~span');

//首项选择过滤器
var jqFirst = $('.pp:first');

//末项选择过滤器
var jqLast = $('.pp:last');

//偶数选择过滤器
//索引值从零开始计算
var jqEven = $('div:even');

//奇数选择过滤器
//索引值从零开始计算
var jqOdd = $('div:odd');

//索引选择过滤器
var jqEq = $('div:eq(1)');

//大于范围选择过滤器
var jqGt = $('div:gt(0)');

//小于范围选择过滤器
var jqLt = $('div:lt(2)');

//标题选择过滤器
var jqHeader = $(':header');

//过滤器
var jqNot = $(':header:not(h2)');

//文本包含选择器
var jqPJustin = $("p:contains('justin')");

//空文本选择器
var jqEmpty = $(':header:empty');

//非空元素选择器（父级元素选择器）
var jqParent = $('div:parent');

//包含元素选择器
var jqHas = $('div:has(p)');

//显示元素选择器
var jqVisible = $(':visible');

//隐藏元素选择器
var jqHidden = $('input:hidden');

//表单选中元素选择器
var jqChecked = $('input:checked');

//表单不可用元素选择器
var jqDisabled = $('input:disabled');

//表单可用元素选择器
var jqEnabled = $('input:enabled');


//下拉菜单被选中元素选择器
var jqSelected = $('select option:selected');

//下拉菜单值变化事件触发的函数
function selectVal(){
    var jqSelected = $('select option:selected');
    // console.log(jqSelected.val())
}
$('select').bind('change',selectVal);

//首子选择器
var jqFirstChild = $('#d5 p:first-child');

//末子选择器
var jqLastChild = $('#d5 p:last-child');

//独子选择器
var jqOnlyChild = $('div p:only-child');

//下标子选择器
//注：下标从1开始
var jqIndexChild = $('#d5 p:nth-child(1)');

//偶数子选择器
//注：下标从1开始
var jqEvenChild = $('#d5 p:nth-child(even)');

//属性选择器
var jqAttr = $('input[type="checkbox"]');

//input选择器
var jqInput = $(':input');

//普通按钮选择器
var jqButton = $(':button');

//复选框选择器
var jqCheckbox = $(':checkbox');

//文件域选择器
var jqFile = $(':file');

//常用方法
//.val设置value
var jqSelect = $('select');

//新增元素
var jqNewP = $('<p id="p1">justin</p>');

//末尾插入元素
// $('div:last').append(jqNewP);

//首项插入元素
// $('div:last').prepend(jqNewP);

//删除节点
$('#d5 span').remove();
$('.pp:last').empty();

//复制节点
$('#d5 p').bind('click',function(){
    $(this).clone(true).insertAfter($(this));
});

//替换节点
$('#d5 p:last').replaceAll($('#d5 p'));

//替换节点
$('input[type="button"]').replaceWith('<input type="button" value="可用按钮">');

//遍历节点
$('#d5 p').each(function(index){$(this).attr('title','我是第'+(index+1)+'个')});

//事件绑定
//方式一
// $('#d6 p').click(function(){console.log($(this).html())});
//方式二
// $('#d6 p').bind('click',function(){console.log($(this).html())});
//问题，无法给尚未存在的标签添加事件
// $('button:last').click(function(){$('#d6').append($('<p>我是新的p</p>'))});
//方式三
$('#d6').delegate('p', 'click', function(){console.log($(this).html())});

//模拟用户点击
var a = $('#b1').bind('click', function(e, mag1, mag2){console.log(mag1, mag2)});
a.trigger('click', ['justin', 'good']); //模拟人点击按钮

//阻止默认行为
$('a').bind('click', function(){console.log('123')}).trigger('click');

//模拟悬停事件
$('#b1').hover(function(){console.log('鼠标移入')},function(){console.log('鼠标移出')});

//事件对象
$('#div1').bind('click', function(e){console.log(e.relatedTarget)});

//阻止事件冒泡
$('#d1').bind('click', function(e){
    $(this).css('background-color','blue');
    e.stopPropagation() //阻塞冒泡事件
});
// $('body').bind('click', function(){$(this).css('background-color','red')});


//动画
//隐藏
$('#b3').bind('click', function(){
    $('#d7').hide(1000, function(){console.log('动画隐藏')})
});

//显示
$('#b4').bind('click',function(){
    $('#d7').show(1000, function(){
        console.log('动画显示')
    })
});

//淡入淡出
$('#b5').bind('click', function(){
    $('#d8').fadeOut(1000, function(){
        console.log('淡出')
    })
});
$('#b6').bind('click', function(){
    $('#d8').fadeIn(1000, function(){
        console.log('淡入')
    })
});

//滑入滑出
var num = 0;
$('#b7').bind('click', function(){
    var b7 = this;
    num++;
    $('#d9').slideToggle(1000, function(){
        if (num%2 === 0){
            $(b7).text('滑出')
        }else{
            $(b7).text('滑入')
        }price

    })
});

//自定义动画
$('#d10').animate({left:"200px", top:"200px"},1000).animate({left:'400px',top:'400px'},2000);