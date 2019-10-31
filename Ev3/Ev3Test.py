import rpyc

conn = rpyc.classic.connect('ev3dev')
ev3_motor = conn.modules['ev3dev2.motor']
ev3_sensor = conn.modules['ev3dev2.sensor.lego']
cv2 = conn.modules['cv2']
print('Ev3 imports done')

webcam = cv2.VideoCapture(0)
print(cv2.__version__)

def take_picture() :
    for x in range(4):
        check = webcam.grab()

    check, frame = webcam.read()
    cv2.imwrite("/home/robot/vscode-hello-python-master/billede/billede" + ".png", frame)

def initialize_and_run_motors() :
    m1 = ev3_motor.LargeMotor('outA')
    m2 = ev3_motor.LargeMotor('outB')

    m1.on(-30)
    m2.on(-30)





