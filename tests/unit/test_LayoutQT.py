from datetime import date
import os
from LayoutQT.LayoutQT import LayoutQT

from tests import *
from tests.helpers import *

class TestLayoutQT(unittest.TestCase):
    def test_init(self):
        self.assertEqual(LayoutQT('path').__class__, LayoutQT)

    def test_init_with_many_pages(self):
        self.assertEqual(LayoutQT('./assets/many_pages.pdf').__class__, LayoutQT)
        
    def test_setup_with_single_page(self):
        directory = os.path.basename(os.getcwd())
        print('Current directory =', directory)
        doc = LayoutQT('./tests/assets/single_page.pdf')
        doc.setup()
        print(doc.df_pages.shape[0])
        assert doc.df_pages.shape[0] > 0

