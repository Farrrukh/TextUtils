from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
    #return HttpResponse('''<h1><a href="https://www.facebook.com/">Facebook</a></h1>''')


def about(request):
    print(request.GET.get('text', 'default'))
    return HttpResponse('''<a href="/">Back</a>''')

def farrukh(request):
    params={'name' : 'farrukh', 'lastname' : 'khan'}
    return render(request,'index.html',params)

def contact(request):
    return render(request, 'index.html')


def analyze(request):
    djtext = request.POST.get('text', 'default')
    print(djtext)

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    # Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif (fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)

    elif (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)

    elif (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
            else:
                print("no")
        print("pre", analyzed)
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        print(params)
        # Analyze the text
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error")


def ex1(request):
    x="<h2>Navigation Bar</h2><a href='https://www.facebook.com/'>Facebook</a><br><a href='https://www.youtube.com/watch?v=lcpqpxVowU0&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=12'>Code with Harry</a> "
    return HttpResponse(x)


def ex2(request):
    s = '''<h1> Headings</h1>
    <style>
    h1{
        color:red;
        font-size:20;
        text-style:none;

    }
    a{
        color:red;
        font-size:20;
        text-style:none;
        margin:20px;
        position:absolute;

    }
    </style>

    <a href=https://www.youtube.com/watch?v=lcpqpxVowU0&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=12>Code with harry bhai </a>
    '''
    return HttpResponse(s)