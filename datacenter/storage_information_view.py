from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone
import pytz


def storage_information_view(request):
    visits = Visit.objects.all()
    unfinished_visits = visits.filter(leaved_at=None)
    serialized_visits = []
    for unfinished_visit in unfinished_visits:
        serialized_visits.append(
          {
            'who_entered': unfinished_visit.passcard,
            'entered_at': timezone.localtime(
                                      unfinished_visit.entered_at,
                                      pytz.timezone('Europe/Moscow')
                          ),
            'duration': Visit.format_duration(
                unfinished_visit.get_duration()
            ),
            }
        )
    context = {
        'serialized_visits': serialized_visits,
    }
    return render(request, 'storage_information.html', context)
