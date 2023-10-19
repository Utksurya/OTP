import validate_otp as otp
import pytest
import unittest
from validate_otp import validate_email, generate_otp


class TestProgramFunctions(unittest.TestCase):

    def test_validate_email(self):

        result = validate_email("suryautkarsh1919@gmail.com")
        expected = True
        self.assertEqual(result, expected)

        result = validate_email("suryautkarsh1919@gmail.com")
        expected = True
        self.assertEqual(result, expected)

    def test_generate_otp(self):
        otp = generate_otp()
        self.assertEqual(len(otp), 6)
        self.assertTrue(otp.isdigit())


if __name__ == '_main_':
    pytest.main()
