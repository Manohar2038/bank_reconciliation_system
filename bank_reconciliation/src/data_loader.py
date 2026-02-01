import csv 
from db_connection import get_connection
def load_internal_transactions(internal_transactions):
    conn = get_connection()
    cursor = conn.cursor()

    with open(internal_transactions, newline='') as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                cursor.execute(
                    """
                    INSERT INTO internal_transactions (txn_id, txn_date, amount, reference)
                    VALUES (%s, %s, %s, %s)
                    """,
                    (row['txn_id'], row['txn_date'], row['amount'], row['reference'])
                )
            except:
                pass  # skip duplicate txn_id

    conn.commit()
    conn.close()

def load_internal_transactions(csv_path):
    conn = get_connection()
    cursor = conn.cursor()

    with open(csv_path, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                cursor.execute(
                    """
                    INSERT INTO internal_transactions
                    (txn_id, txn_date, amount, reference)
                    VALUES (%s, %s, %s, %s)
                    """,
                    (
                        row['txn_id'],
                        row['txn_date'],
                        row['amount'],
                        row['reference']
                    )
                )
            except:
                pass  # ignore duplicate txn_id

    conn.commit()
    cursor.close()
    conn.close()

def load_bank_transactions(csv_path):
    conn = get_connection()
    cursor = conn.cursor()

    with open(csv_path, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                cursor.execute(
                    """
                    INSERT INTO bank_transactions
                    (txn_id, txn_date, amount, reference)
                    VALUES (%s, %s, %s, %s)
                    """,
                    (
                        row['txn_id'],
                        row['txn_date'],
                        row['amount'],
                        row['reference']
                    )
                )
            except:
                pass

    conn.commit()
    cursor.close()
    conn.close()
