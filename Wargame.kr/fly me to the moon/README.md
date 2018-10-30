# fly me to the moon
### First impressions
```
javascript game.

can you clear with bypass prevent cheating system?
```
자바스크립트 게임. 31337점 이상을 받아야 통과한다.  
우주선 양 옆에 벽이 있고, 이를 벗어나면 게임이 끝난다.
### Trial and error
* uglified code를 beautify 해보았다. [Online JavaScript beautifier](https://beautifier.io/)

```js
function secureGame() {
    var _0x8618x2 = this;
    var _0x8618x3 = true;

    function _0x8618x4() {
        _0x8618x3 = false;
        return true
    };

    function _0x8618x5() {
        return _0x8618x3
    };
    this['killPlayer'] = function() {
        _0x8618x4();
        return true
    };
    this['checkLife'] = function() {
        return _0x8618x5()
    };
    var _0x8618x6 = 0;

    function _0x8618x7() {
        return _0x8618x6
    };

    function _0x8618x8() {
        if (_0x8618x3) {
            _0x8618x6++
        };
        return true
    };
    this['getScore'] = function() {
        return _0x8618x7()
    };
    this['BincScore'] = function() {
        _0x8618x8();
        return true
    };
    var _0x8618x9 = 320;

    function _0x8618xa() {
        _0x8618x9 -= 20;
        return true
    };

    function _0x8618xb() {
        return _0x8618x9
    };
    this['shrinkTunnel'] = function() {
        _0x8618xa();
        return true
    };
    this['widthTunnel'] = function() {
        return _0x8618xb()
    }
};
var bg_val = 0;
var rail_left = 0;
var rail_right = 500;
var ship_x = 234;
var pos_x = 234;
var c_s = 0;
var c_r = 0;
var c_w = 0;
var t_state = 0;
left_wall = new Array(20);
right_wall = new Array(20);

function initTunnel() {
    BTunnelGame = new secureGame();
    if ('object' == typeof console) {
        console['warn']('Do cheating, if you can')
    };
    rail_left = document['getElementById']('tunnel')['offsetLeft'];
    rail_right += rail_left;
    y = 0;
    for (y = 0; y < 20; y++) {
        left_wall[y] = 80;
        right_wall[y] = 400
    };
    $('img.left_wall')['each'](function(_0x8618x16) {
        y = _0x8618x16 * 25;
        $(this)['css']('top', '' + y + 'px');
        $(this)['css']('display', 'block')
    });
    $('img.right_wall')['each'](function(_0x8618x16) {
        y = _0x8618x16 * 25;
        $(this)['css']('top', '' + y + 'px');
        $(this)['css']('display', 'block')
    });
    $('div#score_table')['click'](function() {
        $('table')['remove']('#high_scores');
        $('div#score_table')['css']('display', 'none');
        restartTunnel();
        updateTunnel()
    })
};

function restartTunnel() {
    BTunnelGame = new secureGame();
    if ('object' == typeof console) {
        console['warn']('Do cheating, if you can')
    };
    ship_x = 234;
    c_s = 0;
    c_r = 0;
    c_w = 0;
    $('span#score')['text']('' + 0);
    $('img#ship')['css']('left', ship_x + 'px');
    y = 0;
    for (y = 0; y < 20; y++) {
        left_wall[y] = 80;
        right_wall[y] = 400
    };
    $('img#ship')['fadeIn']('slow');
    $('img.left_wall')['each'](function(_0x8618x16) {
        y = _0x8618x16 * 25;
        $(this)['css']('top', '' + y + 'px');
        $(this)['css']('display', 'block')
    });
    $('img.right_wall')['each'](function(_0x8618x16) {
        y = _0x8618x16 * 25;
        $(this)['css']('top', '' + y + 'px');
        $(this)['css']('display', 'block')
    })
};

function updateTunnel() {
    bg_val = bg_val + 2;
    if (bg_val > 20) {
        bg_val = 0
    };
    $('div#tunnel')['css']('background-position', '50% ' + bg_val + 'px');
    if (ship_x + 32 < 500) {
        if (ship_x + 46 < pos_x) {
            ship_x += 4
        } else {
            if (ship_x + 16 < pos_x) {
                ship_x += 2
            }
        }
    };
    if (ship_x > 0) {
        if (ship_x - 14 > pos_x) {
            ship_x -= 4
        } else {
            if (ship_x + 16 > pos_x) {
                ship_x -= 2
            }
        }
    };
    $('img#ship')['css']('left', ship_x + 'px');
    c_r++;
    if (c_r > 60) {
        c_r = 0;
        t_state = Math['floor'](Math['random']() * 2)
    };
    if (left_wall[0] < 10) {
        t_state = 1
    } else {
        if (right_wall[0] > 470) {
            t_state = 0
        }
    };
    y = 0;
    for (y = 20; y > 0; y--) {
        left_wall[y] = left_wall[y - 1];
        right_wall[y] = right_wall[y - 1]
    };
    if (t_state == 0) {
        left_wall[0] -= 3
    };
    if (t_state == 1) {
        left_wall[0] += 3
    };
    right_wall[0] = left_wall[0] + BTunnelGame['widthTunnel']();
    $('img.left_wall')['each'](function(_0x8618x16) {
        $(this)['css']('left', '' + left_wall[_0x8618x16] + 'px')
    });
    $('img.right_wall')['each'](function(_0x8618x16) {
        $(this)['css']('left', '' + right_wall[_0x8618x16] + 'px')
    });
    if (BTunnelGame['widthTunnel']() >= 120) {
        c_w++;
        if (c_w > 100) {
            c_w = 0;
            BTunnelGame['shrinkTunnel']();
            left_wall[0] += 10
        }
    };
    c_s++;
    if (c_s > 20) {
        c_s = 0;
        BTunnelGame.BincScore();
        $('span#score')['text']('' + BTunnelGame['getScore']())
    };
    if (ship_x <= left_wall[18] + 20 || ship_x + 32 >= right_wall[18]) {
        BTunnelGame['killPlayer']()
    };
    if (BTunnelGame['checkLife']()) {
        setTimeout('updateTunnel()', 10)
    } else {
        $('img#ship')['fadeOut']('slow');
        $('img.left_wall')['css']('display', 'none');
        $('img.right_wall')['css']('display', 'none');
        $['ajax']({
            type: 'POST',
            url: 'high-scores.php',
            data: 'token=' + token + '&score=' + BTunnelGame['getScore'](),
            success: function(_0x8618x19) {
                showHighScores(_0x8618x19)
            }
        })
    }
};

function scoreUpdate() {
    return
};

function showHighScores(_0x8618x19) {
    $('div#score_table')['html'](_0x8618x19);
    $('div#score_table')['css']('display', 'block')
};
$(document)['ready'](function() {
    $('p#welcome')['css']('display', 'block');
    updateToken();
    setInterval('updateToken()', 10000);
    $('p#welcome')['click'](function() {
        $('p#welcome')['css']('display', 'none');
        initTunnel();
        updateTunnel()
    });
    $('#christian')['mouseover'](function() {
        $(this)['html']('thx, Christian Montoya')
    });
    $('#christian')['mouseout'](function() {
        $(this)['html'](temp)
    })
});
var temp = 'Christian Montoya';
$(document)['mousemove'](function(_0x8618x1d) {
    pos_x = _0x8618x1d['pageX'] - rail_left
});
var token = '';

function updateToken() {
    $['get']('token.php', function(_0x8618x20) {
        token = _0x8618x20
    })
};
```
* 목숨, 벽 사이 거리 등의 변수는 이름이 난독화되었다.
* 해당 변수들을 건드는 함수가 있다. (`killPlayer()`, `BincScore()` 등)
* 18?번째 벽들을 HTML 속성을 이용하여 엉뚱한 위치에 놓았지만, 게임이 끝나는 건 똑같다.
* 이는 벽의 위치도 자바스크립트 게임 인스턴스 내에 변수로 저장되어 있다는 뜻이다.
* 게임을 시작하고 나서 콘솔에서 `BTunnelGame['killPlayer']`를 다음과 같이 바꾸었더니, 계속 살아있다.

```js
BTunnelGame['killPlayer'] = function(){ return true; }
```

* 위 방법으로도 통과가 가능할 거라고 생각은 했지만, 너무 시간이 오래 걸린다.
### Solution
* 게임을 시작한다.
* 콘솔에 다음 코드를 실행한다. 이는 1점 얻는 것을 31337번 반복하는 것이다.

```js
var lmt = 31337;
for(var i=0; i<lmt; i++){
    BTunnelGame['BincScore']();
}
```
* 이후 FlAG 값이 나타난다.