<?php

if($_COOKIE[test]==md5("$_SERVER[REMOTE_ADDR]") && $_POST[kk]==md5("$_SERVER[HTTP_USER_AGENT]"))
{
echo("<a href=###>Next</a>");
}
else
{
echo("hint : $_SERVER[HTTP_USER_AGENT]");
}

?>