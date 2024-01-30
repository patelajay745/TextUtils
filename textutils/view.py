#I have created this file - Ajay


from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    
    return render(request,'index.html')
def analyze(request):
    
    djtext=request.POST.get('input_value','defualt')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    spaceremover=request.POST.get('spaceremover','off')
    charcounter=request.POST.get('charcounter','off')

    params={}
    
    if removepunc=="on":
        analyzed=""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed= analyzed + char
        djtext=analyzed
        #params['Removed_Punctuations']=analyzed

    if fullcaps=="on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        djtext=analyzed
        #params['Changed_to_UpperCase']=analyzed
        

    if newlineremover=="on":
        analyzed=""
        for char in djtext:
            if char != "\n" and char != "\r" :
                analyzed=analyzed+char
        djtext=analyzed
        #params['Removed_New_line']=analyzed
        
    if spaceremover=="on":
        analyzed=""
        for char in djtext:
            if char != " " :
                analyzed=analyzed+char
        djtext=analyzed
        #params['Removed_Space']=analyzed
        
    if charcounter=="on":
        djtext=djtext+ "\n" +"Total character: "+ str(len(djtext))
        
        
    
    
    params={'purpose': 'Output', 'analyzed_text': djtext}
     
    
    #print(request.GET.get('removepunc','defualt'))
    return render(request,'analyze.html',params)

