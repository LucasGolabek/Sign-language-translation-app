from django.shortcuts import render
import os

from .forms import ImageForm, VideoForm

from .file_processing.predict import predict, predict_video


def index_view(request):
    context = {}
    return render(request, 'pages/index.html', context)


def photo_view(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            saved = form.save()

            form = ImageForm()

            try:
                result = predict([os.path.abspath(str(saved.image))])[0]
            except RuntimeError:
                result = 'Error :('

            context = {'form': form,
                       'file_sent': True,
                       'result': result}
            return render(request, 'pages/from_photo.html', context)
    else:
        form = ImageForm()
    return render(request, 'pages/from_photo.html', {'form': form})


def video_view(request):
    if request.method == "POST":
        form = VideoForm(request.POST, request.FILES)

        if form.is_valid():
            saved = form.save()

            form = VideoForm()

            try:
                result = predict_video(os.path.abspath(str(saved.video)))
            except RuntimeError:
                result = "Error :("
            context = {'form': form,
                       'file_sent': True,
                       'result': result}
            return render(request, 'pages/from_video.html', context)
    else:
        form = VideoForm()
    return render(request, 'pages/from_video.html', {'form': form})


def info_view(request):
    context = {}
    return render(request, 'pages/info.html', context)


def register_view(request):
    context = {}
    return render(request, 'pages/register.html', context)


def login_view(request):
    context = {}
    return render(request, 'pages/login.html', context)
