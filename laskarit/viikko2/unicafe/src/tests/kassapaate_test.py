import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
    
    def test_kassapaate_luodaan_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_syo_edullisesti_kateisella_kasvattaa_kassaa_oikein(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
    
    def test_syo_edullisesti_kateisella_kasvattaa_lounaiden_maaraa_oikein(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_syo_maukkaasti_kateisella_kasvattaa_kassaa_oikein(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
    
    def test_syo_maukkaasti_kateisella_kasvattaa_lounaiden_maaraa_oikein(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_syo_edullisesti_kateisella_ei_kasvata_kassaa_jos_rahaa_ei_riita(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_syo_edullisesti_kateisella_ei_kasvata_lounaiden_maaraa_jos_rahaa_ei_riita(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_syo_maukkaasti_kateisella_ei_kasvata_kassaa_jos_rahaa_ei_riita(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_syo_maukkaasti_kateisella_ei_kasvata_lounaiden_maaraa_jos_rahaa_ei_riita(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_syo_edullisesti_kortilla_palauttaa_true(self):
        kortti = Maksukortti(1000)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti), True)
    
    def test_syo_edullisesti_kortilla_palauttaa_false(self):
        kortti = Maksukortti(200)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti), False)

    def test_syo_maukkaasti_kortilla_palauttaa_true(self):
        kortti = Maksukortti(1000)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti), True)
    
    def test_syo_maukkaasti_kortilla_palauttaa_false(self):
        kortti = Maksukortti(200)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti), False)

    def test_syo_edullisesti_kortilla_vahentaa_saldoa_oikein(self):
        kortti = Maksukortti(1000)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(kortti.saldo_euroina(), 7.60)

    def test_syo_edullisesti_kortilla_ei_vie_saldoa_negatiiviseksi(self):
        kortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(kortti)

        self.assertEqual(kortti.saldo_euroina(), 2.0)

    def test_syo_maukkaasti_kortilla_vahentaa_saldoa_oikein(self):
        kortti = Maksukortti(1000)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(kortti.saldo_euroina(), 6.00)
    
    def test_syo_maukkaasti_kortilla_ei_vie_saldoa_negatiiviseksi(self):
        kortti = Maksukortti(300)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)

        self.assertEqual(kortti.saldo_euroina(), 3.0)

    def test_syo_edullisesti_kortilla_ei_vie_saldoa_negatiiviseksi(self):
        kortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(kortti)

        self.assertEqual(kortti.saldo_euroina(), 2.0)
    
    def test_syo_maukkaasti_kortilla_ei_vie_saldoa_negatiiviseksi(self):
        kortti = Maksukortti(300)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)

        self.assertEqual(kortti.saldo_euroina(), 3.0)
    
    def test_syo_edullisesti_kortilla_kasvattaa_lounaiden_maaraa_oikein(self):
        kortti = Maksukortti(1000)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_syo_edullisesti_kortilla_ei_kasvata_lounaiden_maaraa_jos_rahaa_ei_riita(self):
        kortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_syo_maukkaasti_kortilla_kasvattaa_lounaiden_maaraa_oikein(self):
        kortti = Maksukortti(1000)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_syo_maukkaasti_kortilla_ei_kasvata_lounaiden_maaraa_jos_rahaa_ei_riita(self):
        kortti = Maksukortti(300)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_lataa_rahaa_kortille_kasvattaa_kortin_saldoa_oikein(self):
        kortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(kortti, 500)
        self.assertEqual(kortti.saldo_euroina(), 15.00)
    
    def test_lataa_rahaa_kortille_ei_kasvata_kortin_saldoa_negatiivisella_arvolla(self):
        kortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(kortti, -500)
        self.assertEqual(kortti.saldo_euroina(), 10.00)
    
    def test_lataa_rahaa_kortille_kasvattaa_kassan_rahaa_oikein(self):
        kortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(kortti, 500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100500)
    
    def test_lataa_rahaa_kortille_ei_kasvata_kassan_rahaa_negatiivisella_arvolla(self):
        kortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(kortti, -500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_kassassa_rahaa_euroina_palauttaa_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.00)