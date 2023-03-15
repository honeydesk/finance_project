# Before executing this file, ensure that there are folders in 'saved_models'

# Testing whether batch_prediction is working or not
# a file is created in 'prediction' folder

import os
from Insurance.pipeline.batch_prediction import start_batch_prediction

file_path= os.getcwd() + "/insurance.csv"
print(__name__)

if __name__=="__main__":
    try:
        #output_file = start_training_pipeline()
        output_file = start_batch_prediction(input_file_path=file_path)
        print(output_file)
    except Exception as e:
        print(e)
