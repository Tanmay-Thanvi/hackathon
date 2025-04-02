from django.views import View
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from .models import PromptData

# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class PromptInputView(View):
    fields_not_to_show = ['isSharable', 'create_date', 'last_modified_date']
    
    def get(self, request, action = None):
        promptId = request.GET['promptId']
        if action == "share":
            return self.share(request, promptId)
        elif action == "view":
            return self.view(request, promptId)
        return JsonResponse({'error': 'Invalid action'}, status=400)

    def share(self, request, promptId):
        if PromptData.objects.filter(id=promptId).exists():
            promptData = PromptData.objects.get(id=promptId)
            promptData.isSharable = True
            promptData.save()
            return JsonResponse({'url_to_share': request.build_absolute_uri('/') + 'prompt/view?promptId=' + promptId})
        return JsonResponse({'message': 'Prompt Id Not Found'}, status=404)

    def view(self, request, promptId):
        if PromptData.objects.filter(id=promptId).exists():
            promptData = PromptData.objects.get(id=promptId)
            if promptData.isSharable :
                return JsonResponse({'promptData': model_to_dict(promptData, exclude=self.fields_not_to_show)})
            else :
                return JsonResponse({'message': 'Prompt is not sharable'}, status=404)
        return JsonResponse({'message': 'Prompt Id Not Found'}, status=404)
    
    def post(self, request, action = None):
        question = request.POST.get("question")
        if question:
            answerFromModel = "We will answer from Model"
            PromptData.objects.create(prompt=question, answer=answerFromModel)
            return JsonResponse({'Answer': answerFromModel})
        return JsonResponse({'error': 'Question not provided properly'}, status=400)