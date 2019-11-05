import rpyc
from paramiko import SSHClient, AutoAddPolicy
from scp import SCPClient
import os
import datetime

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


#Skal bruges til at hente billedet fra Ev3'en
def create_ssh_client(server, port, user, password) :
    client = SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(AutoAddPolicy())
    client.connect(server, port, user, password)
    return client


#Henter billedet fra Ev3'en via en ssh forbindelse og ligger filen ind i mappen pictures i PyCharm
def get_picture(picture_name, pc_path, i) :
    ssh = create_ssh_client("ev3dev", "22", "robot", "maker")
    scp = SCPClient(ssh.get_transport())
    #scp.get("/home/robot/vscode-hello-python-master/billede/billede.png", "C:/Users/danny/PycharmProjects/P5/Ev3/pictures")
    scp.get("/home/robot/vscode-hello-python-master/billede/" + picture_name, pc_path)
    scp.close()
    print(str(i) + "_______" + str(datetime.datetime.now().time()))


#Initializer og retunere de 2 motorer til båndet
def initialize_motors() :
    m1 = ev3_motor.LargeMotor('outA')
    m2 = ev3_motor.LargeMotor('outB')
    return m1, m2


#initializer den infarøde sensor og retunere den samt dens første læste værdi
def initialize_inf() :
    inf = ev3_sensor.InfraredSensor()
    start_value = inf.proximity
    return inf, start_value


#Tager et billede og gemmer det på Ev3'en derefter bliver det flyttet over til computeren
def take_picture() :
    for x in range(4):
        check = webcam.grab()

    check, frame = webcam.read()
    cv2.imwrite("/home/robot/vscode-hello-python-master/billede/billede" + ".png", frame)
    print("Picture taken")
    get_picture("billede.png", os.path.abspath("pictures"), 0)

def take_test_pictures(i) :
    for x in range(4):
        check = webcam.grab()

    check, frame = webcam.read()
    cv2.imwrite("/home/robot/vscode-hello-python-master/billede/billede" + str(i) + ".png", frame)
    print(str(i) + "_______" + str(datetime.datetime.now().time()))

    get_picture("billede" + str(i) + ".png", os.path.abspath("test_pictures"), i)
    write_to_screen("billede gemt")

def run_motors(m1, m2, speed) :
    m1.on(speed)
    m2.on(speed)


def stop_motors(m1, m2) :
    m1.on(0)
    m2.on(0)


#Opdaterer Ev3'ens skærm med den angivne tekst
def write_to_screen(text) :
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


def main() :
    print("cv2 version: " + cv2.__version__)

    m1, m2 = initialize_motors()
    inf, start_value = initialize_inf()

    run_motors(m1, m2, 0)
    #take_picture()

    i = 0
    while True :
        take_test_pictures(i)
        i += 1


if __name__ == '__main__':
    main()