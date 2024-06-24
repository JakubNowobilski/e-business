**Zadanie 1 Docker**

Należy stworzyć obraz oraz umieścić obraz na hub.docker.com, a Dockerfile na githubie.

:white_check_mark: 3.0 Obraz ubuntu z Pythonem w wersji 3.8: [link](https://github.com/JakubNowobilski/e-business/commit/a769069885377c78e2f2813bbfa3d7155f1314fa)

:white_check_mark: 3.5 Obraz ubuntu:22.04 z Javą w wersji 8 oraz Kotlinem: [link](https://github.com/JakubNowobilski/e-business/commit/00cd8bf8a13db4b1e41b33d158affaf1ad86c0ca)

:white_check_mark: 4.0 Do powyższego należy dodać najnowszego Gradle’a oraz paczkę JDBC SQLite w ramach projektu na Gradle (build.gradle) [link](https://github.com/JakubNowobilski/e-business/commit/0fe8ac176865b6b1e4be30478057cf324dfc3432)

:white_check_mark: 4.5 Należy stworzyć przykład typu HelloWorld oraz uruchomienie aplikacji przez CMD oraz gradle [link](https://github.com/JakubNowobilski/e-business/commit/0fe8ac176865b6b1e4be30478057cf324dfc3432)

:white_check_mark: 5.0 Należy dodać konfigurację docker-compose [link](https://github.com/JakubNowobilski/e-business/commit/336c2245579683ca7417690c00bfe8627eb78dc6)

Kod: https://github.com/JakubNowobilski/e-business/tree/main/zad1

Dockerhub: https://hub.docker.com/r/jakubnowobilski/eb_zad1

Demo video: https://github.com/JakubNowobilski/e-business/tree/main/demo/zad1.tar.gz

**Zadanie 2 Scala**

Należy stworzyć aplikację na frameworku Play w Scali 2.

:white_check_mark: 3.0 Należy stworzyć kontroler do Produktów [link](https://github.com/JakubNowobilski/e-business/commit/97a9ee1ce26d09df0a6e7d8201b4b8c7a8ba8564)

:white_check_mark: 3.5 Do kontrolera należy stworzyć endpointy zgodnie z CRUD - dane pobierane z listy [link](https://github.com/JakubNowobilski/e-business/commit/97a9ee1ce26d09df0a6e7d8201b4b8c7a8ba8564)

:x: 4.0 Należy stworzyć kontrolery do Kategorii oraz Koszyka + endpointy zgodnie z CRUD

:x: 4.5 Należy aplikację uruchomić na dockerze (stworzyć obraz) oraz dodać skrypt uruchamiający aplikację via ngrok

:x: 5.0 Należy dodać konfigurację CORS dla dwóch hostów dla metod CRUD

Kod: https://github.com/JakubNowobilski/e-business/tree/main/zad2

Demo video: https://github.com/JakubNowobilski/e-business/tree/main/demo/zad2.tar.gz

**Zadanie 3 Kotlin**

:white_check_mark: 3.0 Należy stworzyć aplikację kliencką w Kotlinie we frameworku Ktor, która pozwala na przesyłanie wiadomości na platformę Discord [link](https://github.com/JakubNowobilski/e-business/commit/fbc2d0eeda805cdf3b3d6bdd22ea8a54c470bc63)

:x: 3.5 Aplikacja jest w stanie odbierać wiadomości użytkowników z platformy Discord skierowane do aplikacji (bota)

:x: 4.0 Zwróci listę kategorii na określone żądanie użytkownika

:x: 4.5 Zwróci listę produktów wg żądanej kategorii

:x: 5.0 Aplikacja obsłuży dodatkowo jedną z platform: Slack, Messenfer, Webex, Skype, Discrod

Kod: https://github.com/JakubNowobilski/e-business/tree/main/zad3

Demo video: https://github.com/JakubNowobilski/e-business/tree/main/demo/zad3.tar.gz

**Zadanie 4 Go**

:white_check_mark: 3.0 Należy stworzyć aplikację we frameworki echo w j. Go, która będzie miała kontroler Produktów zgodny z CRUD [link](https://github.com/JakubNowobilski/e-business/commit/a43c71463d104894e9c388fb98d8d9b563457e1d)

:x: 3.5 Należy stworzyć model Produktów wykorzystując gorm oraz wykorzystać model do obsługi produktów (CRUD) w kontrolerze (zamiast listy)

:x: 4.0 Należy dodać model Koszyka oraz dodać odpowiedni endpoint

:x: 4.5 Należy stworzyć model kategorii i dodać relację między kategorią, a produktem

:x: 5.0 pogrupować zapytania w gorm’owe scope'y

Kod: https://github.com/JakubNowobilski/e-business/tree/main/zad4

Demo video: https://github.com/JakubNowobilski/e-business/tree/main/demo/zad4.tar.gz

**Zadanie 5 Frontend**

Należy stworzyć aplikację kliencką wykorzystując bibliotekę React.js. W ramach projektu należy stworzyć trzy komponenty:
Produkty, Koszyk oraz Płatności. Koszyk oraz Płatności powinny wysyłać do aplikacji serwerowej dane, a w Produktach
powinniśmy pobierać dane o produktach z aplikacji serwerowej. Aplikacja serwera w jednym z trzech języków: Kotlin,
Scala, Go. Dane pomiędzy wszystkimi komponentami powinny być przesyłane za pomocą React hooks.

:white_check_mark: 3.0 W ramach projektu należy stworzyć dwa komponenty: Produkty oraz Płatności; Płatności powinny
wysyłać do aplikacji serwerowej dane, a w Produktach powinniśmy pobierać dane o produktach z aplikacji serwerowej [link](https://github.com/JakubNowobilski/e-business/commit/3dcde52bb693b32c2407cfe92eea443117615d86)

:x: 3.5 Należy dodać Koszyk wraz z widokiem; należy wykorzystać routing

:x: 4.0 Dane pomiędzy wszystkimi komponentami powinny być przesyłane za pomocą React hooks

:x: 4.5 Należy dodać skrypt uruchamiający aplikację serwerową oraz kliencką na dockerze via docker-compose

:x: 5.0 Należy wykorzystać axios’a oraz dodać nagłówki pod CORS

Kod: https://github.com/JakubNowobilski/e-business/tree/main/zad5

Demo video: https://github.com/JakubNowobilski/e-business/tree/main/demo/zad5.tar.gz

**Zadanie 6 Testy**

Należy stworzyć 20 przypadków testowych w jednym z rozwiązań:

- Cypress JS (JS)
- Selenium (Kotlin, Python, Java, JS, Go, Scala)

Testy mają w sumie zawierać minimum 50 asercji (3.5). Mają również uruchamiać się na platformie Browserstack (5.0).
Proszę pamiętać o stworzeniu darmowego konta via https://education.github.com/pack.

:white_check_mark: 3.0 Należy stworzyć 20 przypadków testowych w CypressJS lub Selenium (Kotlin, Python, Java, JS, Go,
Scala) [link](https://github.com/JakubNowobilski/e-business/commit/9846bf106d8b4e8264a1794e2c77d5633991748f)

:x: 3.5 Należy rozszerzyć testy funkcjonalne, aby zawierały minimum 50 asercji

:x: 4.0 Należy stworzyć testy jednostkowe do wybranego wcześniejszego projektu z minimum 50 asercjami

:x: 4.5 Należy dodać testy API, należy pokryć wszystkie endpointy z minimum jednym scenariuszem negatywnym per endpoint

:x: 5.0 Należy uruchomić testy funkcjonalne na Browserstacku

Kod: https://github.com/JakubNowobilski/e-business/tree/main/zad6

Demo video: https://github.com/JakubNowobilski/e-business/tree/main/demo/zad6.tar.gz

**Zadanie 7 Sonar**

Należy dodać projekt aplikacji klienckiej oraz serwerowej (jeden branch, dwa repozytoria) do Sonara w wersji chmurowej
(https://sonarcloud.io/). Należy poprawić aplikacje uzyskując 0 bugów, 0 zapaszków, 0 podatności, 0 błędów
bezpieczeństwa. Dodatkowo należy dodać widżety sonarowe do README w repozytorium dane projektu z wynikami.

:white_check_mark: 3.0 Należy dodać litera do odpowiedniego kodu aplikacji serwerowej w hookach gita [link](https://github.com/JakubNowobilski/e-business/commit/49cc16f168127c510a997636e2b2d65a2ba07997)

:x: 3.5 Należy wyeliminować wszystkie bugi w kodzie w Sonarze (kod aplikacji serwerowej)

:x: 4.0 Należy wyeliminować wszystkie zapaszki w kodzie w Sonarze (kod aplikacji serwerowej)

:x: 4.5 Należy wyeliminować wszystkie podatności oraz błędy bezpieczeństwa w kodzie w Sonarze (kod aplikacji serwerowej)

:x: 5.0 Należy wyeliminować wszystkie błędy oraz zapaszki w kodzie aplikacji klienckiej

Kod: https://github.com/JakubNowobilski/e-business/commit/49cc16f168127c510a997636e2b2d65a2ba07997

Demo video: https://github.com/JakubNowobilski/e-business/tree/main/demo/zad7.tar.gz

**Zadanie 8 Oauth2**

Należy skonfigurować klienta Oauth2 (4.0). Dane o użytkowniku wraz z tokenem powinny być przechowywane po stronie bazy
serwera, a nowy token (inny niż ten od dostawcy) powinien zostać wysłany do klienta (React). Można zastosować mechanizm
sesji lub inny dowolny (5.0). Zabronione jest tworzenie klientów bezpośrednio po stronie React'a wyłączając z
komunikacji aplikację serwerową, np. wykorzystując auth0.

Prawidłowa komunikacja: react-sewer-dostawca-serwer(via return uri)-react.

:white_check_mark: 3.0 logowanie przez aplikację serwerową (bez Oauth2) [link](https://github.com/JakubNowobilski/e-business/commit/ef54e987210459fe2109c19d4338dad9e31d864a)

:x: 3.5 rejestracja przez aplikację serwerową (bez Oauth2)

:x: 4.0 logowanie via Google OAuth2

:x: 4.5 logowanie via Facebook lub Github OAuth2

:x: 5.0 zapisywanie danych logowania OAuth2 po stronie serwera

Kod: https://github.com/JakubNowobilski/e-business/tree/main/zad8

Demo video: https://github.com/JakubNowobilski/e-business/tree/main/demo/zad8.tar.gz

**Zadanie 9 ChatGPT bot**

Należy rozszerzyć funkcjonalność wcześniej stworzonego bota. Do niego należy stworzyć aplikajcę frontendową, która
połączy się z osobnym serwisem, który przeanalizuje tekst od użytkownika i prześle zapytanie do GPT, a następnie
prześle odpowiedź do użytkownika. Cały projekt należy stworzyć w Pythonie.

Dla studentów, którzy nie chcą lub nie mogą korzystać z GPT, zamiast GPT należy wykorzystać LLAMA2 za pomocą narzędzi
do wykorzystania LLM lokalnie: https://ollama.com/download/windows

:white_check_mark: 3.0 należy stworzyć po stronie serwerowej osobny serwis do łącznia z chatGPT do usługi chat [link](https://github.com/JakubNowobilski/e-business/commit/2fe99aa9ad9c93cc8cf4df14bcebc0e2445be57e)

:x: 3.5 należy stworzyć interfejs frontowy dla użytkownika, który komunikuje się z serwisem; odpowiedzi powinny być wysyałen do frontendowego interfejsu

:x: 4.0 stworzyć listę 5 różnych otwarć oraz zamknięć rozmowy

:x: 4.5 filtrowanie po zagadnieniach związanych ze sklepem (np. ograniczenie się jedynie do ubrań oraz samego sklepu) do GPT

:x: 5.0 filtrowanie odpowiedzi po sentymencie

Kod: https://github.com/JakubNowobilski/e-business/tree/main/zad9

Demo video: https://github.com/JakubNowobilski/e-business/tree/main/demo/zad9.tar.gz

**Zadanie 10 Chmura/CI**

Należy wykorzystać GitHub Actions (dopuszczalne są inne rozwiązania CI) oraz chmurę Azure (dopuszczalne inne chmury),
aby zbudować oraz zdeployować aplikację kliencką (frontend) oraz serwerową (backend) jako osobne dwie aplikacje.
Należy do tego wykorzystać obrazy dockerowe, a aplikacje powinny działać na kontenerach. Dopuszczalne jest zbudowanie
wcześniej aplikacji (jar package) oraz budowanie aplikacji via Github Actions. Należy zwrócić uwagę na zasoby dostępne
na chmurze.

:white_check_mark: 3.0 Należy stworzyć odpowiednie instancje po stronie chmury na dockerze [link](https://github.com/JakubNowobilski/e-business/commit/efdcc0cbab3cfe4f38d46e16a8e250ac87a28804)

:x: 3.5 Stworzyć odpowiedni pipeline w Github Actions do budowania aplikacji (np. via fatjar)

:x: 4.0 Dodać notyfikację mailową o zbudowaniu aplikacji

:x: 4.5 Dodać krok z deploymentem aplikacji serwerowej oraz klienckiej na chmurę

:x: 5.0 Dodać uruchomienie regresyjnych testów automatycznych (funkcjonalnych) jako krok w Actions

Kod: https://github.com/JakubNowobilski/e-business/tree/main/zad10

Demo video: https://github.com/JakubNowobilski/e-business/tree/main/demo/zad10.tar.gz
