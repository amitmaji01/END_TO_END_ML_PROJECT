from mlProject.constants import *  # here i call all constant file path
from mlProject.utils.common import read_yaml, create_directories   # using utils i read that file and create directory
from mlProject.entity.config_entity import (DataIngestionConfig) # in this line i import DataIngestionConfig from entity 


#create a configure manager class where a read the config and params and schema file and create a directory
#this config manager give us all the configure  we need to build the end to end project
#05 update the configuration manager in src config

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config

