import unittest
import sys
import string
import random
sys.path.append(".")
from environment import Environment

class TestEnvironment(unittest.TestCase):
    def setUp(self):
        self.envclient = Environment("localhost", 50080, False)

    def test_add_host(self):
        host = {
            "hostid": "testhostid2",
            "total_cpu": 8000,
            "total_mem": 16785711104 
        }

        self.envclient.add_host(host)

if __name__ == '__main__':
    unittest.main()
