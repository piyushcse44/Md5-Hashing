from django.shortcuts import render
from .hashing_fn import vigenere_encrypt,vigenere_decrypt

def home(request):
    text = request.POST.get('PlainText')
    key = request.POST.get('key')
    message = vigenere_encrypt(str(text),str(key))
    encypted_message=""
    encypted_message = request.POST.get('EncyptMessage')
    try:
        decypted_message = vigenere_decrypt(str(encypted_message))
    
    except:
        decypted_message = ""

    
    data ={
        'PlainText':text,
        'key':key,
        'message' : message,
        'flag': True,
        'decypt_message': decypted_message,
        'EncyptMessage':encypted_message,

    }
    return render(request,'home.html',data)

