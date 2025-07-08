import pandas as pd

def analyze_workflow(df):
    df["Created_At"] = pd.to_datetime(df["Created_At"])
    df["Reviewed_At"] = pd.to_datetime(df["Reviewed_At"])
    df["Merged_At"] = pd.to_datetime(df["Merged_At"])

    df["Time_to_First_Review"] = (df["Reviewed_At"] - df["Created_At"]).dt.total_seconds() / 3600
    df["Time_to_Merge"] = (df["Merged_At"] - df["Created_At"]).dt.total_seconds() / 3600

    return df
