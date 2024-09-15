import unittest
from fastapi.testclient import TestClient
from solution.main import app, Base, engine
from sqlalchemy.orm import sessionmaker
from solution.models import CodeSubmission

client = TestClient(app)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class TestSubmitCodeEndpoint(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Create tables
        Base.metadata.create_all(bind=engine)

    @classmethod
    def tearDownClass(cls):
        # Drop tables
        Base.metadata.drop_all(bind=engine)

    def test_submit_code_success(self):
        """Test that successful code execution results are saved to the database."""
        code = "print('Database Save Test')"
        response = client.post("/submit_code", json={"code": code})
        data = response.json()
        self.assertTrue(data["db_success"])

        # Verify that the submission exists in the database
        db = SessionLocal()
        submission = db.query(CodeSubmission).filter_by(code=code).first()
        self.assertIsNotNone(submission)
        self.assertEqual(submission.output.strip(), 'Database Save Test')
        db.close()

    def test_submit_code_failure(self):
        """Test that failed code executions are not saved to the database."""
        code = "raise Exception('Test Error')"
        response = client.post("/submit_code", json={"code": code})
        data = response.json()
        self.assertFalse(data["db_success"])

        # Verify that the submission does not exist in the database
        db = SessionLocal()
        submission = db.query(CodeSubmission).filter_by(code=code).first()
        self.assertIsNone(submission)
        db.close()

if __name__ == '__main__':
    unittest.main()
