import os
import urllib.request as request
import zipfile
from src.Project import logger
from pathlib import Path
from src.Project.utils.common import get_size
from src.Project.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_url,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}")

        else:
            logger.info(f"File Already Exists of size : {get_size(Path(self.config.local_data_file))}")

    
    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)