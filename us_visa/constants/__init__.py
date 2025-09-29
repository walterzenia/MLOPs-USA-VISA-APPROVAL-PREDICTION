import os
from datetime import datet

DATABSE_NAME = 'US_VISA_DB'
COLLECTION_NAME = 'US_VISA_APP'

MONGO_DB_URL = 'export MONGODB_URI='mongodb+srv://usvisaproject:usavisaproject@cluster0.hawfanf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0''

PIPELINE_NAME: str = 'us_visa_pipeline'
ARTIFACT_DIR: str = 'artifact'

MODEL_FILE_NAME: str = 'model.pkl'

"""
Data Ingestion related constant start with DATA_INGESTION VARIBLE NAME
"""

DATA_INGESTION_COLLECTION_NAME: str = 'US_VISA_APP'
DATA_INGESTION_DIR_NAME: str = 'data_ingestion'
DATA_INGESTION_FEATURE_STORE_DIR: str = 'feature_store'
DATA_INGESTION_INGESTED_DIR: str = 'ingested'
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION: float = 0.2

