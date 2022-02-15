from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View, DeleteView, UpdateView, View
from .models import studyModel
import datetime
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class SignupView(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        target_username = request.POST['username']
        target_password = request.POST['password']
        try:
            User.objects.get(username=target_username)
            return render(request, 'signup.html', {'error': 'このユーザーは登録されています'})
        except:
            user = User.objects.create_user(target_username, '', target_password)
            return redirect('studylist')


class SigninView(View):
    def get(self, request):
        return render(request, 'signin.html')

    def post(self, request):
        target_username = request.POST['username']
        target_password = request.POST['password']
        user = authenticate(username=target_username, password=target_password)
        if user is not None:
            login(request, user)
            return redirect('studylist')
        else:
            return render(request, 'signin.html', {'error': '登録されていないユーザーです。\nユーザーを新規登録してください'})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return render(request, 'signin.html', {'message': 'ログアウトしました。'})


@method_decorator(login_required, name='dispatch')
class StudylistView(ListView):
    template_name = 'studylist.html'

    def get_queryset(self):
        current_user = self.request.user
        return studyModel.objects.filter(user=current_user.username)

    def post(self, request):
        current_user = self.request.user
        models = studyModel(
                        title = request.POST["title"], 
                        detail = "",
                        finishFlg = False,
                        created = datetime.datetime.now(),
                        user = current_user.username,
                        category = request.POST["category"]
                        )
        models.save()
        return self.get(request)


class DetailView(DetailView):
    model = studyModel
    template_name = "detail.html"


class ChangeFinishView(View):
    def get(self, request, pk):
        result = studyModel.objects.get(pk=pk)

        if result.finishFlg:
            result.finishFlg = False
        else:
            result.finishFlg = True
        
        result.save()
        return redirect('studylist')


class DeleteView(DeleteView):
    template_name = 'delete.html'
    model = studyModel
    success_url = reverse_lazy('studylist')


class UpdateView(UpdateView):
    template_name = "update.html"
    model = studyModel
    fields = ('title', 'detail', 'category')
    success_url = reverse_lazy('studylist') 