# Ohjelmistotekniikka harjoitustyö

Teen harjoitustyönä sovelluksen __musikaali- ja näytelmäprojektien__ hallintaan. Sovelluksessa projekteihin voi lisätä tärkeitä päivämääriä, kuten harjoituksia ja esityksiä, sekä nuottitiedostoja.

Sovellusta on mahdollista käyttää usealla eri käyttäjällä. Jokaisella käyttäjällä on oma projektilista.

## Viimeisin release
[Viikko 5 release](../../releases/latest)

## Dokumentaatio
- [vaatimuusmäärittely](projekti-sovellus/dokumentaatio/vaatimuusmaarittely.md)
- [työaikakirjanpito](projekti-sovellus/dokumentaatio/tyoaikakirjanpito.md)
- [changelog](projekti-sovellus/dokumentaatio/changelog.md)
- [arkkitehtuurikuvaus](projekti-sovellus/dokumentaatio/arkkitehtuuri.md)
- [asennus- ja käyttöohjeet](projekti-sovellus/dokumentaatio/asennusohjeet.md)

## Asennus
1. Siirry kansioon projekti-sovellus

2. Asenna riippuvuudet komennolla

```bash
poetry install
```
3. Alusta sovellus komennolla

```bash
poetry run invoke build
```

4. Käynnistä sovellus komennolla

```bash
poetry run invoke start
```

## Komentorivitoiminnot

### Testaus

Testaaminen toimii komennolla

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuus raportin voi generoida _htmlcov_-hakemistoon komennolla

```bash
poetry run invoke coverage-report
```

### Pylint

Tiedoston [.pylintrc](https://github.com/lottatoivanen/ot-harjoitustyo/blob/b1eb2f63f51b003513c2d8734d63dfa0bc50cf77/projekti-sovellus/.pylintrc) määrittelemät tarkistukset voi suorittaa komennolla:

```bash
poetry run invoke lint
```

### Ylimääräinen koodikatselmointi

Tein koodikatselmoinnin Anna Kivekkään repositorioon

- [Issue](https://github.com/AnnaKivekass/ot-harjoitustyo/issues/1)

- [Annan repositorio](https://github.com/AnnaKivekass/ot-harjoitustyo)
