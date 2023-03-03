import pandas as pd
from pymongo import mongo_client
import os
import sys
from Insurance_Premium.exception import InsuranceException
from Insurance_Premium.config import mongo_client
from Insurance_Premium.logger import logging


def get_collection_as_dataframe(database_name: str, collection_name: str)->pd.DataFrame:
    try:
        logging.info(f"Reading data from database:{database_name} and collection:{collection_name}")
        df = pd.DataFrame(mongo_client[database_name][collection_name].find())
        logging.info(f"Find columns: {df.columns}")
        if "_id" in df.columns:
            logging.info("Dropping Columns: _id")
            df = df.drop("_id", axis=1)
        logging.info(f'Rows and columns in df:{df.shape}')
        return df

    except Exception as e:
        raise InsuranceException(e, sys)






