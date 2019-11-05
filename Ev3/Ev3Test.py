import rpyc
from paramiko import SSHClient, AutoAddPolicy
from scp import SCPClient
import os

#imports
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

#initializations
webcam = cv2.VideoCapture(0)
display = ev3_display.Display()

print('initializations done')


def create_ssh_client(server, port, user, password) :
    client = SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(AutoAddPolicy())
    client.connect(server, port, user, password)
    return client


def get_picture() :
    ssh = create_ssh_client("ev3dev", "22", "robot", "maker")
    scp = SCPClient(ssh.get_transport())
    #scp.get("/home/robot/vscode-hello-python-master/billede/billede.png", "C:/Users/danny/PycharmProjects/P5/Ev3/pictures")
    scp.get("/home/robot/vscode-hello-python-master/billede/billede.png", os.path.abspath("pictures"))
    scp.close()
    print("picture saved")


def initialize_motors() :
    m1 = ev3_motor.LargeMotor('outA')
    m2 = ev3_motor.LargeMotor('outB')
    return m1, m2

def initialize_inf() :
    inf = ev3_sensor.InfraredSensor()
    return inf

def take_picture() :
    for x in range(4):
        check = webcam.grab()

    check, frame = webcam.read()
    cv2.imwrite("/home/robot/vscode-hello-python-master/billede/billede" + ".png", frame)
    print("Picture taken")
    get_picture()


def run_motors(m1, m2, speed) :
    m1.on(speed)
    m2.on(speed)


def stop_motors(m1, m2) :
    m1.on(0)
    m2.on(0)


def write_to_screen(text) :
    display.text_pixels(text, 120, 50, True, 'black', font=ev3_fonts.load('helvB24'))
    display.update()

def main() :
    print("cv2 version: " + cv2.__version__)

    #m1, m2 = initialize_motors()
    #inf = initialize_inf()

    # run_motors(m1, m2, 0)
    take_picture()

    #while True :
        #write_to_screen(str(inf.proximity))


if __name__ == '__main__':
    main()