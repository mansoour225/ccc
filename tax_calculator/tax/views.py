from django.shortcuts import render

# Create your views here.
tax_rate = 0.15

def index(request):
    return render(request, 'index.html')

def calculate_tax(request, amount):
    total_price = float(amount) + (float(amount) * tax_rate)
    return render(request, 'calculate_tax.html', {'total_price': total_price})

def tax_rate(request):
    return render(request, 'tax_rate.html', {'tax_rate': tax_rate})
