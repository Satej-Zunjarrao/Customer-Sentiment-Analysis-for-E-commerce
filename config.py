# Configuration file for storing reusable settings and constants

# Database connection settings
DB_CONFIG = {
    "host": "satej_database_host",
    "port": "3306",  # Default MySQL port
    "user": "satej_user",
    "password": "satej_password",
    "database": "satej_database_name"
}

# API connection settings
API_CONFIG = {
    "url": "https://satej-api.com/reviews",
    "key": "satej_api_key"
}

# Model paths for saving and loading pre-trained models
MODEL_PATHS = {
    "logistic_regression": "./satej_models/logistic_regression_model.pkl",
    "vectorizer": "./satej_models/tfidf_vectorizer.pkl",
    "bert_model": "./satej_models/bert_model/"
}

# Scheduler settings for automation
SCHEDULER_CONFIG = {
    "run_time": "02:00"  # 24-hour format time for pipeline execution
}

# Visualization settings
VISUALIZATION_SETTINGS = {
    "default_palette": "viridis",
    "plot_style": "ggplot"
}

# Logging configuration
LOGGING_CONFIG = {
    "log_file": "./satej_logs/pipeline.log",
    "log_level": "INFO"  # Options: DEBUG, INFO, WARNING, ERROR, CRITICAL
}

# General settings
GENERAL_SETTINGS = {
    "random_seed": 42,  # Ensures reproducibility across random processes
    "max_tfidf_features": 5000  # Maximum features for the TF-IDF vectorizer
}
