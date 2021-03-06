from keras.models import load_model
from Ev3.functions import *


def main():
    model = load_model('../models/cnn.h5')

    # Initialize Ev3 motors and sensors
    us1, us2 = initialize_ultra_sonic_sensors()
    belt_motor_one, belt_motor_two = initialize_belt_motors()
    arm_motor = initialize_arm_motor()

    us_buffer1, us_buffer2 = calibrate_us(us1, us2)

    run_belt_motors(belt_motor_one, belt_motor_two, speed=-30)

    # Set the starting arm position
    current_arm_position = 1

    picture = take_picture()

    predict_image(model, picture)

    print('Ready')

    while True:
        if ultrasonic_detects_object(us1, us2, us_buffer1, us_buffer2, buffer=2) :
            pictures = take_pictures(number_of_pictures=5, time_between_pictures=0.1)
            predict_array = get_prediction_from_pictures(pictures, model)
            highest_prediction_number = get_higest_prediction_array_number(predict_array)
            move_arm(highest_prediction_number, current_arm_position , arm_motor)
            current_arm_position = highest_prediction_number


if __name__ == '__main__':
    main()