from django.shortcuts import render
def eff(request):
    D = int(request.POST.get('Distance', 0))
    V = int(request.POST.get('Volume', 0))
    M = D/V if request.method == 'POST' else 0
    print("Distance=",D)
    print("Volume=",V)
    print("Mileage=",M)
    return render(request, 'Mathapp/Math.html', {'D': D, 'V': V, 'M': M})
