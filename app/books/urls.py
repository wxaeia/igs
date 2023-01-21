from django.urls import path
from .views import (BooksViewSet)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', BooksViewSet, basename='books')

urlpatterns = [
    # path('countries-activities/', CountryActivityList.as_view(), name='activity'),
    # path('trainings/', CountryTraining.as_view(), name='training'),
]
urlpatterns += router.urls
