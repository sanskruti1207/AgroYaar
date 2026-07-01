import sqlite3
import os

DB_PATH = 'history.db'

# Check environment variables as a first pass
is_serverless = os.environ.get('VERCEL') or os.environ.get('AWS_LAMBDA_FUNCTION_NAME')
if is_serverless:
    DB_PATH = '/tmp/history.db'

def get_db_connection():
    global DB_PATH
    
    # Bulletproof check: try to write a test table. If it fails, fallback to /tmp/history.db
    try:
        db_dir = os.path.dirname(os.path.abspath(DB_PATH))
        if not os.access(db_dir, os.W_OK):
            raise sqlite3.OperationalError("Database directory is read-only")
            
        conn = sqlite3.connect(DB_PATH)
        # Validate write privileges
        conn.execute("CREATE TABLE IF NOT EXISTS write_check (id INTEGER PRIMARY KEY)")
        conn.execute("DROP TABLE IF EXISTS write_check")
        conn.commit()
    except (sqlite3.OperationalError, PermissionError, OSError):
        DB_PATH = '/tmp/history.db'
        conn = sqlite3.connect(DB_PATH)
        
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS scans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            image_path TEXT NOT NULL,
            disease_key TEXT NOT NULL,
            crop_name TEXT NOT NULL,
            confidence REAL NOT NULL,
            severity TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()
    print("Database initialized successfully.")

def add_scan(image_path, disease_key, crop_name, confidence, severity):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO scans (image_path, disease_key, crop_name, confidence, severity)
        VALUES (?, ?, ?, ?, ?)
    ''', (image_path, disease_key, crop_name, confidence, severity))
    conn.commit()
    scan_id = cursor.lastrowid
    conn.close()
    return scan_id

def get_history(limit=10):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT id, image_path, disease_key, crop_name, confidence, severity, created_at
        FROM scans
        ORDER BY created_at DESC
        LIMIT ?
    ''', (limit,))
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def get_scan(scan_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT id, image_path, disease_key, crop_name, confidence, severity, created_at
        FROM scans
        WHERE id = ?
    ''', (scan_id,))
    row = cursor.fetchone()
    conn.close()
    return dict(row) if row else None
