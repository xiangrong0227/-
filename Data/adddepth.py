import pandas as pd

# 讀取 a 檔和 b 檔
a_file = "Data/alldata.csv"  # 替換為你的 a 檔路徑
b_file = "Data/catalog_with_mmi.csv"  # 替換為你的 b 檔路徑

df_a = pd.read_csv(a_file)
df_b = pd.read_csv(b_file)

# 確保 A 欄標題一致（如果不一致，可以重新命名）
# 假設 a 檔和 b 檔的 A 欄標題分別為 "A_col_in_a" 和 "A_col_in_b"
# df_a.rename(columns={"A_col_in_a": "A"}, inplace=True)
# df_b.rename(columns={"A_col_in_b": "A"}, inplace=True)

# 合併 b 檔的 B 欄到 a 檔，根據 A 欄匹配
# 假設 A 欄標題為 "A"，b 檔的 B 欄標題為 "B"
df_merged = pd.merge(df_a, df_b[['DisNo.', 'Depth']], on='DisNo.', how='left')

# 將合併結果保存為新的 Excel 文件
output_file = "merged_file.xlsx"
df_merged.to_csv(output_file, index=False)

print(f"合併完成！結果已保存到 {output_file}")