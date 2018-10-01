from django.shortcuts import render
from django.http import HttpResponse

'''
Created on Oct 1, 2018

@author: vuexiong
'''

def index(request):
    return HttpResponse("Test to see if I can push pull without any issue.")
