from data_extraction import extract_from_sql, extract_from_api
from data_cleaning import preprocess_data
from exploratory_data_analysis import visualize_rating_distribution, generate_word_cloud
from sentiment_model import train_logistic_regression, fine_tune_bert

def sentiment_analysis_pipeline(sql_query):
    """
    Orchestrates the sentiment analysis pipeline.

    Args:
        sql_query (str): SQL query for data extraction.

    Returns:
        None
    """
    try:
        # Step 1: Data Extraction
        data = extract_from_sql(sql_query)
        if data is None:
            raise Exception("Data extraction failed.")
        print("Step 1: Data extraction complete.")
        
        # Step 2: Data Cleaning
        cleaned_data = preprocess_data(data, text_column="review_text")
        print("Step 2: Data cleaning complete.")
        
        # Step 3: Exploratory Data Analysis
        visualize_rating_distribution(cleaned_data, rating_column="rating")
        generate_word_cloud(cleaned_data, text_column="review_text")
        print("Step 3: EDA complete.")
        
        # Step 4: Sentiment Model Training
        logistic_model, vectorizer = train_logistic_regression(cleaned_data, "review_text", "sentiment")
        print("Step 4: Logistic Regression model training complete.")
        
        bert_model = fine_tune_bert(cleaned_data, "review_text", "sentiment")
        print("Step 4: BERT model fine-tuning complete.")
        
    except Exception as e:
        print(f"Error in sentiment analysis pipeline: {e}")

if __name__ == "__main__":
    # SQL query example
    sql_query = "SELECT * FROM customer_reviews WHERE review_date > '2022-01-01'"
    sentiment_analysis_pipeline(sql_query)
