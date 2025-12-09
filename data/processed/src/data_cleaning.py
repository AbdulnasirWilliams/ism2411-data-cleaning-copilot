#Fix a messy code file by improving readability, removing redundancies, and following best practices.
import pandas as pd
def load_data(file_path:str):
    df = pd.red_csv(file_path)
    return df
def clean_data(df:pd.DataFrame) -> pd.DataFrame:
    # Remove duplicates
    df = df.drop_duplicates()
    # Handle missing values
    df = df.fillna(method='ffill').fillna(method='bfill')
    # Standardize column names
    df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]
    return df
def handle_missing_values(df:pd.DataFrame) -> pd.DataFrame:
    for col in df.select_dtypes(include=['float64', 'int64']).columns:
        df[col].fillna(df[col].mean(), inplace=True)
    for col in df.select_dtypes(include=['object']).columns:
        df[col].fillna(df[col].mode()[0], inplace=True)
    return df
def remove_invalid_rows(df:pd.DataFrame) -> pd.DataFrame:
    for col in df.select_dtypes(include=['float64', 'int64']).columns:
        df = df[df[col] >= 0]
    return df
if __name__ == "__main__":
    raw_path = 'data/raw/data.csv'
    cleaned_path = 'data/processed/cleaned_data.csv'
    df_raw = load_data(raw_path)
    df_cleaned = clean_data(df_raw)
    df_cleaned = handle_missing_values(df_cleaned)
    df_cleaned = remove_invalid_rows(df_cleaned)

    df_cleaned
    print("Cleaning is complete. Cleaned data saved to", cleaned_path)
    print(df_cleaned.head())
    