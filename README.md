# Ohjelmistotekniikka harjoitustyö

Teen harjoitustyönä sovelluksen __musikaali- ja näytelmäprojektien__ hallintaan ja _harjoitusten seurantaan_.

## Dokumentaatio
- [vaatimuusmäärittely](https://github.com/lottatoivanen/ot-harjoitustyo/blob/568fd2610679f53f89dd70d5edb18d8f0f8451a6/projekti-sovellus/dokumentaatio/vaatimuusmaarittely.md)
- [työaikakirjanpito](https://github.com/lottatoivanen/ot-harjoitustyo/blob/568fd2610679f53f89dd70d5edb18d8f0f8451a6/projekti-sovellus/dokumentaatio/tyoaikakirjanpito.md)
- [changelog](https://github.com/lottatoivanen/ot-harjoitustyo/blob/568fd2610679f53f89dd70d5edb18d8f0f8451a6/projekti-sovellus/dokumentaatio/changelog.md)
- [arkkitehtuurikuvaus](https://github.com/lottatoivanen/ot-harjoitustyo/blob/568fd2610679f53f89dd70d5edb18d8f0f8451a6/projekti-sovellus/dokumentaatio/arkkitehtuuri.md)

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
