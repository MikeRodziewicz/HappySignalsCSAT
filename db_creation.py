import psycopg2
import os

conn = psycopg2.connect(
    host="localhost",
    database="happy_signals",
    user= "postres",
    password= os.getenv('DB_PASS'),
    port=5432
)

cur = conn.cursor()



cur.execute("""
CREATE TABLE IF NOT EXISTS stp_mapping (
    queue_name TEXT,
    stp_name TEXT
) """)

# table for happy_signals data from csv
cur.execute("""
CREATE TABLE IF NOT EXISTS hs_data (
    created TEXT,
    request_number TEXT,
    category TEXT,
    location TEXT,
    score INTEGER,
    comment TEXT,
    time_lost INTEGER,
    department TEXT,
    language TEXT,
    sent_date TEXT,
    channel TEXT,
    company TEXT,
    reassigment_count INTEGER,
    priority TEXT,
    country TEXT,
    configuration_item TEXT,
    enterprise TEXT,
    sec_category TEXT,
    third_category TEXT,
    region TEXT,
    external_ticket TEXT,
    top_company TEXT,
    sub_company TEXT,
    it_profile TEXT,
    extra_data TEXT,
    referrer_url TEXT,
    referrer_id TEXT,
    hs_id INTEGER,
    factor TEXT
) """)

# table for remedy INC data with req number for hs mapping

cur.execute("""
CREATE TABLE IF NOT EXISTS remedy_inc (
    service_request_idS TEXT,
    incident_id TEXT,
    summary TEXT,
    service_request TEXT,
    priority TEXT,
    status TEXT,
    assigned_group TEXT,
    assignee TEXT,
    target_date TEXT,
    slm_real_time TEXT,
    reported_date TEXT,
    vendor_ticket TEXT,
    product_name TEXT,
    incident_association TEXT,
    security_related TEXT,
    security_type TEXT,
    configuration_item TEXT,
    product_category_one TEXT,
    product_category_two TEXT,
    product_category_three TEXT,
    resolution TEXT,
    resolution_cat TEXT,
    resolution_cat_one TEXT,
    resolution_cat_two TEXT,
    resolution_cat_three TEXT,
    resolution_method TEXT
) """)

conn.close()
