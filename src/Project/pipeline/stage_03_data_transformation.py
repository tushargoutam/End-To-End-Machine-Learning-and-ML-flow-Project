from src.Project.config.configuration import ConfigurationManager
from src.Project.components.data_transformation import DataTransformation
from src.Project import logger
from pathlib import Path

STAGE_NAME = "Data Transformation Stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass 

    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"),"r") as f:
                status = f.read().split(" ")[-1]

            if status == "True":
                config =  ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation =  DataTransformation(config= data_transformation_config)
                data_transformation.train_test_spliting()
            else:
                raise Exception("Your Data schema is not valid")
            
        except Exception as e:
            print(e)




if __name__=='__main__':
    try:
        logger.info(f">>>>>>>>> Stage {STAGE_NAME} started <<<<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>> Stage {STAGE_NAME} completed <<<<<<<<")

    except Exception as e:
        logger.exception(e)
        raise e
    

        