from django.shortcuts import render
import markdown2
from . import util
from entries import *
import entries
from django.urls import reverse
from django.http import HttpResponseRedirect
import random


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def search(request):
    if request.method == "POST":
        print("Yes")
        Title = request.POST["q"]
        print("Got title")
        Entry = util.get_entry(Title)
        print("Got Wiki")
        if Entry == None:
            return render(request, "encyclopedia/available.html", {
                "entries": util.list_entries()})
        else:
            Entrycon = markdown2.markdown(Entry)
            print("Converted")
            return render(request, "encyclopedia/result.html", {
                "entry": Entry,
                "title": Title.capitalize(),
                "e": Entrycon
            })


def test(request):
    htmls = markdown2.markdown_path("entries/css.md")
    p = markdown2.markdown_path("entries/git.md")
    a = markdown2.markdown_path("entries/django.md")
    html = htmls
    return render(request, "encyclopedia/test.html", {
        "httm": html,
        "p": p,
        "a": a})


def searched(request, name):
    if request.method == "GET":
        Entries = util.get_entry(name)
        if Entries == None:
            return render(request, "encyclopedia/error.html")
        else:
            Entry_ry = markdown2.markdown(Entries)
            return render(request, "encyclopedia/new.html", {
                "name": Entry_ry
            })


def NewPage(request):
    return render(request, "encyclopedia/newpage.html")


def savepage(request):
    if request.method == "POST":
        Title = request.POST["Title"]
        Content = request.POST["Content"]
        if util.get_entry(Title):
            return render(request, "encyclopedia/newpage.html", {
                "Entry_used": "This entry title already exists!"
            })
        else:
            util.save_entry(Title, Content)
            return render(request, "encyclopedia/saved.html")


def editpage(request):
    return render(request, "encyclopedia/editpage.html")


def editted(request):
    if request.method == "POST":
        Title = request.POST["Title"]
        Content = request.POST["Content"]
        util.save_entry(Title, Content)
        return render(request, "encyclopedia/saved.html")


def randompage(request):
    a = random.randint(1, 6)
    if a == 1:
        htmls = markdown2.markdown_path("entries/css.md")
        return render(request, "encyclopedia/random.html", {
            "html": htmls,
            "title": "CSS"}
        )
    elif a == 2:
        htmls = markdown2.markdown_path("entries/django.md")
        return render(request, "encyclopedia/random.html", {
            "html": htmls,
            "title": "Django"
        })
    elif a == 3:
        htmls = markdown2.markdown_path("entries/python.md")
        return render(request, "encyclopedia/random.html", {
            "html": htmls,
            "title": "Python"
        })
    elif a == 4:
        htmls = markdown2.markdown_path("entries/html.md")
        return render(request, "encyclopedia/random.html", {
            "html": htmls,
            "title": "Html"
        })
    elif a == 5:
        htmls = markdown2.markdown_path("entries/git.md")
        return render(request, "encyclopedia/random.html", {
            "html": htmls,
            "title": "Git"
        })
    else:
        htmls = markdown2.markdown_path("entries/Dog.md")
        return render(request, "encyclopedia/random.html", {
            "html": htmls,
            "title": "Dog"
        })
