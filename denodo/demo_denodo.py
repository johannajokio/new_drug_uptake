from my_postgresql import MyDenodoDB

my_denodo_object = MyDenodoDB()
my_denodo_object.connect()
print(my_denodo_object.query_to_df("SELECT data_source, sex FROM scomed.scomed_prescription WHERE p_presc_date_from = DATE '2024-01-01' AND p_presc_date_to = DATE '2024-12-31' LIMIT 1"))
my_denodo_object.close()

