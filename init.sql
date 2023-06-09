-- Create the numbers table
CREATE TABLE IF NOT EXISTS numbers (
    id SERIAL PRIMARY KEY,
    value INTEGER NOT NULL,
    timestamp TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

-- Create a trigger to automatically set the timestamp on INSERT
CREATE OR REPLACE FUNCTION set_timestamp()
    RETURNS TRIGGER AS $$
BEGIN
    NEW.timestamp = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER numbers_set_timestamp
    BEFORE INSERT ON numbers
    FOR EACH ROW EXECUTE FUNCTION set_timestamp();
