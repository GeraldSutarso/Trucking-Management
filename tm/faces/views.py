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

def checkup_face(request):
    if request.method == 'POST':
        if 'checkup' in request.POST:
            captured_image_data = request.POST['captured_image']
            format, imgstr = captured_image_data.split(';base64,')
            img_data = base64.b64decode(imgstr)
            img = Image.open(BytesIO(img_data))
            img.save('temp.png')

            # Load the trained model
            model = load_model('trained_model/face_model.h5')
            
            # Preprocess the image
            img_cv2 = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2GRAY)
            img_cv2 = cv2.resize(img_cv2, (64, 64)).reshape(1, 64, 64, 1)

            # Predict
            result = np.argmax(model.predict(img_cv2), axis=-1)[0]
            labels = ['Tired', 'Normal', 'Sicks', 'Normal']
            result = labels[result]

            # Overlay text on image
            img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
            cv2.putText(img, result, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
            success, encoded_image = cv2.imencode('.png', img)
            if success:
                image_file = ContentFile(encoded_image.tobytes())
                file_name = default_storage.save('photos/annotated_image.png', image_file)
                uploaded_file_url = default_storage.url(file_name)

            # Save to database
            photo = FacePhoto()
            photo.image.save(file_name, image_file)
            photo.result = result
            photo.save()

            context = {
                'uploaded_file_url': uploaded_file_url,
                'result': result
            }

            return render(request, 'checkup_face.html', context)

        elif 'next' in request.POST:
            return redirect('upload_photo_face')

    return render(request, 'checkup_face.html')

def upload_photo_face(request):
    if request.method == 'POST':
        if 'backup' in request.POST:
            return redirect('checkup_face')
        
        if request.FILES.get('face_image'):
            face_image = request.FILES['face_image']
            fs = FileSystemStorage()
            filename = fs.save(face_image.name, face_image)
            uploaded_file_url = fs.url(filename)

            # Load the trained model
            model = load_model('trained_models/face_model.h5')
            
            # Preprocess the image
            img = cv2.imread(fs.path(filename), cv2.IMREAD_GRAYSCALE)
            img = cv2.resize(img, (64, 64)).reshape(1, 64, 64, 1)

            # Predict
            result = np.argmax(model.predict(img), axis=-1)[0]
            labels = ['Tired', 'Normal', 'Sicks', 'Normal']
            result = labels[result]
            
            # Save to database
            photo = FacePhoto(image=face_image, result=result)
            photo.save()

            return render(request, 'upload_photo_face.html', {
                'uploaded_file_url': uploaded_file_url,
                'result': result
            })

    return render(request, 'upload_photo_face.html')
