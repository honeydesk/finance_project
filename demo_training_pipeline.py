import os
from Insurance.pipeline.training_pipeline import start_training_pipeline

file_path= os.getcwd() + "/insurance.csv"
print(__name__)

if __name__=="__main__":
    try:
        output_file = start_training_pipeline()
        print(output_file)
    except Exception as e:
        print(e)