from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template import loader
from  .models import Member
# Create your views here.
import psycopg2


def members(request: HttpRequest):
    members = Member.objects.all().values()
    template = loader.get_template("all_members.html")
    context = {
        'mymembers': members,
     
    }
    return HttpResponse(template.render(context, request))

def users(request):
    return HttpResponse("users page")


def member_details(request: HttpRequest ,id):
    find_member = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    
    context = {
        'mymember' : find_member
    }
    return HttpResponse(template.render(context,request))

def main_page(request):
    

    try:
        conn = psycopg2.connect(
            dbname="django_2",
            user="django_2",
            password="django-123",
            host="database-2.ch280gy42n7e.ap-southeast-2.rds.amazonaws.com",
            port="5432"
        )
        print("Connection successful!")
    except Exception as e:
        print(f"Error: {e}")

    template = loader.get_template('main.html')
    print(request)
    return HttpResponse(template.render())

def testing(request):
    template = loader.get_template('template.html')
    context = {
        'fruits': [
            'Apple', "Banana", "Pork Choi"
        ]
    }
    return HttpResponse(template.render(context,request))
