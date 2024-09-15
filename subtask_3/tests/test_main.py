import unittest
from fastapi.testclient import TestClient
from solution.main import app

client = TestClient(app)

class TestDockerExecution(unittest.TestCase):

    def test_docker_execution(self):
        """Test that code is executed inside a Docker container and output is returned."""
        code = "print('Running in Docker')"
        response = client.post("/run_code", json={"code": code})
        data = response.json()
        self.assertEqual(data["output"].strip(), "Running in Docker")
        self.assertTrue(data["success"])

    def test_docker_security(self):
        """Test that the code cannot access the host system or network."""
        code = "import socket; socket.socket().connect(('localhost', 80))"
        response = client.post("/run_code", json={"code": code})
        data = response.json()
        self.assertFalse(data["success"])
        self.assertIn("PermissionError", data["error"])

    def test_docker_resource_limitation(self):
        """Test that resource limits are enforced."""
        code = "a = ' ' * (1024 * 1024 * 256)"  # Try to allocate 256MB
        response = client.post("/run_code", json={"code": code})
        data = response.json()
        self.assertFalse(data["success"])
        self.assertIn("MemoryError", data["error"])

if __name__ == '__main__':
    unittest.main()
