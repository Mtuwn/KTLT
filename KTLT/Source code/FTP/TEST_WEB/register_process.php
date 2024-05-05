<?php

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    if (isset($_POST["username"]) && isset($_POST["password"])) {
        include_once 'connect.php';
        $username = $_POST["username"];
        $password = $_POST["password"];

	$sql = "insert into Dang_ky(username,password) values(?,?)";
        $stmt = $connect->prepare($sql);
        $stmt->bind_param("ss", $username, $password);
        if ($stmt->execute()) {
            header("location:login.php");
        } else {
            echo "Error inserting record: " . $connect->error;
        }

        // Close the statement and connection
        $connect->close();
    }
}
