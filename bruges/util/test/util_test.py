# -*- coding: utf-8 -*-
"""
Testing util.

:copyright: 2015 Agile Geoscience
:license: Apache 2.0
"""
import unittest
import numpy as np
from bruges.util import next_pow2, rms, top_and_tail
from bruges.noise import noise_db


class UtilTest(unittest.TestCase):

    def test_toptail(self):
        a = np.asarray([np.nan, np.nan, 3, 4, 5, np.nan])
        b = np.asarray([6, 5, 4, 3, 2, 1])
        c = np.asarray([1, 2, 3, 4, 5, 6])
        d = np.asarray([6, 5, 4, 3, 2, 1])
        A, B, C, D = top_and_tail(a, b, c, d)
        for arr in (A, B, C, D):
            self.assertEqual(len(arr), 3)

    def test_nextpow2(self):
        num = 888
        ans = 1024

        self.assertEqual(ans, next_pow2(num))

    def test_rms(self):
        l = np.array([2, 3, 4.5])
        ans = 3.329164
        self.assertAlmostEqual(ans, rms(l), places=5)

        l = [[[1, 2, 3], [4, 5, 6]], [[2,3,4], [5, 6, 7]]]
        ans = 2.1602469
        self.assertAlmostEqual(ans, rms(l, axis=-1)[0, 0], places=5)

    def test_noise_db(self):
        a = np.ones(1000000)
        self.assertAlmostEqual(rms(noise_db(a, 10)), 10 ** (-10 / 20), delta=0.03)
        self.assertAlmostEqual(rms(noise_db(a, 0)), 1.0, delta=0.05)
        self.assertAlmostEqual(rms(noise_db(a, -10)), 10 ** (10 / 20), delta=0.2)

if __name__ == '__main__':

    suite = unittest.TestLoader().loadTestsFromTestCase(UtilTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
