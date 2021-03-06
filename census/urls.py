from django.urls import path

from census.views import EmployeeCreateView, EmployeeListView, EmployeeDetailView, EmployeeUpdateView, \
    AgreementDetailView, PrintConfirmView

urlpatterns = [
    path('', EmployeeCreateView.as_view()),
    path('employees/', EmployeeListView.as_view(), name='employees'),
    path('employee/<int:pk>/', EmployeeDetailView.as_view(), name='employee'),
    path('employee/<int:pk>/change/', EmployeeUpdateView.as_view(), name='update'),
    path('employee/<int:pk>/agreement/', AgreementDetailView.as_view(), name='agreement'),
    path('ajax/employee/<int:pk>/print-confirm/', PrintConfirmView.as_view(), name='badge-print-confirm')
]
