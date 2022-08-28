from django.urls import path
from .views import (
    createAuditions_view, 
    AuditionDeleteView, 
    AuditionUpdateView, 
    star_unstar_auditions, 
    participation_requests_view,
)

app_name = 'auditions'

urlpatterns = [
    path('',createAuditions_view, name='main-audition-view'),
    path('starred/',star_unstar_auditions, name='star-audition-view'),
    path('my-participants/', participation_requests_view, name='my-participants-view'),
    path('<pk>/delete/', AuditionDeleteView.as_view(), name='audition-delete'),
    path('<pk>/update/', AuditionUpdateView.as_view(), name='audition-update'),

    # path('my-participants/accept/', accept_participants, name='accept-participants'),
    # path('my-participants/reject/', reject_participants, name='reject-participants'),
]