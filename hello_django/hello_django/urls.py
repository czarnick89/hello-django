"""
URL configuration for hello_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
import math

def rectangle_area(response, height, width):
    return HttpResponse(f"<h1>Area of a rectangle with height {height} and width {width} is {round(height*width, 2)} when rounded to two decimal places.</h1>")

def rectangle_perimeter(response, height, width):
    return HttpResponse(f"<h1>Perimeter of a rectangle with height {height} and width {width} is {round((height*2)+(width*2), 2)} when rounded to two decimal places.</h1>")

def circle_area(response, radius):
    return HttpResponse(f"<h1>Area of a circle with radius {radius} is {round(math.pi * (radius ** 2), 2)} when rounded to two decimal places.</h1>")

def circle_perimeter(response, radius):
    return HttpResponse(f"<h1>Perimeter of a circle with radius {radius} is {round(2*math.pi * (radius), 2)} when rounded to two decimal places.</h1>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rectangle/area/<int:height>/<int:width>', rectangle_area),
    path('rectangle/perimeter/<int:height>/<int:width>', rectangle_perimeter),
    path('circle/area/<int:radius>', circle_area),
    path('circle/perimeter/<int:radius>', circle_perimeter),
]
