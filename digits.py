
import os
import cv2
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.python.keras.utils import np_utils
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense, Dropout, Flatten
from tensorflow.python.keras.layers import Conv2D, MaxPooling2D
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

#
"""
mnist = tf.keras.datasets.mnist
(X_train, y_train), (X_test, y_test) = mnist.load_data()


# normalizace
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255


# převedení na pole tributů
X_train = X_train.reshape(X_train.shape[0], 28, 28, 1)
X_test = X_test.reshape(X_test.shape[0], 28, 28, 1)


# převedení na one-hot encoding
n_classes = 10

y_train = np_utils.to_categorical(y_train, n_classes)
y_test = np_utils.to_categorical(y_test, n_classes)


# vytvoření modelu
model = Sequential()

model.add(Conv2D(32, kernel_size=(3, 3),
                 activation='relu',
                 input_shape=(28, 28, 1)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(n_classes, activation='softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])


# trénování
model.fit(X_train, y_train,
          batch_size=128,
          epochs=10,
          verbose=1,
          validation_data=(X_test, y_test))

model.save('handwritten.model')
"""
#

model = tf.keras.models.load_model('handwritten.model')


# výsledky pravděpodobnosti
"""y_pred = model.predict(X_test)#

y_test_class = np.argmax(y_test, axis=1)#
y_pred_class = np.argmax(y_pred, axis=1)#"""


# výpis výsledků
"""print("Accuracy score: ", accuracy_score(y_test_class, y_pred_class))#
print("Confusion matrix: \n", confusion_matrix(y_test_class, y_pred_class))#"""


# načtení a klasifikace obrázků
image_number = 1
index = 0
grid = []

while os.path.isfile(f"digits/digit{image_number}.png"):
    try:
        abs_path = os.path.abspath(f"digits/digit{image_number}.png")
        img = cv2.imread(abs_path)[:,:,0]
        img = np.invert(np.array([img]))
        img = img.reshape(1, 28, 28, 1)
        prediction = model.predict(img)
        predicted_value = np.argmax(prediction)
        grid.append(predicted_value)
        #print(f"Toto číslo je nejspíše {np.argmax(prediction)}")
        #plt.imshow(img[0], cmap=plt.cm.binary)#
        #plt.show()#
        
    except:
        print("ERROR!!!")
    
    finally:
        image_number += 1
    
#   vytvoření matrixu
 
sudoku = [[0 for _ in range(9)] for _ in range(9)]

for i in range(len(grid)):
    if i < 81:
        sudoku[i // 9][i % 9] = grid[i]
    
