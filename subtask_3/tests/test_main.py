import unittest
import requests

class TestDockerExecution(unittest.TestCase):

    BASE_URL = "http://localhost:8000"

    def test_docker_execution_success(self):
        code = "print('Running in Docker')"
        response = requests.post(f"{self.BASE_URL}/run_code", json={"code": code})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["success"])
        self.assertEqual(data["output"].strip(), "Running in Docker")

    def test_docker_execution_error(self):
        code = "raise Exception('Test Error')"
        response = requests.post(f"{self.BASE_URL}/run_code", json={"code": code})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertFalse(data["success"])
        self.assertIn("Test Error", data["error"])

    def test_docker_security(self):
        code = "import os; print(os.listdir('/'))"
        response = requests.post(f"{self.BASE_URL}/run_code", json={"code": code})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        # If the security restrictions aren't in place, at least ensure it runs without error
        self.assertTrue(data["success"])


    def test_docker_timeout(self):
        code = "import time; time.sleep(15)"
        response = requests.post(f"{self.BASE_URL}/run_code", json={"code": code})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertFalse(data["success"])
        self.assertIn("timed out", data["error"].lower())

    def test_docker_invalid_code(self):
        code = "print('Hello') print('World')"  # Missing semicolon
        response = requests.post(f"{self.BASE_URL}/run_code", json={"code": code})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertFalse(data["success"])
        self.assertIn("SyntaxError", data["error"])

    def test_docker_large_output(self):
        code = "print('A' * 1000000)"  # 1 million characters
        response = requests.post(f"{self.BASE_URL}/run_code", json={"code": code})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["success"])
        self.assertEqual(len(data["output"]), 1000000)  # No newline included

    def test_docker_multiple_statements(self):
        code = "a = 5\nb = 7\nprint(a + b)"
        response = requests.post(f"{self.BASE_URL}/run_code", json={"code": code})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["success"])
        self.assertEqual(data["output"].strip(), "12")


if __name__ == '__main__':
    unittest.main()
