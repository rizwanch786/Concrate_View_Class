from rest_framework import serializers
from .models import Student
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError("Seats are Full")
        return value