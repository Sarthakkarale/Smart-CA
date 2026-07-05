-- CREATE DATABASE smart_ca;
use smart_ca;

CREATE TABLE roles (
    role_id INT AUTO_INCREMENT PRIMARY KEY,
    role_name ENUM('USER','CA','ADMIN') NOT NULL UNIQUE
);


CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    phone VARCHAR(15),
    password_hash TEXT NOT NULL,
    role_id INT NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,

    FOREIGN KEY (role_id) REFERENCES roles(role_id)
);

CREATE TABLE financial_profile (
    profile_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL UNIQUE,
    age INT NOT NULL,
    occupation VARCHAR(100),
    monthly_income DECIMAL(12,2) NOT NULL,
    monthly_expenses DECIMAL(12,2),
    annual_income DECIMAL(12,2),
    family_size INT,
    dependents INT,
    marital_status ENUM('SINGLE','MARRIED','OTHER'),
    risk_appetite ENUM('LOW','MODERATE','HIGH'),
    financial_goals TEXT,
    existing_savings DECIMAL(12,2),
    existing_investments DECIMAL(12,2),
    existing_insurance DECIMAL(12,2),
    debt_amount DECIMAL(12,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

CREATE TABLE uploaded_documents (
    document_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    document_type ENUM('SALARY_SLIP','BANK_STATEMENT','FORM_16','INSURANCE_POLICY','INVESTMENT_STATEMENT','OTHER') NOT NULL,
    file_name VARCHAR(255) NOT NULL,
    file_path TEXT NOT NULL,
    file_type VARCHAR(50),
    file_size BIGINT,
    upload_status ENUM('UPLOADED','PROCESSING','PROCESSED','FAILED') DEFAULT 'UPLOADED',
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

CREATE TABLE extracted_financial_data (
    extract_id INT AUTO_INCREMENT PRIMARY KEY,
    document_id INT NOT NULL,
    user_id INT NOT NULL,
    extracted_text LONGTEXT,
    structured_json JSON,
    extraction_confidence DECIMAL(5,2),
    processed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (document_id) REFERENCES uploaded_documents(document_id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

CREATE TABLE transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    document_id INT,
    transaction_date DATE NOT NULL,
    description TEXT,
    merchant VARCHAR(150),
    amount DECIMAL(12,2) NOT NULL,
    transaction_type ENUM('CREDIT','DEBIT') NOT NULL,
    category VARCHAR(100),
    predicted_category VARCHAR(100),
    confidence_score DECIMAL(5,2),
    source ENUM('MANUAL','OCR','BANK_UPLOAD') DEFAULT 'MANUAL',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (document_id) REFERENCES uploaded_documents(document_id) ON DELETE SET NULL
);

CREATE TABLE expense_reports (
    expense_report_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    month INT NOT NULL,
    year INT NOT NULL,
    total_income DECIMAL(12,2),
    total_expense DECIMAL(12,2),
    category_breakdown JSON,
    spending_insights TEXT,
    generated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

CREATE TABLE tax_reports (
    tax_report_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    annual_income DECIMAL(12,2) NOT NULL,
    hra DECIMAL(12,2) DEFAULT 0,
    deduction_80c DECIMAL(12,2) DEFAULT 0,
    deduction_80d DECIMAL(12,2) DEFAULT 0,
    nps_deduction DECIMAL(12,2) DEFAULT 0,
    old_regime_tax DECIMAL(12,2),
    new_regime_tax DECIMAL(12,2),
    best_regime ENUM('OLD','NEW'),
    estimated_savings DECIMAL(12,2),
    tax_suggestions TEXT,
    generated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);
CREATE TABLE investment_reports (
    investment_report_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    risk_cluster ENUM('CONSERVATIVE','MODERATE','AGGRESSIVE'),
    current_investment DECIMAL(12,2),
    recommended_sip DECIMAL(12,2),
    asset_allocation JSON,
    recommended_products JSON,
    investment_advice TEXT,
    generated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
); 
CREATE TABLE insurance_reports (
    insurance_report_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    existing_health_cover DECIMAL(12,2),
    recommended_health_cover DECIMAL(12,2),
    existing_term_cover DECIMAL(12,2),
    recommended_term_cover DECIMAL(12,2),
    coverage_gap DECIMAL(12,2),
    recommendation_text TEXT,
    generated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);
CREATE TABLE financial_health_scores (
    score_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    savings_score INT DEFAULT 0,
    investment_score INT DEFAULT 0,
    debt_score INT DEFAULT 0,
    insurance_score INT DEFAULT 0,
    tax_score INT DEFAULT 0,
    expense_score INT DEFAULT 0,
    final_score INT NOT NULL,
    score_breakdown JSON,
    remarks TEXT,
    generated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);
CREATE TABLE recommendations (
    recommendation_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    expense_report_id INT,
    tax_report_id INT,
    investment_report_id INT,
    insurance_report_id INT,
    score_id INT,
    recommendation_text LONGTEXT NOT NULL,
    recommendation_json JSON,
    generated_by ENUM('AI','CA') DEFAULT 'AI',
    status ENUM('AI_GENERATED','PENDING_CA_REVIEW','CA_APPROVED','CA_MODIFIED','CA_REJECTED') DEFAULT 'AI_GENERATED',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (expense_report_id) REFERENCES expense_reports(expense_report_id) ON DELETE SET NULL,
    FOREIGN KEY (tax_report_id) REFERENCES tax_reports(tax_report_id) ON DELETE SET NULL,
    FOREIGN KEY (investment_report_id) REFERENCES investment_reports(investment_report_id) ON DELETE SET NULL,
    FOREIGN KEY (insurance_report_id) REFERENCES insurance_reports(insurance_report_id) ON DELETE SET NULL,
    FOREIGN KEY (score_id) REFERENCES financial_health_scores(score_id) ON DELETE SET NULL
);
CREATE TABLE ca_users (
    ca_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL UNIQUE,
    membership_number VARCHAR(100) NOT NULL UNIQUE,
    firm_name VARCHAR(150),
    specialization VARCHAR(150),
    experience_years INT,
    verification_status ENUM('PENDING','VERIFIED','REJECTED') DEFAULT 'PENDING',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);
CREATE TABLE ca_reviews (
    review_id INT AUTO_INCREMENT PRIMARY KEY,
    recommendation_id INT NOT NULL,
    ca_id INT NOT NULL,
    action ENUM('APPROVED','MODIFIED','REJECTED') NOT NULL,
    original_recommendation LONGTEXT,
    modified_recommendation LONGTEXT,
    comments TEXT,
    reviewed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (recommendation_id) REFERENCES recommendations(recommendation_id) ON DELETE CASCADE,
    FOREIGN KEY (ca_id) REFERENCES ca_users(ca_id) ON DELETE CASCADE
);

CREATE TABLE chatbot_history (
    chat_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    user_query TEXT NOT NULL,
    bot_response LONGTEXT NOT NULL,
    rag_context JSON,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);
CREATE TABLE rag_documents (
    rag_document_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    source_type ENUM('INCOME_TAX','SEBI','RBI','AMFI','IRDAI','OTHER'),
    file_path TEXT,
    document_url TEXT,
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE rag_chunks (
    chunk_id INT AUTO_INCREMENT PRIMARY KEY,
    rag_document_id INT NOT NULL,
    chunk_text LONGTEXT NOT NULL,
    chunk_index INT,
    embedding_id VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (rag_document_id) REFERENCES rag_documents(rag_document_id) ON DELETE CASCADE
);
CREATE TABLE user_sessions (
    session_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    refresh_token TEXT,
    ip_address VARCHAR(100),
    user_agent TEXT,
    expires_at DATETIME,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);
CREATE TABLE audit_logs (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    action VARCHAR(150) NOT NULL,
    table_name VARCHAR(100),
    record_id INT,
    old_data JSON,
    new_data JSON,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE SET NULL
);
INSERT INTO roles (role_name)
VALUES ('USER'), ('CA'), ('ADMIN');
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_transactions_user_date ON transactions(user_id, transaction_date);
CREATE INDEX idx_documents_user ON uploaded_documents(user_id);
CREATE INDEX idx_recommendations_user_status ON recommendations(user_id, status);
CREATE INDEX idx_ca_reviews_ca ON ca_reviews(ca_id);
CREATE INDEX idx_chatbot_user ON chatbot_history(user_id);

desc users
show INDEX FROM chatbot_history;
SELECT * FROM users;
ALTER TABLE user_sessions
ADD COLUMN is_revoked BOOLEAN DEFAULT FALSE,
ADD COLUMN last_used_at TIMESTAMP NULL,
ADD COLUMN device_name VARCHAR(150);

ALTER TABLE user_sessions
ADD COLUMN is_revoked BOOLEAN DEFAULT FALSE;
DESC user_sessions;
SELECT * FROM user_sessions;
select * from users;



SHOW TABLES;
SELECT * FROM roles;

USE smart_ca;

ALTER TABLE user_sessions
ADD COLUMN is_revoked BOOLEAN DEFAULT FALSE,
ADD COLUMN last_used_at TIMESTAMP NULL,
ADD COLUMN device_name VARCHAR(150);

DESC user_sessions;

select * from financial_profile;

DROP TABLE financial_profile;


CREATE TABLE financial_profile (

    profile_id INT AUTO_INCREMENT PRIMARY KEY,

    user_id INT UNIQUE NOT NULL,

    -- Personal
    dob DATE,
    gender VARCHAR(20),
    phone VARCHAR(20),
    city VARCHAR(100),
    state VARCHAR(100),
    pincode VARCHAR(10),

    -- Tax
    pan VARCHAR(20),
    aadhaar VARCHAR(20),
    tax_regime VARCHAR(30),
    resident_status VARCHAR(30),
    gst_registered BOOLEAN DEFAULT FALSE,
    gst_number VARCHAR(30),
    itr_history VARCHAR(30),

    -- Professional
    employment_type VARCHAR(50),
    occupation VARCHAR(100),
    company_name VARCHAR(150),
    annual_income DECIMAL(12,2),
    experience INT,
    business_type VARCHAR(100),

    -- Financial
    bank_name VARCHAR(100),
    monthly_expense DECIMAL(12,2),
    existing_investments DECIMAL(12,2),
    loan_amount DECIMAL(12,2),
    insurance_cover DECIMAL(12,2),
    emergency_fund DECIMAL(12,2),

    -- Goals
    retirement BOOLEAN DEFAULT FALSE,
    buy_house BOOLEAN DEFAULT FALSE,
    buy_car BOOLEAN DEFAULT FALSE,
    child_education BOOLEAN DEFAULT FALSE,
    wealth_creation BOOLEAN DEFAULT FALSE,
    travel BOOLEAN DEFAULT FALSE,
    other_goal TEXT,
    target_year INT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id)
        REFERENCES users(user_id)
        ON DELETE CASCADE
);
