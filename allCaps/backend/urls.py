from django.urls import path
from . import views as methods

urlpatterns = [
    path('ask', methods.PromptInputView.as_view(),name="AskPrompt"),
    path('<str:action>', methods.PromptInputView.as_view(), name="ViewPrompt")
]