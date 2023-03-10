from Insurance_Premium.logger import logging
from Insurance_Premium.exception import InsuranceException
import os
import sys
from Insurance_Premium.utils import get_collection_as_dataframe
from Insurance_Premium.entity.config_entity import DataIngestionConfig
from Insurance_Premium.entity import config_entity
from Insurance_Premium.components.data_ingestion import DataIngestion


# def test_logger_and_exception():
#     try:
#         logging.info("Starting the test_logger_and_exception")
#         result = 3/0
#         print(result)
#         logging.info("Ending point of the test_logger_and_exception")
#
#     except Exception as e:
#         logging.debug(str(e))
#         raise InsuranceException(e, sys)


if __name__ == "__main__":
    try:
        # test_logger_and_exception()
        # get_collection_as_dataframe(database_name="INSURANCE",
        #                             collection_name="INSURANCE_PROJECT")
        training_pipeline_config = config_entity.TrainingPipelineConfig()
        data_ingestion_config = config_entity.DataIngestionConfig(training_pipeline_config=training_pipeline_config)
        print(data_ingestion_config.to_dict())

        data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
    except Exception as e:
        print(e)
