import pymongo # pip install pymongo
import pandas as pd
import json
import os

client = pymongo.MongoClient("mongodb+srv://mongodb:mongodb@cluster0.id3gb.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")


ROOT_DIR = os.getcwd()  #to get current working directory
DATA_FILE_PATH = os.path.join(ROOT_DIR,"insurance.csv")
DATABASE_NAME = "INSURANCE"
COLLECTION_NAME = "INSURANCE_PROJECT"


if __name__=="__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns: {df.shape}")

    df.reset_index(drop = True, inplace = True)
    
    # Transposing the data, since Mongodb takes data in format of JSON
    # So we will have the data in Key:Value form
    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])
    
    # Inserting in mongodb
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
