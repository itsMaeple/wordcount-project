from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    # Getting text from the form
    fulltext = request.GET['fulltext']
    # Sending results to count page
    wordlist = fulltext.split()
    # Checking words that are repeatedly used
    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            # Increase
            worddictionary[word] +=1
        else:
            # Add to the dictionary
            worddictionary[word] = 1
    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
    # Sending results to count page
    return render(request, 'count.html', {'fulltext': fulltext, 'count':len(wordlist),'sortedwords':sortedwords})
