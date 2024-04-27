from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductAPIView.as_view()),
    path('register/', views.UserRegistrationView.as_view()),
    path('img/', views.ProductImageAPIView.as_view()),
    path('comments-create/', views.CommentCreateAPIView.as_view()),
    path('comments/', views.CommentAPIView.as_view()),
    path('rating-create/', views.RatingCreateAPIView.as_view()),
    path('rating/', views.RatingAPIView.as_view()),
    path('comments-editor/', views.EditorCommentAPIView.as_view()),
    path('rating-editor/', views.EditorRatingAPIView.as_view()),
    path('profile/', views.UserRegistrationView.as_view()),
]
