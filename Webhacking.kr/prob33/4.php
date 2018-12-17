<?php
if($_GET[password]==md5(time()))
{
echo("<a href=###>Next</a>");
}
else
{
echo("hint : ".time());
}
?>