from sqlalchemy import create_engine

def create_mview():
    engine = create_engine('postgresql://username:password@localhost:5432/mydatabase')

    sql = """
    CREATE MATERIALIZED VIEW mview_weekly_sales AS
    SELECT 
        pos_site_id,
        sku_id,
        fsclwk_id,
        price_substate_id,
        type,
        SUM(sales_units) AS total_sales_units,
        SUM(sales_dollars) AS total_sales_dollars,
        SUM(discount_dollars) AS total_discount_dollars
    FROM fact_sales
    GROUP BY pos_site_id, sku_id, fsclwk_id, price_substate_id, type;
    """
    
    with engine.connect() as connection:
        connection.execute(sql)

if __name__ == "__main__":
    create_mview()
