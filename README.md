# dataops-ntd-monthly-ridership
Complete Monthly Ridership (with Adjustments and Estimates) from the National Transit Database

## frequency
The pipeline runs once an hour, but the data only changes once per month.

## columns
| column | example | description |
| :--- | :--- | :--- |
| **NTD ID** | `"40001"` | The unique agency id |
| **Legacy NTD ID** | `"40001"` | The unique agency id |
| **Agency** | `"Chattanooga Area Regional Transportation Authority` | The official name of the agency |
| **Mode/Type of Service Status** | `"Active"` | Whether mode is still running |
| **Reporter Type** | `"Full Reporter"` | Whether agency has to do full reporting |
| **UACE CD** | `"15832"` | Urban Area Census Code from Census Bureau |
| **UZA Name** | `"Chattanooga, TN--GA"` | Urbanized Area Name from Census Bureau |
| **Mode** | `"DR"` | Transit type (e.g., DR = 'Direct Response', IP = 'Inclined Plane', MB = 'Bus') |
| **TOS** | `"DO"` | (e.g., DO="Directly Operated", PT="Purchased Transportation", TN="Transportation Network", TX="Taxi Operators") |
| **3 Mode** | `"Bus"` | High-level mode group |
| **Date** | `"January 2002"` | Month of Reporting |
| **UPT** | `2736` | Unlinked Passenger Trips |
| **VOMS** | `11` | Vehicles Operated at Maximum Service for the specific mode | 
| **VRH** | `2683` | Vehicle Revenue Hours |
| **VRM** | `38090` | Vehicle Revenue Miles |
| **Agency Mode TOS Date** | `"40001_DR_DO_Active_Full Reporter_15832_2002-01-01"` | |
| **State** | `"TN"` | State where the Agency is headquartered |
| **FTA Region** | `"4"` | FTA Region |

## download links
- [metadata](https://gocarta.s3.us-east-2.amazonaws.com/public/data/ntd_monthly_ridership/v1/meta.json)
- [csv](https://gocarta.s3.us-east-2.amazonaws.com/public/data/ntd_monthly_ridership/v1/data.csv)
- [json](https://gocarta.s3.us-east-2.amazonaws.com/public/data/ntd_monthly_ridership/v1/data.json)
- [json lines](https://gocarta.s3.us-east-2.amazonaws.com/public/data/ntd_monthly_ridership/v1/data.jsonl)
- [parquet](https://gocarta.s3.us-east-2.amazonaws.com/public/data/ntd_monthly_ridership/v1/data.parquet)

## preview link
- You can query the data with SQL using [duckdb](https://shell.duckdb.org/#queries=v0,CREATE-TABLE-dataset-AS-SELECT-*-FROM-'s3%3A%2F%2Fgocarta%2Fpublic%2Fdata%2Fntd_monthly_ridership%2Fv1%2Fdata.parquet'~,Describe-dataset~,SELECT-Date%2C-UPT-FROM-dataset-WHERE-Agency-%3D-'Chattanooga-Area-Regional-Transportation-Authority'-AND-Mode-%3D-'IP'-ORDER-BY-Date-DESC-LIMIT-5~).

## support
Post an issue [here](https://github.com/gocarta/dataops-ntd-monthly-ridership/issues) or email the package author at DanielDufour@gocarta.org.
