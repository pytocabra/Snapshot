from django.shortcuts import render
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView, 
    DeleteView
)
from django.contrib.auth.mixins import (
    LoginRequiredMixin, 
    UserPassesTestMixin
)
from .models import Snap


class SnapListView(ListView):
    model = Snap
    template_name = 'main/index.html'
    context_object_name = 'snapshots'
    ordering = ['-date_posted']


class SnapDetailView(DetailView):
    model = Snap
    template_name = 'main/snapshot_detail.html'
    context_object_name = 'snap'


class SnapCreateView(LoginRequiredMixin, CreateView):
    model = Snap
    fields = ['title', 'description', 'snap', 'tag', ]
    success_url = '/profile/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class SnapUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Snap
    fields = ['title', 'description', 'snap', 'tag', ]
    success_url = '/profile/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self) -> bool:
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class SnapDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Snap
    success_url = '/'

    def test_func(self) -> bool:
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def searchTag(request):
    if request.method == 'GET':
        search = request.GET['search'].split(' ')
        context = {
            'snapshots': Snap.objects.filter(tag__name__in=search)
        }
    return render(request, 'main/index.html', context)