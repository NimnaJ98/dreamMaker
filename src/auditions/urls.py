from django.urls import path
from .views import createAuditions_view, AuditionDeleteView, AuditionUpdateView, participate_unparticipate_auditions, star_unstar_auditions

app_name = 'auditions'

urlpatterns = [
    path('',createAuditions_view, name='main-audition-view'),
    path('starred/',star_unstar_auditions, name='star-audition-view'),
    path('partcipate/',participate_unparticipate_auditions, name='participate-audition-view'),    
    path('<pk>/delete/', AuditionDeleteView.as_view(), name='audition-delete'),
    path('<pk>/update/', AuditionUpdateView.as_view(), name='audition-update'),
]