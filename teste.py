# Código básico em Python para extração e carga
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://user:password@host/db')

query = "SELECT * FROM sales WHERE date >= CURRENT_DATE - INTERVAL '30 days';"
sales_data = pd.read_sql(query, engine)

# Transformação
sales_summary = sales_data.groupby('product_id').agg({'sales_amount': 'sum'}).reset_index()

# Carga no dashboard
sales_summary.to_sql('dashboard_table', engine, if_exists='replace', index=False)























