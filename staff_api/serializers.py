from rest_framework.serializers import ModelSerializer
from staff_api.models import Staff


class PublicListSerializer(ModelSerializer):
    """
    Basic Details for Public API Listing.
    """

    class Meta:
        model = Staff
        fields = ["name",
                  "mobile",
                  "email_id",
                  "address_line_1",
                  "address_line_2",
                  "city",
                  "pincode",
                  "state",
                  ]
        read_only_fields = ("__all__",)
