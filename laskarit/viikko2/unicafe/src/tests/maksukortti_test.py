import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
    
    def test_lataa_rahaa_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(250)
        self.assertEqual(self.maksukortti.saldo_euroina(), 12.50)
    
    def test_ota_rahaa_vahentaa_saldoa_oikein(self):
        self.maksukortti.ota_rahaa(250)
        self.assertEqual(self.maksukortti.saldo_euroina(), 7.50)
    
    def test_ota_rahaa_ei_vahenna_saldoa_negatiiviseksi(self):
        self.maksukortti.ota_rahaa(1250)
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.00)
    
    def test_ota_rahaa_palauttaa_true_jos_rahaa_riittaa(self):
        self.assertEqual(self.maksukortti.ota_rahaa(250), True)
    
    def test_ota_rahaa_palauttaa_false_jos_rahaa_ei_riita(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1250), False)
    


