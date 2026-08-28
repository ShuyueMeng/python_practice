PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL CHECK (length(trim(full_name)) > 0),
    email TEXT NOT NULL UNIQUE,
    phone TEXT,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS currencies (
    currency_code TEXT PRIMARY KEY CHECK (length(currency_code) = 3),
    currency_name TEXT NOT NULL,
    symbol TEXT NOT NULL,
    is_active INTEGER NOT NULL DEFAULT 1 CHECK (is_active IN (0, 1))
);

CREATE TABLE IF NOT EXISTS exchange_rates (
    rate_id INTEGER PRIMARY KEY AUTOINCREMENT,
    base_currency_code TEXT NOT NULL,
    quote_currency_code TEXT NOT NULL,
    rate REAL NOT NULL CHECK (rate > 0),
    effective_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (base_currency_code) REFERENCES currencies(currency_code),
    FOREIGN KEY (quote_currency_code) REFERENCES currencies(currency_code),
    CHECK (base_currency_code <> quote_currency_code)
);

CREATE TABLE IF NOT EXISTS exchange_transactions (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    from_currency_code TEXT NOT NULL,
    to_currency_code TEXT NOT NULL,
    rate_id INTEGER NOT NULL,
    from_amount REAL NOT NULL CHECK (from_amount > 0),
    applied_rate REAL NOT NULL CHECK (applied_rate > 0),
    to_amount REAL NOT NULL CHECK (to_amount > 0),
    transaction_fee REAL NOT NULL DEFAULT 0 CHECK (transaction_fee >= 0),
    transacted_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (from_currency_code) REFERENCES currencies(currency_code),
    FOREIGN KEY (to_currency_code) REFERENCES currencies(currency_code),
    FOREIGN KEY (rate_id) REFERENCES exchange_rates(rate_id),
    CHECK (from_currency_code <> to_currency_code)
);

CREATE INDEX IF NOT EXISTS idx_rates_pair_time
ON exchange_rates(base_currency_code, quote_currency_code, effective_at DESC);

CREATE INDEX IF NOT EXISTS idx_transactions_customer
ON exchange_transactions(customer_id, transacted_at DESC);
