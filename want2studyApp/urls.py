from django.urls import path
from .views import StudylistView, DetailView, ChangeFinishView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', StudylistView.as_view(), name='studylist'),
    path('list/', StudylistView.as_view(), name='studylist'),
    path('detail/<int:pk>', DetailView.as_view(), name='detail'),
    path('changeFinish/<int:pk>', ChangeFinishView.as_view(), name='changefinish'),
] 
