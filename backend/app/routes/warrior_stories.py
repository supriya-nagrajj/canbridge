from fastapi import APIRouter, HTTPException
from datetime import datetime
from app.services.db import get_connection

router = APIRouter(prefix="/stories", tags=["Warrior Stories"])


# -------------------------------------------------
# GET stories + love count (owner only)
# -------------------------------------------------
@router.get("/")
def get_stories(username: str | None = None):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, title, content, author, created_at
        FROM warrior_stories
        ORDER BY created_at DESC
    """)
    rows = cursor.fetchall()

    stories = []
    for r in rows:
        story_id = r[0]

        love_count = 0
        if username and r[3] == username:
            cursor.execute(
                "SELECT COUNT(*) FROM story_love WHERE story_id = ?",
                (story_id,)
            )
            love_count = cursor.fetchone()[0]

        stories.append({
            "id": story_id,
            "title": r[1],
            "content": r[2],
            "author": r[3],
            "created_at": r[4],
            "love_received": love_count
        })

    conn.close()
    return stories


# -------------------------------------------------
# HOME PAGE UPDATES (LOVE RECEIVED)
# -------------------------------------------------
@router.get("/updates")
def get_love_updates(username: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT ws.title, COUNT(sl.id)
        FROM warrior_stories ws
        JOIN story_love sl ON ws.id = sl.story_id
        WHERE ws.author = ?
        GROUP BY ws.id
        HAVING COUNT(sl.id) > 0
        ORDER BY MAX(sl.created_at) DESC
    """, (username,))

    rows = cursor.fetchall()
    conn.close()

    return [
        {
            "title": r[0],
            "count": r[1]
        }
        for r in rows
    ]


# -------------------------------------------------
# CREATE STORY
# -------------------------------------------------
@router.post("/")
def create_story(title: str, content: str, author: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO warrior_stories (title, content, author, created_at)
        VALUES (?, ?, ?, ?)
    """, (
        title,
        content,
        author,
        datetime.utcnow().isoformat()
    ))

    conn.commit()
    conn.close()
    return {"message": "Story added"}

# -----------------------------
# SEND LOVE (ONCE PER USER)
# -----------------------------
@router.post("/{story_id}/love")
def send_love(story_id: int, username: str):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO story_love (story_id, sender_username, created_at)
            VALUES (?, ?, ?)
        """, (
            story_id,
            username,
            datetime.utcnow().isoformat()
        ))

        conn.commit()
        conn.close()

        return {
            "status": "sent",
            "message": "Love sent 💖"
        }

    except Exception as e:
        conn.close()

        # UNIQUE constraint failed → love already sent
        if "UNIQUE constraint failed" in str(e):
            return {
                "status": "exists",
                "message": "Love already sent 💕"
            }

        raise HTTPException(status_code=500, detail="Failed to send love")

# -----------------------------
# GET love received by user
# -----------------------------
@router.get("/love/received")
def get_love_received(username: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 
            ws.title,
            COUNT(sl.id) as love_count
        FROM story_love sl
        JOIN warrior_stories ws ON ws.id = sl.story_id
        WHERE ws.author = ?
        GROUP BY ws.id
        ORDER BY MAX(sl.created_at) DESC
    """, (username,))

    rows = cursor.fetchall()
    conn.close()

    return [
        {
            "story_title": r[0],
            "count": r[1]
        }
        for r in rows   
    ]
