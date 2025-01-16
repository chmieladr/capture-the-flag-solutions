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
    <h2>Login</h2>
    <form method="post" action="login.php">
        <div class="input-group">
            <label for="username">Nazwa użytkownika</label>
            <input type="text" id="username" name="username" required>
        </div>
        <div class="input-group">
            <label for="password">Hasło</label>
            <input type="password" id="password" name="password" required>
        </div>
        <button type="submit">Zaloguj</button>
            </form>
</div>
</body>
</html>
