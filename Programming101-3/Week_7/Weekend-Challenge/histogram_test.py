import unittest
from histogram import Histogram


class HistogramTests(unittest.TestCase):

    def setUp(self):
        self.ap = 'Apache'
        self.ng = 'nginx'
        self.iis = 'IIS'
        self.h = Histogram()

    def testAddRecord(self):
        self.h.add(self.ap)
        self.assertEqual(1, len(self.h.get_dict()))

    def testAddRecord_2(self):
        self.h.add(self.ap)
        self.h.add(self.ng)
        self.assertEqual(2, len(self.h.get_dict()))

    def testCountRecord(self):
        self.h.add(self.ap)
        self.assertEqual(1, self.h.count("Apache"))

    def testCountRecord_2(self):
        self.h.add(self.ap)
        self.h.add(self.ap)
        self.assertEqual(2, self.h.count("Apache"))

    def testCountRecord_3(self):
        self.h.add(self.ap)
        self.h.add(self.ap)
        self.h.add(self.ng)
        self.assertEqual(None, self.h.count("IBM Web Server"))

    def testGetDict_4(self):
        self.h.add(self.ap)
        self.h.add(self.ap)
        self.h.add(self.ng)
        self.h.add(self.ng)
        self.h.add(self.iis)
        self.assertEqual(self.h.get_dict(), {"Apache": 2, "nginx": 2, "IIS": 1})

if __name__ == '__main__':
    unittest.main()
