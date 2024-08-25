<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <link rel="stylesheet" href="css/styles.css">
</head>
<body>
<div class="login-container">
    <h2>Wykryto próbę wyświetlenia ważnych informacji!</h2>
    <h3>Aby kontynuować podaj hasło</h3>
    <form method="post" action="confirm.php">
        <div class="input-group">
            <label for="password">Hasło</label>
            <input type="password" id="password" name="password" required>
        </div>
        <button type="submit">Zaloguj</button>
    </form>
    <form method="get" action="index.php">
        <button style="background-color: red;" type="submit">Anuluj</button>
            </form>
</div>
</body>
</html>