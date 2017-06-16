import unittest
import e07_python_repos3 as pr

# testing for e07_python_repos3.py
class PythonReposTestCase(unittest.TestCase):

    def setUp(self):
        # call all functions here and test elements separately
        self.r = pr.get_response()
        self.repo_dicts = pr.get_repo_dicts(self.r)
        self.repo_dict = self.repo_dicts[0]
        self.names, self.plot_dicts = pr.get_names_plot_dicts(self.repo_dicts)

    def test_get_response(self):
        # tests if we got a valid response of 200
        self.assertEqual(self.r.status_code, 200)

    def test_repo_dicts(self):
        # test to see if we actually get correct data

        # There should be 30 repositories
        self.assertEqual(len(self.repo_dicts), 30)

        # repositories should have required keys
        required_keys = ['name', 'owner', 'stargazers_count', 'html_url']
        for key in required_keys:
            self.assertTrue(key in self.repo_dict.keys())

unittest.main()