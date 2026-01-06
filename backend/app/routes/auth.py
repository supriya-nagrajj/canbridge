from fastapi import APIRouter, HTTPException
from datetime import datetime

from app.services.db import get_connection
from app.core.security import hash_password, verify_password
from app.schemas.user import RegisterRequest, LoginRequest

router = APIRouter(prefix="/auth", tags=["Authentication"])


# ---------------- REGISTER ----------------
@router.post("/register")
def register_user(payload: RegisterRequest):
    conn = get_connection()
    cursor = conn.cursor()

    # Check if email already exists
    cursor.execute(
        "SELECT id FROM users WHERE email = ?",
        (payload.email,)
    )
    if cursor.fetchone():
        conn.close()
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = hash_password(payload.password)

    cursor.execute(
        """
        INSERT INTO users (username, email, password_hash, role, created_at)
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            payload.username,
            payload.email,
            hashed_password,
            "user",
            datetime.utcnow().isoformat()
        )
    )

    conn.commit()
    conn.close()

    return {"message": "User registered successfully"}


# ---------------- LOGIN ----------------
@router.post("/login")
def login_user(payload: LoginRequest):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id, username, email, password_hash, role
        FROM users
        WHERE username = ?
        """,
        (payload.username,)
    )
    user = cursor.fetchone()
    conn.close()

    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not verify_password(payload.password, user["password_hash"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {
        "id": user["id"],
        "username": user["username"],
        "email": user["email"],
        "role": user["role"]
    }
