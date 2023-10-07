from rest_framework import serializers
from .models import EmailSettings, DomainEmailSettings

class EmailSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailSettings
        fields = '__all__'

class DomainEmailSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DomainEmailSettings
        fields = '__all__'
