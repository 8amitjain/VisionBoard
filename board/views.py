from django.http import JsonResponse
from django.views import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required

from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView
)

from .forms import PhotoForm
from .models import Photo, Vision


class BasicUploadView(LoginRequiredMixin, View):
    def get(self, request, pk):
        photos_list = Photo.objects.all()
        vision_list = Vision
        return render(self.request, 'board/index.html', {'photos': photos_list,
                                                         'vision': vision_list,
                                                         'pk': pk})

    def post(self, request, pk):
        form = PhotoForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            form.instance.vision_id = pk
            photo = form.save()
            data = {'is_valid': True, 'name': photo.file.name, 'url': photo.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)


# class AllVisionListView(LoginRequiredMixin, UserPassesTestMixin, ListView):  # listing all vision boards
#     model = Vision
#     template_name = 'board/vision-view-all.html'  # app/<model>_<viewtype>.html
#     vision = Vision.objects.filter(user=user)
#     context_object_name = 'vision'
#
#     def get_queryset(self):
#         user = get_object_or_404(User, username=self.kwargs.get('username'))
#         return Vision.objects.filter(user=user)
#
#     def test_func(self):
#         user = get_object_or_404(User, username=self.kwargs.get('username'))
#         if self.request.user == user:
#             return True
#         return False

@login_required
def all_list_view(request):  # listing all vision boards
    vision = Vision.objects.filter(user=request.user)
    vision_F = Vision.objects.filter(user=request.user).first()
    len_vision = len(vision)
    data = len_vision - 5
    context = {
        'vision': vision,
        'vision_F': vision_F,
        'len_vision': len_vision,
        'data': data
    }
    return render(request, 'board/vision-view-all.html', context)


@login_required
def detail_view(request, pk):  # listing all vision boards
    vision = Vision.objects.all()
    context = {
        'vision': vision,
        'pk': pk
    }
    return render(request, 'board/popup.html', context)


# def test_func(self):
#     vision = self.get_object()
#     if self.request.user == vision.user:
#         return True
#     return False


@login_required
# @user_passes_test(test_func)
def vision_view(request, pk):  # listing all vision boards
    photo = Photo.objects.filter(vision__id=pk)

    len_photo = len(photo)
    num_rows = int(len_photo/3)
    if num_rows == 0:
        num_rows = 1
    context = {
        'photo': photo,
        'pk': pk,
        'len_photo': len_photo,
        'num_rows': num_rows
    }
    return render(request, 'board/vision-view.html', context)


# class VisionListView(LoginRequiredMixin, ListView):  # listing photos of a particular vision board
#     model = Photo
#     template_name = 'board/vision-view.html'  # app/<model>_<viewtype>.html
#     context_object_name = 'photo'
#
#     def get_queryset(self):
#         pk = self.kwargs.get('pk')
#         total_photo = Photo.objects.filter(vision__id=pk)
#         a = len(total_photo)
#         return a


class CreateVision(LoginRequiredMixin, CreateView):
    model = Vision
    fields = ['image', 'title', 'content']
    # default template vision_form
    success_url = '../view/all/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UpdateVision(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Vision
    fields = ['image', 'title', 'content']
    # default template vision_form

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        vision = self.get_object()
        if self.request.user == vision.user:
            return True
        return False


class VisionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Vision
    success_url = '../../view/all/'

    def test_func(self):
        vision = self.get_object()
        if self.request.user == vision.user:
            return True
        return False


class VisionImageDeleteView(LoginRequiredMixin, DeleteView, UserPassesTestMixin):
    model = Photo
    success_url = '../../../view/all/'
    def test_func(self, pk):

        vision = Photo.objects.get(id=pk).photo.delete(save=True)
        if self.request.user == vision.user:
            return True
        return False




