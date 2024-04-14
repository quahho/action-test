import os
import json
from google.cloud import bigquery
from google.oauth2 import service_account
# credentials = service_account.Credentials.from_service_account_file('2x-bq-key.json')

secret_key = os.environ["SOME_SECRET"]

json_acct_info = json.loads(secret_key)
credentials = service_account.Credentials.from_service_account_info(json_acct_info)

project_id = 'x-marketing'
client = bigquery.Client(credentials= credentials,project=project_id)

query_job = client.query("""
    SELECT property_name.value 
    FROM `x-marketing.sandler_hubspot.companies` 
    LIMIT 10
""")

results = query_job.result() # Wait for the job to complete.

for row in results:
    print(row)
