import logging
import os
import random
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Initialize logging
from config import LOGGING_CONFIG

logging.basicConfig(
    filename=LOGGING_CONFIG["log_file"],
    level=getattr(logging, LOGGING_CONFIG["log_level"]),
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_message(message, level="INFO"):
    """
    Logs a message to the log file and console.

    Args:
        message (str): The message to log.
        level (str): Logging level (e.g., INFO, WARNING, ERROR).

    Returns:
        None
    """
    try:
        log_function = getattr(logging, level.lower(), logging.info)
        log_function(message)
        print(message)
    except Exception as e:
        print(f"Error in logging message: {e}")

def create_directory(path):
    """
    Creates a directory if it does not exist.

    Args:
        path (str): Path of the directory to create.

    Returns:
        None
    """
    try:
        if not os.path.exists(path):
            os.makedirs(path)
            log_message(f"Directory created: {path}", "INFO")
    except Exception as e:
        log_message(f"Error creating directory {path}: {e}", "ERROR")

def set_random_seed(seed):
    """
    Sets the random seed for reproducibility.

    Args:
        seed (int): The random seed value.

    Returns:
        None
    """
    try:
        random.seed(seed)
        np.random.seed(seed)
        log_message(f"Random seed set to {seed}", "INFO")
    except Exception as e:
        log_message(f"Error setting random seed: {e}", "ERROR")

def calculate_metrics(y_true, y_pred):
    """
    Calculates and logs common evaluation metrics for classification.

    Args:
        y_true (list): True labels.
        y_pred (list): Predicted labels.

    Returns:
        dict: Dictionary containing accuracy, precision, recall, and F1-score.
    """
    try:
        metrics = {
            "accuracy": accuracy_score(y_true, y_pred),
            "precision": precision_score(y_true, y_pred, average="weighted"),
            "recall": recall_score(y_true, y_pred, average="weighted"),
            "f1_score": f1_score(y_true, y_pred, average="weighted")
        }
        log_message(f"Evaluation metrics calculated: {metrics}", "INFO")
        return metrics
    except Exception as e:
        log_message(f"Error calculating metrics: {e}", "ERROR")
        return {}

def load_csv(file_path):
    """
    Loads a CSV file into a Pandas DataFrame.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded DataFrame.
    """
    try:
        data = pd.read_csv(file_path)
        log_message(f"CSV file loaded successfully: {file_path}", "INFO")
        return data
    except Exception as e:
        log_message(f"Error loading CSV file {file_path}: {e}", "ERROR")
        return pd.DataFrame()
