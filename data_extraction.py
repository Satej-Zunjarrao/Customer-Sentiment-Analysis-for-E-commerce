import pandas as pd
import sqlalchemy
import requests

# Database configuration details
DB_CONFIG = {
    "host": "your_database_host",
    "port": "your_database_port",
    "user": "your_username",
    "password": "your_password",
    "database": "your_database_name"
}

# API configuration details
API_URL = "https://example-api.com/reviews"
API_KEY = "your_api_key"

def extract_from_sql(query):
    """
    Extracts data from an SQL database using the provided query.
    Utilizes SQLAlchemy for database connection and querying.

    Args:
        query (str): SQL query to execute for data extraction.

    Returns:
        pd.DataFrame: Data extracted from the SQL database.
    """
    try:
        # Establish the database connection using SQLAlchemy
        engine = sqlalchemy.create_engine(
            f"mysql+pymysql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
        )
        # Execute the query and fetch the data into a DataFrame
        with engine.connect() as connection:
            data = pd.read_sql(query, connection)
        print("Successfully extracted data from the SQL database.")
        return data
    except Exception as e:
        print(f"Error during SQL data extraction: {e}")
        return None

def extract_from_api():
    """
    Fetches data from an API endpoint.
    Utilizes the Requests library to make GET requests and fetch data in JSON format.

    Returns:
        pd.DataFrame: Data extracted from the API.
    """
    try:
        # Configure headers for API authentication
        headers = {"Authorization": f"Bearer {API_KEY}"}
        response = requests.get(API_URL, headers=headers)
        # Validate the response and parse JSON data
        if response.status_code == 200:
            data = response.json()
            print("Successfully extracted data from the API.")
            return pd.DataFrame(data)  # Convert JSON response to a Pandas DataFrame
        else:
            print(f"API request failed with status code {response.status_code}: {response.text}")
            return None
    except Exception as e:
        print(f"Error during API data extraction: {e}")
        return None

def save_to_file(data, filename):
    """
    Saves a DataFrame to a CSV file.

    Args:
        data (pd.DataFrame): Data to save.
        filename (str): Path to the output file.

    Returns:
        None
    """
    try:
        # Save the DataFrame to a CSV file without the index
        data.to_csv(filename, index=False)
        print(f"Data successfully saved to {filename}.")
    except Exception as e:
        print(f"Error saving data to file: {e}")

if __name__ == "__main__":
    # Example SQL query to extract customer reviews
    sql_query = "SELECT * FROM customer_reviews"
    
    # Extract data from SQL and API
    sql_data = extract_from_sql(sql_query)
    api_data = extract_from_api()
    
    # Save extracted data to CSV files
    if sql_data is not None:
        save_to_file(sql_data, "customer_reviews_sql.csv")
    if api_data is not None:
        save_to_file(api_data, "customer_reviews_api.csv")
