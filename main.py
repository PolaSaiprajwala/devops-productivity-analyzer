import pandas as pd
from analysis.bottleneck_detector import detect_bottlenecks
from recommendations.suggestor import generate_recommendations

data = pd.read_csv('data/sample_data.csv')
bottlenecks = detect_bottlenecks(data)
recs = generate_recommendations(bottlenecks)

print("💡 Recommendations:")
for rec in recs:
    print(f"PR #{rec[0]}: {rec[1]}")
