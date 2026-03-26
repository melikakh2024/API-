**Mock API JSON to PostgreSQL ETL Project**

This project demonstrates an ETL (Extract, Transform, Load) pipeline for handling nested JSON data and loading it into a PostgreSQL database.

📂 Project Overview
*Reads a mock API JSON file containing user, project, and address data.*

**Flattens nested JSON structures to create clean, tabular data.**

**Explodes list fields (like tags) for proper relational representation.**

**Merges project and address datasets into a single final table.**

**Loads the cleaned dataset into a PostgreSQL database for further analysis.**


***⚙️ Key Features***
Handles nested JSON and multi-level arrays.
Maintains relationships between users, projects, and addresses.
Supports a full ETL workflow: JSON → DataFrame → PostgreSQL.
Prepares data for analytics or reporting in relational databases.

🗂 Input Data
JSON file: mock.json.txt
Contains nested data under keys: users, projects, address.history, tags.

🏁 Output
Flattened project data.

Flattened address history data.

Merged final dataset.

PostgreSQL table: public.mockAPI.

⚡ Prerequisites
Python libraries: pandas, sqlalchemy, psycopg2.
PostgreSQL database with access credentials.


✅ Notes
The project is modular and can be adapted for any nested JSON API.
The final table is ready for SQL queries, BI tools, or analytics pipelines.
