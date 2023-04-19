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

@csrf_exempt
def send_telegram_message(request):
    if request.method == 'POST':
        # Process the form data here...
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # Then send a message to Telegram
        bot = telegram.Bot(token='5962755012:AAHMvrF3i9QdYvxCcac6asDPlA3SkX8Xj_8')
        bot.send_message(chat_id='1816256414', text=f'New contact form submission from {name} ({email}): {message}')
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

# def comment(request):
#     comments = Comment.objects.all()
#     return render(request, 'portfoliweb/index.html', {
#         "comments": comments,
#     },)
