import unittest
from credit_card_validator import credit_card_validator


class TestCreditCardValidator(unittest.TestCase):
    # invalid check bits
    def test1(self):
        """Verifies if Visa Card of valid length and invalid check bit
        returns False."""
        self.assertFalse(credit_card_validator(4123563478973632), True)

    def test2(self):
        """Verifies if MasterCard of valid length and invalid check bit
        returns False."""
        self.assertFalse(credit_card_validator(5123645787098736), True)

    def test3(self):
        """Verifies if American Express of valid length and invalid check bit
        returns False."""
        self.assertFalse(credit_card_validator(372364578709873), True)

    # invalid length tests
    def test4(self):
        """Verifies if Visa Card of short length and valid check bit
        returns False."""
        self.assertFalse(credit_card_validator(412356347897363), True)

    def test5(self):
        """Verifies if MasterCard of short length and valid check bit
        returns False."""
        self.assertFalse(credit_card_validator(512364578709876), True)

    def test6(self):
        """Verifies if American Express of short length and valid check bit
        returns False."""
        self.assertFalse(credit_card_validator(37236457870985), True)

    def test7(self):
        """Verifies if Visa Card of long length and valid check bit
        returns False."""
        self.assertFalse(credit_card_validator(41235634789736383), True)

    def test8(self):
        """Verifies if MasterCard of long length and valid check bit
        returns False."""
        self.assertFalse(credit_card_validator(51236457870987626), True)

    def test9(self):
        """Verifies if American Express of long length and valid check bit
        returns False."""
        self.assertFalse(credit_card_validator(3723645787098542), True)

    # MasterCard prefix checks
    def test10(self):
        """Verifies if MasterCard of valid length and valid check bit
        with edge case prefixes returns True."""
        self.assertTrue(credit_card_validator(5123645787098766), True)

    def test11(self):
        """Verifies if MasterCard of valid length and valid check bit
        with edge case prefixes returns True."""
        self.assertTrue(credit_card_validator(5523645787098762), True)

    def test12(self):
        """Verifies if MasterCard of valid length and valid check bit
        with edge case prefixes returns False."""
        self.assertFalse(credit_card_validator(5023645787098767), True)

    def test13(self):
        """Verifies if MasterCard of valid length and valid check bit
        with edge case prefixes returns True."""
        self.assertTrue(credit_card_validator(5223645787098765), True)

    def test14(self):
        """Verifies if MasterCard of valid length and valid check bit
        with edge case prefixes returns False."""
        self.assertFalse(credit_card_validator(5623645787098761), True)

    def test15(self):
        """Verifies if MasterCard of valid length and valid check bit
        with edge case prefixes returns True."""
        self.assertTrue(credit_card_validator(2221645787098764), True)

    def test16(self):
        """Verifies if MasterCard of valid length and valid check bit
        with edge case prefixes returns True."""
        self.assertTrue(credit_card_validator(2720645787098760), True)

    def test17(self):
        """Verifies if MasterCard of valid length and valid check bit
        with edge case prefixes returns False."""
        self.assertFalse(credit_card_validator(2220645787098765), True)

    def test18(self):
        """Verifies if MasterCard of valid length and valid check bit
        with edge case prefixes returns True."""
        self.assertTrue(credit_card_validator(2225645787098760), True)

    def test19(self):
        """Verifies if MasterCard of valid length and valid check bit
        with edge case prefixes returns False."""
        self.assertFalse(credit_card_validator(2721645787098769), True)

    # American Express check if prefix check is a range
    def test20(self):
        """Verifies if American Express of valid length and valid check bit
        with valid prefix 34 returns True."""
        self.assertTrue(credit_card_validator(3423645787098545), True)

    def test21(self):
        """Verifies if American Express of valid length and valid check bit
        with valid prefix 37 returns True."""
        self.assertTrue(credit_card_validator(3723645787098542), True)

    def test22(self):
        """Verifies if American Express of valid length and valid check bit
        with invalid prefix 35 returns False."""
        self.assertFalse(credit_card_validator(3523645787098544), True)

    def test23(self):
        """Verifies if American Express of valid length and valid check bit
        with invalid prefix 33 returns True."""
        self.assertFalse(credit_card_validator(3323645787098546), True)

    def test24(self):
        """Verifies if American Express of valid length and valid check bit
        with valid prefix 38 returns True."""
        self.assertFalse(credit_card_validator(3823645787098541), True)

    # Test blank input
    def test25(self):
        """Verifies blank input returns False."""
        self.assertFalse(credit_card_validator(), True)

    # invalid length, invalid checksum, valid prefix
    def test26(self):
        """Verifies Visa card invalid length, invalid checksum,
        valid prefix returns False."""
        self.assertFalse(credit_card_validator(412356347897364), True)

    def test27(self):
        """Verifies MasterCard invalid length, invalid checksum,
        valid prefix returns False."""
        self.assertFalse(credit_card_validator(512364578709872), True)

    def test28(self):
        """Verifies American Express invalid length, invalid checksum,
        valid prefix returns False."""
        self.assertFalse(credit_card_validator(37236457870989), True)

    def test29(self):
        """Verifies length 16, invalid prefix, correct checksum
        returns False."""
        self.assertFalse(credit_card_validator(0000000000000000), True)

    # Test fully valid cards
    def test30(self):
        """Verifies Visa with valid length, valid prefix, valid checksum
        returns True."""
        self.assertTrue(credit_card_validator(4123563478973630), True)

    def test31(self):
        """Verifies Mastercard with valid length, valid prefix, valid checksum
        returns True."""
        self.assertTrue(credit_card_validator(5123645787098733), True)

    def test32(self):
        """Verifies American Express with valid length, valid prefix,
        valid checksum returns True."""
        self.assertTrue(credit_card_validator(372364578709875), True)

    def test33(self):
        """Verifies Mastercard with valid length, valid prefix, valid checksum
        returns True."""
        self.assertTrue(credit_card_validator(2221645787098731), True)

    def test34(self):
        """Verifies Mastercard with valid length, valid prefix, valid checksum
        returns True."""
        self.assertTrue(credit_card_validator(5523645787098739), True)

    def test35(self):
        """Verifies Mastercard with valid length, valid prefix, valid checksum
        returns True."""
        self.assertTrue(credit_card_validator(5323645787098731), True)

    def test36(self):
        """Verifies Mastercard with valid length, valid prefix, valid checksum
        returns True."""
        self.assertTrue(credit_card_validator(2720645787098737), True)

    def test37(self):
        """Verifies Mastercard with valid length, valid prefix, valid checksum
        returns True."""
        self.assertTrue(credit_card_validator(2700645787098731), True)


if __name__ == '__main__':
    unittest.main()
