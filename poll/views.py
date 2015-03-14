from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http.response import HttpResponse
from poll.models import Question
# Create your views here.



def list(request):
    poll_list = Question.objects.all()
    return render_to_response("poll/list.html", {"poll_list":poll_list})


def choice(request, poll_id):
    try :
        p = Question.objects.get(pk=poll_id)
        return render_to_response("poll/choice.html", {"poll":p})
    except Question.DoesNotExist :
        return HttpResponse("Data Not Found")