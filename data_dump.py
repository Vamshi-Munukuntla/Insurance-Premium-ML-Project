import pymongo
import pandas as pd
import json

client = pymongo.MongoClient("mongodb+srv://vamshi_munukuntla:cbl9Gap7zD2s4KJg@insurance-premium-ml-pr.btcg1vy"
                             ".mongodb.net/?retryWrites=true&w=majority")

DATA_FILE_PATH = r"D:\Insurance-Premium-ML-Project\insurance.csv"
DATABASE_NAME = "INSURANCE"
COLLECTION_NAME = "INSURANCE_PROJECT"

if __name__ == "__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and Columns: {df.shape}")

    df.reset_index(drop=True, inplace=True)

    # Transposing the data and convert it to json format and saving in a list.
    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)


