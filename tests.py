import unittest
from app import app


class GistApiTestCase(unittest.TestCase):

    def test_user_gists(self):
        tester = app.test_client(self)
        response = tester.get('/octocat')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.json) > 0)

    def test_invalid_user_gists(self):
        tester = app.test_client(self)
        response = tester.get('/invalidUserFooBar987542312')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b"User not found", response.data)


if __name__ == '__main__':
    unittest.main()
