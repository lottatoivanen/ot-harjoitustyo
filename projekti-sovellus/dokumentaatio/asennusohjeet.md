# Musikaali- ja näytelmäprojektisovelluksen asennus- ja käyttöohjeet

### Ohjelman asennus

1. Lataa sovelluksen uusin release valitsemalla lähdekoodi _Source code_, joka sijaitsee _Assets_-osion alapuolella.

2. Siirry projekti-sovellus kansioon komennolla

```bash
cd projekti-sovellus
```

3. Lataa poetry-riippuvuudet komennolla

```bash
poetry install
```

4. Suorita tietokantojen alustustoimenpiteet komennolla

```bash
poetry run invoke build
```

5. Käynnistä sovellus komennolla

```bash
poetry run invoke start
```

### Sovelluksen rekisteröinti ja kirjautuminen

Sovellus avautuu kirjautumisnäkymään heti sen käynnistyessä.

Sovellukseen voi kirjautua jo olemassa olevilla käyttäjätunnuksella ja salasanalla. _Login_-nappia painamalla kirjautuminen vahvistuu.

Rekisteröitymisnäkymään pääsee _Register as user_ -napista.

Rekisteröitymissivulla tulee kirjoittaa uniikki käyttäjätunnus, joka on vähintään 4 merkkiä pitkä sekä salasana, joka on vähintään 6 merkkiä pitkä. Salasana pitää vielä vahvistaa kirjoittamalla se uudestaan _Password again_ -kenttään.

Kun rekisteröityminen onnistuu, vie sovellus takaisin kirjautumisnäkymään, josta käyttäjä voi kirjautua sisään.

### Projektin luominen ja hallinta

Kirjautumisen jälkeen sovellukseen avautuu projektien listausnäkymä.

Sovellukseen pystyy luomaan projektin napista _Add project_. Tämä avaa projektin lisäysnäkymän, jossa voi nimen lisäksi lisätä projektille myös kuvauksen. Lisäyksen jälkeen sovellus palaa listaus näkymään.

Halutun projektin voi avata painamalla projektin kohdalla sijaitsevaa _Open_-nappia. Tällöin avautuu projektinäkymä, jossa näkyy projektin nimi ja kuvaus. Tästä näkymästä pystyy myös editoimaan tai poistamaan projektin.

Projektinäkymässä projektiin pystyy myös lisäämään tärkeitä päivämääriä (harjoituksia, esityksiä tai muita) sekä lisäämään projektiin liittyviä nuotteja.