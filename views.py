# from rest_framework import viewsets
# from django_filters.rest_framework import DjangoFilterBackend
# from . import models, serializers, schemas


# class ObjectViewSet(viewsets.ModelViewSet):
#     queryset = models.Object.objects.all()
#     serializer_class = serializers.ObjectSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = '__all__'
#     schema = schemas.MetaDataSchema()


# class ImageViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = models.Image.objects.all()
#     serializer_class = serializers.ImageSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = '__all__'
#     schema = schemas.MetaDataSchema()

# class TagViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = models.Tag.objects.all()
#     serializer_class = serializers.TagSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = '__all__'
#     schema = schemas.MetaDataSchema()

# class MuseumViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = models.Museum.objects.all()
#     serializer_class = serializers.MuseumSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = '__all__'
#     schema = schemas.MetaDataSchema()

# class MaterialViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = models.Material.objects.all()
#     serializer_class = serializers.MaterialSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = '__all__'
#     schema = schemas.MetaDataSchema()

# class PersonViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = models.Person.objects.all()
#     serializer_class = serializers.PersonSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = '__all__'
#     schema = schemas.MetaDataSchema()