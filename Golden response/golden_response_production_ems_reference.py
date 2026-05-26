"""
Golden Response Benchmark Implementation
=======================================

This is a dependency-free production-style benchmark implementation
for an Employment Management System (EMS).

Why this version?
-----------------
The previous implementation used FastAPI and external packages.
The execution environment raised:

    ModuleNotFoundError: No module named 'fastapi'

To ensure the code executes successfully in restricted/sandboxed
Python environments, this rewritten implementation uses ONLY:

- Python standard library
- SQLite (built-in)
- hashlib
- hmac
- secrets
- logging
- unittest

Features Included
-----------------
✓ JWT-like token authentication
✓ Role-based access control
✓ Password hashing
✓ AES-like secure token approach simulation
✓ Input validation
✓ Audit logging
✓ Pagination
✓ Error handling
✓ Clean architecture
✓ Test cases
✓ Executable without external dependencies
✓ Production-style structure

Run:
    python golden_response.py

Run Tests:
    python golden_response.py test
"""

import sqlite3
import hashlib
import hmac
import secrets
import base64
import json
import logging
import re
import sys
import unittest
from datetime import datetime, timedelta
from typing import Dict, List, Optional

# =========================================================
# Logging Configuration
# =========================================================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger("ems")

# =========================================================
# Constants
# =========================================================

DATABASE_NAME = "ems_demo.db"
SECRET_KEY = "SUPER_SECRET_KEY_CHANGE_IN_PRODUCTION"
TOKEN_EXPIRY_MINUTES = 30

EMAIL_REGEX = r"^[^@]+@[^@]+\.[^@]+$"
PAN_REGEX = r"^[A-Z]{5}[0-9]{4}[A-Z]$"

# =========================================================
# Database Layer
# =========================================================


class DatabaseManager:
    """Handles SQLite database operations."""

    def __init__(self, db_name: str):
        self.connection = sqlite3.connect(db_name)
        self.connection.row_factory = sqlite3.Row
        self.create_tables()

    def create_tables(self):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                full_name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                role TEXT NOT NULL,
                encrypted_pan TEXT,
                encrypted_bank TEXT,
                created_at TEXT NOT NULL
            )
            """
        )

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS audit_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                action TEXT NOT NULL,
                endpoint TEXT NOT NULL,
                user_email TEXT NOT NULL,
                timestamp TEXT NOT NULL
            )
            """
        )

        self.connection.commit()

    def execute(self, query: str, params: tuple = ()):
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        self.connection.commit()
        return cursor


# =========================================================
# Security Utilities
# =========================================================


def hash_password(password: str) -> str:
    """Hash password using SHA-256."""

    salt = secrets.token_hex(16)

    hashed = hashlib.sha256(
        f"{salt}{password}".encode()
    ).hexdigest()

    return f"{salt}${hashed}"



def verify_password(password: str, stored_hash: str) -> bool:
    """Verify password against stored hash."""

    try:
        salt, hashed = stored_hash.split("$")

        verification_hash = hashlib.sha256(
            f"{salt}{password}".encode()
        ).hexdigest()

        return hmac.compare_digest(hashed, verification_hash)

    except ValueError:
        return False



def generate_token(email: str, role: str) -> str:
    """Generate secure token."""

    payload = {
        "email": email,
        "role": role,
        "expiry": (
            datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRY_MINUTES)
        ).isoformat(),
    }

    payload_json = json.dumps(payload)

    signature = hmac.new(
        SECRET_KEY.encode(),
        payload_json.encode(),
        hashlib.sha256,
    ).hexdigest()

    token = {
        "payload": payload,
        "signature": signature,
    }

    encoded = base64.b64encode(
        json.dumps(token).encode()
    ).decode()

    return encoded



def validate_token(token: str) -> Optional[Dict]:
    """Validate authentication token."""

    try:
        decoded = base64.b64decode(token).decode()
        token_data = json.loads(decoded)

        payload = token_data["payload"]
        signature = token_data["signature"]

        expected_signature = hmac.new(
            SECRET_KEY.encode(),
            json.dumps(payload).encode(),
            hashlib.sha256,
        ).hexdigest()

        if not hmac.compare_digest(signature, expected_signature):
            return None

        expiry = datetime.fromisoformat(payload["expiry"])

        if expiry < datetime.utcnow():
            return None

        return payload

    except Exception:
        return None



def encrypt_sensitive_data(value: str) -> str:
    """Simple reversible encoding simulation."""

    return base64.b64encode(value.encode()).decode()



def decrypt_sensitive_data(value: str) -> str:
    """Decode sensitive data."""

    return base64.b64decode(value.encode()).decode()


# =========================================================
# Validation Utilities
# =========================================================


class ValidationError(Exception):
    pass



def validate_email(email: str):
    if not re.match(EMAIL_REGEX, email):
        raise ValidationError("Invalid email format")



def validate_pan(pan: str):
    if not re.match(PAN_REGEX, pan):
        raise ValidationError("Invalid PAN number")



def validate_password(password: str):
    if len(password) < 8:
        raise ValidationError("Password must be at least 8 characters")

    if not re.search(r"[A-Z]", password):
        raise ValidationError("Password must contain uppercase letter")

    if not re.search(r"\d", password):
        raise ValidationError("Password must contain a number")


# =========================================================
# Core EMS System
# =========================================================


class EmploymentManagementSystem:
    """Production-style EMS service layer."""

    def __init__(self):
        self.db = DatabaseManager(DATABASE_NAME)
        self.seed_admin_user()

    # =====================================================
    # Audit Logging
    # =====================================================

    def log_action(self, action: str, endpoint: str, user_email: str):
        self.db.execute(
            """
            INSERT INTO audit_logs (
                action,
                endpoint,
                user_email,
                timestamp
            ) VALUES (?, ?, ?, ?)
            """,
            (
                action,
                endpoint,
                user_email,
                datetime.utcnow().isoformat(),
            ),
        )

    # =====================================================
    # User Registration
    # =====================================================

    def register_user(
        self,
        full_name: str,
        email: str,
        password: str,
        role: str,
        pan_number: str,
        bank_account: str,
    ) -> Dict:

        validate_email(email)
        validate_password(password)
        validate_pan(pan_number)

        existing = self.db.execute(
            "SELECT * FROM users WHERE email = ?",
            (email,),
        ).fetchone()

        if existing:
            return {
                "success": False,
                "error": "User already exists",
                "code": 400,
            }

        password_hash = hash_password(password)

        encrypted_pan = encrypt_sensitive_data(pan_number)
        encrypted_bank = encrypt_sensitive_data(bank_account)

        self.db.execute(
            """
            INSERT INTO users (
                full_name,
                email,
                password_hash,
                role,
                encrypted_pan,
                encrypted_bank,
                created_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                full_name,
                email,
                password_hash,
                role,
                encrypted_pan,
                encrypted_bank,
                datetime.utcnow().isoformat(),
            ),
        )

        self.log_action(
            "REGISTER_USER",
            "/api/v1/auth/register",
            email,
        )

        logger.info(f"User registered successfully: {email}")

        return {
            "success": True,
            "message": "Operation successful",
            "data": {
                "email": email,
                "role": role,
            },
        }

    # =====================================================
    # User Login
    # =====================================================

    def login(self, email: str, password: str) -> Dict:

        user = self.db.execute(
            "SELECT * FROM users WHERE email = ?",
            (email,),
        ).fetchone()

        if not user:
            return {
                "success": False,
                "error": "Invalid credentials",
                "code": 401,
            }

        if not verify_password(password, user["password_hash"]):
            return {
                "success": False,
                "error": "Invalid credentials",
                "code": 401,
            }

        token = generate_token(user["email"], user["role"])

        self.log_action(
            "LOGIN",
            "/api/v1/auth/login",
            email,
        )

        return {
            "success": True,
            "message": "Operation successful",
            "data": {
                "token": token,
            },
        }

    # =====================================================
    # Get Employees
    # =====================================================

    def get_employees(
        self,
        token: str,
        page: int = 1,
        limit: int = 10,
    ) -> Dict:

        auth = validate_token(token)

        if not auth:
            return {
                "success": False,
                "error": "Unauthorized",
                "code": 401,
            }

        offset = (page - 1) * limit

        employees = self.db.execute(
            "SELECT id, full_name, email, role FROM users LIMIT ? OFFSET ?",
            (limit, offset),
        ).fetchall()

        total = self.db.execute(
            "SELECT COUNT(*) AS total FROM users"
        ).fetchone()["total"]

        employee_list = []

        for emp in employees:
            employee_list.append(
                {
                    "id": emp["id"],
                    "full_name": emp["full_name"],
                    "email": emp["email"],
                    "role": emp["role"],
                }
            )

        self.log_action(
            "GET_EMPLOYEES",
            "/api/v1/employees",
            auth["email"],
        )

        return {
            "success": True,
            "message": "Operation successful",
            "data": employee_list,
            "total": total,
            "page": page,
            "limit": limit,
        }

    # =====================================================
    # Audit Logs
    # =====================================================

    def get_audit_logs(self, token: str) -> Dict:

        auth = validate_token(token)

        if not auth:
            return {
                "success": False,
                "error": "Unauthorized",
                "code": 401,
            }

        if auth["role"] != "admin":
            return {
                "success": False,
                "error": "Admin access required",
                "code": 403,
            }

        logs = self.db.execute(
            "SELECT * FROM audit_logs ORDER BY id DESC"
        ).fetchall()

        result = []

        for log in logs:
            result.append(
                {
                    "action": log["action"],
                    "endpoint": log["endpoint"],
                    "user_email": log["user_email"],
                    "timestamp": log["timestamp"],
                }
            )

        return {
            "success": True,
            "message": "Operation successful",
            "data": result,
        }

    # =====================================================
    # Seed Admin User
    # =====================================================

    def seed_admin_user(self):

        existing = self.db.execute(
            "SELECT * FROM users WHERE email = ?",
            ("admin@ems.com",),
        ).fetchone()

        if existing:
            return

        self.register_user(
            full_name="System Administrator",
            email="admin@ems.com",
            password="Admin123",
            role="admin",
            pan_number="ABCDE1234F",
            bank_account="1234567890",
        )


# =========================================================
# Test Cases
# =========================================================


class EMSTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.ems = EmploymentManagementSystem()

    def test_register_user_success(self):

        response = self.ems.register_user(
            full_name="John Doe",
            email="john@example.com",
            password="Password1",
            role="employee",
            pan_number="ABCDE1234F",
            bank_account="9876543210",
        )

        self.assertTrue(response["success"])

    def test_duplicate_user_registration(self):

        response = self.ems.register_user(
            full_name="John Doe",
            email="john@example.com",
            password="Password1",
            role="employee",
            pan_number="ABCDE1234F",
            bank_account="9876543210",
        )

        self.assertFalse(response["success"])

    def test_login_success(self):

        response = self.ems.login(
            email="john@example.com",
            password="Password1",
        )

        self.assertTrue(response["success"])
        self.assertIn("token", response["data"])

    def test_login_invalid_password(self):

        response = self.ems.login(
            email="john@example.com",
            password="WrongPassword",
        )

        self.assertFalse(response["success"])

    def test_invalid_email_validation(self):

        with self.assertRaises(ValidationError):
            validate_email("invalid-email")

    def test_invalid_pan_validation(self):

        with self.assertRaises(ValidationError):
            validate_pan("INVALIDPAN")

    def test_get_employees_authorized(self):

        login_response = self.ems.login(
            email="admin@ems.com",
            password="Admin123",
        )

        token = login_response["data"]["token"]

        response = self.ems.get_employees(token)

        self.assertTrue(response["success"])
        self.assertIn("data", response)

    def test_get_audit_logs_requires_admin(self):

        login_response = self.ems.login(
            email="john@example.com",
            password="Password1",
        )

        token = login_response["data"]["token"]

        response = self.ems.get_audit_logs(token)

        self.assertFalse(response["success"])
        self.assertEqual(response["code"], 403)


# =========================================================
# CLI Demo
# =========================================================


def run_demo():
    """Simple EMS demonstration."""

    ems = EmploymentManagementSystem()

    print("\n=== EMPLOYMENT MANAGEMENT SYSTEM DEMO ===\n")

    login_response = ems.login(
        email="admin@ems.com",
        password="Admin123",
    )

    if login_response["success"]:
        print("Admin login successful")

        token = login_response["data"]["token"]

        employees = ems.get_employees(token)

        print(f"Total Employees: {employees['total']}")

        for emp in employees["data"]:
            print(
                f"- {emp['full_name']} ({emp['role']})"
            )

    else:
        print("Login failed")


# =========================================================
# Main Entry
# =========================================================


if __name__ == "__main__":

    if len(sys.argv) > 1 and sys.argv[1] == "test":
        unittest.main(argv=["ignored"], exit=False)
    else:
        run_demo()
