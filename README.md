# Ex.04 Design a Website for Server Side Processing
## Date:13/12/2025

## AIM:
To create a web page to calculate vehicle mileage and fuel efficiency using server-side scripts.

## FORMULA:
M = D / F
<br> M --> Mileage (in km/l)
<br> D --> Distance Travelled (in km)
<br> F --> Fuel Consumed (in l)

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM:
~~~
Math.html
<html>
    <head>
        <title>Vehicle Mileage</title>
    </head>
    <style>
        .box
        {
            margin-top: 10%;
            margin-left: 25%;
            margin-right:25%;
            border: 8px  darkcyan; 
            background-color: peru;
            text-align: center; 
        }
    </style>
    <body>
        <div class="box">
        <h1> Calculator for Vehicle Mileage </h1>
        <h3>Bavin Balaji R</h3>
        <h3>25012625</h3>
        <br>
        <form method="POST">
            {% csrf_token %}
            <label>Distance: </label>
            <input type="text" name="Distance" value="{{D}}" required> Km
            <br><br>
            <label>Amount of Fuel: </label>
            <input type="text" name="Volume" value="{{V}}" required> L
            <br><br>
            <input type="submit" value="Calculate">
            <br><br>
            <label>Mileage: </label>
            <input type="text" name="Mileage" value="{{M}}"> Km/L
        </form>
        </div>
    </body>
</html>
views.py

from django.shortcuts import render
def eff(request):
    D = int(request.POST.get('Distance', 0))
    V = int(request.POST.get('Volume', 0))
    M = D/V if request.method == 'POST' else 0
    print("Distance=",D)
    print("Volume=",V)
    print("Mileage=",M)
    return render(request, 'Mathapp/Math.html', {'D': D, 'V': V, 'M': M})

urls.py

from django.urls import path
from Mathapp import views
urlpatterns = [
    path('', views.eff, name='eff'),
]

~~~


## OUTPUT - SERVER SIDE:

![alt text](<Screenshot 1.png>)


## OUTPUT - WEBPAGE:
![alt text](<Screenshot 2.png>)

## RESULT:
The a web page to calculate vehicle mileage and fuel efficiency using server-side scripts is created successfully.
