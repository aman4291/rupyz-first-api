from rest_framework.serializers import ModelSerializer

from staff_api.models import Staff


class CreateStaffSerializer(ModelSerializer):

    class Meta:
        model = Staff
        fields = "__all__"


class ListStaffSerializer(ModelSerializer):

    class Meta:
        model = Staff
        fields = [
            "id",
            "name",
            "mobile",
            "email",
            "city",
            "created_at",
        ]


class DetailOrUpdateStaffSerializer(ModelSerializer):

    class Meta:
        model = Staff
        fields = "__all__"
        read_only_fields = ["id", ]
