from django.utils.crypto import get_random_string
from rest_framework import viewsets, status
from .serializers import UrlSerializer, CreateUrlSerializer
from .models import Url
from rest_framework.response import Response
from django.http.response import HttpResponseRedirect, HttpResponseNotFound


def redirect_to(request, key):
    url = Url.objects.filter(key=key).first()
    if not url:
        return HttpResponseNotFound()
    else:
        return HttpResponseRedirect(redirect_to=url.redirect_url)


class UrlViewSet(viewsets.ModelViewSet):
    queryset = Url.objects.all()
    serializer_class = UrlSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateUrlSerializer
        return UrlSerializer

    def create(self, request, *args, **kwargs):
        url = Url.objects.filter(redirect_url=request.data.get('redirect_url')).first()
        if url:
            serializer = self.get_serializer(url)
        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        unique = False
        while not unique:
            key = get_random_string(length=7)
            unique = not Url.objects.filter(key=key).exists()
        serializer.save(key=key)
