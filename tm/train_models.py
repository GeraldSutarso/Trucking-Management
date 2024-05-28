import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.preprocessing.image import ImageDataGenerator

def load_images_from_folder(folder, label):
    images = []
    labels = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename), cv2.IMREAD_GRAYSCALE)
        if img is not None:
            img = cv2.resize(img, (64, 64))
            images.append(img)
            labels.append(label)
    return images, labels

def prepare_data():
    drowsiness_normal_images, drowsiness_normal_labels = load_images_from_folder('dataset/drowsiness/normal', 0)
    tired_images, tired_labels = load_images_from_folder('dataset/drowsiness/tired', 1)
    sickness_normal_images, sickness_normal_labels = load_images_from_folder('dataset/sickness/normal', 2)
    sicks_images, sicks_labels = load_images_from_folder('dataset/sickness/sicks', 3)
    
    X = drowsiness_normal_images + tired_images + sickness_normal_images + sicks_images
    y = drowsiness_normal_labels + tired_labels + sickness_normal_labels + sicks_labels

    X = np.array(X).reshape(-1, 64, 64, 1)
    y = to_categorical(np.array(y), num_classes=4)

    return train_test_split(X, y, test_size=0.2, random_state=42)

def create_model():
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 1)),
        MaxPooling2D((2, 2)),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Flatten(),
        Dense(128, activation='relu'),
        Dropout(0.5),
        Dense(4, activation='softmax')
    ])
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

def train_models():
    X_train, X_test, y_train, y_test = prepare_data()

    datagen = ImageDataGenerator(
        rotation_range=10,
        zoom_range=0.1,
        width_shift_range=0.1,
        height_shift_range=0.1
    )
    datagen.fit(X_train)

    model = create_model()
    model.fit(datagen.flow(X_train, y_train, batch_size=32), epochs=10, validation_data=(X_test, y_test))

    loss, accuracy = model.evaluate(X_test, y_test)
    print(f'Accuracy: {accuracy}')

    model.save('trained_model/face_model.h5')

if __name__ == "__main__":
    train_models()
