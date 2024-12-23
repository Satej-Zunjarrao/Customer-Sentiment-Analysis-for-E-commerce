import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from transformers import BertTokenizer, BertForSequenceClassification, Trainer, TrainingArguments

def train_logistic_regression(data, text_column, label_column):
    """
    Trains a Logistic Regression model for sentiment classification.

    Args:
        data (pd.DataFrame): Dataset with text and labels.
        text_column (str): Name of the column with text data.
        label_column (str): Name of the column with sentiment labels.

    Returns:
        LogisticRegression: Trained Logistic Regression model.
    """
    try:
        # Split the dataset into train and test sets
        X_train, X_test, y_train, y_test = train_test_split(
            data[text_column], data[label_column], test_size=0.2, random_state=42
        )
        
        # Convert text to TF-IDF features
        vectorizer = TfidfVectorizer(max_features=5000)
        X_train_tfidf = vectorizer.fit_transform(X_train)
        X_test_tfidf = vectorizer.transform(X_test)
        
        # Train the Logistic Regression model
        model = LogisticRegression()
        model.fit(X_train_tfidf, y_train)
        
        # Evaluate the model
        predictions = model.predict(X_test_tfidf)
        print("Classification Report for Logistic Regression:\n")
        print(classification_report(y_test, predictions))
        
        return model, vectorizer
    except Exception as e:
        print(f"Error training Logistic Regression model: {e}")
        return None, None

def fine_tune_bert(data, text_column, label_column):
    """
    Fine-tunes a pre-trained BERT model for sentiment classification.

    Args:
        data (pd.DataFrame): Dataset with text and labels.
        text_column (str): Name of the column with text data.
        label_column (str): Name of the column with sentiment labels.

    Returns:
        BertForSequenceClassification: Fine-tuned BERT model.
    """
    try:
        # Initialize the tokenizer and model
        tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
        model = BertForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=3)
        
        # Tokenize and encode the dataset
        encoded_data = data[text_column].apply(
            lambda x: tokenizer(x, padding="max_length", truncation=True, return_tensors="pt")
        )
        labels = data[label_column].values
        
        # Define training arguments
        training_args = TrainingArguments(
            output_dir="./satej_bert_model",
            num_train_epochs=3,
            per_device_train_batch_size=8,
            save_steps=10_000,
            save_total_limit=2,
        )
        
        # Trainer setup
        trainer = Trainer(
            model=model,
            args=training_args,
            train_dataset=encoded_data,
            eval_dataset=encoded_data,
        )
        
        # Fine-tune the model
        trainer.train()
        print("BERT fine-tuning complete.")
        
        return model
    except Exception as e:
        print(f"Error fine-tuning BERT model: {e}")
        return None
