from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.core.exceptions import ObjectDoesNotExist

from clock import models
from clock.serializers import CreateClockSerializer, ReadClockSerializer
from users.permissions import IsEmployeePermission


class Clock(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsEmployeePermission]

    def get(self, request, *args, **kwargs):
        try:
            clocks = models.Clock.objects.filter(created_by=request.user)
            if not clocks.exists():
                raise ObjectDoesNotExist('No data found')
            serializer = ReadClockSerializer(clocks, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist as exc:
            return Response({'detail': str(exc)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as exc:
            return Response({'detail': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, *args, **kwargs):
        serializer = CreateClockSerializer(data=request.data)
        try:
            if serializer.is_valid(raise_exception=True):
                serializer.validated_data['created_by'] = request.user
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as exc:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
