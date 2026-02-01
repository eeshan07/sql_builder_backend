CREATE SCHEMA IF NOT EXISTS app_db;

CREATE TABLE app_db.saved_queries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    sql_text TEXT,
    canvas_json JSON,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
