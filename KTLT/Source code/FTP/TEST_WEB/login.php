<?php
$cookie_name = "loggedIn";
if (isset($_COOKIE[$cookie_name])) {
    $cookie_value = $_COOKIE[$cookie_name];
    $value = base64_decode($cookie_value);
    $array = explode("-", $value);
    $username = $array[0];
    $password = $array[1];
    echo $password;
    include_once 'connect.php';
    $sql = "select  *  From Dang_ky where username = ? and password = ?";
    $stmt = mysqli_prepare($connect, $sql);
    mysqli_stmt_bind_param($stmt, "ss", $username, $password);
    $result = $stmt->execute();
    $result = $stmt->get_result();
    $result_name = $result->fetch_assoc();
    echo $result_name;
   if (empty($result_name))
	pass;
	else header("location:index.php");
	
}
?>

<h2>Sign in</h2>
<form method="post" action="index.php" class="form">

    <input type="text" id="username" class="input" name="username" autocomplete="off" placeholder="Tên đăng nhập" required>
    <br>
    <br>
    <br>

    <input type="password" class="input" name="password" id="password" autocomplete="off" placeholder="Mật khẩu" required><br>
    <br>
    <span style="width: 100%; justify-content: center; font-size: 20px; color: #ff6633;">
        <?php
        if (isset($_GET['error'])) {
            echo 'Sai tài khoản hoặc mật khẩu';
        }
        ?>
    </span>
    <br>
    <br>

    <Button type="submit">Log in</Button>
    <br>
    <span id="dang_ky">
        <a href="register.php">Register?</a>
    </span>
    
</form>

</form>
</div>
