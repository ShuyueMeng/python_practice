"""Object-oriented money exchange database application."""
from __future__ import annotations

import sqlite3
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path


@dataclass(frozen=True)
class ExchangeReceipt:
    transaction_id: int
    from_amount: float
    from_currency: str
    to_amount: float
    to_currency: str
    applied_rate: float
    fee: float


class Database:
    def __init__(self, path: str = "money_exchange.db") -> None:
        self.connection = sqlite3.connect(path)
        self.connection.row_factory = sqlite3.Row
        self.connection.execute("PRAGMA foreign_keys = ON")

    def create_schema(self) -> None:
        schema = Path(__file__).with_name("schema.sql").read_text(encoding="utf-8")
        self.connection.executescript(schema)

    def close(self) -> None:
        self.connection.close()


class CustomerRepository:
    def __init__(self, database: Database) -> None:
        self.db = database

    def add(self, full_name: str, email: str, phone: str | None = None) -> int:
        cursor = self.db.connection.execute(
            "INSERT INTO customers (full_name, email, phone) VALUES (?, ?, ?)",
            (full_name.strip(), email.strip().lower(), phone),
        )
        self.db.connection.commit()
        return cursor.lastrowid


class CurrencyRepository:
    def __init__(self, database: Database) -> None:
        self.db = database

    def add(self, code: str, name: str, symbol: str) -> None:
        self.db.connection.execute(
            "INSERT OR IGNORE INTO currencies (currency_code, currency_name, symbol) VALUES (?, ?, ?)",
            (code.upper(), name, symbol),
        )
        self.db.connection.commit()


class RateRepository:
    def __init__(self, database: Database) -> None:
        self.db = database

    def add(self, base: str, quote: str, rate: float) -> int:
        if rate <= 0:
            raise ValueError("Rate must be greater than zero.")
        cursor = self.db.connection.execute(
            """INSERT INTO exchange_rates
               (base_currency_code, quote_currency_code, rate, effective_at)
               VALUES (?, ?, ?, ?)""",
            (base.upper(), quote.upper(), rate, datetime.now(timezone.utc).isoformat()),
        )
        self.db.connection.commit()
        return cursor.lastrowid

    def latest(self, base: str, quote: str) -> sqlite3.Row | None:
        return self.db.connection.execute(
            """SELECT rate_id, rate FROM exchange_rates
               WHERE base_currency_code = ? AND quote_currency_code = ?
               ORDER BY effective_at DESC, rate_id DESC LIMIT 1""",
            (base.upper(), quote.upper()),
        ).fetchone()


class MoneyExchangeService:
    def __init__(self, database: Database) -> None:
        self.db = database
        self.rates = RateRepository(database)

    def exchange(self, customer_id: int, from_code: str, to_code: str,
                 from_amount: float, fee: float = 0.0) -> ExchangeReceipt:
        from_code, to_code = from_code.upper(), to_code.upper()
        if from_code == to_code:
            raise ValueError("Source and destination currencies must differ.")
        if from_amount <= 0 or fee < 0:
            raise ValueError("Amount must be positive and fee cannot be negative.")
        rate = self.rates.latest(from_code, to_code)
        if rate is None:
            raise LookupError(f"No exchange rate available for {from_code}/{to_code}.")
        to_amount = round(from_amount * rate["rate"] - fee, 2)
        if to_amount <= 0:
            raise ValueError("Fee leaves no amount to exchange.")
        with self.db.connection:
            cursor = self.db.connection.execute(
                """INSERT INTO exchange_transactions
                   (customer_id, from_currency_code, to_currency_code, rate_id,
                    from_amount, applied_rate, to_amount, transaction_fee, transacted_at)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (customer_id, from_code, to_code, rate["rate_id"], from_amount,
                 rate["rate"], to_amount, fee, datetime.now(timezone.utc).isoformat()),
            )
        return ExchangeReceipt(cursor.lastrowid, from_amount, from_code, to_amount,
                               to_code, rate["rate"], fee)
