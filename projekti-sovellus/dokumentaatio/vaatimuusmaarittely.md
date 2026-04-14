# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen avulla käyttäjä voi lisätä tulevia tai nykyisiä musikaali- tai näytelmäprojekteja. Käyttäjät pystyvät lisäämään sovellukseen harjoitusaikoja, roolilistoja ja muistutuksia.

## Käyttäjät

Sovelluksen alkuvaiheessa on yksi käyttäjärooli. Myöhemmin sovellukseen saatetaan lisätä _ohjaajarooli_, jolla on laajemmat hallintaoikeudet.

## Perusversion tarjoama toiminnallisuus

### Ennen kirjautumista
- Käyttäjä voi luoda sovellukseen käyttäjätunnuksen. TEHTY
    - Käyttäjätunnuksen täytyy olla uniikki ja vähintään 4 merkkiä pitkä. TEHTY
    - Salasanan täytyy olla vähintään 6 merkkiä pitkä. TEHTY
- Käyttäjä voi kirjautua järjestelmään. TEHTY
    - Kirjautuminen onnistuu vain jo olemassa olevalla käyttäjätunnuksella ja salasanalla. TEHTY
    - Jos käyttäjätunnusta ei ole olemassa tai salasana ei täsmää, järjestelmä näyttää virheilmoituksen. TEHTY

### Kirjautumisen jälkeen
- Käyttäjä näkee omat projektinsa. TEHTY
- Käyttäjä voi luoda ja poistaa projekteja.
- Käyttäjä voi lisätä harjoituksia, roolilistoja ja muistutuksia projekteihin.
- Käyttäjä voi kirjautua ulos järjestelmästä.

## Jatkokehitysideoita

- Harjoitusnauhojen, käsiohjelman ja musiikkinuottien lisääminen.
- Projektitiimit, jolloin useampi käyttäjä voi nähdä ja muokata projektin tietoja.
- Kutsujärjestelmä, jolla käyttäjät voivat liittyä projekteihin.
- Harjoitusaktiivisuuden seuranta ja raportit.
- Integraatio kalenteripalveluihin (Google Calendar, Outlook)
