import unittest
import os

from oplus import Simulation
from tests.util import iter_eplus_versions, RESOURCES_DIR_PATH


class ErrTest(unittest.TestCase):
    def test_err(self):
        for eplus_version in iter_eplus_versions(self):
            if eplus_version == (9, 0, 1):  # todo: make 9.0.1 tests !!
                continue
            version_str = "-".join([str(v) for v in eplus_version])
            s = Simulation(os.path.join(
                RESOURCES_DIR_PATH,
                "simulations-outputs",
                "one_zone_uncontrolled",
                version_str
            ))
            self.assertIsNotNone(s.err)
