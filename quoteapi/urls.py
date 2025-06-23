from django.urls import path
from .views import QuoteEndpoint  # ✅ This is the correct way

urlpatterns = [
    path('quotes/', QuoteEndpoint.as_view()),
]
