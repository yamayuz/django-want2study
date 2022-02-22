from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View, DeleteView, UpdateView, View
from .models import studyModel
import datetime
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http.response import JsonResponse


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
        if 'q1' in self.request.POST and self.request.POST["q1"] == '1':
            return studyModel.objects.filter(user=current_user.username, finishFlg=True)
        elif 'q1' in self.request.POST and self.request.POST["q1"] == '2':
            return studyModel.objects.filter(user=current_user.username, finishFlg=False)
        else:
            return studyModel.objects.filter(user=current_user.username)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        if 'q1' in self.request.POST:
            context['sort'] = self.request.POST["q1"]
        else:
            context['sort'] = '0'
        return context

    def post(self, request):
        if 'q1' in request.POST:
            print('ラジオボタン')
        else:
            current_user = self.request.user
            models = studyModel(
                            title = request.POST["title"], 
                            detail = "　",
                            finishFlg = False,
                            created = datetime.datetime.now(),
                            user = current_user.username,
                            category = request.POST["category"],
                            favorite = False,
                            deadline = datetime.datetime.now(),
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
        return redirect('detail', pk=pk)


class DeleteView(DeleteView):
    model = studyModel
    success_url = reverse_lazy('studylist')


class UpdateView(View):
    def post(self, request, pk):
        result = studyModel.objects.get(pk=pk)
        result.detail = request.POST["detail"]
        result.category = request.POST["category"]
        result.deadline = request.POST["deadline"]
        result.save()
        return redirect('detail', pk=pk)


class FavoriteView(View):
    def get(self, request, pk):
        result_dic = {"pk":pk}

        try:
            result = studyModel.objects.get(pk=pk)
            if result.favorite:
                result.favorite = False
                result_dic['add_star'] = False
            else:
                result.favorite = True
                result_dic['add_star'] = True
            result.save()
            result_dic['status'] = '0'      
        except:
            result_dic['status'] = '1'    
    
        json_data = {"result":result_dic}
        return JsonResponse(json_data)


class FavoriteListView(ListView):
    template_name = 'favorite_list.html'

    def get_queryset(self):
        current_user = self.request.user
        return studyModel.objects.filter(user=current_user.username, favorite=True)

    def post(self, request):
        favorite_list = studyModel.objects.filter(user=self.request.user, favorite=True)
        favorite_list.update(favorite=False)
        return self.get(request)