import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

print("Loading Dataset...")

# Read only first 5000 reviews for faster execution
df = pd.read_csv("Reviews.csv", nrows=5000)

print("Dataset Loaded Successfully!")

df = df[["Score", "Summary", "Text"]]

# Remove missing values
df = df.dropna()

print("\nNumber of Reviews:", len(df))

def get_sentiment(review):

    polarity = TextBlob(review).sentiment.polarity

    if polarity > 0:
        return "Positive"

    elif polarity < 0:
        return "Negative"

    else:
        return "Neutral"

print("\nAnalyzing Reviews...")

df["Sentiment"] = df["Text"].apply(get_sentiment)

print("Analysis Complete!")

print("\nSample Results:\n")

print(df[["Summary", "Sentiment"]].head(10))

print("\nSentiment Count:\n")

print(df["Sentiment"].value_counts())

df.to_csv("output.csv", index=False, encoding="utf-8-sig")

print("\nCSV File Saved Successfully!")

plt.figure(figsize=(8,5))

df["Sentiment"].value_counts().plot(kind="bar")

plt.title("Amazon Review Sentiment Analysis")

plt.xlabel("Sentiment")

plt.ylabel("Number of Reviews")

plt.savefig("sentiment_bar_chart.png")

plt.show()

plt.figure(figsize=(6,6))

df["Sentiment"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.ylabel("")

plt.title("Sentiment Distribution")

plt.savefig("sentiment_pie_chart.png")

plt.show()

print("\nCharts Saved Successfully!")

print("\nProject Completed Successfully!")