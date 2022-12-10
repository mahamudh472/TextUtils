from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')
def analyzer(request):
    my_text = request.GET.get('text', "default")
    punc = request.GET.get('removepunc', 'off')
    upper = request.GET.get('uppercase', 'off')
    lower = request.GET.get('lowercase', 'off')
    reverse = request.GET.get('reverse', 'off')
    analyzed = ""
    print(upper)
    if punc == 'on':
        analyzed = ""
        for i in my_text:
            if i not in '''+-*/`~@!#$%^&*()_+-=;:'"<>?/''':
                analyzed += i
    if upper == "on":
        analyzed = my_text.upper()
    if lower == "on":
        analyzed = my_text.lower()
    if reverse == "on":
        analyzed = my_text[::-1]
    
    params = {
        'purpuse' : "remove punctuations",
        'text' : analyzed
    }
    
    return render(request, 'analyzer.html', params)