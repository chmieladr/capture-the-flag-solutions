<?php

session_start();

if (!isset($_COOKIE['loggedin']) || $_COOKIE['loggedin'] !== '1') {
    header('Location: index.php');
    exit();
}

if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_FILES['file'])) {
    $target_dir = "images/";
    $target_file = $target_dir . basename($_FILES["file"]["name"]);
    $upload_ok = 1;
    $image_file_type = strtolower(pathinfo($target_file, PATHINFO_EXTENSION));

    // Check if file already exists
    if (file_exists($target_file)) {
        echo "Plik o danej nazwie już istnieje!";
        $upload_ok = 0;
    }

    // Check file size
    if ($_FILES["file"]["size"] > 10000) {
        echo "Plik jest za duży!";
        $upload_ok = 0;
    }

    // Check if $upload_ok is set to 0 by an error
    if ($upload_ok == 0) {
        echo "";
        // if everything is ok, try to upload file
    } else {
        if (move_uploaded_file($_FILES["file"]["tmp_name"], $target_file)) {
            header('Location: index.php');
            exit();
        } else {
            echo "Błąd podczas wysyłania pliku!";
        }
    }
}
?>