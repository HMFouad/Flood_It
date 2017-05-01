# ==============================================================================
# Floodit : 
# ==============================================================================
__author__  = "Hocini Mohamed Fouad & Rahali Lina Samar"
__version__ = "1.0"
__date__    = "2013-12-20"
# ==============================================================================
import random
from tkinter import *
# ==============================================================================
def cb_ok():
  global Taille, colors, compteur, Nbcolor, nb_coup

  root[112]['bg']="white"
  root[122]['bg']="white"
  for i in range(Nbcolor):
    root[i+1000].destroy()

  for i in range(Taille*Taille):
    col, row = i%Taille, i//Taille
    root[col,row].destroy()

  a=0
  try:
    Taille = int(root[112].get())
    a=1
    #root[21]['text'] = ""
  except:
    root[112]['bg']="red"
    Erreur(1)
  if a==1:
    a=0
    try: 
      Nbcolor = int(root[122].get())
      a=1
    except:
      root[122]['bg']="red"
      Erreur(2)
    #generation_couleur()
    if a==1:
      nb_coup=Taille+Nbcolor+(Taille*Taille)%Nbcolor

      root[311] = Frame(root[31], relief=SOLID, border=0)
      root[311].pack(side=TOP, padx=5, pady=5,fill=BOTH)

      root[312]['text'] = str(compteur)+"/"+str(nb_coup)
      root[312].pack(side=TOP, fill=BOTH, pady=5, padx=5)

      root[313] = Button(root[31], text="Nouvelle partie", command=cb_newgame)
      root[313].pack(side=TOP, pady=5, padx=5)

      root[321] = Frame(root[32], relief=SOLID, border=0)
      root[321].pack(side=TOP, padx=5, pady=5,fill=BOTH)

      Remplissage(Taille, Nbcolor)
# ------------------------------------------------------------------------------  
def Remplissage(Taille, Nbcolor):
  #Remplissage de la matrice aléatoirement
  global compteur

  a, b=5, 2
  if Nbcolor>=10: a, b=3, 1
  #elif Nbcolor>=24: a,b=1, 0
  for i in range(Nbcolor):
    j=1000+i   
    root[j] = Button(root[311], width=a, height=b, bg=colors[i], command= lambda coll=colors[i] :diff(coll))    
    root[j].pack(side=TOP, padx=0, pady=0)
  a, b=5, 2
  if Taille>=14: a, b=3, 1
  elif Taille>=24: a,b=1, 0
  for i in range(Taille*Taille):
    col, row = i%Taille, i//Taille
    root[col,row] = Label(root[321], width=a, height=b, bg=random.choice(colors[0:Nbcolor]))
    root[col,row].grid(column=col, row=row, padx=0, pady=0)
# ------------------------------------------------------------------------------  
def diff(couleur_remplacement):
  global compteur
  if compteur<nb_coup:
          compteur+=1
          root[312]['text'] = str(compteur)+"/"+str(nb_coup)
          root[312].pack(side=TOP, fill=BOTH, pady=5, padx=5)
          diffusion(0, 0, root[0,0]['bg'], couleur_remplacement)
          if compteur==nb_coup: resultat(0)
          verification()
  else: resultat(0)
# ------------------------------------------------------------------------------
def verification():
  a=1
  for i in range (Taille):
   for j in range (Taille):
     if root[i,j]['bg']!=root[0,0]['bg']:a=0
  if a==1: resultat(1)
# ------------------------------------------------------------------------------
def cb_newgame():
  #Boutton Newgame
  global compteur
  compteur=0
  root[312]['text'] = str(compteur)+"/"+str(nb_coup)
  root[312].pack(side=TOP, fill=BOTH, pady=5, padx=5)

  root[112]['bg']="white"
  root[122]['bg']="white"
  root[311].destroy()
  root[313].destroy()
  root[321].destroy()
  root[112].delete(0,END)
  root[122].delete(0,END)
  root[312]['text']=""
# ------------------------------------------------------------------------------
def diffusion(i, j, couleur_actuel, couleur_remplacement):
  #Algorithme de diffusion
 if i<Taille and j<Taille:
  if root[i,j]['bg'] == couleur_actuel:
      root[i,j]['bg'] = couleur_remplacement
      if i>0: diffusion(i-1, j, couleur_actuel, couleur_remplacement)
      if i<Taille: diffusion(i+1, j, couleur_actuel, couleur_remplacement)
      if j>0: diffusion(i, j-1, couleur_actuel, couleur_remplacement)
      if j<Taille: diffusion(i, j+1, couleur_actuel, couleur_remplacement)
# ------------------------------------------------------------------------------
def resultat(i):
  #Fenêtre resultat qui affiche gagné ou perdu
  resultat= Tk()
  global Taille, Nbcolor

  Text1= Label(resultat, border=0, relief=SOLID)
  if i==0: Text1['text']= "                    Vous avez perdu                    "
  elif i==1: Text1['text']="                    Vous avez gagné                    "

  resultat.geometry("400x80+500+300")
  Text1.pack(fill=BOTH, pady=5, padx=5)

  resultat.title('Resultat')
  resultat.resizable(width=False, height=False)
  
  Boutton = Button(resultat, text="Fermer", command= resultat.destroy)
  Boutton.pack(side=TOP, pady=5, padx=5)

  disable_boutton()
  # ----------------------------------------------------------------------------
def disable_boutton():
  #Disable les bouttons
  for i in range(Nbcolor):
    j=1000+i
    root[j]['bg'] = "#EBECEC"
    root[j]['command']=""
  # ----------------------------------------------------------------------------
def Help():
  #Fenêtre Help
  Help= Tk()
  
  Text1 = Label(Help, border=0, relief=SOLID, text="Le but de flood-it est de recouvrir toute la surface du plateau d'une seule couleur en un minimum de coup.\n\nPour cela il suffit de changer la couleur du carré en haut à gauche du plateau, toute les pieces de memes couleur qui touchent cette piece vont à leur tour prendre cette couleur.\n\nChaque fois que vous sélectionnez une couleur le compteur s'incrémente.")
  Text1.pack(side=TOP, fill=BOTH, pady=5, padx=5)

  #Help.overrideredirect(1)
  Help.title('Aide!')
  Help.resizable(width=False, height=False)
  Help.iconbitmap("Icon2.ico")
  Help.geometry("1000x120+280+300")

  Boutton = Button(Help, text="Fermer", command= Help.destroy)
  Boutton.pack(side=TOP, pady=5, padx=5)
  # ----------------------------------------------------------------------------
def Apropos():
  #Fenetre Apropos
  Apropos= Tk()
  
  Text1 = Label(Apropos, border=0, relief=SOLID, text="Floodit, Fait par:\n          * Hocini Mohamed Fouad.\n          * Rahali Lina Samar.")
  Text1.pack(side=LEFT, fill=BOTH, pady=5, padx=5)

  #Help.overrideredirect(1)
  Apropos.title('A propos')
  Apropos.resizable(width=False, height=False)
  Apropos.iconbitmap("Apropos.ico")
  #Apropos.geometry("100x50+280+300")

  Boutton = Button(Apropos, text="Fermer", command= Apropos.destroy)
  Boutton.pack(side=TOP, pady=5, padx=5)  
  # ----------------------------------------------------------------------------
def Erreur(i):
  #Affichage des messages d'erreurs
  Erreur= Tk()
  Text1 = Label(Erreur, border=0, relief=SOLID)
  Text1.pack(side=TOP, fill=BOTH, pady=5, padx=5)

  if i==1:Text1['text']="Erreur: la taille de la grille doit être un entier"
  elif i==2:Text1['text']="Erreur: le nombre de couleurs doit être un entier"

  Erreur.title('Erreur')
  Erreur.resizable(width=False, height=False)
  Erreur.iconbitmap("Erreur.ico")
  Erreur.geometry("400x90+280+300")

  Boutton = Button(Erreur, text="Fermer", command= Erreur.destroy)
  Boutton.pack(side=TOP, pady=5, padx=5)
# ------------------------------------------------------------------------------
def Niveau():
  #Choisir la difficulté de jeu
  global nbcoup, choix
  Choix=choix.get()
  if Choix==0: nbcoup=int(nbcoup+(nbcoup*10)/100)
  elif Choix==1: nbcoup=nbcoup*1
  elif Choix==2: int(nbcoup-(nbcoup*10)/100)
# ------------------------------------------------------------------------------
##def generation_couleur():
# On a voulu génerer les couleurs aléatoirement suite au choix de nombre de couleurs, mais a cause de géneration des couleurs presque les mêmes, on a éviter ça
##  global Nbcolor, colors
##  for i in range(Nbcolor):
##    colors=colors+"'"+str(random.choice(Nombre))+str(random.choice(Nombre))+str(random.choice(Nombre))+"',"
# ------------------------------------------------------------------------------
def main():
  global root, Taille, colors, compteur, Nbcolor, nb_coup, choix
  root, font = {0: Tk()}, 'Arial 16 bold'
  colors = ('#2DDC01', '#FE0101', '#9B0086', '#FE35E3', '#1A01FB', '#FEF601', '#000000', '#FEFFFF', '#7FC6BC', '#B4AF91', '#FE9901', '#780F0F')
  #Nombre=('00','01','02','03','04','05','06','07','08','09','0A','0B','0C','0D','0E','0F','10','11','12','13','14','15','16','17','18','19','1A','1B','1C','1D','1E','1F','20','21','22','23','24','25','26','27','28','29','2A','2B','2C','2D','2E','2F','30','31','32','33','34','35','36','37','38','39','3A','3B','3C','3D','3E','3F','40','41','42','43','44','45','46','47','48','49','4A','4B','4C','4E','4F','50','51','52','53','54','55','56','57','58','59','5A','5B','5C','5D','5E','5F','60','61','62','63','64','65','66','67','68','69','6A','6B','6C','6D','6E','6F','70','71','72','73','74','75','76','77','78','79','7A','7B','7C','7D','7E','7F','80','81','82','83','84','85','86','87','88','89','8A','8B','8C','8D','8E','8F','90','91','92','93','94','95','96','97','98','99','9A','9B','9C','9D','9E','9F','A0','A1','A2','A3','A4','A5','A6','A7','A8','A9','AA','AB','AC','AD','AE','AF','B0','B1','B2','B3','B4','B5','B6','B7','B8','B9','BA','BB','BC','BD','BE','BF','C0','C1','C2','C3','C4','C5','C6','C7','C8','C9','CA','CB','CC','CD','CE','CF','D0','D1','D2','D3','D4','D5','D6','D7','D8','D9','DA','DB','DC','DD','DE','DF','E0','E1','E2','E3','E4','E5','E6','E7','E8','E9','EA','EB','EC','ED','EE','EF','F0','F1','F2','F3','F4','F5','F6','F7','F8','F9','FA','FB','FC','FD','FE','FF')
  Taille=0
  Nbcolor=0
  compteur=0
  nb_coup=0
  # ----------------------------------------------------------------------------  
  #Barre des Menu
  mainmenu = Menu(root[0])
  menuFichier = Menu(mainmenu)
  menuFichier.add_command(label="Nouvelle partie", command=cb_newgame)  
  menuFichier.add_separator() ## Ajout d'une ligne séparatrice
  menuFichier.add_command(label="Quitter", command=root[0].destroy)

  menuAide = Menu(mainmenu)
  menuAide.add_command(label="A propos", command= Apropos)  
  menuAide.add_separator() ## Ajout d'une ligne séparatrice
  menuAide.add_command(label="Aide!", command=Help)

  mainmenu.add_cascade(label = "Fichier", menu = menuFichier)
  root[0].config(menu = mainmenu)
  mainmenu.add_cascade(label = "Aide", menu = menuAide)
  root[0].config(menu = mainmenu)
  # ----------------------------------------------------------------------------  
#Fond de fenetre
  Fond=PhotoImage(file="Bordeaux_2.gif")
  root[0].image=Fond
  # ----------------------------------------------------------------------------  
  root[1] = Frame(root[0], relief=SOLID)
  root[1].pack(side=TOP, padx=5, pady=5)

  root[11] = Frame(root[1], relief=SOLID, border=0)
  root[11].pack(side=LEFT, padx=5, pady=5, fill=BOTH)
  root[111] = Label(root[11], font=font, border=0, relief=SOLID, text="Entrer la taille de la grille:          ")
  root[111].pack(side=TOP, fill=BOTH, pady=5, padx=5)
  root[112]= Entry(root[11], width=30)
  root[112].pack()
                                # -------------------
  root[12] = Frame(root[1], relief=SOLID, border=0)
  root[12].pack(side=TOP, padx=5, pady=5, fill=BOTH)
  root[121] = Label(root[12], font=font, border=0, relief=SOLID, text="Entrer le nombre de couleurs:")
  root[121].pack(side=TOP, fill=BOTH, pady=5, padx=5)
  root[122]= Entry(root[12], width=30)
  root[122].pack()
  # ----------------------------------------------------------------------------
  root[2] = Frame(root[0], relief=SOLID)
  root[2].pack(side=TOP, padx=5, pady=5)

  root[21] = Label(root[2], font=font, border=0, relief=SOLID, text="Choisis votre niveau:")
  root[21].pack(side=TOP, fill=BOTH, pady=5, padx=5)
  
  choix = StringVar()
  Rad1 = Radiobutton(root[2] ,text = "Débutant", variable= choix, value= 0, command= Niveau())
  Rad1.pack(side="left")
 
  Rad2 = Radiobutton(root[2] ,text = "Moyen", variable= choix, value= 1, command= Niveau())
  Rad2.pack(side="left")

  Rad3 = Radiobutton(root[2] ,text = "Expert", variable= choix, value= 2, command= Niveau())
  Rad3.pack(side="left")  
                                
  root[22] = Button(root[0],width=10, height=1, text="Commencer", command=cb_ok)
  root[22].pack(side=TOP)

  root[23] = Button(root[0],width=10, height=1, text="Aide!", command=Help)
  root[23].pack(side=TOP)

  # ----------------------------------------------------------------------------
  root[3] = Frame(root[0], relief=SOLID, border=0)
  root[3].pack(padx=5, pady=5)

  root[31] = Frame(root[3], relief=SOLID, border=0)
  root[31].pack(side=LEFT, padx=5, pady=5)

  root[312] = Label(root[31], font=font, border=0, relief=SOLID)
  root[312].pack(side=TOP, fill=BOTH, pady=5, padx=5)

  root[314] = Label(root[31], font=font, border=0, relief=SOLID)
  root[314].pack(side=TOP, fill=BOTH, pady=5, padx=5)

  root[32] = Frame(root[3], relief=SOLID, border=0)
  root[32].pack(side=TOP, padx=5, pady=5)  
  # ----------------------------------------------------------------------------
  root[0].title('Floodit'); root[0].resizable(width=True, height=True); root[0].iconbitmap("Icon1.ico"); root[0].config (bg = "#EDF7F2"); root[0].wm_state(newstate="zoomed"); root[0].mainloop()
  # ------------------------------------------------------------------------------
if __name__ == '__main__':
  main()
  # ==============================================================================
