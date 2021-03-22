#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from .procedures import pointer, transliterate
from .models import Articles_tree, Articles
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

NON_NEED_LOGIN = True

def yandex_63a3d0a896e29e17(request):
    return render(request, 'yandex_63a3d0a896e29e17.html', {})

def site_wellcome(request, art_tree_id = 1):
    if request.user.is_authenticated or NON_NEED_LOGIN:
        # Do something for authenticated users.
        if not NON_NEED_LOGIN: full_name = request.user.get_full_name()
    else:
        # Do something for anonymous users. 
        return HttpResponseRedirect(reverse('logins', args=[]))      
    #art_parent = Articles_tree.objects.raw("")
    art_parent = get_object_or_404(Articles_tree, pk=art_tree_id)
    return render(request, 'site_main.html', {'art_tree_id' : art_tree_id, 'art_parent' : art_parent.parent, 'type' : art_parent.type,})

def wrapper(request):
    if request.user.is_authenticated or NON_NEED_LOGIN:
        # Do something for authenticated users.
        if not NON_NEED_LOGIN: full_name = request.user.get_full_name()
    else:
        # Do something for anonymous users. 
        return HttpResponseRedirect(reverse('logins', args=[]))      
    id_arc_tree      = request.GET['id_art_tree']
    id_artile = get_object_or_404(Articles_tree, pk=id_arc_tree).id_articles
    head_line = get_object_or_404(Articles, pk=id_artile).title
    my_pointer = pointer(id_arc_tree, [])
    return render(request, 'site_wrapper.html', {'pointer' : my_pointer, 'head_line' : head_line, })

# Create your views here.
def site_main(request):
    if request.user.is_authenticated or NON_NEED_LOGIN:
        # Do something for authenticated users.
        if not NON_NEED_LOGIN: full_name = request.user.get_full_name()
    else:
        # Do something for anonymous users. 
        return HttpResponseRedirect(reverse('logins', args=[]))      
    return render(request, 'site_main.html', {})

def site_main_new(request, id_arc_tree = 1, article_name = ''):
    if request.user.is_authenticated or NON_NEED_LOGIN:
        # Do something for authenticated users.
        if not NON_NEED_LOGIN: full_name = request.user.get_full_name()
    else:
        # Do something for anonymous users. 
        return HttpResponseRedirect(reverse('logins', args=[]))      
    SQL = """SELECT p1.*, p2.id as id1, p2.id_articles as id_articles1, p2.url as url1, p2.title as title1 
        FROM mysite_articles_tree p1
            LEFT JOIN mysite_articles_tree p2 ON p2.parent = p1.id
        WHERE {} IN (p1.parent)
        ORDER BY p1.parent, p1.possision, p2.possision""" 
    Articles_tree_record = get_object_or_404(Articles_tree, pk=id_arc_tree)
    Article = get_object_or_404(Articles, pk=Articles_tree_record.id_articles)
    #head_line = Article.title
    my_pointer = pointer(id_arc_tree, [])
    id_art_parent = Articles_tree_record.parent
    head_tree =  Articles_tree.objects.raw(SQL.format(0))[:60]
    for line in head_tree:
        if line.title1:
            line.title_trans = transliterate(line.title) + '-' + transliterate(line.title1)
        else:
            line.title_trans = transliterate(line.title)
    tree = Articles_tree.objects.raw(SQL.format(my_pointer[0]['id']))[:60]
    for line in tree:
        if line.title1:
            line.title_trans = transliterate(line.title) + '-' + transliterate(line.title1)
        else:
            line.title_trans = transliterate(line.title)
    return render(request, 'site_main.html', {'head_tree' : head_tree,
                                                 'tree' : tree,
                                                 'id_arc_tree' : id_arc_tree,
                                                 'id_art_parent' : id_art_parent,
                                                 'pointer' : my_pointer, 
                                                 'head_line' : Article.title,
                                                 'art_content' : Article.art_data,
                                                 'type' : Articles_tree_record.type,})

def site_tree_test(request):
    if request.user.is_authenticated or NON_NEED_LOGIN:
        # Do something for authenticated users.
        if not NON_NEED_LOGIN: full_name = request.user.get_full_name()
    else:
        # Do something for anonymous users. 
        return HttpResponseRedirect(reverse('logins', args=[]))     
    ul = [['<ul class="sidebar-navigation">', '</ul>'],['<ul class="item-submenu-selected">','</ul>']]
    li = [['<li class="root-item"><a href="/o-kompanii/">', '</li>'],['<li><a href="/o-kompanii/nasha-komanda/#administrativnyy-departament"><i class="fa"></i>','</li>']]
    #result = footer(my_parent = 2, glubina = 2, ul = ul, li = li)
    #result = ""
    return render(request, 'site_tree_test.html', {'tree' : result, })

def site_head(request):
    if request.user.is_authenticated or NON_NEED_LOGIN:
        # Do something for authenticated users.
        if not NON_NEED_LOGIN: full_name = request.user.get_full_name()
    else:
        # Do something for anonymous users. 
        return HttpResponseRedirect(reverse('logins', args=[]))     
    id_arc_tree      = request.GET['id_art_tree']
    tree = Articles_tree.objects.raw("""
        SELECT p1.*, p2.id as id1, p2.id_articles as id_articles1, p2.url as url1, p2.title as title1 
        FROM mysite_articles_tree p1
            LEFT JOIN mysite_articles_tree p2 ON p2.parent = p1.id
        WHERE 0 IN (p1.parent)
        ORDER BY p1.parent, p1.possision, p2.possision""")[:60]      
    return render(request, 'site_head.html', {'tree' : tree, 'id_arc_tree' : id_arc_tree})

def site_navigator(request):
    if request.user.is_authenticated or NON_NEED_LOGIN:
        # Do something for authenticated users.
        if not NON_NEED_LOGIN: full_name = request.user.get_full_name()
    else:
        # Do something for anonymous users. 
        return HttpResponseRedirect(reverse('logins', args=[]))     
    id_arc_tree      = request.GET['id_art_tree']
    id_art_parent    = request.GET['id_art_parent']
    tree = Articles_tree.objects.raw("""
        SELECT p1.*, p2.id as id1, p2.id_articles as id_articles1, p2.url as url1, p2.title as title1 
        FROM mysite_articles_tree p1
            LEFT JOIN mysite_articles_tree p2 ON p2.parent = p1.id
        WHERE {} IN (p1.parent)
        ORDER BY p1.parent, p1.possision, p2.possision""".format(id_art_parent))[:60]        
    return render(request, 'site_navigator.html',  {'tree' : tree, 'id_arc_tree' : id_arc_tree})

def site_article(request):
    if request.user.is_authenticated or NON_NEED_LOGIN:
        # Do something for authenticated users.
        if not NON_NEED_LOGIN: full_name = request.user.get_full_name()
    else:
        # Do something for anonymous users. 
        return HttpResponseRedirect(reverse('logins', args=[]))     
    id_arc_tree      = request.GET['id_art_tree']
    #art_content = 'test'
    #zap_art_content = Articles.objects.raw("SELECT PA.* FROM mysite_articles_tree PAT, mysite_articles PA WHERE PAT.id = {} AND PAT.id_articles = PA.id".format(id_arc_tree))[:60]
    id_artile = get_object_or_404(Articles_tree, pk=id_arc_tree)
    art_content = get_object_or_404(Articles, pk=id_artile.id_articles).art_data
    #art_content = zap_art_content[0].art_data
    return render(request, 'site_content.html', {'id_arc_tree' : id_arc_tree, 'art_content' : art_content, 'type' : id_artile.type, })


def logins(request):
    error_message = ""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # Redirect to a success page.
                return HttpResponseRedirect(reverse('site_main', args=[]))
                #return HttpResponse( Messages)            
            else:
                # Return a 'disabled account' error message
                error_message = "Ваш аккаунт отключен, Дозвиданья!"
                return render(request, 'login.html', { 'error_message' : error_message, })
        else:
            # Return an 'invalid login' error message.
            error_message = "Не верный логин или пароль"   
            return render(request, 'login.html', { 'error_message' : error_message, })
    else:
        return render(request, 'login.html', { 'error_message' : error_message, })
       
def logouts(request):
    logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect(reverse('logins', args=[]))  








