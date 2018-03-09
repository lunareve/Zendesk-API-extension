"""Tests for Zendesk API extension."""

from unittest import TestCase
from server import app
from flask import session

class FlaskTests(TestCase):

    def setUp(self):
        """Stuff to do before every test."""
        self.client = app.test_client()
        app.config["TESTING"] = True

    def test_index(self):
        """Test index route."""
        result = self.client.get("/")
        self.assertEqual(result.status_code, 200)
        self.assertIn("Enter your Zendesk credentials:", result.data)

    def test_login(self):
        """Test log in form."""
        with self.client as c:
            result = c.post("/",
                            data={"email": "test@test.com", "password": "test", "subdomain": "test"},
                            follow_redirects=True
                            )
            self.assertEqual(session["email"], "test@test.com")
            self.assertIn("Please logout and try logging in again", result.data)

    def test_logout(self):
        """Test logout route."""

        with self.client as c:
            with c.session_transaction() as sess:
                sess["email"] = "test@test.com"

            result = self.client.get("/logout", follow_redirects=True)

            self.assertNotIn("email", session)
            self.assertIn("Logged out", result.data)


if __name__ == '__main__':

    import unittest
    unittest.main()