import os
import sys
import json

from dotenv import load_dotenv
load_dotenv()

import certifi
import pandas as pd
import numpy as np
import pymongo

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

MONGO_DB_URL = os.getenv("MONGO_DB_URL")
ca = certifi.where()


class NetworkDataExtract:
    def __init__(self):
        try:
            if MONGO_DB_URL is None:
                raise Exception("MONGO_DB_URL not found in environment variables.")
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def csv_to_json_convertor(self, file_path):
        """
        Reads CSV and converts to JSON records list.
        """
        try:
            if not os.path.exists(file_path):
                raise Exception(f"CSV file not found at path: {file_path}")

            logging.info(f"Reading CSV file: {file_path}")
            data = pd.read_csv(file_path)

            if data.shape[0] == 0:
                raise Exception("CSV file loaded but contains **zero rows**.")

            data.reset_index(drop=True, inplace=True)
            records = list(json.loads(data.T.to_json()).values())

            logging.info(f"CSV converted to {len(records)} records.")
            return records

        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def insert_data_mongodb(self, records, database, collection):
        """
        Inserts JSON records into MongoDB.
        """
        try:
            logging.info("Connecting to MongoDB...")
            mongo_client = pymongo.MongoClient(MONGO_DB_URL, tlsCAFile=ca)

            db = mongo_client[database]
            col = db[collection]

            if len(records) == 0:
                raise Exception("Cannot insert: records list is empty.")

            result = col.insert_many(records)

            logging.info(f"Inserted {len(result.inserted_ids)} records into MongoDB.")
            return len(result.inserted_ids)

        except Exception as e:
            raise NetworkSecurityException(e, sys)


if __name__ == '__main__':
    try:
        # Update with correct file path
        FILE_PATH = r"E:\NetworkSecurity\Network_Data\phisingData.csv"

        DATABASE = "ANANTAI"
        COLLECTION = "NetworkData"

        logging.info("Starting data push script...")

        network_obj = NetworkDataExtract()

        # Convert CSV → JSON records
        records = network_obj.csv_to_json_convertor(file_path=FILE_PATH)
        print(f"Total Records Loaded: {len(records)}")

        # Insert into MongoDB
        count = network_obj.insert_data_mongodb(records, DATABASE, COLLECTION)
        print(f"Total Records Inserted into MongoDB: {count}")

    except Exception as e:
        raise NetworkSecurityException(e, sys)
