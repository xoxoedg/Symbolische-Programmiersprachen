import unittest
from regular_ex import *

class TestRegexMethods(unittest.TestCase):

    def test_valid_email(self): # [1 points]
        # [a-z]+\.[a-z]+@[a-z]\.[a-z]{3,}
        self.assertTrue(is_valid_email("john.doe@example.com"))
        self.assertFalse(is_valid_email("john.doe@"))
        self.assertFalse(is_valid_email("@example.com"))
        self.assertFalse(is_valid_email("john.doe"))
        self.assertFalse(is_valid_email("john.doe@example"))

    def test_find_mentions(self): # [1 points]
        self.assertEqual(find_mentions("@john Hey @jane!"), ["@john", "@jane"])
        self.assertEqual(find_mentions("Hello world!"), [])
        self.assertEqual(find_mentions("@john @john @john"), ["@john", "@john", "@john"])

    def test_redact_mentions(self): # [1 points]
        text = "The users @peter123 and @sarah099 are friends."
        replaced = "The users [redacted] and [redacted] are friends."
        self.assertEqual(redact_mentions(text, "[redacted]"), replaced)

    def test_is_strong_password(self): # [1 points]
        self.assertTrue(is_strong_password("StrongPass123"))
        self.assertFalse(is_strong_password("short1"))
        self.assertFalse(is_strong_password("ONLYUPPERCASE123"))
        self.assertFalse(is_strong_password("nouppercase123"))
        self.assertFalse(is_strong_password("NoNumberPassword"))
        self.assertFalse(is_strong_password("Password WithSpace1"))
        self.assertFalse(is_strong_password("PasswordWith\tTab1"))
        self.assertTrue(is_strong_password("ValidPassw0rd"))
        self.assertFalse(is_strong_password("Passw0rd"))

    def test_replace_links(self): # [1 points]
        text = "Visit our site at https://example.com or http://test.com"
        replaced = "Visit our site at [LINK] or [LINK]"
        self.assertEqual(replace_links(text, "[LINK]"), replaced)
