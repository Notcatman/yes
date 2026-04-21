from django.shortcuts import render, redirect, get_object_or_404
from .models import *

def base(request):
    return render(request, 'base.html')

def vacancies(request):
    vacancies = Vacancy.objects.all().order_by('-uploaded_at')
    return render(request, 'vacancies.html', {'vacancies': vacancies})

def post_vacancy(request):
    users = User.objects.all()
    
    if request.method == 'POST':
        author_id = request.POST.get('author')
        title = request.POST.get('title')
        description = request.POST.get('description')
        salary = request.POST.get('salary')
        
        if author_id and title and salary:
            author = get_object_or_404(User, id=author_id)
            Vacancy.objects.create(
                author=author,
                title=title,
                description=description,
                salary=salary
            )
            return redirect('vacancies')
    
    return render(request, 'post_vacancy.html', {'users': users})

def apply_vacancy(request, vacancy_id):
    vacancy = get_object_or_404(Vacancy, id=vacancy_id)
    users = User.objects.all()
    
    if request.method == 'POST':
        user_id = request.POST.get('user')
        content = request.POST.get('content')
        wanted_salary = request.POST.get('wanted_salary')
        
        if user_id and content and wanted_salary:
            user = get_object_or_404(User, id=user_id)
            Applicant.objects.create(
                author=user,
                vacancy=vacancy,
                content=content,
                wanted_salary=wanted_salary
            )
            return redirect('vacancy_detail', vacancy_id=vacancy.id)
    
    return render(request, 'apply.html', {'vacancy': vacancy, 'users': users})

def vacancy_detail(request, vacancy_id):
    vacancy = get_object_or_404(Vacancy, id=vacancy_id)
    applications = Applicant.objects.filter(vacancy=vacancy).order_by('-id')
    return render(request, 'vacancy_detail.html', {'vacancy': vacancy, 'applications': applications})


