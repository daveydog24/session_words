from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime

def index(request):
    if 'context' not in request.session:
        request.session['context'] = []
    context = {
        "sessions":request.session['context']
    }
    return render(request, "session_words_templates/index.html", context)

def process(request):
    if 'context' not in request.session:
        request.session['context'] = []
    if request.method == "POST":
        word = request.POST['word']
        if "color" in request.POST:
            color = request.POST['color']
        else:
            color = "black"
        if "big_font" in request.POST:
            font = "big"
        else:
            font = "normal"
    time = datetime.strftime(datetime.now(), "%H:%M:%S %p, %B %d, %Y")

    request.session['context'].append({'word': word, 'color': color, 'font': font, 'time': time})
    request.session.modified = True
    return redirect("/session_words")

def clear(request):
    if request.method == "POST":
        request.session.clear()
        return redirect("/session_words")
