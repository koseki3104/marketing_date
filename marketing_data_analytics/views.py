from openpyxl import Workbook, load_workbook
from openpyxl.styles import PatternFill
import pandas as pd
import os
from django.http import HttpResponse
from django.conf import settings
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

    # 数値データのみを含むDataFrameを作成
    numerical_data_df = data_df[['age', 'overall_satisfaction', 'food_satisfaction', 'price_satisfaction', 'ambience_satisfaction', 'service_satisfaction']]

    # 平均値を計算
    average_data = numerical_data_df.mean().round(2)

    # 相関行列を計算
    correlation_matrix = numerical_data_df.corr().round(2)

    # Excelファイルに平均値と相関行列を出力（ファイル名を変更）
    file_path = os.path.join(settings.MEDIA_ROOT, 'data_analytics.xlsx')
    with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
        average_data.to_excel(writer, sheet_name='Average')  # Corrected here (index=True is used by default)
        correlation_matrix.to_excel(writer, sheet_name='CorrelationMatrix')

    # 相関行列のシートを開いてセルの色を設定
    book = load_workbook(file_path)
    sheet = book['CorrelationMatrix']

    # セルの色を設定するためのカスタム関数
    def set_cell_color(cell, color):
        cell.fill = PatternFill(start_color=color, end_color=color, fill_type="solid")

    for row in sheet.iter_rows(min_row=2, max_row=correlation_matrix.shape[0]+1, min_col=2, max_col=correlation_matrix.shape[1]+1):
        for cell in row:
            value = cell.value
            if value < -0.7:
                set_cell_color(cell, "6495ED")  # 負の相関で濃い青に設定
            elif value < -0.5:
                set_cell_color(cell, "ADD8E6")  # 負の相関でもう少し濃い青に設定
            elif value < -0.3:
                set_cell_color(cell, "B0C4DE")  # 負の相関でさらに薄い青に設定
            elif value < 0.3:
                set_cell_color(cell, "FF6347")  # 正の相関でオレンジ色に設定
            elif value < 0.5:
                set_cell_color(cell, "FF4500")  # 正の相関で金色に設定
            elif value < 0.7:
                set_cell_color(cell, "FF0000")  # 正の相関でダークオレンジ色に設定

    week_correlation_cell = sheet.cell(row=correlation_matrix.shape[0]+3, column=2)  
    week_correlation_cell.value = "相関係数-0.3以上-0.5未満で弱い負の相関"
    set_cell_color(week_correlation_cell, "B0C4DE")  # 負の相関でトマト色に設定

    normal_correlation_cell = sheet.cell(row=correlation_matrix.shape[0]+4, column=2)
    normal_correlation_cell.value = "相関係数-0.5以上-0.7未満で普通の負の相関"
    set_cell_color(normal_correlation_cell, "ADD8E6")  # 負の相関で橙赤に設定

    strong_correlation_cell = sheet.cell(row=correlation_matrix.shape[0]+5, column=2)
    strong_correlation_cell.value = "相関係数-0.7以上で強い負の相関"
    set_cell_color(strong_correlation_cell, "6495ED")  # 負の相関で濃い赤に設定

    strong_positive_correlation_cell = sheet.cell(row=correlation_matrix.shape[0]+6, column=2)
    strong_positive_correlation_cell.value = "相関係数0.7以上で強い正の相関"
    set_cell_color(strong_positive_correlation_cell, "FF0000")  # 正の相関でダークオレンジ色に設定

    normal_positive_correlation_cell = sheet.cell(row=correlation_matrix.shape[0]+7, column=2)
    normal_positive_correlation_cell.value = "相関係数0.5以上0.7未満で普通の正の相関"
    set_cell_color(normal_positive_correlation_cell, "FF4500")  # 正の相関でオレンジ色に設定

    weak_positive_correlation_cell = sheet.cell(row=correlation_matrix.shape[0]+8, column=2)
    weak_positive_correlation_cell.value = "相関係数0.3以上0.5未満で弱い正の相関"
    set_cell_color(weak_positive_correlation_cell, "FF6347")  # 正の相関で金色に設定

    book.save(file_path)

    # ExcelファイルをダウンロードさせるためのResponseオブジェクトを作成
    with open(file_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=data_analytics.xlsx'

    return response
