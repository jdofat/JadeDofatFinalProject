# controls what each page does
# what data to show
# which template to load

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Internship
import requests
import os

# Adzuna API
ADZUNA_APP_ID = os.environ.get("ADZUNA_APP_ID", "")
ADZUNA_APP_KEY = os.environ.get("ADZUNA_APP_KEY", "")
ADZUNA_COUNTRY = "us"

# home page
def home(request):
    return render(request, "internships/home.html")

# functions to call api
# returns list internship dictionaries (or empty list)
def fetch_adzuna_internships(search_term=""):
    base_url = f"https://api.adzuna.com/v1/api/jobs/{ADZUNA_COUNTRY}/search/1"

    params = {
        "app_id": ADZUNA_APP_ID,
        "app_key": ADZUNA_APP_KEY,
        "what": search_term
    }

    try:
        resp = requests.get(base_url, params=params, timeout=5)
        data = resp.json()
        return data.get("results", [])
    except Exception:
        return []

# shows internships from Adzuna and DB (or search results)
# admins see delete
def results(request):
    search_text = request.GET.get("q", "")

    # fetch from your database
    db_internships = Internship.objects.filter(title__icontains=search_text) if search_text else Internship.objects.all()

    # fetch from Adzuna API
    adzuna_results = fetch_adzuna_internships(search_text)
    api_internships = []

    for item in adzuna_results:
        # prepend "api_" to ensure IDs are unique vs database IDs
        api_internships.append({
            "id": f"api_{item.get('id')}",
            "title": item.get("title", "No Title"),
            "company": item.get("company", {}).get("display_name", ""),
            "description": item.get("description", ""),
            "url": item.get("redirect_url", ""),
            "location": item.get("location", {}).get("display_name", "")
        })

    # combine both database and API results
    all_internships = list(db_internships) + api_internships

    # message if none found
    message = "" if all_internships else "None found"

    return render(request, "internships/results.html", {
        "internships": all_internships,
        "message": message,
        "search_text": search_text
    })


def internship_detail(request, internship_id):
    # Loads details for the internship
    # checks if it's a database or API internship
    selected = None

    if str(internship_id).startswith("api_"):
        # fetch from Adzuna API
        api_id = internship_id.replace("api_", "")
        data = fetch_adzuna_internships("")
        for item in data:
            if str(item.get("id")) == api_id:
                selected = item
                break
    else:
        # fetch from DB
        try:
            selected = Internship.objects.get(id=internship_id)
        except Internship.DoesNotExist:
            selected = None

    if not selected:
        return HttpResponse("You need to login to view more details.")

    # format data to read it easily
    if isinstance(selected, Internship):
        clean = {
            "title": selected.title,
            "company": selected.company,
            "description": selected.description,
            "url": selected.url
        }
    else:
        clean = {
            "title": selected.get("title"),
            "company": selected.get("company", {}).get("display_name", ""),
            "description": selected.get("description", ""),
            "url": selected.get("redirect_url", "")
        }

    return render(request, "internships/detail.html", {"intern": clean})


def admin_login(request):
    # admin logs in here
    # success or error popup
    message = ""

    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST.get("username"),
            password=request.POST.get("password")
        )

        if user:
            login(request, user)
            message = "success"
        else:
            message = "error"

    return render(request, "internships/login.html", {"message": message})


def create_admin(request):
    # creates a new admin user:
    # success or error
    message = ""

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            message = "exists"
        else:
            User.objects.create_user(username=username, password=password)
            message = "created"

    return render(request, "internships/create.html", {"message": message})


def delete_internship(request, internship_id):
    # admin can delete an internship from db
    if not request.user.is_authenticated:
        # redirect to login page with message
        return redirect(f"{reverse('login')}?message=you need to log in as an admin to delete an entry")

    # Only database internships can be deleted
    if not str(internship_id).startswith("api_"):
        # fetch from DB or 404
        internship = get_object_or_404(Internship, id=internship_id)
        internship.delete()

    # redirect to results page
    return redirect("results")


