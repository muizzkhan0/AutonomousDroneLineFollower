
import numpy as np
import tensorflow as tf
from matplotlib import pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Activation, Flatten, Dense
from tensorflow.keras.optimizers import Adam

# This line loads the data in batches of 32 and also does a variety of other useful functions on the data
data = tf.keras.utils.image_dataset_from_directory('Dataset');

# Iterator for accessing data
data_iterator = data.as_numpy_iterator()

class_labels = ["Move Left","Move Right","No Line","Straight","Turn Left","Turn Right"]

data = data.map(lambda x,y: (x/255, y))
scaled_iterator = data.as_numpy_iterator();

# Roughly 70% trianing, 20% validation and 10% testing splits
train_size = 45
val_size = 13
test_size = 6

train = data.take(train_size)
val = data.skip(train_size).take(val_size)
test = data.skip(train_size+val_size).take(test_size)

# initialize the number of epochs to train for, initial learning rate,and batch size
EPOCHS = 3
INIT_LR = 1e-3
BS = 32

# initialize the model
print("[INFO] compiling model...")
model = Sequential()

#first set of CONV=> RELU => POOL layers
model.add(Conv2D(20, (5, 5), padding="same", input_shape=(256,256,3))) #256x256 image, 3 for RGB
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

# second set of CONV => RELU => POOL layers
model.add(Conv2D(50, (5,5), padding="same"))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

# first (and only) set of FC => RELU layers
model.add(Flatten())
model.add(Dense(500))
model.add(Activation("relu"))

# softmax classifier
model.add(Dense(6)) #6 classes
model.add(Activation("softmax"))

opt = Adam(learning_rate=INIT_LR, decay=INIT_LR / EPOCHS)
model.compile(loss="sparse_categorical_crossentropy", optimizer=opt, metrics=["accuracy"])

model.summary()


# train the model
print("[INFO] training network...")
H = model.fit(train, batch_size=BS,
              validation_data=val,
              epochs=EPOCHS, verbose=1)

# Plot the training accuracy and loss
plt.figure()
plt.plot(H.history["accuracy"], label="train_acc")
plt.plot(H.history["val_accuracy"], label="val_acc")
plt.title("Training and Validation Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()
plt.show()

# Uncomment to save the model to the pc
#model.save("model.h5")

print("TRAINING COMPLETE------------")
#evaluating the model after training
test_loss, test_acc = model.evaluate(test)
print(test_acc)