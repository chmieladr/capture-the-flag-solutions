<?php
session_start();

if (!isset($_COOKIE['loggedin'])) {
    setcookie('loggedin', '0');
    header('Location: index.php');
    exit();
}
?>
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <title>Galeria</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
<header>
    <h1>Moja galeria :D</h1>
    <nav>
        <?php if ($_COOKIE['loggedin'] == '1'): ?>
            <a href="logout.php">Wyloguj</a>
        <?php else: ?>
            <a href="login.php">Zaloguj</a>
        <?php endif; ?>
    </nav>
</header>
<main>
    <?php if ($_COOKIE['loggedin'] === '1'): ?>
        <section class="upload-section">
            <h2>Dodaj zdjęcie</h2>
            <form action="upload.php" method="post" enctype="multipart/form-data">
                <label for="file">Wybierz plik</label>
                <input type="file" name="file" id="file" accept="image/*">
                <button type="submit">Wyślij</button>
            </form>
        </section>
    <?php endif; ?>
    <section class="gallery-section">
        <h2>Zdjęcia</h2>
        <div class="gallery">
            <?php
            $images = glob('images/*', GLOB_BRACE);
            foreach ($images as $image) {
                echo '<img src="' . $image . '" alt="' . $image . '">';
            }
            ?>
        </div>
    </section>
</main>
<footer>
    <p>Uwaga! Strona korzysta z ciasteczek!</p>
</footer>
</body>
</html>