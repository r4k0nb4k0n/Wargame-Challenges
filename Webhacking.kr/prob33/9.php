<?php
for($i=97;$i<=122;$i=$i+2)
{
$ch=chr($i);

$answer.=$ch;

}

if($_GET[ans]==$answer)
{
echo("<a href=###>Next</a>");
}
else
{
echo("Wrong");
}
?>