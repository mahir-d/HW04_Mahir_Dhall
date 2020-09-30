""" Author: Mahir Dhall """
import unittest
from githubAPI_Mahir_Dhall import get_repo_info


class github_api_test(unittest.TestCase):
    """ This test checks for correct validation of input type """

    def test_input_type(self):
        with self.assertRaises(TypeError):
            get_repo_info(123)
        with self.assertRaises(TypeError):
            get_repo_info(None)

    def test_empty_input(self):
        with self.assertRaises(ValueError):
            get_repo_info("")
        with self.assertRaises(ValueError):
            get_repo_info(" ")

    def test_valid_id_status_code(self):
        """ This tests for a successful status code returned, 
        when user_id is valid """
        self.assertEqual(get_repo_info("mahir-d"), 200)

    def test_invalid_id_status_code(self):
        """ This checks for a raised ValueError for invalid user_id """
        with self.assertRaises(ValueError):
            get_repo_info("this_is_an_invalid_user_id")


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(verbosity=2)
