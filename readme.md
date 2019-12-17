# Waste sorting with image recognition
Link to GitHub: https://github.com/tdybda17/P5

This report sets out to solve a classification problem of sorting waste with image classification. 
The report is focused on using machine learning to make a waste sorting machine. With a self produced 
data set it was possible to train a convolutional neural network with a overall accuracy of 
88.45 %, with data the model have never seen before.

To read about the hardware setup the report is needed. To run the program, read the guide below.

## How to install the project

### Checkout the project
The project can be downloaded from github with this link

    $ git clone https://github.com/tdybda17/P5.git
    
### Install requirements
From `/requirements.txt` download and install all requirements or with pip

    $ pip install -r requirements.txt
    
    
### Download test sets
If you do not want to run the model with our test sets, skip this section

#### 1. Download the test sets
The test sets folder can be downloaded from this link

    https://www.paste.link.dk/

#### 2. Add it to the project
Place the downloaded `test_set_cropped` in the `/images` folder

## How to test the trained model

### Download the trained model
The trained model is named `cnn.h5` and can be downloaded from

    Indsæt-link
    
Place the `cnn.h5` file inside the python directory called `/models`

### Test model with test set
To run predictions on the test set `/images/test_set_cropped` simply run this command

    $ python models/cnn/cnn_predict_all_tests.py
    
### Test model with own images
If you were to get predictions on your own pictures with the model, place them into the `models/test_images` 
folder and then run the following command

    $ python models/cnn/cnn_predict_test.py
    
## How to install and run the EV3 program
### Mount the flash image
First, mount the flash image (can be downloaded from: INDSÆT LINK)
to a microSD card and insert it into the EV3

### Connection to EV3
With your EV3 connected to the internet 
(guide: https://www.ev3dev.org/docs/tutorials/connecting-to-the-internet-via-usb/), you can establish a 
connection with ssh with these credentials:

    Hostname: ev3dev
    Port: 22
    Username: robot
    Password: maker

### Run the server
Next, find and run `rpyc_server.sh`

    $ vscode-hello-python-master/rpyc_server.sh
    
Or find it directly on the EV3 display and run it


### Running the program
Wait for the server to start up and then run the following command

    $ python Ev3/run_machine.py
    
