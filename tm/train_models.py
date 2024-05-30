import numpy as np
import os
import cv2
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Dropout, GlobalAveragePooling2D
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
from sklearn.model_selection import train_test_split
from sklearn.utils import class_weight
from collections import Counter

def load_images_from_folder(folder, label):
    images = []
    labels = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename), cv2.IMREAD_GRAYSCALE)
        if img is not None:
            img = cv2.resize(img, (224, 224))  # Increase resolution for better feature extraction
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)  # Convert grayscale to RGB
            images.append(img)
            labels.append(label)
    return images, labels

def prepare_data():
    not_tired_images, not_tired_labels = load_images_from_folder('dataset/drowsiness/not tired', 0)
    drowsiness_images, drowsiness_labels = load_images_from_folder('dataset/drowsiness/drowsy', 1)
    not_sicks_images, not_sicks_labels = load_images_from_folder('dataset/sickness/not sicks', 2)
    sickness_images, sickness_labels = load_images_from_folder('dataset/sickness/sickness detection', 3)
    
    X = not_tired_images + drowsiness_images + not_sicks_images + sickness_images
    y = not_tired_labels + drowsiness_labels + not_sicks_labels + sickness_labels

    print("Distribution of data:", Counter(y))

    X = np.array(X).astype('float32') / 255.0  # Normalization
    y = np.array(y)

    return train_test_split(X, y, test_size=0.2, random_state=42), y

def create_model():
    from tensorflow.keras.applications import EfficientNetB0
    base_model = EfficientNetB0(input_shape=(224, 224, 3), include_top=False, weights='imagenet')
    base_model.trainable = False  # Freeze the base model
    model = Sequential([
        base_model,
        GlobalAveragePooling2D(),
        Dense(256, activation='relu', kernel_regularizer='l2'),
        Dropout(0.5),
        Dense(4, activation='softmax')
    ])
    model.compile(optimizer=Adam(learning_rate=1e-4), loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model

def train_model():
    (X_train, X_test, y_train, y_test), y = prepare_data()

    datagen = ImageDataGenerator(
        rotation_range=40,
        zoom_range=0.2,
        width_shift_range=0.2,
        height_shift_range=0.2,
        horizontal_flip=True,
        brightness_range=[0.5, 1.5],
        shear_range=0.2,
        fill_mode='nearest'
    )
    datagen.fit(X_train)

    model = create_model()

    # Calculate class weights to handle class imbalance
    class_weights = class_weight.compute_class_weight('balanced', classes=np.unique(y), y=y_train)
    class_weights_dict = dict(enumerate(class_weights))

    checkpoint = ModelCheckpoint('trained_model/face_model_best.keras', monitor='val_loss', save_best_only=True, mode='min')
    early_stopping = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)

    model.fit(datagen.flow(X_train, y_train, batch_size=32), 
              epochs=100, 
              validation_data=(X_test, y_test),
              class_weight=class_weights_dict,
              callbacks=[checkpoint, early_stopping])

    loss, accuracy = model.evaluate(X_test, y_test)
    print(f'Akurasi: {accuracy}')

    model.save('trained_model/face_model.h5')

if __name__ == "__main__":
    train_model()
