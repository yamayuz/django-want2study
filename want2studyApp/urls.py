from django.urls import path
from .views import StudylistView, DetailView, ChangeFinishView, DeleteView, UpdateView, SignupView, SigninView, LogoutView, FavoriteView, FavoriteListView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', StudylistView.as_view(), name='studylist'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('signin/', SigninView.as_view(), name='signin'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('list/', StudylistView.as_view(), name='studylist'),
    path('detail/<int:pk>', DetailView.as_view(), name='detail'),
    path('changeFinish/<int:pk>', ChangeFinishView.as_view(), name='changefinish'),
    path('delete/<int:pk>', DeleteView.as_view(), name='delete'),
    path('update/<int:pk>', UpdateView.as_view(), name='update'),
    path('favorite/<int:pk>', FavoriteView.as_view(), name='favorite'),
    path('favorite/<int:pk>', FavoriteView.as_view(), name='favorite'),
    path('favorite_list/', FavoriteListView.as_view(), name='favorite_list'),
] 
