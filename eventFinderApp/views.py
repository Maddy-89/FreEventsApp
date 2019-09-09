from django.http import HttpResponse
from django.views import generic
from django.shortcuts import render
from .models import Event
from .forms import EventForm


class IndexView(generic.ListView):
    template_name = 'eventFinderApp/index.html'
    context_object_name = 'events_list'

    def get_queryset(self):
        '''Return the events.'''
        return Event.objects.all()

class NewEventView(generic.FormView):
    template_name = 'eventFinderApp/newEventForm.html'
    form_class = EventForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super().form_valid(form)

class EventView(generic.DetailView):
    model = Event
    template_name = 'eventFinderApp/event.html'

def account(request):
    return render(request, 'eventFinderApp/account.html')

#long hand method for form example
# def formPage(request):
#     form = EventForm()
#     if request.POST:
#         # if handling a submitted form
#         my_event = form(request)
#         if my_event.valid():
#             my_event.save()
#         form = EventForm(intance=my_event)
#     return render(request, 'eventFinderApp/newEventForm.html', {'form': form})