from rest_framework import serializers

from clock.models import Clock

# Dates and times follow the ISO 8601: https://www.iso.org/iso-8601-date-and-time-format.html


class CreateClockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clock
        fields = ['check_in', 'check_out']
        extra_kwargs = {'check_in': {'required': True},
                        'check_out': {'required': True}}

    def validate(self, data):
        check_in = data.get('check_in')
        check_out = data.get('check_out')

        if check_out <= check_in:
            raise serializers.ValidationError(
                'check_out field must be a date more recent than check_in field')
        return data


class ReadClockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clock
        fields = ['id', 'created_at', 'created_by', 'updated_at',
                  'updated_by', 'check_in', 'check_out']
