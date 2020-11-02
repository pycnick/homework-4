import sys
import unittest
from tests.tests_yakovidis.authentication import AuthenticationTest
from tests.tests_yakovidis.profile import ProfileTest
from tests.tests_postnikov.test import AddRestaurantTest


if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(AuthenticationTest),
        unittest.makeSuite(ProfileTest)
    ))

    result = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(not result.wasSuccessful)
