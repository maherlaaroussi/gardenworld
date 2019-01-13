# Maher LAAROUSSI
# TP2 MR

# Initialisation

#!/usr/bin/env python
# -*- coding: utf-8 -*- 

try:
    initialisation
except NameError:
    initialisation = True
    from gardenworld import *
    from game0 import *
    init('tiny_complete')
    orientation = 2
    xcoord = 9
    ycoord = 0
    

    
# Demitour du personnage
def demitour():
    global orientation
    tg()
    tg()
    orientation += 2
    
# Tourner a gauche avec orientation
def tgo():
    global orientation
    tg()
    orientation += 1
    
# Tourner a droite avec orientation
def tdo():
    global orientation
    td()
    orientation += -1
    
# Connaitre l'orientation du personnage
def quelle_orientation():
    if orientation % 4 == 1:
        return "Nord"
    elif orientation % 4 == 2:
        return "Ouest"
    elif orientation % 4 == 3:
        return "Sud"
    elif orientation % 4 == 0:
        return "Est"
    else:
        return "Erreur"
        
# Avance le personnage avec MAJ de x et y
def avxy():
    global xcoord
    global ycoord
    
    if obstacle() :
        return 'false'
    
    if quelle_orientation() == 'Est' :
        if not obstacle() :
            av()
            xcoord += 1
            return 'true'
    if quelle_orientation() == 'Ouest' :
        if not obstacle() :
            av()
            xcoord += -1
            return 'true'
    if quelle_orientation() == 'Nord' :
        if not obstacle() :
            av()
            ycoord += 1
            return 'true'
    if quelle_orientation() == 'Sud' :
        if not obstacle() :
            av()
            ycoord += -1
            return 'true'
            
# Avance le personnage avec MAJ de x et y et avec detour
def avxy3():
    global xcoord
    global ycoord
    
    # Pour compter le nombre d'obstacle
    casesOb = 0
    
    # Si le personnage se trouve a la limite de la map
    if xcoord == 9 and quelle_orientation() == "Est" :
        return ;
    if xcoord == -9 and quelle_orientation() == "Ouest" :
        return ;
    if ycoord == 9 and quelle_orientation() == "Nord" :
        return ;
    if ycoord == -9 and quelle_orientation() == "Sud" :
        return ;
    
    # Si le personnage ne peut pas avancer
    if avxy() == 'false':
        
        orientationNow = quelle_orientation()
        
        # On sauvegarde notre position initiale
        xnow = xcoord
        ynow = ycoord
        
        # On incremente la variable des obstacles
        casesOb += 1
            
        # On essaye de contourner l'obstacle par la gauche
        tgo();avxy();tdo()
        
        # Si la case fait 1
        if not obstacle() :
            avxy()

            if not obstacle():            
                avxy();tdo()
            else:
                return ;
            
            #S'il n y a pas d'obstacle sur la case apres l'obstacle
            if not obstacle() :    
                avxy()
                orienter(orientationNow)
                return ;
            
        # S'il y a un obstacle on le contournera jusqu'a mettre le personnage sur une case libre
        while obstacle():
            casesOb += 1
            tgo();avxy();tdo()
            
            # S'il n'y a pas d'obstacle sur la prochaine case
            if not obstacle():
                avxy()
                orienter(orientationNow)
                break
            
            # S'il y a un obstacle sur la n case
            else:
                # On avancera jusqu'a trouver une case libre
                while obstacle():
                    casesOb += 1
                    tgo();avxy();tdo()
        
                if not obstacle() :    
                    avxy()
                    orienter(orientationNow)
                    return ;
            
        
        
                
def avxy3n(nbr):
    for i in range(nbr):
        avxy3()

        
# Oriente le personnage
def orienter(pc):
    while quelle_orientation() != pc:
        tgo()
        
# Pour parler au personnages
def parlePerso(nom):
    
    if nom == "Roi" :
        aller_a(1,0)
        orienter("Ouest")
        parle("bonjour %s" % nom)
        
    if nom == "Robin" :
        aller_a(5,2)
        orienter("Est")
        parle("bonjour %s" % nom)
        
    if nom == "Milton" :
        aller_a(-7,-6)
        orienter("Est")
        parle("bonjour %s" % nom)
        
    if nom == "Mmouarf" :
        aller_a(5,7)
        orienter("Ouest")
        parle("bonjour %s" % nom)
        
    if nom == "Pim" :
        aller_a(5,-5)
        orienter("Est")
        parle("bonjour %s" % nom)
        
    if nom == "Poum" :
        aller_a(7,-7)
        orienter("Sud")
        parle("bonjour %s" % nom)
        
    if nom == "Thomas" :
        aller_a(-4,5)
        orienter("Nord")
        parle("bonjour %s" % nom)
        
# Deplace le personnage vers une case de la map sans prendre en compte les obstacles
def aller_a(xpc,ypc):
    global xcoord
    global ycoord
    
    if xcoord == xpc and ycoord == ypc:
        return ;
        
    else:
        while xcoord != xpc or ycoord != ypc:
            
            if ycoord > ypc :
                orienter("Sud")
                while ycoord != ypc:
                    avxy3()
                
            if xcoord > xpc :
                orienter("Ouest")
                while xcoord != xpc:
                    avxy3()
                
            if ycoord < ypc :
                orienter("Nord")
                while ycoord != ypc:
                    avxy3()
                
            if xcoord < xpc :
                orienter("Est")
                while xcoord != xpc:
                    avxy3()
    
        
        
