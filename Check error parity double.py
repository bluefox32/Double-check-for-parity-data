import numpy as np

def calculate_parity(data):
    # 行パリティと列パリティの計算
    row_parity = np.mod(data.sum(axis=1), 2)
    col_parity = np.mod(data.sum(axis=0), 2)
    return row_parity, col_parity

def add_parity_bits(data):
    row_parity, col_parity = calculate_parity(data)
    
    # データに行パリティを追加
    extended_data = np.hstack((data, row_parity.reshape(-1, 1)))
    # 列パリティを追加
    extended_data = np.vstack((extended_data, np.append(col_parity, 0)))
    
    return extended_data

def check_and_correct_errors(extended_data):
    row_parity_check, col_parity_check = calculate_parity(extended_data[:-1, :-1])
    
    error_row = np.where(row_parity_check != extended_data[:-1, -1])[0]
    error_col = np.where(col_parity_check != extended_data[-1, :-1])[0]
    
    if error_row.size > 0 and error_col.size > 0:
        extended_data[error_row[0], error_col[0]] ^= 1
        print(f"Error corrected at position ({error_row[0]}, {error_col[0]})")
    
    return extended_data

# サンプルデータの生成
data = np.random.randint(2, size=(4, 4))
print("Original Data:")
print(data)

# パリティビットの追加
extended_data = add_parity_bits(data)
print("Extended Data with Parity Bits:")
print(extended_data)

# エラーの挿入（例として[1, 1]の位置にエラーを挿入）
extended_data[1, 1] ^= 1
print("Data with Error Inserted:")
print(extended_data)

# エラーの検出と訂正
corrected_data = check_and_correct_errors(extended_data)
print("Corrected Data:")
print(corrected_data)