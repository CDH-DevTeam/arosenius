from rest_framework import serializers
from . import models

class ArtifactSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Artifact
        fields = '__all__'
        depth = 1
