import rpyc
from paramiko import SSHClient, AutoAddPolicy
from scp import SCPClient
import os
import time
import random

#imports for Ev3
conn = rpyc.classic.connect('ev3dev')
ev3_motor = conn.modules['ev3dev2.motor']
ev3_sensor = conn.modules['ev3dev2.sensor.lego']
ev3_os = conn.modules['os']
ev3_time = conn.modules['time']
ev3_sys = conn.modules['sys']
ev3_display = conn.modules['ev3dev2.display']
ev3_fonts = conn.modules['ev3dev2.fonts']
cv2 = conn.modules['cv2']

print('Imports done')


#initializations for Ev3
webcam = cv2.VideoCapture(0)
webcam.set(3, 300)
webcam.set(4, 300)


display = ev3_display.Display()

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


#Tager et billede og gemmer det på Ev3'en derefter bliver det flyttet over til computeren
def take_picture(scp) :
    for x in range(4):
        check = webcam.grab()

    check, frame = webcam.read()
    cv2.imwrite("/home/robot/vscode-hello-python-master/billede/billede" + ".png", frame)
    print("Picture taken")
    get_picture("billede.png", os.path.abspath("pictures"), scp)
    print("picture saved")

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
    display.text_pixels(text, 0, 0, True, 'black', font=ev3_fonts.load('helvB24'))
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

def move_one_step(targetposition, currentposition, engine):

    if targetposition == currentposition:
        return currentposition

    elif targetposition > currentposition:
        engine.on_for_rotations(speed=30, rotations=0.45)
        currentposition = currentposition + 1
        return move_one_step(targetposition, currentposition, engine)

    elif targetposition < currentposition:
        engine.on_for_rotations(speed=-30, rotations=0.45)
        currentposition = currentposition - 1
        return move_one_step(targetposition, currentposition, engine)



def main() :
    print("cv2 version: " + cv2.__version__)
    scp = setup_ev3_ssh()

    belt_motor_one, belt_motor_two = initialize_belt_motors()
    arm_motor = initialize_arm_motor()
    #inf, start_value = initialize_inf()
    ts = initialize_ts()

    run_belt_motors(belt_motor_one, belt_motor_two, 0)
    current_position = 2
    print('Ready')
    while True :
        if ts.is_pressed :
            take_picture(scp)
            random_number = random.randint(1, 2)
            write_to_screen(str(random_number))
            current_position = move_one_step(random_number, current_position, arm_motor)
            ts.wait_for_released()



    #scp.close()


if __name__ == '__main__':
    main()
