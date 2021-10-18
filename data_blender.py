import pandas as pd
registry_df = pd.read_csv('data/datagov-uk-6859075c-3857-4b26-b5b6-cac93232d99b'
	'/data/numbers_of_patients_registered_at_a_gp_practice_january_2017_gp_2.csv')
names_df = pd.read_csv('data/GP_names.csv')
names_df.drop_duplicates(subset=['gp_practice_code'], keep='last', inplace=True)
final_df = registry_df.merge(names_df, on='gp_practice_code', how="inner")
final_df.to_csv('data/blended_data.csv', index=False)
