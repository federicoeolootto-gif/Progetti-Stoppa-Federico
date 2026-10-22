CREATE TABLE IF NOT EXISTS support_tickets (
    ticket_id INTEGER PRIMARY KEY,
    customer_id TEXT NOT NULL,
    team TEXT NOT NULL CHECK (team IN ('Support', 'BTGuard')),
    operator_id TEXT NOT NULL,
    opened_at TIMESTAMP NOT NULL,
    first_viewed_at TIMESTAMP,
    closed_at TIMESTAMP,
    category TEXT NOT NULL,
    status TEXT NOT NULL CHECK (status IN ('Open','Closed')),
    CHECK (first_viewed_at IS NULL OR first_viewed_at >= opened_at),
    CHECK (closed_at IS NULL OR closed_at >= opened_at),
    CHECK ((status = 'Open' AND closed_at IS NULL) OR (status = 'Closed' AND closed_at IS NOT NULL))
);
