import psycopg2
from setconfigs import load_config

def connect(config):
  """ Connect to the PostgreSQL database server """
  try:
    #config.py module: pass the configuration to the connect() function and unpack it using the ** operator.
      conn = psycopg2.connect(**config)
      return conn
      print('Connected to the PostgreSQL server.')
  except (psycopg2.DatabaseError, Exception) as error:
    print(error)

#if __name__ == '__main__':
config = load_config()
conn = connect(config)
cursor = conn.cursor()

