from django.forms import Select
from django_filters import FilterSet, ModelChoiceFilter
from .models import Callboard, Reply

def my_ads_requests(request):
    if request is None:
        return Callboard.objects.none()

    return Callboard.objects.filter(author = request.user)

class ReplyFilter(FilterSet):
    callb = ModelChoiceFilter(
        queryset=my_callb_requests,
        empty_label='Все объявления',
        label='',
        widget=Select(attrs = {'class': 'form-control'}),
    )

    class Meta:
        model = Reply
        fields = [
            'callb',
        ]