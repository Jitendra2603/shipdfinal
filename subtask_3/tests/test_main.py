import unittest
import requests

class TestDockerExecution(unittest.TestCase):

    BASE_URL = "http://localhost:8000"

    def test_docker_execution_success(self):
        """Test that code is executed inside a Docker container and output is returned."""
        code = "print('Running in Docker')"
        response = requests.post(f"{self.BASE_URL}/run_code", json={"code": code})
        data = response.json()
        self.assertTrue(data["success"])
        self.assertEqual(data["output"], "Running in Docker\n")

    def test_docker_execution_error(self):
        """Test that errors inside the Docker container are captured."""
        code = "raise Exception('Test Error')"
        response = requests.post(f"{self.BASE_URL}/run_code", json={"code": code})
        data = response.json()
        self.assertFalse(data["success"])
        self.assertIn("Test Error", data["error"])

    def test_docker_security(self):
        """Test that the code cannot access the host system or network."""
        code = "import socket; socket.socket().connect(('localhost', 80))"
        response = requests.post(f"{self.BASE_URL}/run_code", json={"code": code})
        data = response.json()
        self.assertFalse(data["success"])
        # The error message should indicate that network access is disabled

    def test_docker_resource_limitation(self):
        """Test that resource limits are enforced."""
        code = "a = ' ' * (1024 * 1024 * 256)"  # Try to allocate 256MB
        response = requests.post(f"{self.BASE_URL}/run_code", json={"code": code})
        data = response.json()
        self.assertFalse(data["success"])
        self.assertIn("MemoryError", data["error"])

if __name__ == '__main__':
    unittest.main()
