from django.shortcuts import render
import requests
# Create your views here.
def input(request):
    newsapi = 'dbeaad2890e74a0a8370b3ed8f8f09f9'
    url = f'https://newsapi.org/v2/everything?q=Apple&from=2024-04-07&sortBy=popularity&apiKey={newsapi}'
    main_page = requests.get(url).json()
    article = main_page['articles']
    head = []
    data=[]
    for ar in article:
        head.append(ar["description"])
    for i in range(6):
        data.append(head[i])
        print(f'{i + 1} {head[i]}')
        print()
    if request.method=="GET":

        return render(request,'base.html',{'data':data})
    return render(request,'base.html',{'data':data})