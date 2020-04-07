"""
Module to run Selenium tests
"""
import unittest
from blog.selenium_tests import test_admin_site, test_add_post

ADMIN_SITE = unittest.TestLoader().loadTestsFromTestCase(test_admin_site.TestAdminSite)
ADD_POST = unittest.TestLoader().loadTestsFromTestCase(test_add_post.TestAddPost)
BLOG_TEST_SUITE = unittest.TestSuite([ADMIN_SITE, ADD_POST]) # add TestCase classes to TestSuite

unittest.TextTestRunner(verbosity=2).run(BLOG_TEST_SUITE)
