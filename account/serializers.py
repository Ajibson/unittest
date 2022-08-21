from .models import User
from rest_framework import serializers

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=40, min_length=8, write_only=True)
    
    class Meta:
        model = User
        fields = ["email", "password"]

    def validate_password(self, value):
        if value.isalpha() or value.isdigit():
            raise serializers.ValidationError(
                "password should be a mixed of letters and numbers"
            )

        return value