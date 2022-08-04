from datetime import date
import os
from docSilhouette.docSilhouette import docSilhouette

from tests import *
from tests.helpers import *

class TestSilhouette(unittest.TestCase):
    def test_init(self):
        self.assertEqual(docSilhouette('path').__class__, docSilhouette)

    def test_init_with_many_pages(self):
        self.assertEqual(docSilhouette('./assets/many_pages.pdf').__class__, docSilhouette)
        
    def test_setup_with_single_page(self):
        directory = os.path.basename(os.getcwd())
        print('Current directory =', directory)
        doc = docSilhouette('./tests/assets/single_page.pdf')
        doc.setup()
        print(doc.df_pages.shape[0])
        assert doc.df_pages.shape[0] > 0

