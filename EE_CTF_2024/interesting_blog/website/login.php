<?php
session_start();

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    if (isset($_POST['guest'])) {
        setcookie('loggedin', '0');
        header('Location: index.php');
        exit();
    }

    $password = $_POST['password'];

    $valid_password = 'e93A93jsf14nF34jAk'; // hard-coded password

    if ($password === $valid_password) {
        setcookie('loggedin', '1');
        header('Location: index.php');
        exit();
    } else {
        $error = 'Podano złe hasło!';
    }
}
?>
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <title>Logowanie</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
<main class="login-main">
    <h1>Logowanie</h1>
    <form action="login.php" method="post" class="login-form">
        <label for="password">Hasło</label>
        <input type="password" name="password" id="password" required>
        <button type="submit">Zaloguj</button>
    </form>
    <form action="login.php" method="post" class="guest-form">
        <button type="submit" name="guest">Kontynuuj jako gość</button>
    </form>
    <?php if (isset($error)): ?>
        <p class="error"><?php echo $error; ?></p>
    <?php endif; ?>
</main>
</body>
</html>