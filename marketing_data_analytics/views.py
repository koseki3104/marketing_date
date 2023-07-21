from django.shortcuts import render, redirect
from django.http import HttpResponse
import pandas as pd
from .models import Review

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

def export_to_excel(request):
    data = Review.objects.all()

    # データをPandas DataFrameに変換
    data_df = pd.DataFrame(list(data.values()))

    # 平均値を計算
    average_data = {
        'age': data_df['age'].mean(),
        'overall_satisfaction': data_df['overall_satisfaction'].mean(),
        'food_satisfaction': data_df['food_satisfaction'].mean(),
        'price_satisfaction': data_df['price_satisfaction'].mean(),
        'ambience_satisfaction': data_df['ambience_satisfaction'].mean(),
        'service_satisfaction': data_df['service_satisfaction'].mean(),
    }

    # 平均値のみを含むDataFrameを作成
    average_df = pd.DataFrame([average_data])

    # Excelファイルに平均値を出力
    with pd.ExcelWriter('data_analytics.xlsx', engine='xlsxwriter') as writer:
        average_df.to_excel(writer, sheet_name='Average', index=False)

    # ExcelファイルをダウンロードさせるためのResponseオブジェクトを作成
    with open('data_analytics.xlsx', 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=average_export.xlsx'

    return response