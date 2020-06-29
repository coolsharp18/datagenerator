import unittest
from generator import datagenerator
import datagen


class TestGenerator(unittest.TestCase):
    def test_list(self):
        data_list = ('SBI', 'HDFC', 'IDFC', 'ING')
        generator = datagenerator.RandomStringFromList(data_list)
        for i in range(5):
            assert (generator.get() in data_list)

    def test_decimal(self):
        for i in range(5):
            generator = datagenerator.RandomDecimal(10, 10000)
            print(generator.get())

    def test_args(self):
        datagen.main(['--config-file', './resources/data_schema.json', '--output-file', './resources/output.csv',
                       '--record-count', '10'])
