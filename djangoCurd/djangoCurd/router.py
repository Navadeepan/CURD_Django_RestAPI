from curdapi.viewsets import EmployeeViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('employee', EmployeeViewset)

# localhost:p/api/employee/
# GET, POST, PUT, DELETE
# list , retrieve
