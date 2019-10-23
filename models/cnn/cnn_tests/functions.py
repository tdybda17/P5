from keras.layers import Convolution2D



def getinitconvlayer(filters, kernel, stride):
    return Convolution2D(filters, kernel, stride, input_shape = (200, 112, 3), activation='relu')

def getconvlayer(filters, kernel, stride):
    return Convolution2D(filters, kernel, stride, activation='relu')
