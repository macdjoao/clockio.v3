from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.core.exceptions import ObjectDoesNotExist

from clock import models
from clock.serializers import CreateClockSerializer, ReadClockSerializer, UpdateClockSerializer
from users.permissions import IsEmployeePermission


class Clock(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsEmployeePermission]

    def get(self, request, *args, **kwargs):
        try:
            id = self.kwargs.get('id')
            if id:
                clock = models.Clock.objects.get(id=id)
                serializer = ReadClockSerializer(clock)
            else:
                clocks = models.Clock.objects.filter(created_by=request.user)
                if not clocks.exists():
                    raise ObjectDoesNotExist('No data found')
                serializer = ReadClockSerializer(clocks, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except models.Clock.DoesNotExist as exc:
            return Response({'detail': str(exc)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as exc:
            print(exc)
            return Response({'detail': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, *args, **kwargs):
        serializer = CreateClockSerializer(data=request.data)
        try:
            if serializer.is_valid():
                serializer.validated_data['created_by'] = request.user
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as exc:
            print(exc)
            return Response({'detail': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request, id, *args, **kwargs):
        try:
            clock = models.Clock.objects.get(id=id)
            if request.user != clock.created_by:
                return Response({'detail': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)
            serializer = UpdateClockSerializer(
                clock, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save(updated_by=request.user)
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except models.Clock.DoesNotExist as exc:
            return Response({'detail': str(exc)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as exc:
            print(exc)
            return Response({'detail': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
