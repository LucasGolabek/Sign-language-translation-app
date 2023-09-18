from django import forms

from .models import ImageModel, VideoModel


class ImageForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ['image']

    def __init__(self, *args, **kwargs):
        super(ImageForm, self).__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update({'class': 'image-selector',
                                                  'name': 'image-selector',
                                                  'id': 'file',
                                                  'label': ''})


class VideoForm(forms.ModelForm):
    class Meta:
        model = VideoModel
        fields = ['video']

    def __init__(self, *args, **kwargs):
        super(VideoForm, self).__init__(*args, **kwargs)
        self.fields['video'].widget.attrs.update({'class': 'video-selector',
                                                  'name': 'video-selector',
                                                  'id': 'video-file',
                                                  'label': ''})