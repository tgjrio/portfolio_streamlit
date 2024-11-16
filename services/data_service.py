import logging
from google.cloud import storage
import streamlit as st
import pandas as pd


# Configure logging to track important events in Redis and Pub/Sub interactions
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def upload_data():
    st.subheader("STEP 1: UPLOAD DATA")
    uploaded_file = st.file_uploader("Maximum [5 Rows | 5 Columns]", type=["csv", "json"])

    if uploaded_file:
        try:
            # Handle file input based on file extension
            if uploaded_file.name.endswith('.csv'):
                data = pd.read_csv(uploaded_file)
            elif uploaded_file.name.endswith('.json'):
                data = pd.read_json(uploaded_file)
            else:
                st.error("Unsupported file format. Please upload a CSV or JSON file.")
                return None  # Return None to indicate an issue

            # Check for number of columns and rows
            if data.shape[1] > 10 or data.shape[0] > 5:
                st.error("File exceeds the maximum allowed limit of 10 columns and 20 rows.")
                return None

            return data  # Return the DataFrame if everything is valid
        except Exception as e:
            st.error(f"An error occurred while processing the file: {e}")
            return None
    else:
        st.info("Please upload a CSV or JSON file to proceed.")
        return None


class GCSManager:
    """
    A class to manage uploads and downloads of files to and from Google Cloud Storage.
    This class provides methods to upload files to a specified bucket and retrieve files from the bucket.
    """

    def __init__(self, bucket_name: str):
        """
        Initialize the GCSManager with the necessary GCS configuration.
        Establish a connection to the GCS bucket.
        
        :param bucket_name: The name of the GCS bucket where files will be stored/retrieved.
        """
        self.bucket_name = bucket_name  # Store the bucket name as a string
        self.storage_client = storage.Client()
        self.bucket = self.storage_client.bucket(bucket_name)  # Bucket object

    def upload_to_gcs(self, destination_blob_name: str, file_path: str):
        """
        Upload a file to GCS.

        :param destination_blob_name: The name of the blob (file) in the GCS bucket.
        :param file_path: The local path to the file that needs to be uploaded.
        """
        blob = self.bucket.blob(destination_blob_name)
        logging.info("Preparing file upload into GCS..")
        try:
            blob.upload_from_filename(file_path)
            logging.info(f"File {file_path} uploaded to {destination_blob_name}.")
        except Exception as e:
            logging.error(f"Failed to upload file {file_path} to {destination_blob_name}: {e}")