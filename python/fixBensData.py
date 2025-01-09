import pandas as pd

df = pd.read_csv('../data/BenExcelStuff.csv', header=None)

df = df.dropna(how='all')

df.columns = df.iloc[0]
df = df[1:].reset_index(drop=True)

df.columns = [f"{col}_{i}" if col in df.columns[:i] else col for i, col in enumerate(df.columns)]

search_string = "Number"

duplicate_columns = df.columns[df.columns.str.contains(search_string, case=False, na=False)]

duplicate_columns = [x for x in duplicate_columns if len(x.split()) < 2]

matching_rows = []

for index, row in df.iterrows():
    if pd.notna(row[duplicate_columns[0]]) and df[duplicate_columns[1]].str.contains(row[duplicate_columns[0]]).any():
        matching_rows.append(row[['Number', 'Number_4', 'Serial Number', 'Status Code', 'Completion Status']])

new_df = pd.DataFrame(matching_rows,
                      columns=['Number', 'Number_4', 'Serial Number', 'Status Code', 'Completion Status'])

print(new_df)

new_df.to_excel('../output/NewDataOutput.xlsx', index=False)
