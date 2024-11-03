import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_negatiivisen_tilavuuden(self):
        self.varasto2 = Varasto(-1)
        self.assertAlmostEqual(self.varasto2.tilavuus, 0)

    def test_konstruktori_luo_negatiivisen_varaston(self):
        self.varasto2 = Varasto(10, -1)
        self.assertAlmostEqual(self.varasto2.saldo, 0)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisaa_varastoon_negatiivinen_maara(self):
        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)

    def test_lisaa_varastoon_liian_paljon(self):
        self.varasto.lisaa_varastoon(self.varasto.paljonko_mahtuu() + 1)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)
        
    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_otetaan_negatiivinen_maara_varastosta(self):
        otettu = self.varasto.ota_varastosta(-1)
        self.assertAlmostEqual(otettu, 0)

    def test_otetaan_liikaa_varastosta(self):
        otettu = self.varasto.ota_varastosta(self.varasto.saldo + 1)
        self.assertAlmostEqual(otettu, self.varasto.saldo)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_palauttaako_oikean_str(self):
        self.varasto.lisaa_varastoon(1)
        self.assertAlmostEqual(str(self.varasto), "saldo = 1, vielä tilaa 9")
