This project loads and processes raw sales data into a data warehouse. The pipeline includes several steps:

1. **Schema Inference**: Automatically infer the schema from raw gzipped files.
2. **Staging Tables**: Load raw data into staging tables.
3. **Normalization**: Normalize hierarchy tables into separate levels.
4. **Materialized View**: Create a materialized view for weekly sales aggregation.
5. **Incremental Loads**: Perform incremental loads for new or updated data.

## Steps to Run:

1. Install dependencies:
pip install -r requirements.txt

2. Configure database and storage settings in `config/config.yaml`.

3. Run the ETL scripts:
- Load data: `python_scripting/load_data.py`
- Normalize hierarchy: `python_scripting/normalize_hierarchy.py`
- Create materialized view: `python_scripting/create_mview.py`
- Run data checks: `python_scripting/checks.py`
- Perform incremental load: `python_scripting/incremental_load.py`