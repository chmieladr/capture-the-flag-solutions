# Hope You Don't Have Trypanophobia

### Challenge  
Before you lies an already familiar notes application, now enhanced with a few useful features. Some of the new features were added by our new intern, Scotty! I’m so proud! I hope you’ll enjoy them.

You can log into the application using the account of user `bob` with the password `bob`. Interestingly, you won't be the only user checking it out! Somewhere in the application, there is a hidden flag in the form of a 16-character alphanumeric string enclosed between `PW{ ... }`. Maybe you can get your hands on it?

PS. Remember, some attacks require the "victim" to visit the location where a trap has been set. Sometimes you'll need to wait a bit, but don’t worry, I promise it won’t take more than 3 minutes!

#### Hint 1  
Scotty wasn’t very careful when implementing the database restoration feature (endpoint `/restore`). Using a clever payload, you can add a note for yourself with a dump of the entire `notes` table or even the whole database. From there, it should get easier!

#### Hint 2  
If you’ve managed to download the contents of the `notes` table, you’ve probably noticed that one of the notes in the database, belonging to the `admin` user, has been encrypted (not without reason!). All the details about how notes are encrypted in the application can be found in other notes (unencrypted ones), in this case, belonging to our dear Scotty. The problem is that cracking the key for such an encrypted note is nearly impossible, so to read the content of the encrypted note, you need to know its password. And of course, the password to the note is only known by `admin`!  

The situation would seem hopeless if not for the fact that the `admin` user is very meticulous and frequently visits the application and their notes (see the `visits` table). Of course, `admin` is very cautious and will only open the note if everything looks as usual. However, you might be able to exploit the unfortunate database restoration function to modify their note in a way that is invisible to them and steal their password!

#### Hint 3  
In this challenge, `admin` behaves more like a human than a machine, so they don’t check the validity of `.html` files. However, if they <u>_see_</u> on the `/hello` endpoint that their note's title has been changed, they won’t open it. Similarly, if they see an additional, unrelated note, they won’t click on it either.  

Moreover, remember that the note is encrypted. If you experiment with your own account (`bob`), you’ll notice that when opening an encrypted note, the application displays a different template than for unencrypted notes. For the template used for encrypted notes, a form is displayed for entering the note's password, and the content of the note is not shown. Thus, this is not a good attack vector.  

However, on this page, there is one element you can modify (using the vulnerability introduced by Scotty in `/restore`). Is there a way to capture what `admin` entered into the form?

### Wyzwanie
Przed Tobą znana Ci już aplikacja do przechowywania notatek rozbudowana o kilka przydatnych funkcji. Niektóre z nowych funkcji dodał nasz nowy stażysta, Scotty! Duma mnie rozpiera! Mam nadzieję, że Ci się spodobają.

Do aplikacji możesz zalogować zalogować się używając konta użytkownika bob `bob` z hasłem `bob`. Co ciekawe nie będziesz jedynym użytkownikiem, który będzie do niej zaglądać! Gdzieś w aplikacji jest ukryta flaga w postaci 16 znaków alfanumerycznych między znakami `PW{ ... }`. Może uda Ci się ją zdobyć?

PS. Pamiętaj, do niektórych ataków potrzebne jest, aby to "ofiara" odwiedziła miejsce, w którym zastawiona została pułapka. Czasami będzie trzeba na to chwilkę zaczekać, ale nie martw się, obiecuję, że nie będzie to więcej niż 3 minuty!

#### Wskazówka 1
Scotty niezbyt uważnie zaimplementował funkcję odtwarzania bazy danych (endpoint `\restore`). Używając zgrabnego payload'u możecie dodać sobie notatkę ze zrzutem całej tabeli notes albo nawet całej bazy. Dalej powinno być już z górki!

#### Wskazówka 2
Jeśli udało Wam się pobrać zawartość tabeli `notes`, to zapewne zauważyliście, że jedna z notatek w bazie, należąca do użytkownika `admin` została zaszyfrowana (nie bez powodu!). Wszystkie informacje co do tego jak szyfrowane są notatki w aplikacji znajdziecie w innych notatkach (niezaszyfrowanych), w tym przypadku należących naszego kochanego Scotty'ego. Problem polega na tym, że złamanie klucza do tak zaszyfrowanej notatki jest prawie niemożliwe, więc żeby odczytać zawartość zaszyfrowanej notatki musicie znać jej hasło. A przecież hasło do notatki zna tylko `admin`! Sprawa byłaby przegrana gdyby nie to, że użytkownik `admin` jest bardzo skrupulatny i często zagląda do aplikacji i swoich notatek (patrz tabela `visits`). Oczywiście `admin` jest bardzo ostrożny i zajrzy do notatki tylko wtedy jeśli wszystko będzie wyglądać tak jak zawsze. Niemniej jednak może uda Wam się wykorzystać nieszczęsną funkcję odtwarzania bazy danych, aby zmodyfikować jego notatkę w niewidoczny dla niego sposób i wykraść jego hasło?

#### Wskazówka 3
W tym zadaniu `admin` ma zachowywać się bardziej jak człowiek, nie jak maszyna, więc nie sprawdza zgodności plików .html. Niemniej jednak jeśli w endpoincie `/hello` <u>_zobaczy_</u>, że jego notatka ma zmieniony tytuł, to w nią nie wejdzie. Tak samo jeśli zobaczy, że ma dodatkową, inną notatkę - również w nią nie kliknie. 
Ponadto pamiętajmy, że notatka jest zaszyfrowana. Jak poeksperymentujecie na własnym koncie (`bob`), to zauważycie, że przy otwieraniu notatki zaszyfrowanej aplikacja wyświetla inny szablon niż w przypadku notatki niezaszyfrowanej. W przypadku szablonu dla notatki zaszyfrowanej wyświetla się formularz do wprowadzenia hasła do notatki i nie wyświetla się jej treść, wiec nie jest to dobry kierunek ataku. Na tej podstronie jest jednak jeden element, który możecie zmodyfikować (korzystając z podatności wprowadzonej przez Scotty'ego w `/restore`). Czy da się jakoś przechwycić to co `admin` wpisał w formularz?