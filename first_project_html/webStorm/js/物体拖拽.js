function objectDragAndDrop(idName) {
    var target = document.getElementById(idName);
    var baseX = 0;
    var baseY = 0;
    var moveX = 0;
    var moveY = 0;
    function myEvent2(e){
        var ee = e;
        moveX = ee.pageX - baseX;
        baseX = ee.pageX;
        moveY = ee.pageY - baseY;
        baseY = ee.pageY;
        target.style.left = target.offsetLeft + moveX + 'px';
        target.style.top = target.offsetTop + moveY + 'px';
    }
    function myEvent1(e){
        var ev = e;
        baseX = ev.pageX;
        baseY = ev.pageY;
        target.addEventListener('mousemove', myEvent2, true)
    }
    target.addEventListener('mousedown', myEvent1, true);
    document.addEventListener('mouseup', function(){
        target.removeEventListener('mousemove', myEvent2, true);
    }, true);
    return [target, target.offsetLeft, target.offsetTop]
}
// var target = document.getElementById('target');
// objectDragAndDrop(target);