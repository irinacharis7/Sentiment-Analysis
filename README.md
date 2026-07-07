# 😊 Amazon Review Sentiment Analysis using Python & NLP

## 📌 Project Overview

This project analyzes customer reviews from an Amazon product review dataset to determine whether each review expresses a **Positive**, **Negative**, or **Neutral** sentiment. The analysis is performed using **Natural Language Processing (NLP)** with the **TextBlob** library.

The processed data is stored in a CSV file, and the sentiment distribution is visualized using charts.

---

## 🚀 Features

- Reads real-world Amazon review data from a Kaggle dataset
- Cleans and processes review text
- Calculates sentiment polarity using TextBlob
- Classifies reviews as:
  - 😊 Positive
  - 😐 Neutral
  - 😞 Negative
- Saves the analyzed data to a CSV file
- Generates bar and pie charts to visualize sentiment distribution

---

## 🛠️ Technologies Used

- Python
- Pandas
- TextBlob
- Matplotlib
- VS Code

---

## 📂 Project Structure

```
Amazon-Sentiment-Analysis
│
├── dataset
│   └── Reviews.csv
│
├── sentiment.py
├── output.csv
├── sentiment_bar_chart.png
├── sentiment_pie_chart.png
├── requirements.txt
└── README.md
```

---

## 📊 Dataset

The project uses the **Amazon Fine Food Reviews** dataset downloaded from Kaggle.

The dataset contains customer reviews, ratings, summaries, and review text, making it suitable for sentiment analysis.

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/amazon-sentiment-analysis.git
```

Navigate to the project folder

```bash
cd amazon-sentiment-analysis
```

Install the required libraries

```bash
pip install -r requirements.txt
```

or

```bash
pip install pandas matplotlib textblob
```

Download the required TextBlob data

```bash
python -m textblob.download_corpora
```

---

## ▶️ Run the Project

Execute the Python script

```bash
python sentiment.py
```

The program will:

1. Load the Amazon reviews dataset
2. Clean the review data
3. Analyze the sentiment of each review
4. Classify reviews as Positive, Neutral, or Negative
5. Save the results to **output.csv**
6. Generate sentiment visualization charts

---

## 📊 Sample Output

| Review | Sentiment |
|---------|-----------|
| Excellent product! | Positive |
| Average quality | Neutral |
| Very disappointed | Negative |

---

## 📈 Sample Visualizations

- 📊 Bar Chart showing sentiment distribution
- 🥧 Pie Chart showing percentage of Positive, Neutral, and Negative reviews

---

## 💡 What I Learned

Through this project, I learned:

- Natural Language Processing (NLP)
- Sentiment Analysis using TextBlob
- Data preprocessing with Pandas
- Working with real-world datasets
- Data visualization using Matplotlib
- Exporting processed data to CSV

---

## 🎯 Challenges Faced

One challenge was understanding how computers interpret human language. I learned that TextBlob assigns a **polarity score** between **-1** and **+1** to each review. Based on this score, reviews are classified as Positive, Negative, or Neutral.

This project helped me understand the basics of sentiment analysis and how businesses can use customer feedback to gain valuable insights.

