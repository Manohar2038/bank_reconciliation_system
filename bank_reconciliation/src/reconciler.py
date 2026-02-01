from datetime import datetime
from db_connection import get_connection

def fetch_internal_transactions():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT txn_id, txn_date, amount FROM internal_transactions")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows

def fetch_bank_transactions():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT txn_id, txn_date, amount FROM bank_transactions")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows

def date_diff_days(d1, d2):
    return abs((d1 - d2).days)

def reconcile_transactions():
    internal = fetch_internal_transactions()
    bank = fetch_bank_transactions()

    internal_map = {}
    for txn in internal:
        internal_map[txn['txn_id']] = txn

    matched_ids = set()

    conn = get_connection()
    cursor = conn.cursor()

    for btxn in bank:
        txn_id = btxn['txn_id']

        if txn_id not in internal_map:
            cursor.execute(
                "INSERT INTO reconciliation_results (txn_id, status, remarks) VALUES (%s, %s, %s)",
                (txn_id, 'MISSING_IN_INTERNAL', 'Not found in internal records')
            )
            continue

        itxn = internal_map[txn_id]
        matched_ids.add(txn_id)

        if float(itxn['amount']) != float(btxn['amount']):
            status = 'AMOUNT_MISMATCH'
            remarks = 'Amount differs'
        else:
            date_diff = date_diff_days(itxn['txn_date'], btxn['txn_date'])
            if date_diff <= 1:
                status = 'MATCHED'
                remarks = 'Matched successfully'
            else:
                status = 'AMOUNT_MISMATCH'
                remarks = 'Date difference too high'

        cursor.execute(
            "INSERT INTO reconciliation_results (txn_id, status, remarks) VALUES (%s, %s, %s)",
            (txn_id, status, remarks)
        )

    for txn_id in internal_map:
        if txn_id not in matched_ids:
            cursor.execute(
                "INSERT INTO reconciliation_results (txn_id, status, remarks) VALUES (%s, %s, %s)",
                (txn_id, 'MISSING_IN_BANK', 'Not found in bank statement')
            )

    conn.commit()
    cursor.close()
    conn.close()

