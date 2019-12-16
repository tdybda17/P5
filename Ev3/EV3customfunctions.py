import numpy
import time
import numpy as np
import cv2
import rpyc

#setup rpyc conn
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

print('Imports done')

#Webcam initialization
webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
webcam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
webcam.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)

display = ev3_display.Display()
buttons = ev3_button.Button()
np.set_printoptions(suppress=True)

print('initializations done')

def predict_image(model, picture):
    test_image = cv2.resize(picture, (150, 150), interpolation=cv2.INTER_AREA)
    test_image = test_image / 255
    test_image = np.expand_dims(test_image, axis = 0)
    result = model.predict_proba(test_image)

    return result[0]


#Initializer og retunere de 2 motorer til båndet
def initialize_belt_motors():
    belt_motor_one = ev3_motor.LargeMotor('outA')
    belt_motor_two = ev3_motor.LargeMotor('outB')
    return belt_motor_one, belt_motor_two


def initialize_arm_motor():
    arm_motor = ev3_motor.MediumMotor('outC')
    return arm_motor


def initialize_ultra_sonic_sensors():
    input1 = ev3_sensor2.INPUT_1
    input2 = ev3_sensor2.INPUT_2
    us1 = ev3_sensor.UltrasonicSensor(input1)
    us2 = ev3_sensor.UltrasonicSensor(input2)
    return us1, us2


def take_picture():
    webcam.read()
    check, frame = webcam.read()

    return frame


def run_belt_motors(m1, m2, speed):
    m1.on(speed)
    m2.on(speed)


def stop_belt_motors(m1, m2):
    m1.on(0)
    m2.on(0)


#Opdaterer Ev3'ens skærm med den angivne tekst
def write_to_screen(text):
    display.clear()
    display.text_pixels(text, 0, 0, False, 'black', font=ev3_fonts.load('helvB24'))
    display.update()


#Checker hvis der er noget indenfor sensoren hvis der er bliver der retuneret true
def inf_check_for_object(inf, start_value):
    distance_buffer = 4
    distance_now = inf.proximity
    if distance_now < (start_value - distance_buffer) :
        write_to_screen('Der er et object ' + str(inf.proximity))
        return True
    else :
        write_to_screen('Der er ikke et object ' + str(inf.proximity))
        return False


def prediction_to_string(number):
    if number == 0 :
        return 'Batteri'
    if number == 1 :
        return 'Dåse'
    if number == 2 :
        return 'Glas'


def move_arm(targetposition, currentposition, engine):
    if currentposition != targetposition:
        rotation = abs(currentposition - targetposition) * 0.22

        if currentposition < targetposition:
            speed = 30
        else:
            speed = -30

        engine.on_for_rotations(speed=speed, rotations=rotation)

def get_higest_prediction_array_number(predictions):
    highest = max(predictions)

    for x in range(len(predictions)) :
        if predictions[x] == highest :
            return x

def ultrasonic_detects_object(us1, us2, us_buffer1, us_buffer2, buffer):
    disnow1 = us1.distance_centimeters
    disnow2 = us2.distance_centimeters
    if disnow1 > us_buffer1 + buffer or disnow1 < us_buffer1 - buffer or disnow2 > us_buffer2 + buffer or disnow2 < us_buffer2 - buffer :
        return True


def calibrate_us(us1, us2):
    us1buffer = 0
    us2buffer = 0
    # calibrate
    for i in range(5):
        us1buffer = us1.distance_centimeters
        us2buffer = us2.distance_centimeters

    print(us1buffer, us2buffer)

    return us1buffer, us2buffer


def take_multiple_pictures(number_of_pictures, time_between_pictures):
    pictures = []
    for _ in range(number_of_pictures) :
        frame = take_picture()
        pictures.append(frame)
        time.sleep(time_between_pictures)
    return pictures


def get_prediction_from_multiple_pictures(pictures, model):
    prediction_array = [0, 0, 0]
    for picture in pictures:
        cropped_picture = numpy.array(picture[120:960, :])
        predicted_image_array = predict_image(model, cropped_picture)
        prediction_array[0] += predicted_image_array[0]
        prediction_array[1] += predicted_image_array[1]
        prediction_array[2] += predicted_image_array[2]
    return prediction_array
