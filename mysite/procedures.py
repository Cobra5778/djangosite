#!/usr/bin/python
# -*- coding: utf-8 -*-
# encoding: utf-8
# vim:fileencoding=utf-8

import sys  

#reload(sys)
#sys.setdefaultencoding('utf8')

from django.db import connection

def pointer(my_child = 47, result = []):
    cursor = connection.cursor()
    my_SQL = "SELECT id, parent, title FROM mysite_articles_tree WHERE id = {}".format(my_child)
    cursor.execute(my_SQL)
    for id, parent, title in cursor:
        pointer(my_child = parent, result = result)
        result.append({'id':id, 'parent':parent, 'title':title})
        #print title
    
    return result

def tree_data(my_parent = 0, glubina = 10,  my_data = 0, result = [], level = 0):
    # Создает список дерева
    if my_data == 0:
        cursor = connection.cursor()
        my_SQL = "SELECT id, parent, url, title, id_articles FROM mysite_articles_tree ORDER BY parent, possision"
        cursor.execute(my_SQL)
        my_data = cursor   
    for id, parent, url, title, id_articles in my_data:
        #print "Level:" + "{}".format(level)         
        if parent == my_parent and level <= glubina - 1:
            #level = level + 1
            #print "{} |".format(level * "    ") + title
            result.append([id, parent, level, url, title, id_articles])
            tree_data(my_parent = id, glubina = glubina,  my_data = my_data, result = result, level = level + 1)
            #level = level - 1 
    # id, parent, level,  name, id_article 
    return result

def tree_data_dic(my_parent = 0, glubina = 10,  my_data = 0, result = [], level = 0):
    # Создает список дерева
    if my_data == 0:
        cursor = connection.cursor()
        my_SQL = "SELECT id, parent, url, title, id_articles FROM mysite_articles_tree ORDER BY parent, possision"
        cursor.execute(my_SQL)
        my_data = cursor   
    for id, parent, url, title, id_articles in my_data:
        #print "Level:" + "{}".format(level)         
        if parent == my_parent and level <= glubina - 1:
            #level = level + 1
            #print "{} |".format(level * "    ") + title
            #result.append([id, parent, level, url, title, id_articles])
            result.append({'id':id, 'parent':parent, 'level':level, 'url':url, 'title':title, 'id_articles':id_articles})
            tree_data_dic(my_parent = id, glubina = glubina,  my_data = my_data, result = result, level = level + 1)
            #level = level - 1 
    # id, parent, level,  name, id_article 
    return result

def footer(my_parent = 0, glubina = 2, i = 0, my_dimm = [], level = 0, result = "", ul = ['<ul>','</ul>'], li = ['<li>','</li>']):
    if my_dimm == []:
        my_dimm = tree_data(my_parent = my_parent, glubina = glubina)
        result += ul[level][0]
        #ul = [['<ul class="sidebar-navigation">', '</ul>'],['<ul class="item-submenu">','</ul>']]#['<ul>','</ul>']
        #li = [['<li class="root-item"><a href="/o-kompanii/">', '</li>'],['<li><a href="/o-kompanii/nasha-komanda/#administrativnyy-departament"><i class="fa"></i>','</li>']]#['<li>','</li>']
        #print(ul[0])  
    while i < len(my_dimm):
        if  level < my_dimm[i][2]:
            result += ul[level+1][0]
            #print("{}{}".format((level+1) * "    ", ul[0]))
            proba = footer(my_parent = my_dimm[i][1], i = i, my_dimm = my_dimm, level = my_dimm[i][2], result = result, ul = ul, li = li)
            i = proba[0]
            result = proba[1]
        if level == my_dimm[i][2]:
            z = my_dimm[i][4].encode('UTF-8')
            result += "{}{}{}".format(li[level][0], z, li[level][1])
            #print ("{}{}{}{}".format((level+1) * "    ", li[0], my_dimm[i][4].encode('UTF-8'), li[1]))
        if  level > my_dimm[i][2]:
            result += ul[level][1]
            #print("{}".format(ul[1]))
            return i, result
        i += 1
    result += ul[level][1]
    #print(ul[1])
    return result

def footer1(my_parent = 0, glubina = 2, i = 0, my_dimm = [], level = 0, result = "", ul = ['<ul>','</ul>'], li = ['<li>','</li>']):
    if my_dimm == []:
        my_dimm = tree_data(my_parent = my_parent, glubina = glubina)
        result += ul[level][0]
        #print(ul[level][0])
    while i < len(my_dimm):
        if  level < my_dimm[i][2]:
            result += ul[level+1][0]
            #print("{}{}".format( (level+1) * "    ", ul[level+1][0]))
            proba = footer1(my_parent = my_dimm[i][1], i = i, my_dimm = my_dimm, level = my_dimm[i][2], result = result, ul = ul, li = li)
            i = proba[0]
            result = proba[1]
        if level == my_dimm[i][2]:
            #Проверяем последняя ли это запись
            if i+1 == len(my_dimm): #Последняя
               result += "{}{}".format( li[level][0].format(my_dimm[i][0], my_dimm[i][4].encode('UTF-8')), li[level][1] )
               #print ("{}{}{}".format( (level+1) * "    ", li[level][0].format(my_dimm[i][4].encode('UTF-8')), li[level][1] ))
            else: # Не последняя
                if level < my_dimm[i+1][2]: #Если сделующая запись новое вложение
                    result += "{}".format( li[level][0].format(my_dimm[i][0],my_dimm[i][4].encode('UTF-8')) )
                    #print ("{}{}".format( (level+1) * "    ", li[level][0].format(my_dimm[i][4].encode('UTF-8')) ))
                else: # Нового вложения нет
                    result += "{}{}".format( li[level][0].format(my_dimm[i][0],my_dimm[i][4].encode('UTF-8')), li[level][1] )
                    #print ("{}{}{}".format( (level+1) * "    ", li[level][0].format(my_dimm[i][4].encode('UTF-8')), li[level][1] ))

        if  level > my_dimm[i][2]:
            result += "{}{}".format(ul[level][1], li[level][1])
            #print("{}{}".format(level*"    ", ul[level][1]))
            #print("{}{}".format(level*"    ", li[level][1] ))
            return i, result
        i += 1
    result += ul[level][1]
    #print "{}".format(ul[level][1])
    return result


#print tree_data_dic(my_parent = 0, glubina = 2)
#k =  poiner()
#for i in k:
#    print i #.encode('UTF-8')
#    print i['title']
#for k in tree_data(my_parent = 0, glubina = 2):
#    print "{} {} L:{} {} {} {}".format(k[0], k[1], k[2], k[3], k[4].encode('UTF-8'), k[5] )
#ul = [['<ul class="sidebar-navigation">', '</ul>'],['<ul class="item-submenu-selected">','</ul>'], ['<ul class="item-submenu">', '</ul>']]
#li = [['<li class="root-item"><a href="/o-kompanii/"><i class="fa"></i>{}</a>', '</li>'],['<li><a href="/o-kompanii/nasha-komanda/#administrativnyy-departament"><i class="fa"></i>{}</a>', '</li>'],['<li><a href="/o-kompanii/nasha-komanda/#administrativnyy-departament"><i class="fa"></i>','</li>']]   

#print footer1(2, 2, ul = ul, li = li)
