function pzjcFunc(jsTarget1, jsTarget2){
    var jsT1Left = jsTarget1.offsetLeft;
    var jsT1Right = jsTarget1.offsetLeft + parseInt(window.getComputedStyle(jsTarget1, null).width);
    var jsT1Top = jsTarget1.offsetTop;
    var jsT1Bottom = jsTarget1.offsetTop + parseInt(window.getComputedStyle(jsTarget1, null).height);

    var jsT2Left = jsTarget2.offsetLeft;
    var jsT2Right = jsTarget2.offsetLeft + parseInt(window.getComputedStyle(jsTarget2, null).width);
    var jsT2Top = jsTarget2.offsetTop;
    var jsT2Bottom = jsTarget2.offsetTop + parseInt(window.getComputedStyle(jsTarget2, null).height);

    if (!(jsT1Left > jsT2Right || jsT1Right < jsT2Left || jsT1Top > jsT2Bottom || jsT1Bottom < jsT2Top)){
        return true
    }else{
        return false
    }
}