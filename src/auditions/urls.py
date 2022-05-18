from django.urls import path
from .views import createAuditions_view, AuditionDeleteView, AuditionUpdateView, star_unstar_auditions

app_name = 'auditions'

urlpatterns = [
    path('auditions/',createAuditions_view, name='create-audition-view'),
    path('starred/',star_unstar_auditions, name='star-audition-view'),
    path('<pk>/delete/', AuditionDeleteView.as_view(), name='audition-delete'),
    path('<pk>/update/', AuditionUpdateView.as_view(), name='audition-update'),
]