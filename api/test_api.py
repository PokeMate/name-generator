import json
import unittest
from main import app


class TestFlaskApi(unittest.TestCase):

    client = app.test_client()

    def test_home_route(self):
        response = self.client.get("/home")

        self.assertEqual(
            response.get_data(), b'"Welcome to PokeMate random name generator!"\n'
        )
        self.assertEqual(response.status_code, 200)

    def test_names_route_default(self):
        response = self.client.get("/names")

        json_data = json.loads(response.get_data())

        self.assertEqual(len(json_data), 1)
        self.assertEqual(response.status_code, 200)

    def test_names_route_lowerbound(self):
        amount = 1
        response = self.client.get("/names?amount=" + str(amount))

        json_data = json.loads(response.get_data())

        self.assertEqual(len(json_data), amount)
        self.assertEqual(response.status_code, 200)

    def test_names_route_upperbound(self):
        amount = 10
        response = self.client.get("/names?amount=" + str(amount))

        json_data = json.loads(response.get_data())

        self.assertEqual(len(json_data), amount)
        self.assertEqual(response.status_code, 200)

    def test_names_route_above_upperbound(self):
        amount = 11
        response = self.client.get("/names?amount=" + str(amount))
        self.assertEqual(response.status_code, 400)

    def test_names_route_below_lowerbound(self):
        amount = 0
        response = self.client.get("/names?amount=" + str(amount))
        self.assertEqual(response.status_code, 400)


if __name__ == "__main__":
    unittest.main()
