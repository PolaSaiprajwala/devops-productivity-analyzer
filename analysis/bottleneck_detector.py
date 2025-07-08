import pandas as pd
from sklearn.ensemble import IsolationForest

def detect_bottlenecks(data):
    # Already a DataFrame
    if "Review_Time_Hours" not in data.columns:
        raise ValueError("Column 'Review_Time_Hours' not found in the data.")

    clf = IsolationForest(contamination=0.3, random_state=42)
    X = data[["Review_Time_Hours"]].values
    preds = clf.fit_predict(X)

    data["Anomaly"] = preds
    bottlenecks = data[data["Anomaly"] == -1]

    return bottlenecks
