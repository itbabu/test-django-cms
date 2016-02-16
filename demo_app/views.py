from django.views.generic import ListView

from demo_app.models import Season


class SeasonListView(ListView):
    context_object_name = "season_list"
    template_name = 'base.html'

    def get_queryset(self):
        return Season.objects.all()
