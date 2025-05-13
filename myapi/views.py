from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.http import Http404,JsonResponse


def home_view(request):
    
    with connection.cursor() as cursor:
        cursor.execute("SELECT ifsc, bank_id, branch, address, city, state FROM branches LIMIT 200")
        rows = cursor.fetchall()
        objects = [
            {
                "ifsc": row[0],
                "bank_id": row[1],
                "branch": row[2],
                "address":row[3],
                "city": row[4],
                "state": row[5],
            }
            for row in rows
        ]

    





    return render(request, "myapi/home.html",{'objects':objects})

def banklist_view(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT name FROM banks")

        rows = cursor.fetchall()
       
        objects=[

            {
                "name": row[0],
            }
            for row in rows
        ]

    
    return JsonResponse({"objects":objects})
    
    
def branches_view(request, bank):
    # bank=bank.replace("%20", " ")
    with connection.cursor() as cursor:
        cursor.execute("SELECT id FROM banks WHERE name= %s", [bank])
        val=cursor.fetchone()
        if not val:

            raise Http404("Invalid Name/Enter name in all Caps")

        cursor.execute("SELECT ifsc, branch, address, city, district, state FROM branches WHERE bank_id=%s LIMIT 200 ", [val])
        rows=cursor.fetchall()

        objects=[
            {
                "ifsc": row[0],
                "branch": row[1],
                "address": row[2],
                "city": row[3],
                "district": row[4],
                "state":row[5]
                
            }
            for row in rows

        ]
    return JsonResponse({"objects":objects})
    # return render(request, "myapi/branchlist.html", {"objects":objects})



def branch_details_view(request, ifsc):
    
    with connection.cursor() as cursor:
        cursor.execute("SELECT bank_id, branch, address, city, district, state FROM branches WHERE ifsc=%s", [ifsc])
        rows=cursor.fetchall()
        if not rows:
            raise Http404("Invalid IFSC CODE")
        for row in rows:
            banknum=row[0]
        cursor.execute("SELECT name FROM banks WHERE id=%s", [banknum])
        bank_name=cursor.fetchone()
        objects=[
            {
                "branch":row[1],
                "address":row[2],
                "city":row[3],
                "district":row[4],
                "state":row[5],
                "bank":bank_name

            }
            for row in rows
            ]
    
    return JsonResponse({"objects":objects}) 
    # return render(request,"myapi/branchdetails.html", {"objects":objects})







# Create your views here.


# Create your views here.
