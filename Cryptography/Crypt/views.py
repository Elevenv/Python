from django.shortcuts import render,redirect
from django.http import HttpResponse
import pycipher
def ui(request):
    return render(request,"ui.html")

def Encrypt(request):
    plain_text = request.POST['plain_text']
    key = request.POST['key']
    plain_text_str = str(plain_text)
    key_int = int(key)
    cipher_text = pycipher.Caesar(key_int).encipher(plain_text_str)
    temp = "Cipher text is : "
    cipher_text12 = temp + cipher_text
    key_temp = "Key is : "
    key12 = key_temp+key
    return render(request,"ui.html",{'cipher_text':cipher_text12,'key':key12})

def Decrypt(request):
    cipher_text = request.POST['cipher_text']
    key = request.POST['key']
    cipher_text_str = str(cipher_text)
    key_int = int(key)
    plain_text1 = pycipher.Caesar(key_int).decipher(cipher_text_str)
    temp = "Plain text is : "
    plain_text12 = temp+plain_text1
    return render(request,"ui.html",{'plain_text':plain_text12})