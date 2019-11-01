import rpyc
from paramiko import SSHClient, AutoAddPolicy
from scp import SCPClient

conn = rpyc.classic.connect('ev3dev')
ev3_motor = conn.modules['ev3dev2.motor']
ev3_sensor = conn.modules['ev3dev2.sensor.lego']
ev3_os = conn.modules['os']
ev3_time = conn.modules['time']
ev3_sys = conn.modules['sys']
ev3_display = conn.modules['ev3dev2.display']
cv2 = conn.modules['cv2']

webcam = cv2.VideoCapture(0)

lcd = ev3_display.Display()

def createSSHClient(server, port, user, password) :
    client = SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(AutoAddPolicy())
    client.connect(server, port, user, password)
    return client

def get_picture() :
    ssh = createSSHClient("ev3dev", "22", "robot", "maker")
    scp = SCPClient(ssh.get_transport())

    scp.get("/home/robot/vscode-hello-python-master/billede/billede.png", "C:/Users/danny/PycharmProjects/P5/Ev3/pictures")
    scp.close()
    print("picture saved")


def initialize_motors() :
    m1 = ev3_motor.LargeMotor('outA')
    m2 = ev3_motor.LargeMotor('outB')
    return m1, m2

def take_picture() :
    for x in range(4):
        check = webcam.grab()

    check, frame = webcam.read()
    cv2.imwrite("/home/robot/vscode-hello-python-master/billede/billede" + ".png", frame)
    print("Picture taken")
    get_picture()

def run_motors(m1, m2) :
    m1.on(-30)
    m2.on(-30)

def stop_motors(m1, m2) :
    m1.on(0)
    m2.on(0)

def main() :
    print('Ev3 imports done')
    print("cv2 version: " + cv2.__version__)

    take_picture()

if __name__ == '__main__':
    main()