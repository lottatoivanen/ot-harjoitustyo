# Testausdokumentti

Musikaali- ja näytelmäprojektisovellusta on testattu automatisoiduilla yksikkö- ja integraatiotestein unittestilla.

Testit voidaan suorittaa komennolla
```bash
poetry run invoke test
```

## Yksikkö- ja integraatiotestaus

### Sovelluslogiikka

Jokaiselle sovelluslogiikasta vastaavalle luokalle ja funktiolle on oma testiluokkansa:

`ProjectService` → `TestProjectService`

`UserService` → `TestUserService`

`MusicService` → `TestMusicService`

`date_service` → `TestDateService`

Testejä varten luodaan testirepositoriot `FakeProjectRepository` ja `FakeUserRepository`. Testirepositorioiden avulla testit voidaan suorittaa erillisessä tietokannassa.

### Repositoriot

Repositoriota `ProjectRepository` testataan luokalla `TestProjectRepository`. Testit käyttävät erillistä testitietokantaa, joka alustetaan ennen testejä ja poistetaan testien jälkeen. Näin varmistetaan, etteivät testit vaikuta sovelluksen oikeaan tietokantaan.

### Käyttöliittymä

Käyttöliittymäkerrosta ei testata automaattisesti lainkaan.

## Testikattavuus

Sovelluksen testauksen haarautumakattavuus on 80%. 

Testikattavuusraportin saa komennolla
```bash
poetry run invoke coverage-report
```

![testikattavuus](coverage.png)

Kokonaan testaamatta jäivät _build.py_ ja _initialize_database.py_. Lisäksi testaamatta jäi erilaisia virhe- ja poikkeustilanteita. Nämä koskevat sekä repositorioita että palveluluokkia. `TestDateService` sekä `TestMusicService` testaavat vain erittäin yleisiä tapahtumia ja rajatapaukset jäävät kokonaan pois.

## Sovellukseen jääneet ongelmat

- Sovellus ei anna kunnollista virheilmoitusta mikäli SQLite tietokantaa ei ole alustettu, eli _poetry run invoke build_ -komentoa ei ole suoritettu

- Sovellus ei käsittele sujuvasti suuria määriä dataa.
