from django.shortcuts import render
from .models import About, Comment, ClientLogo, Education, Experince, Portfolio, Skills, Category, Service

def about(request):
    about = About.objects.all()
    comments = Comment.objects.all()
    clientlogo = ClientLogo.objects.all()
    education = Education.objects.all()
    experince = Experince.objects.all()
    skills = Skills.objects.all()
    categorys = Category.objects.all()
    projects = Portfolio.objects.all()
    service = Service.objects.all()
    return render(request, 'portfoliweb/index.html', {
        "about": about,
        "comments": comments,
        "clientlogo": clientlogo,
        "education": education,
        "experince": experince,
        "skills": skills,
        "categorys": categorys,
        "projects": projects,
        "service": service,
 },)

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import telegram


# def comment(request):
#     comments = Comment.objects.all()
#     return render(request, 'portfoliweb/index.html', {
#         "comments": comments,
#     },)
