<?php
extract($_GET);

if(!$_GET[addr]) $addr=$_SERVER[REMOTE_ADDR];

if($addr=="127.0.0.1")
{
echo("<a href=###>Next</a>");
}
else
{
echo("Wrong");
}
?>