from django.urls import path
from django.urls import include
from . import views
from rest_framework_nested import routers

router=routers.DefaultRouter()
router.register('students',views.StudentView)
router.register('schools',views.SchoolView)

urlpatterns = [
   path('', include(router.urls))

]
