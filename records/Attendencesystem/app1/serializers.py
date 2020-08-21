from rest_framework import serializers
from .models.members import Members
from .models .activity_periods import Activity_periods


class mySerializer(serializers.ModelSerializer):

    class Meta:
        model = Members
        fields= '__all__'


class mytimeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Activity_periods
        fields='__all__'