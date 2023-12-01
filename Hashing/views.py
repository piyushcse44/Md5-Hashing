from django.shortcuts import render
from .hashing_fn import vigenere_encrypt

def home(request):
    text = request.POST.get('PlainText')
    key = request.POST.get('key')
    message = vigenere_encrypt(str(text),str(key))
    return render(request,'home.html',{'message' : message})

