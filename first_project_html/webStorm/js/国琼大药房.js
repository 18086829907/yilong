//屏幕宽度与rem绑定
$(function(){
    $('html').css('font-size', parseInt($('html').css('width'))/10 + 'px');
});

//副导航栏二级菜单打开规则
var n;
function dropdownMenu2ClickEven(idName){
    n = 1;
    $('#{0}'.format(idName)).click(function(){
        if (n % 2 === 0){
            $('#{0}-ul'.format(idName)).css('display','none');
        }else{
            $('#{0}-ul'.format(idName)).css('display','block');
        }
        n += 1;
        return false
    });
    $(document).on('click',function(){
        $('#{0}-ul'.format(idName)).css('display','none');
    })
}

//简化代码
function clearAdd(newAddHeadLabelId,contentId){
    //清空所有新增li的active
    $('#main-right li').removeClass('active');
    //给点击的新增li增加active
    $('#{0}'.format(newAddHeadLabelId)).addClass('active');
    //清空所有的主页
    $('.well').css('display','none');
    //显示对应的主页
    $('#{0}'.format(contentId)).css('display','block');
}


//新增头标签、单击选择事件、双击关闭事件、关闭按钮事件
function tableAppendRemove(leftNavLabelId, leftNavLabelName, newAddHeadLabelId, contentId){
    var k = 1;
    //副导航栏的a绑定事件
    $('#{0}'.format(leftNavLabelId)).on('click',function(){
        //点导航栏的a第一次执行：
        if (k === 1){
            k += 1;
            //清空所有新增标签li的active
            $('#main-right li').removeClass('active');
            //插入标签li#idName，.active, 自定义属性myAttr=“{0}”.关闭按钮
            $('#main-right').append($('<li id="{0}" role="presentation" myAttr="{1}" class="myTable active"><a href="#">{2} <button type="button" class="glyphicon glyphicon-remove close"></button></a></li>'.format(newAddHeadLabelId, contentId, leftNavLabelName)));
            //清空所有的主页
            $('.well').css('display','none');
            //显示对应的主页
            $('#{0}'.format(contentId)).css('display','block');


            //单击新增头标签
            //设置延迟定时器的名字
            var time;
            //新增头标签绑定单击事件
            $('#{0}'.format(newAddHeadLabelId)).on('click',function(){
                //清除延迟定时器
                clearTimeout(time);
                //启动延迟定时器
                time = window.setTimeout(function(){
                    clearAdd(newAddHeadLabelId,contentId);
                },100);
            });

            //双击新增头标签-关闭窗口
            $('#{0}'.format(newAddHeadLabelId)).on('dblclick',function(){
                // 清除延迟定时器
                clearTimeout(time);
                //关闭对象删除
                $('#{0}'.format(newAddHeadLabelId)).remove();
                //隐藏对应的主页
                $('#{0}'.format(contentId)).css('display','none');
                //给前一个标签增加.active
                $('#main-right li:last').addClass('active');
                //让前一个主页显示
                var qianId = $('#main-right li:last').attr('myAttr');
                $('#{0}'.format(qianId)).css('display','block');
                k = 1;
            });

            //给关闭按钮绑定点击事件
            $('#{0} a button'.format(newAddHeadLabelId)).on('click',function(){
                //关闭对象删除
                $('#{0}'.format(newAddHeadLabelId)).remove();
                //隐藏对应的主页
                $('#{0}'.format(contentId)).css('display','none');
                //给前一个标签增加.active
                $('#main-right li:last').addClass('active');
                //让前一个主页显示
                var qianId = $('#main-right li:last').attr('myAttr');
                $('#{0}'.format(qianId)).css('display','block');
                k = 1;
            });
            //点导航栏的a第二次执行：
        }else{
            console.log(2);
            clearAdd(newAddHeadLabelId,contentId);
        }
    });
}

//if __name__=='__main__':
$(function(){
    //二级下拉菜单定下拉规则
    dropdownMenu2ClickEven('menu1');
    dropdownMenu2ClickEven('menu2');
    dropdownMenu2ClickEven('menu3');
    dropdownMenu2ClickEven('menu4');
    dropdownMenu2ClickEven('menu5');

    //获取所有的下拉菜单选项,并排除二级下拉按钮
    var jqleftNavLabel = $('.leftNavLabel');
    // 遍历调用函数
    for (var a=0; a<jqleftNavLabel.length; a++){
        var leftNavLabelName = jqleftNavLabel[a].innerText;
        tableAppendRemove('leftNavLabel{0}'.format(a+1), leftNavLabelName, 'newAddHeadLabel{0}'.format(a+1),'content{0}'.format(a+1));
    }//循环结束

    //常用菜单
    tableAppendRemove('cycd-btn1','商品销售','newAddHeadLabel30','content30');
    tableAppendRemove('cycd-btn2','商品入库','newAddHeadLabel18','content18');
    tableAppendRemove('cycd-btn3','验收入库单','newAddHeadLabel17','content17');
    tableAppendRemove('cycd-btn4','出库结算单','newAddHeadLabel22','content2');
    tableAppendRemove('cycd-btn5','商品字典','newAddHeadLabel2','content2');
    tableAppendRemove('cycd-btn6','根据供货单位采购','newAddHeadLabel24','content24');
    tableAppendRemove('cycd-btn7','会员资料','newAddHeadLabel9','content9');
    tableAppendRemove('cycd-btn8','操作员权限设置','newAddHeadLabel26','content126');
    tableAppendRemove('cycd-btn9','库存盘点','newAddHeadLabel40','content40');
    tableAppendRemove('cycd-btn10','调整价格','newAddHeadLabel42','content42');
    tableAppendRemove('cycd-btn11','凭处方销售登记','newAddHeadLabel37','content37');
    tableAppendRemove('cycd-btn12','系统设置','newAddHeadLabel129','content129');
    tableAppendRemove('cycd-btn13','有效期管理','newAddHeadLabel43','content43');
});