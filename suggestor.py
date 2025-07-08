def suggest_improvements(bottlenecks_df):
    suggestions = []
    for _, row in bottlenecks_df.iterrows():
        if row["Review_Time_Hours"] > 48:
            suggestions.append("Assign backup reviewers to reduce long review times.")
        elif row["Review_Time_Hours"] > 24:
            suggestions.append("Ensure reviewer availability during PR assignment.")
        else:
            suggestions.append("Investigate possible process delays.")
    return suggestions
