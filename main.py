# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "datablob",
#     "requests",
#     "simple-env",
# ]
# ///
import csv
import datablob
import io
import requests
import simple_env as se

AWS_BUCKET_NAME = se.get("AWS_BUCKET_NAME")

AWS_BUCKET_PATH = se.get("AWS_BUCKET_PATH")


metadata_url = "https://data.transportation.gov/api/views/8bui-9xvu.json"
metadata_response = requests.get(metadata_url)
metadata_response.raise_for_status()
metadata_data = metadata_response.json()
numerical_columns = [
    column["name"]
    for column in metadata_data["columns"]
    if column["dataTypeName"] == "number" and column["renderTypeName"] == "number"
]

url = "https://data.transportation.gov/api/views/8bui-9xvu/rows.csv?accessType=Download"
response = requests.get(url)
response.raise_for_status()

f = io.StringIO(response.text)
rows = list(csv.DictReader(f))

if len(rows) < 10:
    raise Exception("[dataops-ntd-monthly-ridership] unexpected number of results")

for row in rows:
    for key in numerical_columns:
        value = row[key]
        if value in ["", None]:
            row[key] = None
        else:
            row[key] = float(value)

client = datablob.DataBlobClient(
    bucket_name=AWS_BUCKET_NAME, bucket_path=AWS_BUCKET_PATH
)

client.update_dataset(
    name="ntd_monthly_ridership",
    description="National Transit Database: Complete Monthly Ridership (with Adjustments and Estimates)",
    version="1",
    data=rows,
    column_names=[
        "NTD ID",
        "Legacy NTD ID",
        "Agency",
        "Mode/Type of Service Status",
        "Active",
        "Reporter Type",
        "UACE CD",
        "UZA Name",
        "Mode",
        "TOS",
        "3 Mode",
        "Date",
        "UPT",
        "VOMS",
        "VRH",
        "VRM",
        "Agency Mode TOS Date",
        "State",
        "FTA Region",
    ],
    json=True,
    jsonl=True,
    parquet=True,
)

print(f"[dataops-ntd-monthly-ridership] updated {len(rows)} rows")
