from django.shortcuts import render
import operator


def home(request):
    return render(request, 'home.html')

def count(request):

    fulltext = request.GET['fulltext']

    wordList = fulltext.split()

    wordDictionary = {}

    for word in wordList:
        if word in wordDictionary:
            wordDictionary[word] += 1
        else:
            wordDictionary[word] = 1


    sortedList = sorted(wordDictionary.items(), key = operator.itemgetter(1), reverse = False)


    return render(request, 'count.html', {'narsi':sortedList})

def about(request):
    return render(request, 'about.html')
