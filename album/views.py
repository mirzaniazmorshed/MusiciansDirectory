from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView
from . import models
from . import forms
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages

# add album
@method_decorator(login_required, name='dispatch')
class AlbumCreateView(CreateView):
    model = models.Album
    form_class = forms.AlbumForm
    template_name = 'add_album.html'
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        # messages.success(self.request, 'Album added successfully!')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Submit'
        context['type2'] = 'Add'
        return context
    
# edit album
@method_decorator(login_required, name='dispatch')
class AlbumEditView(UpdateView):
    model = models.Album
    form_class = forms.AlbumForm
    template_name = 'add_album.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        # messages.success(self.request, 'Album updated successfully!')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Update'
        context['type2'] = 'Edit'
        return context
    
# delete album
@method_decorator(login_required, name='dispatch')
class AlbumDeleteView(DeleteView):
    model = models.Album
    template_name = 'add_album.html'
    success_url = reverse_lazy('homepage')

    def delete(self, request, *args, **kwargs):
        # messages.success(self.request, 'Album deleted successfully!')
        return super().delete(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Delete'
        context['type2'] = 'Delete'
        return context