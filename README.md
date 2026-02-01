# bank_reconciliation_system

>>problem statement:
In real-world financial systems, organizations maintain their own transaction records while banks provide separate transaction statements. Due to delays, errors, or missing entries, these two data sources often do not perfectly match. Manual reconciliation is time-consuming and error-prone.
This project automates the bank transaction reconciliation process by comparing internal transaction records with bank statements, identifying matches, mismatches, and missing entries, and generating an audit-ready reconciliation report.

>>objectives:
Automatically match transactions between internal records and bank statements
Detect discrepancies such as missing or mismatched transactions
Generate a clear reconciliation summary and report
Simulate a real-world backend financial system

>>Tech Stack:
Python – Core backend logic
MySQL – Persistent data storage
CSV Files – Input transaction data
DSA Concepts – Hash maps, sets, optimized lookups

>>Database Design:
The system uses three tables:
1️.internal_transactions
Stores company-side transaction records.
txn_id (UNIQUE)
txn_date
amount
reference
2️. bank_transactions
Stores bank-provided transaction records.
txn_id (UNIQUE)
txn_date
amount
reference
3️. reconciliation_results
Stores reconciliation outcomes.
txn_id
status (MATCHED, AMOUNT_MISMATCH, MISSING_IN_INTERNAL, MISSING_IN_BANK)

>>System Workflow:
Load internal and bank transactions from CSV files
Store records in MySQL with duplicate protection
Compare transactions using optimized hash-based logic
Classify each transaction by reconciliation status
Store results in database
Generate summary and CSV report

>> Reconciliation Algorithm:
Internal transactions are loaded into a hash map using transaction ID as key
Bank transactions are scanned and compared in O(1) time per record
A set tracks matched transaction IDs
Remaining internal records are marked as missing in bank

>>Time Complexity:
Building hash map: O(n)
Comparing bank transactions: O(m)
Final internal scan: O(n)
Overall Complexity: O(n + m)

>>Edge Cases Handled:
Duplicate transaction entries
Missing transactions in either source
Amount mismatches
Date posting delays
Safe money handling using DECIMAL
Re-runnable reconciliation without duplicate results

>>Sample Output
Console Summary:
MATCHED: 2
AMOUNT_MISMATCH: 1
MISSING_IN_INTERNAL: 1
MISSING_IN_BANK: 1
>>Generated File:
reconciliation_report.csv
