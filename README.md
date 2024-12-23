# Customer-Sentiment-Analysis-for-E-commerce
Built an NLP-based system to analyze customer reviews and derive sentiment insights.

# Customer Sentiment Analysis System

## Overview
The **Customer Sentiment Analysis System** is a Python-based solution designed to analyze customer reviews and feedback for e-commerce products. The system utilizes advanced Natural Language Processing (NLP) techniques and machine learning models to extract valuable insights from textual data, enabling businesses to improve customer satisfaction and product offerings.

This project includes a modular and scalable pipeline for data collection, cleaning, exploratory analysis, sentiment classification, visualization, and automation.

---

## Key Features
- **Data Collection**: Extracts customer reviews from SQL databases and APIs.
- **Data Cleaning**: Preprocesses text using tokenization, stop-word removal, and stemming.
- **Exploratory Data Analysis (EDA)**: Visualizes rating distributions and common review terms.
- **Sentiment Classification**: Builds ML models (Logistic Regression, BERT) to classify reviews into positive, negative, or neutral sentiments.
- **Visualization**: Generates sentiment trends and distribution plots.
- **Automation**: Automates the pipeline to process new data periodically.

---

## Directory Structure

```plaintext
project/
│
├── data_extraction.py          # Handles data loading from databases and APIs
├── data_cleaning.py            # Preprocesses and cleans raw text data
├── exploratory_data_analysis.py# Generates visualizations and insights
├── sentiment_model.py          # Trains and fine-tunes sentiment classification models
├── sentiment_pipeline.py       # Orchestrates the entire sentiment analysis pipeline
├── visualization.py            # Creates sentiment-related visualizations
├── automation.py               # Automates the pipeline with scheduled runs
├── config.py                   # Stores reusable configurations and constants
├── utils.py                    # Provides helper functions for logging, metrics, etc.
├── README.md                   # Project documentation
```

# Modules

## 1. `data_extraction.py`
- Extracts data from SQL databases and APIs.
- Saves extracted data in CSV format for preprocessing.

## 2. `data_cleaning.py`
- Preprocesses text using NLP techniques (e.g., tokenization, stemming).
- Outputs a cleaned dataset for analysis.

## 3. `exploratory_data_analysis.py`
- Visualizes rating distributions and generates word clouds.
- Provides insights into review patterns.

## 4. `sentiment_model.py`
- Trains ML models for sentiment classification.
- Supports Logistic Regression and fine-tuned BERT models.

## 5. `sentiment_pipeline.py`
- Orchestrates the complete sentiment analysis workflow.
- Modular design enables seamless integration of all components.

## 6. `visualization.py`
- Creates sentiment-related visualizations.
- Plots sentiment trends and distributions for stakeholder reporting.

## 7. `automation.py`
- Automates the pipeline to process new data daily.
- Uses the `schedule` library for task scheduling.

## 8. `config.py`
- Centralized configuration file for database, API, model paths, and logging.

## 9. `utils.py`
- Helper functions for logging, directory creation, random seed initialization, and metric calculations.

# Contact

For queries or collaboration, feel free to reach out:

- **Name**: Satej Zunjarrao  
- **Email**: zsatej1028@gmail.com

