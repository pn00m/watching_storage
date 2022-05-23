from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def passcard_info_view(request, passcode):
    visits = Visit.objects.all()
    serialized_visits = []
    passcard = Passcard.objects.get(passcode=passcode)
    selected_visits = visits.filter(passcard=passcard)
    for visit in selected_visits:
        duration = visit.get_duration()
        is_strange = Visit.is_visit_long(duration)
        serialized_visits.append(
            {'entered_at': visit.entered_at,
                'duration': duration,
                'is_strange': is_strange}
        )
    context = {
        'passcard': passcard,
        'this_passcard_visits': serialized_visits
    }
    return render(request, 'passcard_info.html', context)
