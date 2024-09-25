import unittest
from fastapi.testclient import TestClient
from solution.server.main import app

client = TestClient(app)

class TestBackendAPI(unittest.TestCase):

    def test_run_code_success(self):
        """Test that the /run_code endpoint successfully executes valid code."""
        code = "print('Hello, World!')"
        response = client.post("/run_code", json={"code": code})
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["output"], "Hello, World!\n")
        self.assertTrue(data["success"])

    def test_run_code_error(self):
        """Test that the /run_code endpoint returns errors for invalid code."""
        code = "print(1/0)"
        response = client.post("/run_code", json={"code": code})
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertIn("ZeroDivisionError", data["error"])
        self.assertFalse(data["success"])

    def test_run_code_timeout(self):
        """Test that the code execution times out for long-running code."""
        code = "while True: pass"
        response = client.post("/run_code", json={"code": code})
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertIn("TimeoutError", data["error"])
        self.assertFalse(data["success"])

if __name__ == '__main__':
    unittest.main()
