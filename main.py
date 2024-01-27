from textSummarization.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarization.logging import logger

STAGE_NAME = "Data Ingestion"
try:
    logger.info(f">>>>>>>> Stage: {STAGE_NAME} started <<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>>> {STAGE_NAME} stage co   mpleted <<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e