from django.shortcuts import render
from django.http import HttpResponse
from .models import Review  # モデルをインポート

def top_page(request):
    return render(request, 'top_page.html')

def save_data(request):
    if request.method == 'POST':
        form = request.POST
        age = form.get('age')
        gender = form.get('gender')
        overall_satisfaction = form.get('overall_satisfaction')
        food_satisfaction = form.get('food_satisfaction')
        price_satisfaction = form.get('price_satisfaction')
        ambience_satisfaction = form.get('ambience_satisfaction')
        service_satisfaction = form.get('service_satisfaction')
        other_comments = form.get('other_comments')

        # フォームのデータを辞書としてまとめる
        data = {
            'age': age,
            'gender': gender,
            'overall_satisfaction': overall_satisfaction,
            'food_satisfaction': food_satisfaction,
            'price_satisfaction': price_satisfaction,
            'ambience_satisfaction': ambience_satisfaction,
            'service_satisfaction': service_satisfaction,
            'other_comments': other_comments,
        }

        review = Review.objects.create(**data)

        return render(request, 'success_page.html')
    else:
        return HttpResponse("Invalid request method. Please use POST.")
    
def success_page(request):
    return render(request, 'success_page.html')