CREATE DATABASE bank_reconciliation;
USE bank_reconciliation;
CREATE TABLE internal_transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    txn_id VARCHAR(50),
    txn_date DATE,
    amount DECIMAL(10,2),
    reference VARCHAR(100),
    UNIQUE (txn_id)
);
CREATE TABLE bank_transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    txn_id VARCHAR(50),
    txn_date DATE,
    amount DECIMAL(10,2),
    reference VARCHAR(100),
    UNIQUE (txn_id)
);
CREATE TABLE reconciliation_results (
    id INT AUTO_INCREMENT PRIMARY KEY,
    txn_id VARCHAR(50),
    status ENUM(
        'MATCHED',
        'AMOUNT_MISMATCH',
        'MISSING_IN_INTERNAL',
        'MISSING_IN_BANK'
    ),
    remarks VARCHAR(255)
);

