import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from spacy.lang.en import English

# Initialize NLP tools
stop_words = set(stopwords.words("english"))  # Set of common stopwords
stemmer = PorterStemmer()  # Stemmer to reduce words to their base form
nlp = English()
tokenizer = nlp.tokenizer  # Tokenizer for splitting text into tokens

def clean_text(text):
    """
    Cleans and preprocesses a given text string.

    Args:
        text (str): Raw text string to clean.

    Returns:
        str: Preprocessed and cleaned text.
    """
    try:
        # Remove non-alphabetic characters and extra spaces
        text = re.sub(r"[^a-zA-Z\s]", "", text)
        text = text.lower().strip()  # Convert to lowercase for consistency
        
        # Tokenize the text into words
        words = word_tokenize(text)
        
        # Remove stopwords from the tokenized list
        words = [word for word in words if word not in stop_words]
        
        # Apply stemming to each word
        words = [stemmer.stem(word) for word in words]
        
        # Reconstruct cleaned text
        return " ".join(words)
    except Exception as e:
        print(f"Error cleaning text: {e}")
        return ""

def preprocess_data(data, text_column):
    """
    Applies text cleaning to a specified column in the DataFrame.

    Args:
        data (pd.DataFrame): Data containing the text to preprocess.
        text_column (str): Name of the column with text data.

    Returns:
        pd.DataFrame: DataFrame with the cleaned text column.
    """
    try:
        # Apply the clean_text function to each row in the specified column
        data[text_column] = data[text_column].apply(lambda x: clean_text(x) if isinstance(x, str) else "")
        print(f"Successfully cleaned data in the column '{text_column}'.")
        return data
    except Exception as e:
        print(f"Error preprocessing data: {e}")
        return data

if __name__ == "__main__":
    # Load the raw data from a CSV file
    raw_data = pd.read_csv("customer_reviews_sql.csv")
    
    # Clean the 'review_text' column in the dataset
    cleaned_data = preprocess_data(raw_data, text_column="review_text")
    
    # Save the cleaned data back to a CSV file
    cleaned_data.to_csv("customer_reviews_cleaned.csv", index=False)
    print("Cleaned data successfully saved.")
