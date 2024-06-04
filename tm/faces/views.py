import base64
import cv2
import numpy as np
from django.shortcuts import render, redirect
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from keras.models import load_model
from .models import FacePhoto
from io import BytesIO
from PIL import Image
import os
from django.contrib.auth.decorators import login_required, user_passes_test
import dlib


#HEY USER, WHO ARE YOU??

def im_customer(user):
    # return hasattr(user, is_customer=1)
    return user.is_customer
def im_superman(user):
    # return hasattr(user, is_superuser=1)
    return user.is_superuser
def im_driver(user):
    # return hasattr(user, is_driver=1)
    return user.is_driver

def get_latest_model():
    model_dir = 'trained_model'
    models = [os.path.join(model_dir, f) for f in os.listdir(model_dir) if f.endswith('.h5')]
    latest_model_path = max(models, key=os.path.getctime)
    return load_model(latest_model_path)

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("trained_model/shape_predictor_68_face_landmarks.dat")
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def preprocess_image(img):
    gray = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        face = gray[y:y+h, x:x+w]
        face = cv2.resize(face, (224, 224)).astype('float32') / 255.0  # Resize to 224x224
        face = np.stack((face,) * 3, axis=-1)  # Convert to 3-channel image
        return face.reshape(1, 224, 224, 3), (x, y, w, h)
    return None, None

def draw_landmarks(image, landmarks, color=(0, 255, 0)):
    for (x, y) in landmarks:
        cv2.circle(image, (x, y), 3, color, -1)

def detect_eyes_and_mouth(image, face_rect):
    shape = predictor(image, face_rect)
    landmarks = [(p.x, p.y) for p in shape.parts()]
    
    eyes_landmarks = landmarks[36:48]  # Eyes landmarks
    mouth_landmarks = landmarks[48:68] # Mouth landmarks

    return eyes_landmarks + mouth_landmarks

@login_required(login_url = 'login')
@user_passes_test(im_driver, login_url='/login')
def checkup_face(request):
    if request.method == 'POST':
        if 'checkup' in request.POST:
            captured_image_data = request.POST['captured_image']
            format, imgstr = captured_image_data.split(';base64,')
            img_data = base64.b64decode(imgstr)
            img = Image.open(BytesIO(img_data))
            img.save('temp.png')

            # Load the latest model
            model = get_latest_model()
            
            # Preprocess the image
            img_cv2 = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
            face_image, face_rect = preprocess_image(img)
            if face_image is None:
                return render(request, 'checkup_face.html', {'error': 'No face detected'})

            # Predict
            result = np.argmax(model.predict(face_image), axis=-1)[0]
            labels = ['not tired', 'Drowsiness detection', 'not sick', 'Sickness detection']
            result_text = labels[result]

            # Draw landmarks on image
            detected_faces = detector(img_cv2, 1)
            for i, face in enumerate(detected_faces):
                landmarks = detect_eyes_and_mouth(img_cv2, face)
                draw_landmarks(img_cv2, landmarks)

            # Overlay text on image
            cv2.putText(img_cv2, result_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
            success, encoded_image = cv2.imencode('.png', img_cv2)
            if success:
                image_file = ContentFile(encoded_image.tobytes())
                file_name = default_storage.save('photos/annotated_image.png', image_file)
                uploaded_file_url = default_storage.url(file_name)

            # Save to database
            photo = FacePhoto()
            photo.image.save(file_name, image_file)
            photo.result = result_text
            photo.save()

            context = {
                'uploaded_file_url': uploaded_file_url,
                'result': result_text
            }

            return render(request, 'checkup_face.html', context)

        elif 'next' in request.POST:
            return redirect('upload_photo_face')

    return render(request, 'checkup_face.html')

@login_required(login_url = 'login')
@user_passes_test(im_driver, login_url='/login')
def upload_photo_face(request):
    if request.method == 'POST':
        if 'backup' in request.POST:
            return redirect('checkup_face')
        
        if request.FILES.get('face_image'):
            face_image = request.FILES['face_image']
            img = Image.open(face_image)
            img.save('uploaded_image.png')

            # Load the latest model
            model = get_latest_model()

            # Preprocess the image
            img_cv2 = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
            face_image, face_rect = preprocess_image(img)
            if face_image is None:
                return render(request, 'upload_photo_face.html', {'error': 'No face detected'})

            # Predict
            result = np.argmax(model.predict(face_image), axis=-1)[0]
            labels = ['not tired', 'Drowsiness detected', 'not sick', 'Sickness detected']
            result_text = labels[result]

            # Draw landmarks on image
            detected_faces = detector(img_cv2, 1)
            for i, face in enumerate(detected_faces):
                landmarks = detect_eyes_and_mouth(img_cv2, face)
                draw_landmarks(img_cv2, landmarks)

            # Save the annotated image
            success, encoded_image = cv2.imencode('.png', img_cv2)
            if success:
                image_file = ContentFile(encoded_image.tobytes())
                file_name = default_storage.save('photos/annotated_image.png', image_file)
                uploaded_file_url = default_storage.url(file_name)

            # Save to database
            photo = FacePhoto()
            photo.image.save(file_name, image_file)
            photo.result = result_text
            photo.save()

            context = {
                'uploaded_file_url': uploaded_file_url,
                'result': result_text
            }

            return render(request, 'upload_photo_face.html', context)

    return render(request, 'upload_photo_face.html')