from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Review

class ReviewModelTestCase(TestCase):

    def test_positive_age_validation(self):
        with self.assertRaises(ValidationError) as context:
            review = Review(age=-5, gender='M', menu='S',
                            overall_satisfaction=4, food_satisfaction=3,
                            price_satisfaction=5, ambience_satisfaction=2,
                            service_satisfaction=4)
            review.full_clean()
        expected_message = ['Ensure this value is greater than or equal to 1.', '年齢は負の値にすることはできません。']
        self.assertEqual(context.exception.messages, expected_message)

    def test_not_empty_choice_validation(self):
        with self.assertRaises(ValidationError) as context:
            review = Review(age=25, gender='', menu='U',
                            overall_satisfaction=2, food_satisfaction=4,
                            price_satisfaction=3, ambience_satisfaction=5,
                            service_satisfaction=1)
            review.full_clean()
        expected_message = ['This field cannot be blank.']
        self.assertEqual(context.exception.messages, expected_message)

    def test_review_creation(self):
        review = Review.objects.create(age=30, gender='M', menu='R',
                                       overall_satisfaction=5, food_satisfaction=4,
                                       price_satisfaction=4, ambience_satisfaction=3,
                                       service_satisfaction=5)
        self.assertEqual(Review.objects.count(), 1)
        self.assertEqual(review.age, 30)
        self.assertEqual(review.gender, 'M')
        self.assertEqual(review.menu, 'R')
        self.assertEqual(review.overall_satisfaction, 5)
        self.assertEqual(review.food_satisfaction, 4)
        self.assertEqual(review.price_satisfaction, 4)
        self.assertEqual(review.ambience_satisfaction, 3)
        self.assertEqual(review.service_satisfaction, 5)
        self.assertIsNone(review.other_comments)

    def test_review_other_comments(self):
        review = Review.objects.create(age=22, gender='F', menu='S',
                                       overall_satisfaction=3, food_satisfaction=2,
                                       price_satisfaction=1, ambience_satisfaction=4,
                                       service_satisfaction=3, other_comments='Good experience.')
        self.assertEqual(review.other_comments, 'Good experience.')
