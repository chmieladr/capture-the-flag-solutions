<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wyrzucarka</title>
    <link rel="stylesheet" href="css/indexstyle.css">
</head>
<body>
<div class="header">
    <h1>Wyrzucarka Studentów</h1>
    <form action="logout.php">
        <button type="submit" id="logoutButton">Wyloguj</button>
    </form>
</div>
<div class="tabs">
    <button class="tab-button" onclick="openTab(event, 'Home')">Strona startowa</button>
    <button class="tab-button" onclick="openTab(event, 'Table')">Lista studentów</button>
    <button class="tab-button" onclick="openTab(event, 'About')">Kontrola systemu</button>
</div>
<div id="Home" class="tab-content">
    <h2>Wyrzucarka studentów</h2>
    <p>Witaj qbjjqUBIiTKrgOIXrrskMOibTazZAcnHAmTtdTZMbWOyQqvzjq!</p>    <p>
        Tutaj znajdziesz listę studentów, którzy niebawem zostaną wyrzuceni z uczelni.<br>
        System jest napisany w taki sposób, że tylko administrator (dziekan) jest w stanie wprowadzić zmiany do listy.<br>
    </p>
</div>
<div id="About" class="tab-content">
    <h2>Brak dostępu!</h2><p>Tylko administrator może wejść na tą stronę!</p></div>
<div id="Table" class="tab-content">
    <h2>Lista studentów</h2>
    <label for="searchInput"></label><input type="text" id="searchInput" onkeyup="searchTable()" placeholder="Wyszukaj nazwisko..">
    <table id="myTable">
        <thead>
            <tr><th>Imię</th><th>Nazwisko</th><th>Numer albumu</th></tr>
        </thead>
        <tbody id = "tableData">
                            <tr>
                    <td>Adam</td>
                    <td>Kowalski</td>
                    <td>333333</td>
                </tr>
                            <tr>
                    <td>Adam</td>
                    <td>Kośmider</td>
                    <td>324233</td>
                </tr>
                            <tr>
                    <td>Anna</td>
                    <td>Nowak</td>
                    <td>315467</td>
                </tr>
                            <tr>
                    <td>Piotr</td>
                    <td>Kowalski</td>
                    <td>367890</td>
                </tr>
                            <tr>
                    <td>Ewa</td>
                    <td>Wiśniewska</td>
                    <td>349876</td>
                </tr>
                            <tr>
                    <td>Krzysztof</td>
                    <td>Wójcik</td>
                    <td>332198</td>
                </tr>
                            <tr>
                    <td>Marta</td>
                    <td>Kowalczyk</td>
                    <td>358234</td>
                </tr>
                            <tr>
                    <td>Paweł</td>
                    <td>Kaczmarek</td>
                    <td>374560</td>
                </tr>
                            <tr>
                    <td>Magdalena</td>
                    <td>Mazur</td>
                    <td>365432</td>
                </tr>
                            <tr>
                    <td>Tomasz</td>
                    <td>Krawczyk</td>
                    <td>391234</td>
                </tr>
                            <tr>
                    <td>Agnieszka</td>
                    <td>Piotrowska</td>
                    <td>387654</td>
                </tr>
                            <tr>
                    <td>Jan</td>
                    <td>Grabowski</td>
                    <td>378900</td>
                </tr>
                            <tr>
                    <td>Karolina</td>
                    <td>Zielińska</td>
                    <td>356789</td>
                </tr>
                            <tr>
                    <td>Rafał</td>
                    <td>Szymański</td>
                    <td>345678</td>
                </tr>
                            <tr>
                    <td>Dorota</td>
                    <td>Woźniak</td>
                    <td>359012</td>
                </tr>
                            <tr>
                    <td>Michał</td>
                    <td>Dąbrowski</td>
                    <td>378123</td>
                </tr>
                            <tr>
                    <td>Joanna</td>
                    <td>Pawłowska</td>
                    <td>364567</td>
                </tr>
                            <tr>
                    <td>Łukasz</td>
                    <td>Witkowski</td>
                    <td>359876</td>
                </tr>
                            <tr>
                    <td>Natalia</td>
                    <td>Walczak</td>
                    <td>371234</td>
                </tr>
                            <tr>
                    <td>Sebastian</td>
                    <td>Stępień</td>
                    <td>349012</td>
                </tr>
                            <tr>
                    <td>Zofia</td>
                    <td>Górska</td>
                    <td>362345</td>
                </tr>
                            <tr>
                    <td>Katarzyna</td>
                    <td>Sikorska</td>
                    <td>352678</td>
                </tr>
                            <tr>
                    <td>Damian</td>
                    <td>Lis</td>
                    <td>395432</td>
                </tr>
                            <tr>
                    <td>Barbara</td>
                    <td>Lewandowska</td>
                    <td>382198</td>
                </tr>
                            <tr>
                    <td>Grzegorz</td>
                    <td>Zając</td>
                    <td>379876</td>
                </tr>
                            <tr>
                    <td>Małgorzata</td>
                    <td>Michalska</td>
                    <td>368234</td>
                </tr>
                            <tr>
                    <td>Adrian</td>
                    <td>Król</td>
                    <td>355678</td>
                </tr>
                            <tr>
                    <td>Aleksandra</td>
                    <td>Jaworska</td>
                    <td>348900</td>
                </tr>
                            <tr>
                    <td>Patryk</td>
                    <td>Borkowski</td>
                    <td>359014</td>
                </tr>
                            <tr>
                    <td>Justyna</td>
                    <td>Wolska</td>
                    <td>341234</td>
                </tr>
                    </tbody>
    </table>
</div>
<script src="js/scripts.js"></script>
</body>
</html>
