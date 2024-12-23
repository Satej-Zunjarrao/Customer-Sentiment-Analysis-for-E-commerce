import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Configure Matplotlib for better visual outputs
plt.style.use("ggplot")

def visualize_rating_distribution(data, rating_column):
    """
    Plots the distribution of ratings in the dataset.

    Args:
        data (pd.DataFrame): Dataset containing ratings.
        rating_column (str): Name of the column with ratings.

    Returns:
        None
    """
    try:
        # Count the occurrences of each rating
        rating_counts = data[rating_column].value_counts().sort_index()
        
        # Plot the rating distribution
        plt.figure(figsize=(8, 6))
        sns.barplot(x=rating_counts.index, y=rating_counts.values, palette="viridis")
        plt.title("Rating Distribution", fontsize=16)
        plt.xlabel("Ratings")
        plt.ylabel("Count")
        plt.show()
    except Exception as e:
        print(f"Error visualizing rating distribution: {e}")

def generate_word_cloud(data, text_column):
    """
    Generates and displays a word cloud for the specified text column.

    Args:
        data (pd.DataFrame): Dataset containing text data.
        text_column (str): Name of the column with text data.

    Returns:
        None
    """
    try:
        # Combine all text into a single string
        text = " ".join(data[text_column].dropna())
        
        # Generate word cloud
        wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
        
        # Display the word cloud
        plt.figure(figsize=(10, 6))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.title("Word Cloud of Reviews", fontsize=16)
        plt.show()
    except Exception as e:
        print(f"Error generating word cloud: {e}")

if __name__ == "__main__":
    # Load cleaned data for EDA
    data = pd.read_csv("customer_reviews_cleaned.csv")
    
    # Visualize rating distribution
    visualize_rating_distribution(data, rating_column="rating")
    
    # Generate a word cloud for the 'review_text' column
    generate_word_cloud(data, text_column="review_text")
