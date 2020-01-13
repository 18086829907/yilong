//动态加载产品
function lineCommodityPosition(lineFirstNum, lineLastNum, lineHeight) {
    var num = 200;
    for (var j = lineFirstNum; j <= lineLastNum; j++) {
        $('#No{0}'.format(j)).css('left', num + 'px').css('top', lineHeight + 'px');
        num += 240
    }
}
function loadCommodity(pageNumber, page){
    $('#commodity').remove();
    $('#main').append($('<div id="commodity"></div>'));
    var commodity = $('#commodity');
    $.ajax({
        type:'get',
        url:'json\\commodityInformation.json',
        dataType:'json',
        success:function(data, status){
            var info = $.parseJSON(data);
            var commodityArray = info[pageNumber][page];
            for (var i=0; i<commodityArray.length; i++){
                var picture  = commodityArray[i]['No.'+(i+1)]['picture'];
                var commodityName = commodityArray[i]['No.'+(i+1)]['commodityName'];
                var commodityAttr = commodityArray[i]['No.'+(i+1)]['commodityAttr'];
                var price = commodityArray[i]['No.'+(i+1)]['price'];
                var discount = commodityArray[i]['No.'+(i+1)]['discount'];
                var originalPrice = commodityArray[i]['No.'+(i+1)]['originalPrice'];
                var advantage = commodityArray[i]['No.'+(i+1)]['advantage'];
                var policy = commodityArray[i]['No.'+(i+1)]['policy'];
                var commodityNode = '<a href="#"><div id="No{0}" class="commodity"><div class="pic"><img src="{1}" width="105" height="105" alt=""></div><div class="title">{2}</div><div class="attr">{3}</div><div class="price"><div class="l">￥<span>{4}</span></div><div class="r"><span class="discount">{5}</span><del class="orig">{6}</del></div></div><div class="advantage">{7}</div><div class="policy">{8}</div></div></a>'.format(i+1, picture, commodityName, commodityAttr, price, discount, originalPrice, advantage, policy);
                commodity.append(commodityNode)
                // commodity.append($('<div id="No{0}" class="commodity"><div class="pic"><img src="{1}" width="105" height="105" alt=""></div><div class="title">{2}</div><div class="attr">{3}</div><div class="price"><div class="l">￥<span>{4}</span></div><div class="r"><span class="discount">{5}</span><del class="orig">{6}</del></div></div><div class="advantage">{7}</div><div class="policy">{8}</div></div>'.format(i+1, picture, commodityName, commodityAttr, price, discount, originalPrice, advantage, policy)))
            }
            var a = 1;
            var b = 5;
            var c = 540;
            for (var k=1 ; k<=20; k++){
                lineCommodityPosition(a, b, c);
                a += 5;
                b += 5;
                c += 310;
            }
        }
    });
}

$(function () {
    //页面加载完，调用此方法动态加载产品
    loadCommodity(0,'0page')
});


//设置翻页
$('#page li:nth-child(2)').addClass('green');
$('#page ul').on('click', 'li:not(#next,#previous)', function(){
    var pageNum = $(this).text();
    var current = parseInt(pageNum) + 1;
    // console.log($('#page li:nth-child({0})'.format(current)));
    $('#page li').removeClass('green');
    $('#page li:nth-child({0})'.format(current)).addClass('green');
    var pageNumber = pageNum - 1;
    var page = pageNum - 1 + 'page';
    loadCommodity(pageNumber, page);
});

$('#page li:first').click(function(){
    var current = $('.green').text();
    if (current === '1_冬季电动车儿童护膝保暖骑车加厚摩托车挡风被防水布男女小孩护腿.html'){
        current = '10'
    }
    $('#page li').removeClass('green');
    $('#page li:nth-child({0})'.format(current)).addClass('green');
    console.log(current-2);
    var pageNumber = current-2;
    var page = current-2 + 'page';
    loadCommodity(pageNumber, page);
});

$('#page li:last').click(function(){
    var current = $('.green').text();
    // console.log(parseInt(current));
    if (current === '9'){
        current = '0'
    }
    $('#page li').removeClass('green');
    $('#page li:nth-child({0})'.format(parseInt(current)+ 2)).addClass('green');
    console.log(parseInt(current));
    var pageNumber = parseInt(current);
    var page = parseInt(current) + 'page';
    loadCommodity(pageNumber, page);
});




