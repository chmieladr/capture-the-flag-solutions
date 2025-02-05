# Hash/Clash

### Challenge
On the server, in the current directory, there is a `flag` file with the flag.
The server accepts Base64-encoded Python scripts.
The script is checked for anything suspicious before the first run.
After acceptance, its hash is remembered.

Server code -> file `ctf-2-server.py`

The flag is in the format `PW{...}`.
In the form below, enter only the characters/numbers that are between `PW{` and `}`.

#### Hint 1
I recommend using the title HashClash by attacking the MD5 hash

#### Hint 2
The file encoding is `latin1`/`L1` and is characterized by the fact that in this mode,
strings can consist of many byte values `0x01`-`0xff`

### Wyzwanie
Na serwerze, w bieżącym katalogu znajduje się plik `flag` z flagą.
Serwer przyjmuje zakodowane Base64 skrypty w Pythonie.
Skrypt, przed pierwszym uruchomieniem jest sprawdzany, czy nie robi nic podejrzanego.
Po akceptacji, zapamiętywany jest jego skrót.

Kod serwera -> plik `ctf-2-server.py`

Flaga ma postać `PW{...}`.
W poniższy formularz wprowadzamy jedynie te znaki/cyfry, które znajdują się między `PW{`, a `}`.

#### Wskazówka 1
Polecam wykorzystać tytułowy HashClash atakując hash MD5

#### Wskazówka 2
Kodowanie pliku to `latin1`/`L1` i charakteryzuje je to,
że w tym trybie łańcuchy znaków mogą się składać się z wielu wartości bajtów `0x01`-`0xff`