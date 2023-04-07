# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 00:38:45 2021

@author: Dell
"""

import numpy as np
summ = 0
min = 1000
path = []
start = 100
minpath = []
m = []
path_string = ""
graph = {}
minarray = []

def bfsR(visited, queue, graph, node, goal):
    global summ, min, path, s, minpath
    visited.append(node)
    queue.append(node)
    while queue:
        s = queue.pop(0)
        
        for neighbour in graph[s]:
            if neighbour in visited:
                if neighbour == goal:
                    m.append(np.array(path))
                    if len(path) < len(minpath):
                        minpath = path
                        path.remove(node)
                    return
            else:
                path.append(neighbour)
                if neighbour==goal:
                    visited.append(neighbour)
                    
                    if len(path) < len(minpath):
                        minpath = path
                        m.append(np.array(path))
                    return
                bfsR(visited, queue, graph, neighbour, goal)
                path.remove(neighbour)
        return
def textpath(arr, start, finish):
    global path_string
    repeat = 0
    for i in range(len(arr)):
        if i == 0:
            if arr[i]==100:
                path_string = "Your starting point is South gate. Follow the recommended path in order to find your goal. Firstly, you need to stand in front of your starting point. "
            else:
                path_string = "Your starting point is " + str(start) + ". Follow the recommended path in order to find your goal. Firstly, you need to stand in front of your starting point. "
            continue
        if i == 1:
            if (int(arr[i]) == int(arr[i-1])-1) and (str(arr[i])[0]=="7" and str(arr[i])[1]=="0" or str(arr[i])[0]=="6"):
                path_string = path_string + "Turn left. "
            elif int(arr[i]) == int(arr[i-1])+1:
                path_string = path_string + "Turn right. "
        if (int(arr[i]) == int(arr[i-1])+1) or (int(arr[i]) == int(arr[i-1])-1):
            if arr[i] == finish:
                path_string = path_string + "Go straight next " + str(repeat+1) + " classrooms. You will see the classroom number " + str(arr[i]) + ". You have come to your destination point."
            repeat = repeat + 1
        else:
            if repeat != 0:
                path_string = path_string + "Go straight next " + str(repeat+1) + " classrooms. You will see the classroom number " + str(arr[i]) + ". "
                repeat = 0
                
            if (str(arr[i])[0] == str(arr[i-1])[0] and arr[i] != finish) or (arr[i-1] == 100):
                path_string = path_string + "You need to turn your face to the classroom number " + str(arr[i]) + ". "
            if arr[i] == finish:
                path_string = path_string + "You need to turn your face to the classroom number " + str(arr[i]) + ". You have come to your destination point."
                break
    return path_string          
def main(start, finish):
    global m, graph, minarray #,start
    graph = {100:[809,816,215,412,417,517,711,511],809:[816,827,100],827:[809,826,803],826:[827,825,804],825:[826,805],816:[809,817,100],817:[816,818],818:[817,820],820:[818],803:[804,805,827],804:[805,803,826],805:[804,825],215:[220,711,214,100],214:[215,213],213:[214,212],212:[213,211],211:[212,210],210:[211,209],209:[210,208],208:[209,207],207:[208,206],206:[207,205],205:[206,204],204:[205,203],203:[204,202],202:[203,302],302:[303,304,202],303:[304,302],304:[312,303,302],311:[312,308,408],308:[421,311],312:[311,304,222],222:[312,221],221:[222,220],220:[215,221,701],408:[311,409,421],409:[408,410,420],410:[409,411,419],411:[410,412,418],412:[411,517,417,100],421:[308,420,408],420:[421,419,409],419:[420,418,410],418:[419,417,411],417:[418,412,511,100],517:[518,511,412,100],518:[517,519,510],519:[518,520,509],520:[519,521,508],521:[520,522,507],522:[523,521,506],523:[524,522,505],524:[614,523,504,603],511:[510,517,417,100],510:[511,509,518],509:[510,508,519],508:[509,507,520],507:[508,506,521],506:[507,505,522],505:[506,504,523],504:[505,503,524],503:[504,502],502:[503,501],501:[502,614],603:[727,524,614,606],614:[524,501,613,603],613:[614,612],612:[613,611],611:[612,610],610:[611,609,603],609:[610,608],608:[609,607],607:[608,606],606:[607,709],711:[701,712,100],712:[711,713,702],713:[712,714,703],714:[715,712,704],715:[716,714,705],716:[715,717,706],717:[718,716,707],718:[717,719,708],719:[718,720,709],720:[721,719],721:[722,720],722:[723,721],723:[724,722],724:[723,725],725:[726,724],726:[727,725],727:[726,603],709:[606,708,721],708:[709,707,720],707:[708,706,719],706:[707,705,718],705:[704,706,717],704:[705,703,716],703:[704,702,715],702:[703,701,714],701:[220,711,702]}
    for i in range(len(graph)):
        minpath.append(1) #defining minimum path as a whole graph in the begining, it will change later
    path.append(start) #add start node to the path
    visited = [] # List to keep track of visited nodes.
    queue = []   # Initialize a queu
    bfsR(visited, queue, graph, start, finish)
    arr = len(m[0])
    minarray = m[0]
    for array in m:
        if len(array) < arr:
            minarray = array #choosing the minimum path out of all paths
    print(minarray)
    s = textpath(minarray, start, finish)
    print(s)
   