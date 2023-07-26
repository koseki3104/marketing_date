from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

def validate_positive_age(value):
    if value < 0:
        raise ValidationError('年齢は負の値にすることはできません。')
    
def validate_not_empty_choice(value):
    if value == '':
        raise ValidationError('選択肢が空の値です。')

class Review(models.Model):
    # 年齢
    age = models.IntegerField(validators=[MinValueValidator(1), validate_positive_age])
    # 性別
    GENDER_CHOICES = (('', '選択してください'),('M', '男性'),('F', '女性'),) 
    gender = models.CharField(choices=GENDER_CHOICES, max_length=2)
    # メニュー
    MENU_CHOICES = (('', '選択してください'),('S', 'そば'),('U', 'うどん'),('R', 'ラーメン')) 
    menu = models.CharField(choices=MENU_CHOICES, max_length=2)
    # 全体の満足度
    SATISFACTION_CHOICES = (('', '選択してください'),(1, '1'),(2, '2'),(3, '3'),(4, '4'),(5, '5'),)
    overall_satisfaction = models.IntegerField(choices=SATISFACTION_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)])
    # 味の満足度
    FOOD_CHOICES = (('', '選択してください'),(1, '1'),(2, '2'),(3, '3'),(4, '4'),(5, '5'),)
    food_satisfaction = models.IntegerField(choices=FOOD_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)])
    # 価格の満足度
    PRICE_CHOICES = (('', '選択してください'),(1, '1'),(2, '2'),(3, '3'),(4, '4'),(5, '5'),)
    price_satisfaction = models.IntegerField(choices=PRICE_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)])
    # 店の雰囲気の満足度
    AMBIENCE_CHOICES = (('', '選択してください'),(1, '1'),(2, '2'),(3, '3'),(4, '4'),(5, '5'),)
    ambience_satisfaction = models.IntegerField(choices=AMBIENCE_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)])
    # 接客の満足度
    SERVICE_CHOICES = (('', '選択してください'),(1, '1'),(2, '2'),(3, '3'),(4, '4'),(5, '5'),)
    service_satisfaction = models.IntegerField(choices=SERVICE_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)])
    # 自由記述
    other_comments = models.TextField(blank=True, null=True)