from django.http import Http404
from rest_framework import generics, status
from rest_framework.response import Response

from api import serializers
from api.models import Course


class CreateCourseView(generics.CreateAPIView):
    """Создание курса"""

    serializer_class = serializers.AllCourseSerializers


class DeleteCourseByIdView(generics.DestroyAPIView):
    """Удаление курса по идентификации"""

    queryset = Course.objects.all()


class DeleteAllCoursesView(generics.DestroyAPIView):
    """Удаление всех курсов"""

    def get_object(self):
        try:
            return Course.objects.all()
        except Course.DoesNotExist:
            raise Http404

    def delete(self, request, format=None, **kwargs):
        """Метод удаления всех курсов"""

        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class UpdateCourseByIdView(generics.UpdateAPIView):
    """Обновление курса по идентификации"""

    serializer_class = serializers.AllCourseSerializers
    queryset = Course.objects.all()


class FindAllCoursesView(generics.ListAPIView):
    """Вывод всех курсов"""

    serializer_class = serializers.AllCourseSerializers
    queryset = Course.objects.all()


class FindCourseByIdView(generics.RetrieveAPIView):
    """Поиск курса по идентификации"""

    serializer_class = serializers.AllCourseSerializers
    queryset = Course.objects.all()
