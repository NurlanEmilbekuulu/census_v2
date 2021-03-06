from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from census.api.serializers import EmployeeSerializer
from census.filters import EmployeeFilter
from census.models import Employee


class EmployeeViewSet(ModelViewSet):
    serializer_class = EmployeeSerializer
    filterset_class = EmployeeFilter

    def get_queryset(self):
        user = self.request.user
        print(user.get_username())
        queryset = Employee.objects.none()
        if self.request.user.is_authenticated:
            print("Hello World")
            queryset = Employee.objects.filter(territory__district=self.request.user.profile.district)
            if self.request.user.is_superuser:
                queryset = Employee.objects.all()
        return queryset

    @action(detail=True, methods=['get'])
    def generate_qr_code(self, request, pk=None):
        employee = self.get_object()
        if not employee.qr_code:
            employee.generate_qr_code()
            employee.save()
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)


class BadgePrintConfirmView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request):
        user = request.user
        return Response("Hello World")
