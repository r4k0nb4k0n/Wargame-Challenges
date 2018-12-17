<?php
if($_GET[myip]==$_SERVER[REMOTE_ADDR])
{
echo("<a href=##.php>Next</a>");
}
else
{
echo("Wrong");
}
?>