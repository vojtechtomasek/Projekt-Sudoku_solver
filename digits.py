"""import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf


mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)


model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten(input_shape=(28, 28)))
model.add(tf.keras.layers.Dense(128, activation='relu'))
model.add(tf.keras.layers.Dense(128, activation='relu'))
model.add(tf.keras.layers.Dense(10, activation='softmax'))


model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(x_train, y_train, epochs=3)

model.save('handwritten.model')


model = tf.keras.models.load_model('handwritten.model')

loss, accuracy = model.evaluate(x_test, y_test) 

print(loss)
print(accuracy)


image_number = 1
while os.path.isfile(f"digits/digit{image_number}.png"):
    try:
        abs_path = os.path.abspath(f"digits/digit{image_number}.png")
        img = cv2.imread(abs_path)[:,:,0]
        img = np.invert(np.array([img]))
        prediction = model.predict(img)
        print(f"Toto cislo je nejspise {np.argmax(prediction)}")
        plt.imshow(img[0], cmap=plt.cm.binary)
        plt.show()
        
    except:
        print("Error")
        
    finally:
        image_number += 1"""
        
        
        

"""
import os
import cv2
import tensorflow as tf
import matplotlib.pyplot as plt
import pickle
from tensorflow.python.keras.utils import np_utils
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense, Activation
import numpy as np
from sklearn import metrics
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

mnist = tf.keras.datasets.mnist
(X_train, y_train), (X_test, y_test) = mnist.load_data()

#print("Rozmery vstupnich trenovacich dat X_train: {}".format(X_train.shape))
#print("Rozmery vystupnich trenovacich dat y_train: {}".format(y_train.shape))
#print("Rozmery vstupnich testovacich dat X_test: {}".format(X_test.shape))
#print("Rozmery vystupnich trenovacich dat y_test: {}".format(y_test.shape))

#   normalizace
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255

#   převedení na pole tributů
X_train_flat = X_train.reshape(60000, 784)
X_test_flat = X_test.reshape(10000, 784)
#print("Rozmery X_train: {}".format(X_train_flat.shape))
#print("Rozmery X_test: {}".format(X_test_flat.shape))


#   převést na one-hot encoding:
n_classes = 10

#print(y_train[49])

y_train = np_utils.to_categorical(y_train, n_classes)
y_test = np_utils.to_categorical(y_test, n_classes)

#print(y_train[49])


model = Sequential()

model.add(Dense(64, input_shape=(784, )))
model.add(Activation('relu'))
model.add(Dense(10))
model.add(Activation('softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

# trénování 
model.fit(X_train_flat, y_train,
          batch_size = 128, epochs = 10, verbose=1,
          validation_data=(X_test_flat, y_test))


#   výsledky pravděpodobnosti
y_pred = model.predict(X_test_flat)

#print(y_pred.shape)

y_test_class = np.argmax(y_test, axis=1)
y_pred_class = np.argmax(y_pred, axis=1)
#print(y_pred_class.shape)


image_number = 1
while os.path.isfile(f"digits/digit{image_number}.png"):
    try:
        abs_path = os.path.abspath(f"digits/digit{image_number}.png")
        img = cv2.imread(abs_path)[:,:,0]
        img = np.invert(np.array([img]))
        img_flat = img.reshape(1, 784)
        prediction = model.predict(img_flat)
        print(f"Toto cislo je nejspise {np.argmax(prediction)}")
        plt.imshow(img[0], cmap=plt.cm.binary)
        plt.show()
        
    except Exception as e:
        print(f"Error: {e}")
        
    finally:
        image_number += 1

"""
#   implementace vyhodnocovacích funkcí
"""print ("Accuracy testovaci mnoziny: {:.4f}".format(accuracy_score(y_test_class, y_pred_class)))
print ()
print(metrics.classification_report(y_test_class, y_pred_class, digits=4))"""


#   ktere tridy u klasifikace do vice trid jsou zamenovany nejcasteji 
#print(confusion_matrix(y_test_class, y_pred_class))

# některé z chybných klasifikovaných příkladů
"""incorrect_indices = np.nonzero(y_pred_class != y_test_class)[0]
print(incorrect_indices)

i = incorrect_indices[5]

plt.imshow(X_test[i], cmap='gray')
plt.title("Predikovano: {}, Spravna trida: {}".format(y_pred_class[i], y_test_class[i]))
plt.show()"""

    
    

import os
import cv2
import tensorflow as tf
import matplotlib.pyplot as plt
import pickle
from tensorflow.python.keras.utils import np_utils
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense, Dropout, Flatten
from tensorflow.python.keras.layers import Conv2D, MaxPooling2D
import numpy as np
from sklearn import metrics
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix


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


# převést na one-hot encoding
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


model = tf.keras.models.load_model('handwritten.model')


# výsledky pravděpodobnosti
y_pred = model.predict(X_test)

y_test_class = np.argmax(y_test, axis=1)
y_pred_class = np.argmax(y_pred, axis=1)


# výpis výsledků
print("Accuracy score: ", accuracy_score(y_test_class, y_pred_class))
print("Confusion matrix: \n", confusion_matrix(y_test_class, y_pred_class))


# načtení a klasifikace obrázků
image_number = 1

while os.path.isfile(f"digits/digit{image_number}.png"):
    try:
        abs_path = os.path.abspath(f"digits/digit{image_number}.png")
        img = cv2.imread(abs_path)[:,:,0]
        img = np.invert(np.array([img]))
        img = img.reshape(1, 28, 28, 1)
        prediction = model.predict(img)
        print(f"Toto číslo je nejspíše {np.argmax(prediction)}")
        plt.imshow(img[0], cmap=plt.cm.binary)
        plt.show()
        
    except:
        print("ERROR!!!")
    
    finally:
        image_number += 1