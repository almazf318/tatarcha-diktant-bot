-- Users table
CREATE TABLE IF NOT EXISTS users (
    id BIGSERIAL PRIMARY KEY,
    tg_id BIGINT UNIQUE NOT NULL,
    username TEXT DEFAULT '',
    first_name TEXT DEFAULT '',
    lang TEXT DEFAULT 'tt',
    created_at TIMESTAMPTZ DEFAULT now(),
    updated_at TIMESTAMPTZ DEFAULT now()
);

-- Sources (knowledge base entries)
CREATE TABLE IF NOT EXISTS sources (
    id BIGSERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMPTZ DEFAULT now()
);

-- Q&A log
CREATE TABLE IF NOT EXISTS qa_log (
    id BIGSERIAL PRIMARY KEY,
    tg_id BIGINT NOT NULL REFERENCES users(tg_id),
    question TEXT NOT NULL,
    answer TEXT NOT NULL,
    lang TEXT DEFAULT 'tt',
    is_off_topic BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMPTZ DEFAULT now()
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_users_tg_id ON users(tg_id);
CREATE INDEX IF NOT EXISTS idx_qa_log_tg_id ON qa_log(tg_id);
CREATE INDEX IF NOT EXISTS idx_qa_log_created ON qa_log(created_at);
CREATE INDEX IF NOT EXISTS idx_sources_active ON sources(active);

-- Auto-update updated_at on users
CREATE OR REPLACE FUNCTION update_updated_at()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = now();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS users_updated_at ON users;
CREATE TRIGGER users_updated_at
    BEFORE UPDATE ON users
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at();
