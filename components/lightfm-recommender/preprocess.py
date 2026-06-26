import pandas as pd

def load_data(path):
    "Load synthetic data from CSV."
    return pd.read_csv(path)

def preprocess(df):
    "Simple preprocessing: fill missing values."
    return df.fillna(0)

if __name__ == "__main__":
    import sys
    df = load_data(sys.argv[1])
    processed = preprocess(df)
    processed.to_csv("processed.csv", index=False)