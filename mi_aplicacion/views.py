import os
from django.conf import settings
from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from django.http import JsonResponse
from .forms import UploadImageForm
from .utils import predict_image
from PIL import Image
import django
import platform
import tensorflow as tf
import cv2
import subprocess
import pkg_resources

def system_info(request):
    django_version = django.get_version()
    tensorflow_version = tf.__version__
    opencv_version = cv2.__version__
    system_info = {
        'System': platform.system(),
        'Node Name': platform.node(),
        'Release': platform.release(),
        'Version': platform.version(),
        'Machine': platform.machine(),
        'Processor': platform.processor(),
        'Architecture': platform.architecture(),
        'Python Version': platform.python_version(),
    }
    installed_packages = {d.project_name: d.version for d in pkg_resources.working_set}
    if platform.system() == "Linux":
        ubuntu_version = subprocess.check_output(['lsb_release', '-a']).decode('utf-8')
    else:
        ubuntu_version = "Not available on this OS"

    context = {
        'django_version': django_version,
        'tensorflow_version': tensorflow_version,
        'opencv_version': opencv_version,
        'system_info': system_info,
        'installed_packages': installed_packages,
        'ubuntu_version': ubuntu_version,
    }

    return JsonResponse(context)

def home(request):
    return redirect('upload_image')

def upload_image(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            img_path = default_storage.save(image.name, image)
            full_img_path = os.path.join(settings.MEDIA_ROOT, img_path)
            max_size = (800, 800)
            img = Image.open(full_img_path)
            img.thumbnail(max_size)
            img.save(full_img_path)
            is_person = predict_image(full_img_path)
            result = "The image is of a person." if is_person else "The image is not of a person."
            return render(request, 'mi_aplicacion/result.html', {'result': result, 'image_url': default_storage.url(img_path)})
    else:
        form = UploadImageForm()
    return render(request, 'mi_aplicacion/upload.html', {'form': form})
