//html中打印
    //document.write("js文件1");
//控制台中打印
    //console.log("js文件2");
//提示框中打印
    //alert("js文件3");
//定义变量
    //var a;
    //console.log(a);
//查看变量数据类型的操作符
    //console.log(typeof(a));
//运算
    //var num1 = 10;
    //var num2 = 10;
    //var sum = num1 + num2;
    //console.log('sum =',sum);
//拼接
    //console.log('sum = ' + sum);
//类型转换
    //console.log(sum.toString());
//数字类型的特殊值
    //var num1 = 1e309;
    //console.log(num1);
    //var num2 = Infinity;
    //var num3 = num2 + 1
    //console.log(num3)
//数字类型的特殊值
    //var num1 = NaN;
    //console.log(typeof(num1));
    //console.log(typeof(NaN));
//定义字符串
    //var str1 = 'justin';
    //console.log(str1)
//定义布尔值
    //var t = true;
    //var f = false;
//真值和假值
//假值：
    //0
    //0.0
    //""
    //NaN
    //undefined
    //false
    //null
//真值：除了假值的值
//prompt框
    //var num = parseInt(prompt('请输入数字：'));
    //console.log(num);
//自增自减少
    //var num1 = 10;
    //var num2 = 10;

    //var a = num1++;
    //console.log(a);
    //console.log(num1);

    //var b = ++num2;
    //console.log(b);
    //console.log(num2);

//if语句
    //if(1){console.log('justin');}

//判断偶数
    //var a = parseInt(prompt('请输入偶数：'));
    //if(a % 2 == 0)
        //{console.log('得到的是偶数')}
    //else
        //{console.log('得到的是奇数')};

//关系运算符
    //console.log(1 == 1);
    //console.log(1 == '1');
    //console.log(1 === '1');

//三目表达式
    //console.log(1?2:3)

//switch语句
//     var a = parseInt(prompt("请输入1-7的数字"));
//     switch (a){
//         case 1:
//             console.log('周一');
//             break;
//         case 2:
//             console.log('周二');
//             break;
//         case 3:
//             console.log('周三');
//             break;
//         case 4:
//             console.log('周四');
//             break;
//         case 5:
//             console.log('周五');
//             break;
//         case 6:
//             console.log('周六');
//             break;
//         case 7:
//             console.log('周日');
//             break;
//         default:
//             console.log('请输入1-7的数字')
//             break;
//     }

//do-while语句
//    var num = 1;
//    var sum = 0;
//    do{
//        sum += num;
//        num++;
//      }while(num<=10);
//    console.log(sum);

//for语句
//    var num = 1;
//    var sum = 0;
//    for (console.log('开始计算1到10之和'); num<=10; num++)
//        {sum += num}
//    console.log(sum);

//for语句死循环
//    var a = 1;
//    for(;;){
//        console.log('一直打印1');
//        console.log('一直打印2');
//    }

//break语句
//    示例1
//        var a = 1;
//        while(a<=10){
//            a++;
//            if(a === 5){
//                break;
//            }
//        }
//        console.log(a);
//    示例2
//         var sum = 0;
//         for (var a=1; a<=10; a++){
//             sum += a;
//             if (a === 5){
//                 break;
//             }
//         }
//         console.log(sum);
//continue语句
//    示例1
//         var a = 0;
//         while(a <= 9){
//             a++;
//             if(a === 5){
//                 continue;
//             }
//             console.log(a);
//         }
//    示例2
//         var sum = 0;
//         for(var a = 1; a<=9; a++){
//             sum += a;
//             if(a === 5){
//                 continue;
//             }
//             console.log(sum)
//         }

//for-in语句
//     var arr1 = [1,2,3,4,5];
//     var arr2 = ['a','b','c','d','e'];
//     for(var i in arr2){
//         console.log('index:'+i+' '+'value:'+arr2[i]);
//     }
//练习
//     var str1 = prompt('请输入英文句子');
//     var count=0;
//     for (var i in str1){
//         count+=1;
//     }
//     console.log(count);
//无参无返回
//    function name(){
//            console.log('justin')
//        }
//    a = name();
//    console.log(a);
//有参有返回
//    function sum1(num1,num2,num3){
//            var a = num1 + num2 + num3;
//            return a
//        }
//    var b = sum1(1,2,3);
//    console.log(b);
//多实参调用
//     function sum(num1, num2, num3){
//         var a = num1 + num2 + num3;
//         for (var i=0; i<arguments.length; i++){
//             console.log(arguments[i])
//         }
//         return a;
//     }
//
//     var b = sum(1,2,3,4,5,6,7);
//     console.log(b);
//变量的作用域
//     var num1=0;
//     function func(){
//         var num2 = 10;
//         console.log(num2);
//         num1 = 10;
//     }
//
//     func();
//     console.log(num1);
//     console.log(num2); 局部变量不能在外部调用
//变量提升
//         function func(){
//             console.log(a);
//             var a = 10;
//             console.log(a);
//             p = 10;
//         }
//         func();
//         console.log(p);
//函数也是一种数据
//     function func(){
//         var a = 10;
//         console.log(a);
//     }
//
//     var b = func;
//     b();
//函数也可以当成参数
//     function mySum(num1, num2){
//         var a = num1 + num2;
//         return a;
//     }
//     var b = mySum;
//     console.log(b(1,2));
//     function myFunc(s,a,b){
//         return s(a,b);
//     }
//     console.log(myFunc(b, 1,2));
//匿名函数
//     var f = function(a,b){return a+b};
//     function mySum(f,a,b){
//         var c = f(a,b);
//         return c
//     }
//     console.log(mySum(f, 1, 2));
//匿名函数可以写在外层函数的调用中，当成参数传入主函数中
//     function func(num1, num2, fc){
//         return fc(num1, num2)
//     }
//     var a = func(1,2,function (num1,num2) {
//         return num1 + num2;
//     });
//     console.log(a);
//即时函数
//    console.log((function(a,b){return a+b})(2,2))
//    var arr=['a','b','c','d','e'];
//    for (var i in arr){
//        console.log(arr[i])
//    }
//数组创建
//     var a = new Array(1,2,3,'abc');
//     console.log(a);
//     var b = [1,2,3,'abc'];
//     console.log(b);
//     var c = new Array(5);
//     console.log(c);
//     c[0] = 1;
//     console.log(c);
//     c[99] = 1;
//     console.log(c);
//数组长度的改变
//     var arr = new Array(1,2,3,4,5);
//     console.log(arr);
//     console.log(arr.length);
//     arr.length =10;
//     console.log(arr);
//     arr.length = 3;
//     console.log(arr);
//     arr[20] = 1;
//     console.log(arr);
//     delete arr[1];
//     console.log(arr);
//数组遍历3
//     arr.forEach(function(item){console.log(item)});
//数组的方法
//     var arr = new Array(1,2,3,4,5);
//     arr.push(6,7);
//     arr.unshift('a', 'b');
//     arr.pop();
//     arr.shift();
//     var arr1 = arr.join(',');
//     arr.reverse();
//     var arr2 = arr.slice(1, 3);
//     var arr3 = arr.splice(1, 3);
//     arr.splice(1, 0, 'b', 'b');
//     var arr4 = arr2.concat(arr3);
//     var index = arr.indexOf('b');
//     var lastIndex = arr.lastIndexOf(1);
//     console.log(arr);
//     console.log(arr1);
//     console.log(arr2);
//     console.log(arr3);
//     console.log(arr4);
//     console.log(index);
//     console.log(lastIndex);
//数组的排序
//     var arr = [5,3,2,4,1];
//     for (var i=0; i<(arr.length-1); i++){
//         for (var j=0; j<(arr.length-1-i); j++){
//             if (arr[j] - arr[j+1] > 0){
//                 var tempty = arr[j];
//                 arr[j] = arr[j+1];
//                 arr[j+1] = tempty;
//             }
//         }
//     }
//     console.log(arr);
//自定义排序规则
//     var arr = new Array('awfrq', 'sds', 'asdfff', 'ds', 'd');
//     arr.sort(function(x,y){return y.length - x.length});
//     arr.sort(function(x,y){return x.length - y.length});
//     console.log(arr);
//字符串
//     var str1 = 'justin';
//     var str2 = new String('justin')
//     str1[0] = 'z';
//     console.log(str1);
//     console.log(str2);
//     console.log(typeof(str1));
//     console.log(typeof(str2));
//Math对象
//     console.log(Math.random());
//     console.log(parseInt(Math.random()*(6 - 2 +1) + 2));
//设置时间
//    var d = new Date();
//    console.log(d);
//时间对象的方法
//     d.getFullYear();
//     d.getMonth();
//     console.log(d.getDate());
//     console.log(d.getDay());
//     d.getHours();
//     d.getMinutes();
//     d.getSeconds();
//     d.getMilliseconds();
//     d.getTime();
//BOM
//     console.log(window.document);
//     window.frames
//     window.navigator
//     window.screen
//     console.log(window.location);
//     window.history
