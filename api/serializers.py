from rest_framework import serializers

from api.models import Course


class AllCourseSerializers(serializers.ModelSerializer):
    """Создание, Изменение и Вывод курсов"""

    class Meta:
        model = Course
        fields = '__all__'
