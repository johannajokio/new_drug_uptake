import psycopg2
from connect import cursor
import pandas as pd

# Execute a command: this creates a new table
cursor.execute("WITH A as (SELECT presc_medicinal_product_join_key, min(getyear(presc_date_time)) AS earliest_date FROM scomed.scomed_prescription WHERE p_presc_date_from = '01-JAN-2020' AND p_presc_date_to = '01-JAN-2025' GROUP BY presc_medicinal_product_join_key) SELECT B.vmp_name, earliest_date  FROM A inner join scomed.medicinal_products B  ON A. presc_medicinal_product_join_key = B.prescribable_item_join_key;")

rows = cursor.fetchall()
columns = [desc[0] for desc in cursor.description]

# Put data in a pandas df
df = pd.DataFrame(rows, columns = columns)

head(df)
