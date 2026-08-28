from money_exchange import (CustomerRepository, CurrencyRepository, Database,
                            MoneyExchangeService, RateRepository)


def main() -> None:
    db = Database()
    db.create_schema()
    currencies = CurrencyRepository(db)
    currencies.add("USD", "US Dollar", "$")
    currencies.add("EUR", "Euro", "€")
    customers = CustomerRepository(db)
    try:
        customer_id = customers.add("Ada Lovelace", "ada@example.com", "+1-555-0100")
    except Exception:  # sample may have been run before
        customer_id = db.connection.execute(
            "SELECT customer_id FROM customers WHERE email = ?", ("ada@example.com",)
        ).fetchone()[0]
    RateRepository(db).add("USD", "EUR", 0.92)
    receipt = MoneyExchangeService(db).exchange(customer_id, "USD", "EUR", 100, fee=1.50)
    print(f"Transaction #{receipt.transaction_id}: {receipt.from_amount:.2f} {receipt.from_currency} -> "
          f"{receipt.to_amount:.2f} {receipt.to_currency} at {receipt.applied_rate} (fee {receipt.fee:.2f})")
    db.close()


if __name__ == "__main__":
    main()
