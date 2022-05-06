from django.shortcuts import render
from googletrans import Translator
import googletrans

# Create your views here.

def index(req):
    context={
        "nd" : googletrans.LANGUAGES
    }
    # context={ 
    #     "d" : {1:"one", 2:"two", 3:"three"},      # dictionary 연습
    # }
    # context={}    # 처음에 나라 5 개 했을 때 post 아닐 경우 
    if req.method == "POST":
        text1=req.POST.get("con")
        a=req.POST.get("fn")
        b=req.POST.get("tn")
        translator = Translator()
        trans1 = translator.translate(text1, src=a, dest=b)
        # print(trans1.text)
        context.update({
            "trans1": trans1.text,
            "con" : text1,
            "fn" : a,
            "tn" : b,
            
        })        

    return render(req, "trans/index.html", context)
