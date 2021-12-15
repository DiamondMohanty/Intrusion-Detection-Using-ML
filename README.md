# Intrusion-Detection-Using-ML
## MACHINE LEARNING APPROACH TO DETECT VULNERABILITIES USING WAF

***To run the training files follow the below steps:***
1. Go to google colab
2. Upload dataset from [Dataset](https://github.com/DiamondMohanty/Intrusion-Detection-Using-ML/tree/main/Datasets) into your Google Drive
3. Go to files and upload the notebook from [Training](https://github.com/DiamondMohanty/Intrusion-Detection-Using-ML/tree/main/Training)
4. Change the path under PATH_TO_DATASET variable
    ```python
    # Loading dataset of command injection
    PATH_TO_DATASET = '/content/gdrive/MyDrive/command-injection-merged.xlsx'
    ```
4. Go to Run tab and select Run All
5. Follow the above steps to run all the files

***To run the flask application server follow the below steps:***
1. Use the [__init__.py](https://github.com/DiamondMohanty/Intrusion-Detection-Using-ML/blob/main/waf_server/__init__.py) file to start the server using the below command
    ```unix
    python __init__.py
    ```
2. The configuration of WAF and application server can be changed using [config.py](https://github.com/DiamondMohanty/Intrusion-Detection-Using-ML/blob/main/waf_server/config.py)
