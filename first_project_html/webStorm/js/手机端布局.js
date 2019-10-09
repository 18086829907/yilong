$(function(){
    $('html').css('font-size', parseInt($('html').css('width'))/10 + 'px');
});

// $('html').resize(function(){
//     var html_size = parseInt($('html').css('width'))/10 + 'px';
//     $('html').css('font-size',html_size);
// })
//真正的移动端开发第一是不用以上方法来适配屏幕大小的，一般都是用media标签，还有如果要用这里的方法适配，其实也不用写resize事件，因为没有人的品目可以改变大小触发此事件执行
