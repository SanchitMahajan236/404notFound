from django.shortcuts import render


# Create your views here.
def Home(request):
    return render(request, "Base_platform/homepage.html")


def Login(request):
    return render(request, "Base_platform/login.html")


def About(request):
    return render(request, "Base_platform/footer.html")

def Profile(request):
  return render(request,"Base_platform/profile.html")

def StockBot(request):
  return render(request,"Base_platform/stockbot.html")

def Analysis(request):
  return render(request,"Base_platform/analysis.html")