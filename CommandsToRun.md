#Library install and save


##Before work:
####pip install -r requirements.txt


##After work:
####pip freeze > requirements.txt


##Lightsail Ubuntu

####How to connect
Download the private-key file from P5 (Messenger)
    
    LightsailDefaultKey-eu-central-1.pem

Open terminal and enter

    ssh -i <path-to-private-key> ubuntu@18.197.97.59
    
You should now be connected to `ubuntu@ip-172-26-11-241:~$`


####Running tests
Run these commands

    cd ~/desktop/models/
    source venv/bin/activate
    cd research/
    export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim
    
Then run the tests by

    python object_detection/builders/model_builder_test.py
    
And you should get this

    ----------------------------------------------------------------
    Ran 16 tests in 0.088s 
    OK
    


