
from rest_framework.response import Response
from rest_framework.views import APIView

from staff_api.models import Staff
from staff_api.serializers import (CreateStaffSerializer, DetailOrUpdateStaffSerializer,
                                   ListStaffSerializer)

# Create your views here.


class QueryHelper:

    @staticmethod
    def get_list_of_staff():
        return Staff.objects.all()

    @staticmethod
    def get_obj_of_staff(id):
        try:
            return Staff.objects.get(id=id)
        except Staff.DoesNotExist:
            return None


class ListAndCreateStaffAPIView(APIView):

    def get(self, request):
        # request_data = request.query_params.copy()

        staff_objs_list = QueryHelper.get_list_of_staff()
        serializer = ListStaffSerializer(staff_objs_list, many=True)
        return Response(serializer.data)

    def post(self, request):
        request_data = request.data.copy()

        serializer = CreateStaffSerializer(data=request_data)
        if not serializer.is_valid():
            return Response({
                "error_message": "please fix the errors",
                "error_info": serializer.errors
            })

        serializer.save()
        return Response(serializer.data)


class DetailAndUpdateAPIView(APIView):

    def get(self, request, pk):
        # request_data = request.query_params.copy()

        staff_obj = QueryHelper.get_obj_of_staff(pk)
        if not staff_obj:
            return Response({
                "error_message": "No staff exists with given id",
                "error_info": []
            })

        serializer = DetailOrUpdateStaffSerializer(staff_obj)

        return Response(serializer.data)

    def post(self, request, pk):
        request_data = request.data.copy()

        staff_obj = QueryHelper.get_obj_of_staff(pk)
        if not staff_obj:
            return Response({
                "error_message": "No staff exists with given id",
                "error_info": []
            })

        serializer = DetailOrUpdateStaffSerializer(staff_obj, data=request_data, partial=True)

        if not serializer.is_valid():
            return Response({
                "error_message": "please fix the errors",
                "error_info": serializer.errors
            })

        serializer.save()
        return Response(serializer.data)


class DeleteStaffAPIView(APIView):

    def post(self, request, pk):
        # request_data = request.data.copy()

        staff_obj = QueryHelper.get_obj_of_staff(pk)
        if not staff_obj:
            return Response({
                "error_message": "No staff exists with given id",
                "error_info": []
            })

        deleted_data = DetailOrUpdateStaffSerializer(staff_obj).data
        staff_obj.delete()

        return Response(deleted_data)
