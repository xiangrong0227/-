import pandas as pd

# 加載表格
table1 = pd.read_csv('table1.csv')  # 第一個表格
table2 = pd.read_csv('table2.csv')  # 第二個表格

# 將第二個表格從 wide 格式轉換為 long 格式
table2_long = table2.melt(id_vars=['ISO'], var_name='year', value_name='發展程度')

# 確保年分是數字格式，便於合併
table2_long['year'] = table2_long['year'].astype(int)

# 合併兩個表格
merged_table = pd.merge(table1, table2_long, on=['ISO', 'year'], how='left')

# 查看結果
print(merged_table)

# 保存結果到 CSV 文件
merged_table.to_csv('merged_table.csv', index=False)