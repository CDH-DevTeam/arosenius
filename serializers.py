# from rest_framework import serializers
# from rest_framework_gis.serializers import GeoFeatureModelSerializer
# from . import models

# class ObjectSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Object
#         fields = '__all__'
#         depth = 1


# class ImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Image
#         fields = '__all__'
#         depth = 1

# class TagSerializer(GeoFeatureModelSerializer):
#     class Meta:
#         model = models.Tag
#         fields = '__all__'

# class PersonSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Person
#         fields = '__all__'
#         depth = 1

# class MuseumSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Museum
#         fields = '__all__'
#         depth = 1

# class MaterialSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Material
#         fields = '__all__'
#         depth = 1