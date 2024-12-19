from django.contrib.auth import login, logout
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
import cv2
from .forms import RegisterForm

# Create your views here.
from .models import ImageProcessing
from deepface import DeepFace


def compare_faces(user, database_image_path):
    result = DeepFace.verify(user, database_image_path)
    return result["verified"]


def image_processing(request):
    if request.method == 'POST':
        pk = request.POST.get('pk')
        print(pk)

        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            print("unable to access the camera")
            exit()

        ret, frame = cap.read()

        if ret:

            instance = ImageProcessing.objects.get(unique_code=pk)
            location = f'.{instance.image.url}'

            image_path = "user_image.jpg"
            cv2.imwrite(image_path, frame)
            if compare_faces(image_path, location) == True:
                return redirect('/')
            else:
                return HttpResponse("access denied")

        cap.release()
        cv2.destroyAllWindows()
    else:
        return render(request, 'auth_app/index.html')


def Register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            ImageProcessing.objects.create(unique_code=data['username'], image=data['image'])

        return render(request, 'home_app/index.html')


    else:
        return render(request, 'auth_app/register.html', {'form': form})


def log_out(request):
    logout(request)
    return render(request, 'auth_app/index.html')
