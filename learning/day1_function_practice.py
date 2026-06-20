import pandas as pd

def remove_column(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    """
    Return a dataframe with one column removed.
    """
    return df.drop(columns=[column_name])

def convert_yes_no_to_binary(series: pd.Series) -> pd.Series:
    """
    Convert yes/no labels into 1/0 labels.
    """
    return series.map({"yes":1, "no":0})

def split_features_target(
    df: pd.DataFrame, 
    target_column: str,
) -> tuple[pd.DataFrame, pd.Series]:
    """
    Split a dataframe into features X and target y.
    """
    if target_column not in df.columns:
        raise ValueError(f"Target column '{target_column}' not found in dataframe.")

    y = convert_yes_no_to_binary(df[target_column])
    X = remove_column(df, target_column)

    return X, y

def main() -> None:

    df = pd.DataFrame(
        {
            "age": [25, 40, 35],
            "job": ["admin", "tech", "admin"],
            "y": ["yes", "no", "yes"],
        }
    )

    X, y = split_features_target(df, "y") 

    print("Original DataFrame:")
    print(df)

    print("\nFeatures after removing target column:")
    print(X)

    print("\nTarget variable after converting yes/no to binary:")
    print(y)

    # Uncomment this to test the error:
    # split_features_target(df, "missing_target")

if __name__ == "__main__":
    main()