from django.http import HttpResponse    
from django.shortcuts import render
import operator 
import string

def home(request):
    return render(request, 'home.html')

def user(request):
    original_text = request.GET['full_Text']
    
    #cleaning punctuation and normalizing 
    translator = str.maketrans('', '', string.punctuation)
    clean_text = original_text.lower().translate(translator)
    
    word_list = clean_text.split()

    word_dic = {}

    #count words
    for word in word_list:
        if word in word_dic:
            word_dic[word] += 1
        else:
            word_dic[word] = 1

    #sort and store inverted
    sorted_dict = sorted(word_dic.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'user.html',{'text':original_text, 'count':len(word_list), 'dictionary':sorted_dict})

def about(request):
    return render(request, 'about.html')
    #return HttpResponse('<h1>About</h1>')

