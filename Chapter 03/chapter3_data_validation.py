# -*- coding: utf-8 -*-
"""Chapter3_Data Validation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZCzHcwmdoO2xPAoRiBv24lhU9GAotP3A
"""

import pandas as pd

def validate_financial_data(data):
    errors = []

    for row_idx, record in enumerate(data):
        # Check for required fields
        required_fields = ['transaction_id', 'amount', 'timestamp', 'account_id']
        missing_fields = [field for field in required_fields if field not in record]
        if missing_fields:
            errors.append(f"Missing required fields in row {row_idx + 1}: {', '.join(missing_fields)}")

        # Check data types
        if not isinstance(record.get('transaction_id', ''), str):
            errors.append(f"Invalid data type for transaction_id in row {row_idx + 1}")
        if not isinstance(record.get('amount', 0), (int, float)):
            errors.append(f"Invalid data type for amount in row {row_idx + 1}")
        else:
          # Check amount range
          if 'amount' in record and not (0 <= record['amount'] <= 1000000):
              errors.append(f"Amount out of range in row {row_idx + 1}")
        if not isinstance(record.get('timestamp', ''), str):
            errors.append(f"Invalid data type for timestamp in row {row_idx + 1}")
        if not isinstance(record.get('account_id', ''), str):
            errors.append(f"Invalid data type for account_id in row {row_idx + 1}")



        # Add more validation rules as needed...

    return errors

# Example financial data

financial_data = [
    {"transaction_id": "txn123", "amount": 500.0, "timestamp": "2023-05-01 10:30:00", "account_id": "acc456"},
    {"transaction_id": "txn124", "amount": 1500.0, "timestamp": "2023-05-01 11:00:00", "account_id": "acc457"},
    {"transaction_id": "txn126", "amount": 800.0, "timestamp": "2023-05-01 13:30:00", "account_id": "acc459"},
    {"transaction_id": "txn127", "amount": 1200.0, "timestamp": 900, "account_id": "acc460"},
    {"transaction_id": "txn128", "amount": "abc", "timestamp": "2023-05-01 15:45:00", "account_id": "acc461"},
    {"transaction_id": "txn129", "amount": 700.0, "timestamp": "2023-05-01 17:00:00", "account_id": "acc462"},
    {"transaction_id": "txn130", "amount": 1800.0, "timestamp": "2023-05-01 18:15:00", "account_id": "acc463"},
    {"transaction_id": "txn131", "amount": 1500.0, "timestamp": "2023-05-01 19:30:00", "account_id": "acc464"},
    {"transaction_id": "txn132", "amount": 2100000.0, "timestamp": "2023-05-01 20:45:00", "account_id": "acc465"},
    {"transaction_id": 1010, "amount": 2100.0, "timestamp": "2023-08-20T23:15:45", "status": "completed"}

]


validation_errors = validate_financial_data(financial_data)
if validation_errors:
    for error in validation_errors:
        print(error)
else:
    print("No validation errors found.")