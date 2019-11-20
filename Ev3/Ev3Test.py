import numpy
import rpyc
from paramiko import SSHClient, AutoAddPolicy
from scp import SCPClient
import os
import time
import random
from keras.models import load_model
import numpy as np
from keras.preprocessing import image
import cv2


#setup rpyc conn
from image_compressor.image_comp import compress_image
conn = rpyc.classic.connect('ev3dev')

#imports for Ev3
ev3_motor = conn.modules['ev3dev2.motor']
ev3_sensor = conn.modules['ev3dev2.sensor.lego']
ev3_sensor2 = conn.modules['ev3dev2.sensor']
ev3_os = conn.modules['os']
ev3_time = conn.modules['time']
ev3_sys = conn.modules['sys']
ev3_display = conn.modules['ev3dev2.display']
ev3_fonts = conn.modules['ev3dev2.fonts']
ev3_button = conn.modules['ev3dev2.button']
#cv2 = conn.modules['cv2']


print('Imports done')


#Webcam initialization
webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
webcam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
webcam.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)

display = ev3_display.Display()
buttons = ev3_button.Button()

print('initializations done')


#Skal bruges til at hente billedet fra Ev3'en
def create_ssh_client(server, port, user, password) :
    client = SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(AutoAddPolicy())
    client.connect(server, port, user, password)
    return client

def setup_ev3_ssh() :
    ssh = create_ssh_client("ev3dev", "22", "robot", "maker")
    scp = SCPClient(ssh.get_transport())
    return scp


#Henter billedet fra Ev3'en via en ssh forbindelse og ligger filen ind i mappen pictures i PyCharm
def get_picture(picture_name, pc_path, scp) :
    scp.get("/home/robot/vscode-hello-python-master/billede/" + picture_name, pc_path)


def predict_image(model, picture) :
    resized = cv2.resize(picture, (190, 190), interpolation=cv2.INTER_AREA)
    test_image = resized
    #test_image = image.img_to_array(test_image)
    test_image = test_image / 255
    test_image = np.expand_dims(test_image, axis = 0)
    result = model.predict_proba(test_image)

    return result[0]


#Initializer og retunere de 2 motorer til båndet
def initialize_belt_motors() :
    belt_motor_one = ev3_motor.LargeMotor('outA')
    belt_motor_two = ev3_motor.LargeMotor('outB')
    return belt_motor_one, belt_motor_two

def initialize_arm_motor() :
    arm_motor = ev3_motor.MediumMotor('outC')
    return arm_motor

#initializer den infarøde sensor og retunere den samt dens første læste værdi
def initialize_inf() :
    inf = ev3_sensor.InfraredSensor()
    start_value = inf.proximity
    return inf, start_value

def initialize_ts() :
    tf = ev3_sensor.TouchSensor()
    return tf

def initialize_ultra_sonic_sensors() :
    input1 = ev3_sensor2.INPUT_1
    input2 = ev3_sensor2.INPUT_2
    us1 = ev3_sensor.UltrasonicSensor(input1)
    us2 = ev3_sensor.UltrasonicSensor(input2)
    return us1, us2


#Tager et billede og gemmer det på Ev3'en derefter bliver det flyttet over til computeren
def take_picture() :

    check, frame = webcam.read()
    cv2.imwrite(os.path.abspath("pictures/billede") + ".jpg", frame)
    #print("Picture taken")
    #get_picture("billede.png", os.path.abspath("pictures"), scp)
    #print("picture saved")

def take_test_pictures(i, scp) :
    for x in range(4):
        check = webcam.grab()

    check, frame = webcam.read()
    cv2.imwrite("/home/robot/vscode-hello-python-master/billede/billede" + ".png", frame)
    #Gemt på Ev3
    print(str(int(round(time.time() * 1000))), end=' ')

    get_picture("billede" + ".png", os.path.abspath("pictures"), scp)
    # billede gemt på computer
    print(str(int(round(time.time() * 1000))), end=' ')



def run_belt_motors(m1, m2, speed) :
    m1.on(speed)
    m2.on(speed)


def stop_belt_motors(m1, m2) :
    m1.on(0)
    m2.on(0)


#Opdaterer Ev3'ens skærm med den angivne tekst
def write_to_screen(text) :
    display.clear()
    display.text_pixels(text, 0, 0, False, 'black', font=ev3_fonts.load('helvB24'))
    display.update()


#Checker hvis der er noget indenfor sensoren hvis der er bliver der retuneret true
def inf_check_for_object(inf, start_value) :
    distance_buffer = 4
    distance_now = inf.proximity
    if distance_now < (start_value - distance_buffer) :
        write_to_screen('Der er et object ' + str(inf.proximity))
        return True
    else :
        write_to_screen('Der er ikke et object ' + str(inf.proximity))
        return False

def prediction_to_string(number) :
    if number == 0 :
        return 'Batteri'
    if number == 1 :
        return 'Dåse'
    if number == 2 :
        return 'Glas'

def move_one_step(targetposition, currentposition, engine):

    if targetposition == currentposition:
        return currentposition

    elif targetposition > currentposition:
        engine.on_for_rotations(speed=30, rotations=0.220)
        currentposition = currentposition + 1
        return move_one_step(targetposition, currentposition, engine)

    elif targetposition < currentposition:
        engine.on_for_rotations(speed=-30, rotations=0.220)
        currentposition = currentposition - 1
        return move_one_step(targetposition, currentposition, engine)

def get_higest_prediction_array_number(predictions) :
    highest = max(predictions)

    for x in range(len(predictions)) :
        if predictions[x] == highest :
            return x

def us_detection(us1, us2, us_buffer1, us_buffer2, buffer) :
    disnow1 = us1.distance_centimeters
    disnow2 = us2.distance_centimeters
    if disnow1 > us_buffer1 + buffer or disnow1 < us_buffer1 - buffer or disnow2 > us_buffer2 + buffer or disnow2 < us_buffer2 - buffer :
        return True

def calibrate_us(us1, us2) :
    us1buffer = 0
    us2buffer = 0
    # calibrate
    for i in range(5):
        us1buffer = us1.distance_centimeters
        us2buffer = us2.distance_centimeters

    print(us1buffer, us2buffer)

    return us1buffer, us2buffer

def main() :

    #scp = setup_ev3_ssh()

    print('Loading model........')
    model = load_model('miModel/test.h5')
    print('Model loaded')



    us1, us2 = initialize_ultra_sonic_sensors()
    belt_motor_one, belt_motor_two = initialize_belt_motors()
    arm_motor = initialize_arm_motor()

    us_buffer1, us_buffer2 = calibrate_us(us1, us2)

    #ts = initialize_ts()
    #inf, start_value = initialize_inf()

    current_belt_motor_speed = 0
    run_belt_motors(belt_motor_one, belt_motor_two, current_belt_motor_speed)
    current_position = 2

    np.set_printoptions(suppress=True)

    take_picture()


    print(us1.other_sensor_present, us2.other_sensor_present)
    print('Ready')
    while True :
        if us_detection(us1, us2, us_buffer1, us_buffer2, 2) :
            print(us1.distance_centimeters)
            print(us2.distance_centimeters)
            print('Buffer = ' + str(us_buffer1))
            print('Buffer = ' + str(us_buffer2))
            time.sleep(0.5)
            #check = webcam.grab()
            #check = webcam.grab()
            webcam.read()
            check, frame = webcam.read()
            cv2.imwrite(os.path.abspath("pictures/billede") + ".jpg", frame)
            picture = numpy.array(frame[120:960, :])
            #take_picture()
            #compress_image(os.path.abspath('pictures/billede.jpg'), os.path.abspath('pictures/billede.jpg'), size=[200, 112])
            #picture = image.load_img('pictures/billede.jpg', target_size=(190, 190))
            predict_array = predict_image(model, picture)
            write_to_screen(prediction_to_string(get_higest_prediction_array_number(predict_array)) + '\n\n' + str(predict_array[0]) + '\n' + str(predict_array[1]) + '\n' + str(predict_array[2]))
            current_position = move_one_step((get_higest_prediction_array_number(predict_array) + 1), current_position, arm_motor)
            print(predict_array)
            time.sleep(6)
            current_position = move_one_step(2, current_position, arm_motor)

        if buttons.any():
            if current_belt_motor_speed == -30 :
                run_belt_motors(belt_motor_one, belt_motor_two, 0)
                current_belt_motor_speed = 0
            else :
                run_belt_motors(belt_motor_one, belt_motor_two, -30)
                current_belt_motor_speed = -30

    #scp.close()


if __name__ == '__main__':
    main()
