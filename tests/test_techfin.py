import unittest
from pytechfin.techfin import Techfin
from pytechfin.enums import Apps



class TestPytechfin(unittest.TestCase):

    def setUp(self) -> None:
        self.tt = Techfin()
        return super().setUp()

    def test_raise_not_valid_api_method(self):
        with self.assertRaises(AssertionError):
            self.tt.call_api(path="provisioner/api/v1/provisioning", techfin_app=Apps.CASHFLOW.value, method='FAKE')
        


if __name__ == '__main__':
    unittest.main(verbosity=2)
