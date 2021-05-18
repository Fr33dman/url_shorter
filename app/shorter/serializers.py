from rest_framework import serializers
from .models import Url
from django.urls import reverse


class UrlSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    def get_url(self, obj):
        if obj.key:
            path = reverse('redirect', kwargs={'key': obj.key})
            request = self.context.get('request')
            if request:
                path = request.build_absolute_uri(path)
            return path

    class Meta:
        model = Url
        fields = ['redirect_url', 'url']


class CreateUrlSerializer(UrlSerializer):

    class Meta:
        model = Url
        fields = ['redirect_url', 'url']
