
# coding=utf-8
"""
Copyright (c) 2021 - AriSan - FusionTI
"""

from django.views.generic import ListView
from apps.amcm.models import Evento
import operator
from django.db.models import Q
from __future__ import unicode_literals
from django.core.exceptions import PermissionDenied
from functools import reduce

class EventoListView(ListView):
    model = Evento
    template_name = "amcm/evento-list.html"
    # search_fields = ("empresaNombre",)
    query = None
    title_list = "Evento"

    """
       Display a Blog List page filtered by the search query.
    """
    #paginate_by = 10

    def get_queryset(self):
        user_id = self.request.user.id
        access_set = Evento.objects.filter(user_id=user_id)

        eventos_array = []
        for access in access_set:
            eventos_array.append(access.id)

        result = super(EventoListView, self).get_queryset()

        query = self.request.GET.get('q')
        if query:
            EventoListView.query = query
            query_list = query.split()
            result = result.filter(
                reduce(operator.and_,
                       (Q(nombre__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(temporada__icontains=q) for q in query_list)))

        else:
            EventoListView.query = ''

        if len(eventos_array) > 0:
            result = result.filter(reduce(operator.or_, (Q(pk=q) for q in eventos_array)))
        else:
            result = Evento.objects.none()

        return result

    def get_context_data(self, **kwargs):
        context = super(EventoListView, self).get_context_data(**kwargs)
        context['title_list'] = EventoListView.title_list
        context['query'] = EventoListView.query
        context['query_string'] = '&q=' + EventoListView.query
        context['has_query'] = (EventoListView.query is not None) and (EventoListView.query != "")
        return context

    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('erp.view_list_project'):
            raise PermissionDenied
        return super(EventoListView, self).dispatch(request, args, kwargs)