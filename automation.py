import schedule
import time
from sentiment_pipeline import sentiment_analysis_pipeline

def scheduled_pipeline_run():
    """
    Triggers the sentiment analysis pipeline to process new data periodically.

    Returns:
        None
    """
    try:
        # SQL query to fetch recent reviews
        sql_query = """
        SELECT * FROM customer_reviews 
        WHERE review_date >= CURDATE() - INTERVAL 7 DAY
        """
        # Run the pipeline
        sentiment_analysis_pipeline(sql_query)
        print("Scheduled pipeline run completed successfully.")
    except Exception as e:
        print(f"Error during scheduled pipeline run: {e}")

def start_scheduler():
    """
    Starts the scheduler to run the pipeline at specified intervals.

    Returns:
        None
    """
    try:
        # Schedule the pipeline to run daily at a specific time
        schedule.every().day.at("02:00").do(scheduled_pipeline_run)
        print("Scheduler initialized. Waiting for the next scheduled run...")
        
        # Keep the script running to execute scheduled tasks
        while True:
            schedule.run_pending()
            time.sleep(1)
    except Exception as e:
        print(f"Error initializing the scheduler: {e}")

if __name__ == "__main__":
    # Start the automation scheduler
    start_scheduler()
