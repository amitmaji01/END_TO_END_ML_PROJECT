# END_TO_END_ML_PROJECT

"""

## 1st I have to create a enviroment 
--> conda create -n redwine python=3.8 -y


## 2nd It will activate 
-->conda activate redwine  

## 3rd i have to setup the file and folder for that I write a code and that code file name is template.py


## 4th  I have to install all te requirements 
-->pip install -r requirements.txt


## 5th I load the dataset from kaggle 

## 6th i create a .ipynb file in the research folder 
There I perform all type of EDA,FE,FS,MODEL TRAINING,MODEL EVALUATION

## 7th I create logger to the src constructor

## 8th I build the utils here I write that code which we use again and again


## 9th workflow for data ingestion means load the data from a outsource url or any database 
1. update config.yaml  #change in config.yaml file
2. update schema.yaml  #change in schema.yaml file
3. update params.yaml  #change in params.yaml file
4. update the entity   #change in entity/config_entity.py file
5. update the configuration manager in src config  #change in src\mlProject\config\configuration.py
6. update the components   #change in src\mlProject\components\data_ingestion.py
7. update the pipeline     #change in src\mlProject\pipeline\stage_01_data_ingestion.py file 
8. update the main.py      #change in main.py file
9. update the app.py

## 10th workflow for data validation means check wheather data is valid or not 
1. update config.yaml  #change in config.yaml file
2. update schema.yaml  
3. update params.yaml  
4. update the entity   #change in entity/config_entity.py file
5. update the configuration manager in src config  #change in src\mlProject\config\configuration.py 
6. update the components   #change in src\mlProject\components\data_validation.py
7. update the pipeline     #change in src\mlProject\pipeline\stage_02_data_validation.py file 
8. update the main.py      #change in main.py file
9. update the app.py


## 11th workflow for data transformation  means here we can build various method to do feature engineering means all preprocessing task 
1. update config.yaml  #change in config.yaml file
2. update schema.yaml  
3. update params.yaml  
4. update the entity   #change in entity/config_entity.py file
5. update the configuration manager in src config  #change in src\mlProject\config\configuration.py 
6. update the components   #change in src\mlProject\components\data_transformation.py
7. update the pipeline     #change in src\mlProject\pipeline\stage_03_data_transformation.py file 
8. update the main.py      #change in main.py file
9. update the app.py


## 12th workflow for model traning here we train various model then we pick the best one 
1. update config.yaml  #change in config.yaml file
2. update schema.yaml  
3. update params.yaml  
4. update the entity   #change in entity/config_entity.py file
5. update the configuration manager in src config  #change in src\mlProject\config\configuration.py 
6. update the components   #change in src\mlProject\components\model_traning.py
7. update the pipeline     #change in src\mlProject\pipeline\stage_04_model_trainer.py file 
8. update the main.py      #change in main.py file
9. update the app.py


## 13th workflow for model evaluation here we evaluate our model 
1. update config.yaml  #change in config.yaml file
2. update schema.yaml  
3. update params.yaml  
4. update the entity   #change in entity/config_entity.py file
5. update the configuration manager in src config  #change in src\mlProject\config\configuration.py 
6. update the components   #change in src\mlProject\components\model_evaluate.py
7. update the pipeline     #change in src\mlProject\pipeline\stage_05_model_evaluation.py file 
8. update the main.py      #change in main.py file
9. update the app.py



## 14th  i create a prediction pipline 
there i load the model and input the data and predict 


## 15th create user app 


"""