from django.urls import path
from . import view
'''
Created on Oct 1, 2018

@author: vuexiong
'''
urlPatterns = [
    path('',view.index, name = 'index'),
    ]