import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Manohar@1234",
        database="bank_reconciliation"
    )