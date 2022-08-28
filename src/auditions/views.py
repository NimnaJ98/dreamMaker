from email import message
from django.shortcuts import render
from .models import Audition, Participant, Star
from profiles.models import Profile
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView
from .forms import AuditionForm
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


@login_required
def createAuditions_view(request):
    qs = Audition.objects.all()
    profile = Profile.objects.get(user=request.user)
    audition_added = False

    # audition_form
    a_form = AuditionForm(request.POST or None, request.FILES or None)
    profile = Profile.objects.get(user=request.user)

    if a_form.is_valid():
        instance = a_form.save(commit=False)
        instance.director = profile
        instance.save()
        audition_added = True
        a_form = AuditionForm()

    context = {
        'qs': qs,
        'profile': profile,
        'a_form': a_form,
        'audition_added': audition_added
    }

    return render(request, 'auditions/audition.html', context)


@login_required
def participate_unparticipate_auditions(request):
    user = request.user
    if request.method == 'POST':
        audition_id = request.POST.get('audition_id')
        aud_obj = Audition.objects.get(id=audition_id)
        profile = Profile.objects.get(user=user)

        if profile in aud_obj.participants.all():
            aud_obj.participants.remove(profile)
        else:
            aud_obj.participants.add(profile)

        participant, created = Participant.objects.get_or_create(
            user=profile, audition_id=audition_id)

        if not created:
            if participant.value == 'Interested':
                participant.value = 'Not'
            else:
                participant.value = 'Interested'
        else:
            participant.value = 'Interested'

            aud_obj.save()
            participant.save()

        data = {
            'value': participant.value,
            'participants': aud_obj.participants.all().count()
        }
        return JsonResponse(data, safe=False)

    return redirect('auditions:main-auditions-view')


@login_required
def star_unstar_auditions(request):
    user = request.user
    if request.method == 'POST':
        audition_id = request.POST.get('audition_id')
        aud_obj = Audition.objects.get(id=audition_id)
        profile = Profile.objects.get(user=user)

        if profile in aud_obj.starred.all():
            aud_obj.starred.remove(profile)
        else:
            aud_obj.starred.add(profile)

        star, created = Star.objects.get_or_create(
            user=profile, audition_id=audition_id)

        if not created:
            if star.value == 'Star':
                star.value = 'Unstar'
            else:
                star.value = 'Star'
        else:
            star.value = 'Star'

            aud_obj.save()
            star.save()

        data = {
            'value': star.value,
            'stars': aud_obj.starred.all().count()
        }
        return JsonResponse(data, safe=False)

    return redirect('auditions:main-auditions-view')


class AuditionDeleteView(LoginRequiredMixin, DeleteView):
    model = Audition
    template_name = 'auditions/confirm_del.html'
    success_url = reverse_lazy('auditions:main-audition-view')

    def get_object(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        obj = Audition.objects.get(pk=pk)
        if not obj.director.user == self.request.user:
            messages.warning(
                self.request, 'You need to be the director of the post in order to delete it.')
        return obj


class AuditionUpdateView(LoginRequiredMixin, UpdateView):
    form_class = AuditionForm
    model = Audition
    template_name = 'auditions/update.html'
    success_url = reverse_lazy('auditions:main-audition-view')

    def form_valid(self, form):
        profile = Profile.objects.get(user=self.request.user)
        if form.instance.director == profile:
            return super().form_valid(form)

        else:
            form.add_error(
                None, "You need to be the author of the post in order to update it.")
            return super().form_invalid(form)
