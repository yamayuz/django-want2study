from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View
from .models import studyModel
import datetime


class StudylistView(ListView):
    template_name = 'studylist.html'
    model = studyModel

    def post(self, request):
        models = studyModel(
                        title = request.POST["title"], 
                        detail = "",
                        finishFlg = False,
                        created = datetime.datetime.now(),
                        user = "",
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