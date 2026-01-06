from fastapi import APIRouter, HTTPException, Header
from datetime import datetime
from app.services.db import get_connection

router = APIRouter(prefix="/stories", tags=["Warrior Stories"])


# -----------------------------
# GET all stories
# -----------------------------
@router.get("/")
def get_stories():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, title, content, author, likes, created_at
        FROM warrior_stories
        ORDER BY created_at DESC
    """)
    rows = cursor.fetchall()
    conn.close()

    return [
        {
            "id": r[0],
            "title": r[1],
            "content": r[2],
            "author": r[3],
            "likes": r[4],
            "created_at": r[5],
        }
        for r in rows
    ]


# -----------------------------
# CREATE new story
# -----------------------------
@router.post("/")
def create_story(title: str, content: str, author: str | None = None):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO warrior_stories (title, content, author, likes, created_at)
        VALUES (?, ?, ?, 0, ?)
    """, (
        title,
        content,
        author,
        datetime.utcnow().isoformat()
    ))

    conn.commit()
    conn.close()

    return {"message": "Story added successfully"}


# -----------------------------
# LIKE a story
# -----------------------------
@router.post("/{story_id}/like")
def like_story(story_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE warrior_stories
        SET likes = likes + 1
        WHERE id = ?
    """, (story_id,))

    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Story not found")

    conn.commit()
    conn.close()

    return {"message": "Story liked"}


# -----------------------------
# DELETE a story (ADMIN ONLY)
# -----------------------------
@router.delete("/{story_id}")
def delete_story(
    story_id: int,
    x_user_role: str = Header(...)
):
    if x_user_role != "admin":
        raise HTTPException(status_code=403, detail="Admin access denied")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM warrior_stories
        WHERE id = ?
    """, (story_id,))

    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Story not found")

    conn.commit()
    conn.close()

    return {"message": "Story deleted by admin"}
