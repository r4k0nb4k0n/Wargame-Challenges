# 15

### First impression
```html
<body>
<script>
alert("Access_Denied");
history.go(-1);
document.write("password is off_script");
</script>password is off_script

</body>
```

### Solution
* 환경에 따라 다르겠지만, 패스워드가 보이지 않고 바로 뒤로가기가 된다면, 자바스크립트 기능을 꺼야 한다.
* 하지만 알림창을 끄고 재빠르게 중지 버튼을 누르면 제대로 볼 수 있다.