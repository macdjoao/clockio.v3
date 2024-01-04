from rest_framework import serializers

from clock.models import Clock

# Dates and times follow the ISO 8601: https://www.iso.org/iso-8601-date-and-time-format.html


class CreateClockSerializer(serializers.ModelSerializer):
    check_in = serializers.DateTimeField(required=True)
    check_out = serializers.DateTimeField(required=True)

    class Meta:
        model = Clock
        fields = ['check_in', 'check_out']

    def validate(self, data):
        check_in = data['check_in']
        check_out = data['check_out']

        if check_out <= check_in:
            raise serializers.ValidationError(
                {'validation_error': 'check_out field must be a date more recent than check_in field'})

        return data


class ReadClockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clock
        fields = ['id', 'created_at', 'created_by', 'updated_at',
                  'updated_by', 'check_in', 'check_out']


class UpdateClockSerializer(serializers.ModelSerializer):
    check_in = serializers.DateTimeField(required=False)
    check_out = serializers.DateTimeField(required=False)

    class Meta:
        model = Clock
        fields = ['check_in', 'check_out']

    def validate(self, data):
        check_in = data.get('check_in')
        check_out = data.get('check_out')
        instance = self.instance

        if not check_in and not check_out:
            raise serializers.ValidationError(
                {'validation_error': 'at least check_in or check_out must be received'})

        if check_in and check_out and check_out <= check_in:
            raise serializers.ValidationError(
                {'validation_error': 'check_out field must be a date more recent than check_in field'})

        if not check_out and check_in and check_in < instance.check_out:
            raise serializers.ValidationError(
                {'check_in': 'check_in field must be a date more recent than the current check_out field'})

        if not check_in and check_out and check_out < instance.check_in:
            raise serializers.ValidationError(
                {'check_out': 'check_out field must be a date older than the current check_in field'})

        return data
