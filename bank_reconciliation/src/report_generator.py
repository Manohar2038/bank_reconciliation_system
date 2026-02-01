import csv
from db_connection import get_connection

def fetch_results():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT txn_id, status, remarks
        FROM reconciliation_results
        ORDER BY status
    """)

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows

def print_summary(results):
    summary = {}

    for row in results:
        status = row['status']
        summary[status] = summary.get(status, 0) + 1

    print("\nReconciliation Summary")
    print("-" * 30)
    for status, count in summary.items():
        print(f"{status}: {count}")
def generate_csv_report(results):
    with open("reconciliation_report.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Transaction ID", "Status", "Remarks"])

        for row in results:
            writer.writerow([
                row['txn_id'],
                row['status'],
                row['remarks']
            ])
