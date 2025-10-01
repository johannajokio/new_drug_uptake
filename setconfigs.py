import configparser

#The load_config() function uses the Python built-in configparser package to read data from the config.ini file.
def load_config(filename='config.ini', section='postgresql'):
  parser = configparser.ConfigParser()
  parser.read(filename)

  # get section, default to postgresql
  config = {}
  if parser.has_section(section):
    params = parser.items(section)
    for param in params:
      config[param[0]] = param[1]
  else:
    raise Exception('Section {0} not found in the {1} file'.format(section, filename))
  return config

#if __name__ == '__main__':
config = load_config()

#use the load_config() function to read the database configuration and connect to PostgreSQL in connect.py 

