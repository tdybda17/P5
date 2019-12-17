# Waste sorting with image recognition

This report sets out to solve a classification problem of sorting waste with image classification. 
The report is focused on using machine learning to make a waste sorting machine. With a self produced 
data set it was possible to train a convolutional neural network with a overall accuracy of 
88.45 %, with data the model have never seen before.

To read about the hardware setup the report is needed. To run the program, read the guide below.

## How to install the project

### 1. Checkout the project
The project can be downloaded from github with this link

    $ git clone https://github.com/tdybda17/P5.git
    
### 2. Install requirements
From `requirements.txt` download and install all requirements or with pip

    $ pip install -r requirements.txt
    
    
## How to test the trained model

### 1. Download the trained model
The trained model is named `cnn.h5` and can be downloaded from

    Indsæt-link
    
Place the `cnn.h5` file inside the python directory called `models`
    
### 2. Testing the model
If you were to get predictions on your own pictures with the model, place them into the `models/test_images` 
folder and then run the following command

    $ python models/cnn/cnn_predict_test.py
    

