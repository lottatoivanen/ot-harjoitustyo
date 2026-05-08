# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen avulla käyttäjä voi lisätä tulevia tai nykyisiä musikaali- tai näytelmäprojekteja. Käyttäjät pystyvät lisäämään sovellukseen harjoitusaikoja, esiintymispäiviä sekä nuottitiedostoja.

## Käyttäjät

Sovelluksen alkuvaiheessa on yksi käyttäjärooli. Myöhemmin sovellukseen saatetaan lisätä _ohjaajarooli_, jolla on laajemmat hallintaoikeudet.

## Perusversion tarjoama toiminnallisuus

### Kirjautuminen

- Käyttäjä voi kirjautua järjestelmään.
    - Kirjautuminen onnistuu vain jo olemassa olevalla käyttäjätunnuksella ja salasanalla.
    - Jos käyttäjätunnusta ei ole olemassa tai salasana ei täsmää, järjestelmä näyttää virheilmoituksen.

### Rekisteröinti

- Käyttäjä voi luoda sovellukseen käyttäjätunnuksen.
    - Käyttäjätunnuksen täytyy olla uniikki ja vähintään 4 merkkiä pitkä.
    - Salasanan täytyy olla vähintään 6 merkkiä pitkä.

### Projektisovelluksen käyttö

- Käyttäjä näkee omat projektinsa listana.
- Käyttäjä voi luoda musikaali- tai näytelmäprojektin ja sille kuvauksen.
    - Projektilla täytyy olla nimi, mutta kuvauksen lisääminen on vapaaehtoista.
    - Projektin nimen puuttuessa, järjestelmä näyttää virheilmoituksen.
- Käyttäjä voi editoida ja poistaa projekteja.
- Käyttäjä voi lisätä sekä poistaa tärkeitä päivämääriä projektiin.
    - Päivämäärä voi olla harjoitus, esitys tai muu.
    - Päivämäärän tulee olla muodossa dd.mm.yyyy tai järjestelmä näyttää virheilmoituksen.
    - Päivämäärään voi lisätä myös kellonajan hh:mm. Mikäli kellonaikaa ei lisätä, antaa sovellus automaattisesti ajan 00:00.
- Käyttäjä voi lisätä projektiin musiikkinuotteja.
    - Nuottien tulee olla PDF-tiedostona, jotta ne voi lisätä projektiin.
    - Jos tiedosto puuttuu tai on väärässä muodossa, järjestelmä näyttää virheilmoituksen.
- Käyttäjä näkee projektiin lisätyt musiikkinuotit listana.
- Käyttäjä voi avata projektin musiikkinuotin.
- Käyttäjä voi kirjautua ulos järjestelmästä.

## Jatkokehitysideoita

- Käsikirjoitusten ja roolilistojen lisääminen projektiin.
- Projektitiimit, jolloin useampi käyttäjä voi nähdä ja muokata projektin tietoja.
- Kutsujärjestelmä, jolla käyttäjät voivat liittyä projekteihin.
- Harjoitusaktiivisuuden seuranta ja raportit.
- Integraatio kalenteripalveluihin (Google Calendar, Outlook)
