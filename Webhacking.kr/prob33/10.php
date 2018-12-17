<?php
$ip=$_SERVER[REMOTE_ADDR];

for($i=0;$i<=strlen($ip);$i++)
{
$ip=str_replace($i,ord($i),$ip);
}

$ip=str_replace(".","",$ip);

$ip=substr($ip,0,10);

@mkdir("answerip/$ip");

$answer=$ip*2;
$answer=$ip/2;
$answer=str_replace(".","",$answer);

$pw="###";

$f=fopen("answerip/$ip/$answer.$ip","w");
fwrite($f,"Password is $pw\n\nclear ip : $_SERVER[REMOTE_ADDR]");
fclose($f);
?>