import psycopg
from setconfigs import load_config

def connect(config):
  """ Connect to the PostgreSQL database server """
  try:
    #config.py module: pass the configuration to the connect() function and unpack it using the ** operator.
    with psycopg.connect(**config) as conn:
      print('Connected to the PostgreSQL server.')
      return conn
  except (psycopg.DatabaseError, Exception) as error:
    print(error)

if __name__ == '__main__':
  config = load_config()
  connect(config)
 
# Open a cursor to perform database operations
#cursor = connection.cursor()#

# Execute a command: this creates a new table
#cursor.execute("SELECT data_source FROM scomed.scomed_prescription WHERE p_presc_date_from = DATE '2024-01-01' AND p_presc_date_to = DATE '2024-12-31' LIMIT 1")
###
#rows = cursor.fetchall()
#columns = [desc[0] for desc in cursor.description]
#print(pd.DataFrame(rows, columns = columns))

