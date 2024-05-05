<?php
$connect = mysqli_connect('localhost', 'root', '', 'DATA');
mysqli_set_charset($connect, 'utf8');
if (mysqli_connect_errno()) {
      echo "Failed to connect: " . mysqli_connect_errno();
}
