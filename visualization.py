import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_sentiment_distribution(data, sentiment_column):
    """
    Plots the distribution of sentiments in the dataset.

    Args:
        data (pd.DataFrame): Dataset containing sentiment predictions.
        sentiment_column (str): Name of the column with sentiment labels.

    Returns:
        None
    """
    try:
        # Count the occurrences of each sentiment
        sentiment_counts = data[sentiment_column].value_counts()
        
        # Plot the sentiment distribution
        plt.figure(figsize=(8, 6))
        sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, palette="coolwarm")
        plt.title("Sentiment Distribution", fontsize=16)
        plt.xlabel("Sentiment")
        plt.ylabel("Count")
        plt.show()
    except Exception as e:
        print(f"Error visualizing sentiment distribution: {e}")

def plot_sentiment_trends(data, date_column, sentiment_column):
    """
    Plots the trend of sentiments over time.

    Args:
        data (pd.DataFrame): Dataset containing date and sentiment columns.
        date_column (str): Name of the column with dates.
        sentiment_column (str): Name of the column with sentiment labels.

    Returns:
        None
    """
    try:
        # Convert the date column to datetime format for better handling
        data[date_column] = pd.to_datetime(data[date_column])
        
        # Group by date and sentiment to calculate daily sentiment counts
        trends = data.groupby([date_column, sentiment_column]).size().reset_index(name="count")
        
        # Plot sentiment trends over time
        plt.figure(figsize=(12, 6))
        sns.lineplot(data=trends, x=date_column, y="count", hue=sentiment_column, marker="o")
        plt.title("Sentiment Trends Over Time", fontsize=16)
        plt.xlabel("Date")
        plt.ylabel("Count")
        plt.legend(title="Sentiment")
        plt.show()
    except Exception as e:
        print(f"Error visualizing sentiment trends: {e}")

if __name__ == "__main__":
    # Load the predictions dataset
    predictions = pd.read_csv("sentiment_predictions.csv")
    
    # Plot sentiment distribution
    plot_sentiment_distribution(predictions, sentiment_column="predicted_sentiment")
    
    # Plot sentiment trends
    plot_sentiment_trends(predictions, date_column="review_date", sentiment_column="predicted_sentiment")
