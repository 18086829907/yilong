var jsBg1 = document.getElementById('bg1');
var jsBg2 = document.getElementById('bg2');
var bgTop1 = 0;
var bgTop2 = -768;

function motion(){
    bgTop1++;
    bgTop2++;
    if (bgTop1 === 768){
        bgTop1 = -768
    }else if(bgTop2 === 768){
        bgTop2 = -768
    }
    jsBg1.style.top = bgTop1 + 'px';
    jsBg2.style.top = bgTop2 + 'px';
}
var timerBack = window.setInterval(motion,10);

//飞机跟随鼠标
var jsMainScreen = document.getElementById('mainScreen');
var jsAirplane = document.getElementById('airplane');

var currentX = 0;
var currentY = 0;

function follow(e){
    currentX = e.screenX - 542;
    currentY = e.screenY - 100;
    jsAirplane.style.left = currentX + 'px';
    jsAirplane.style.top = currentY + 'px';
}
jsMainScreen.addEventListener('mousemove', follow, false);

//发射子弹
function createBullet(){
    //创建子弹
    var jsBullet = document.createElement('div');
    jsBullet.className = 'bullet';
    jsBullet.style.left = currentX + 33 + 'px';
    jsBullet.style.top = currentY - 30 + 'px';
    jsMainScreen.appendChild(jsBullet);

    //让子弹飞
    var timerBulletFly = window.setInterval(function () {
        var bulletPositionY = jsBullet.offsetTop - 30;
        jsBullet.style.top = bulletPositionY - 30 + 'px';
        if (jsBullet.offsetTop < 0){
            jsMainScreen.removeChild(jsBullet);
            clearInterval(timerBulletFly);
        }
    },100);
    jsBullet.timer = timerBulletFly;
}
var timerBullet = window.setInterval(createBullet,1000);

//出现敌机
function createEnemy(){
    //创建敌机
    var jsEnemy = document.createElement('div');
    jsEnemy.className = 'enemy';
    jsEnemy.style.left = parseInt(Math.random()*412) + 'px';
    jsEnemy.style.top = '0';
    jsMainScreen.appendChild(jsEnemy);

    //让敌机飞
    var timerEnemyFly = window.setInterval(function () {
        var enemyPositionY = jsEnemy.offsetTop + 1;
        jsEnemy.style.top = enemyPositionY + 'px';
        if (jsEnemy.offsetTop > 768){
            jsMainScreen.removeChild(jsEnemy);
            clearInterval(timerEnemyFly);
        }
    },10);
    jsEnemy.timer = timerEnemyFly;
}
var timerEnemy = window.setInterval(createEnemy,800);

// 子弹与敌机碰撞
var timerBAndEPzjc = window.setInterval(function(){
    var allEnemy = document.getElementsByClassName('enemy');
    var allBullet = document.getElementsByClassName('bullet');
    if (allEnemy.length > 0 && allBullet.length > 0){
        for (var i = 0; i<allBullet.length ; i++){
            for (var j = 0; j<allEnemy.length; j++){
                if (pzjcFunc(allBullet[i], allEnemy[j])){
                    clearInterval(allBullet[i].timer);
                    clearInterval(allEnemy[j].timer);
                    jsMainScreen.removeChild(allBullet[i]);
                    jsMainScreen.removeChild(allEnemy[j]);
                    break
                }
            }
        }
    }
},50);


//敌机与我方碰撞
var timerEAndAPzjc = window.setInterval(function(){
    var allEnemy = document.getElementsByClassName('enemy');
    for (var i = 0; i<allEnemy.length ; i++){
        if (pzjcFunc(jsAirplane, allEnemy[i])){
            jsAirplane.style.backgroundImage = "url('@/../img/aircraftWars/boom.png')";
            jsAirplane.style.backgroundSize = "85px 76px";
            var jsGameOver = document.createElement('p');
            jsGameOver.id = 'gameOver';
            jsGameOver.innerHTML = 'GAME OVER';
            jsMainScreen.appendChild(jsGameOver);
            jsMainScreen.removeEventListener('mousemove', follow, false);
            clearInterval(timerBack);
            clearInterval(timerBullet);
            clearInterval(timerEnemy);
            clearInterval(timerBAndEPzjc);
            clearInterval(timerEAndAPzjc);
        }
    }
},50);
