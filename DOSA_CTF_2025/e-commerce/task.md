# E-commerce (Web)
by **Szczurowsky**

## Task
Three flags must be found, with the final flag (for the aggregator) in the format `flag{1_...}_flag{2_...}_flag{3_...}`.

> **WARNING!** The use of any automation tools is prohibited; using such programs will result in a permanent ban!

### Hints for flag 1
The person who has this first flag is the `admin` <img src="lenny.png" alt="lenny" width="16" height="16" style="vertical-align: middle"/>
> - [Basics of HTTP Protocol](https://sekurak.pl/protokol-http-podstawy/)
> - [SSRF](https://portswigger.net/web-security/ssrf)

### Hint for flag 2
> - [Access Control - IDOR](https://portswigger.net/web-security/access-control/idor)

### Hints for flag 3
It is worth looking at what software generates the PDF file and checking its documentation.

The software you see can be found in the metadata of the file. If you check its documentation, you will easily find a very telling section regarding files with practically ready payloads.

## Zadanie
Do znalezienia są trzy flagi, flaga ostateczna (do agregatora) w formacie `flag{1_...}_flag{2_...}_flag{3_...}`.

> **UWAGA!** Zakazane jest używanie wszelkich automatów, użycie takich programów będzie skutkowało permanentnym banem

### Wskazówka do flagi 1
Osoba, która posiada pierwszą flagę to `admin` <img src="lenny.png" alt="lenny" width="16" height="16" style="vertical-align: middle"/>
> - [Protokół HTTP - podstawy](https://sekurak.pl/protokol-http-podstawy/)
> - [SSRF](https://portswigger.net/web-security/ssrf)

### Wskazówka do flagi 2
> - [Access Control - IDOR](https://portswigger.net/web-security/access-control/idor)

### Wskazówki do flagi 3
Warto spojrzeć, jakie oprogramowanie generuje plik PDF oraz sprawdzić jego dokumentację.

Oprogramowanie znajdziecie w metadanych pliku. Jeśli wejdziecie w jego dokumentację, łatwo znajdziecie tam bardzo wymowną sekcję dot. plików z praktycznie gotowym payloadem.