
from django.http import JsonResponse



def getinfo(request):
    if request.method == "GET":
        content = {
            "slackUsername":"Johanan",
            "backend":True,
            "age":22,
            "bio":"I like watching anime and working with computers"
        }
        return JsonResponse(content)
    
