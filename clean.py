import pandas as pd

# Load the dataset with proper encoding
df = pd.read_csv(r'C:\Users\ASUS\desktop\DataCleanTask1\sales_data_sample.csv', encoding='ISO-8859-1', delimiter=',')

# 1. Show original column names and dataset shape
print("Original Columns:\n", df.columns.tolist())
print("Shape (rows, columns):", df.shape)
print("First 5 rows:\n", df.head())

# 2. Clean column names: strip spaces, lowercase, replace spaces/special characters with underscores
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(' ', '_')
    .str.replace('[^a-z0-9_]', '', regex=True)  # Remove special characters
)

print("\nCleaned Columns:\n", df.columns.tolist())

# 3. Drop duplicate rows
df.drop_duplicates(inplace=True)

# 4. Drop rows with all NaN values
df.dropna(how='all', inplace=True)

# 5. Fill missing values
for col in df.columns:
    if df[col].dtype == 'O':  # object/string columns
        df[col] = df[col].fillna('unknown')
    else:
        df[col] = df[col].fillna(0)

# 6. Standardize string formatting (lowercase and strip whitespace)
string_cols = df.select_dtypes(include='object').columns
df[string_cols] = df[string_cols].apply(lambda x: x.str.strip().str.lower())

# 7. Convert 'orderdate' to datetime if present
if 'orderdate' in df.columns:
    df['orderdate'] = pd.to_datetime(df['orderdate'], errors='coerce')

# 8. Print summary of missing values
print("\nMissing values after cleaning:\n", df.isnull().sum())

# 9. Save cleaned data to new CSV file
df.to_csv('cleaned_sales_data.csv', index=False)

print("Data cleaning complete. Cleaned data saved to 'cleaned_sales_data.csv'")
