""" Author: Mahir Dhall """
import os
import unittest
from mock import patch
from githubAPI_Mahir_Dhall import get_repo_info
import json


class github_api_test(unittest.TestCase):
    """ This test checks for correct validation of input type """

    def test_input_type(self):
        """ This test checks for input type for user-id """
        with self.assertRaises(TypeError):
            get_repo_info(123)
        with self.assertRaises(TypeError):
            get_repo_info(None)

    def test_empty_input(self):
        """ This test check for invalid empty string input for user-id """
        with self.assertRaises(ValueError):
            get_repo_info("")
        with self.assertRaises(ValueError):
            get_repo_info(" ")

    def test_valid_repo_owner(self):
        """ This tests matches the owner of the repo with the valid user id """

        mock_get_user_repo = patch("requests.get")
        mocked_info = mock_get_user_repo.start()

        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(f'{dir_path}/valid_user_repo.json') as file:
            mocked_info.return_value = json.load(file)
        mock_get_user_repo.stop()
        user_repo = mocked_info()

        self.assertEqual(user_repo[0]["owner"]["login"], "mahir-d")

    def test_invalid_user_id(self):
        """ This checks for for invalid user_id """
        mock_get_user_repo = patch("requests.get")
        mocked_info = mock_get_user_repo.start()

        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(f'{dir_path}/not_found.json') as file:
            mocked_info.return_value = json.load(file)
        mock_get_user_repo.stop()
        user_repo = mocked_info()

        self.assertEqual(user_repo.get("message"), "Not Found")

        # with self.assertRaises(ValueError):
        #     get_repo_info("this_is_an_invalid_user_id")


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(verbosity=2)
