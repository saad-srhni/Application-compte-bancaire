import os
from _ast import If
from setuptools.command.build_ext import if_dl
from test.test_eof import EOFTestCase
os.chdir("C:\Users\saad1\OneDrive\Bureau")



class Personne:
    
    def __init__(self): 
        self.nom = ""
        self.prenom =""
        self.date_de_naissance = ""
        self.cin =""

    def __str__(self):
        return "le code ncompte {} ,le prenom {} ,le nom {},la date nessance {}  ".format(self.cin, self.prenom, self.nom, self.date_de_naissance)
    
    def ajouterPersonne(self):
         try:
             f = open("personne.txt", 'a')
             if(f.tell()):
                 f.write('\n')
             f.write("{:10s}".format(self.cin))
             f.write("{:20s}".format(self.nom))
             f.write("{:30s}".format(self.prenom))
             f.write("{:20s}".format(self.date_de_naissance))
             f.write("\n")
             f.close()
         except IOError:
                 print("erreur d'ouverture de fichier")
    
          
    def get_nom(self):
         return self.nom 
     
    def get_prenom(self):
         return self.prenom 
     
    def get_date_de_naissance(self):
         return self.date_de_naissance
     
    def get_cin(self):
         return self.cin   
     
    def set_nom(self,nom):
         self.nom=nom   
         
    def set_prenom(self,prenom):
         self.prenom=prenom
     
    def set_date_de_naissance(self,date_de_naissance):
         self.date_de_naissance=date_de_naissance  
    
    def set_cin(self,ncompte):
         self.cin=ncompte
         
    def set_info(self,cin,nom,prenom,date_de_naissance):
         self.set_prenom(prenom)
         self.set_nom(nom)
         self.set_date_de_naissance(date_de_naissance)
         self.set_cin(cin)
             
    def afficherPersonne(self,cinp):
         try:
             f = open("personne.txt", 'r')
             while(True):
                 ncompte = f.read(10)
                 if ncompte == '':  # fin de fichier
                     f.close()
                     return 0
                 ncompte = ncompte.replace(" ", "")
                 if ncompte == str(cinp):
                     self.cin = ncompte
                     self.nom= f.read(20).replace(" ", "")
                     self.prenom = f.read(30).replace(" ", "")
                     self.date_de_naissance = f.read(20).replace(" ", "")
                     f.close()
                     return 1
                 else:
                     f.readline()
             return 0
         except IOError:
             print("Erreur d'ouverture de fichier <", NomFichier, ">")   
                 
class Compte :

     def __init__(self): 
         self.solde = 0.0
         self.cin_personne=0
         self.ncompte=0
         
     def set_solde(self,solde):
         self.solde=solde
         
     def set_cin_personne(self,cin_personne):
         self.cin_personne=cin_personne
         
     def set_ncompte(self,ncompte):
         self.ncompte=ncompte
         
     def set_info(self,solde,cin_personne,ncompte):
         self.set_cin_personne(cin_personne)
         self.set_ncompte(ncompte)
         self.set_solde(solde)

     def debiter(self, x):
            s=float(self.solde)
            if s - x < 0:
                return 0
            else :
                s -= x
                self.solde=s
                return 1
        
     def crediter(self, x):
        s=float(self.solde)
        s += x
        self.solde=s
     
     def MiseAjourCompte(self):
        try:
            f=open("compte.txt",'r+')
            while(True):
                cmp=f.read(10)
                if cmp=='':#fin de fichier
                    print("ce compte n'existe pas dans la base")
                    f.close()
                    return 0
                cmp=cmp.replace(" ","")
                if cmp==self.ncompte:
                    f.write("{:10s}".format(str(self.ncompte)))
                    f.write("{:20s}".format(self.cin_personne))
                    f.write("{:20s}".format(str(self.solde)))
                    f.close()
                    return 1
                else:
                    f.readline()
        except IOError:
            print("Erreur d'ouverture de fichier <"">")
            return 0
     
     def __str__(self):
        return "solde {} ,le N compte {} de la personne ncompte : {}".format(self.solde, self.ncompte,self.cin_personne)

     def ajouterCompte(self):
         try:
             f = open("compte.txt", 'a')
             if(f.tell()):
                 f.write('\n')
             f.write("{:10s}".format(str(self.ncompte)))
             f.write("{:20s}".format(str(self.cin_personne)))
             f.write("{:20s}".format(str(self.solde)))
             f.write("\n")
             f.close()
         except IOError:
             print("erreur d'ouverture de fichier")


        
     def afficherCompte(self,nc):
         try:
             f = open("compte.txt", 'r')
             while(True):
                 ncompte = f.read(10)
                 if ncompte == '':  # fin de fichier
                     f.close()
                     return 0
                 ncompte = ncompte.replace(" ", "")
                 if ncompte == str(nc):
                     self.ncompte = ncompte
                     self.cin_personne= f.read(20).replace(" ", "")
                     self.solde = f.read(20).replace(" ", "")
                     f.close()
                     return 1
                 else:
                     f.readline()
             return 0
         except IOError:
             print("Erreur d'ouverture de fichier <", NomFichier, ">")   


#---------------------------
repance = 1;
while(repance != 7):
    print("1-tape 1 pour ajouter un personne.");
    print("2-tape 2 pour ajouter un compte.");
    print("3-tape 3 pour afficher un compte.");
    print("4-tape 4 pour afficher un personne.")
    print("5-tape 5 pour retirer un debit");
    print("6-tape 6 pour ajouter un credie");
    print("7-tape 7 pour quiter");
    repance = int(input());
    if(repance == 1):
         nom = raw_input("donner votre nom  ");
         prenom = raw_input("donner votre prenom");
         date_naissance = raw_input("donner votre date naissance");
         cin = raw_input("donner votre cin");
         p=Personne()
         p.set_info(cin,nom,prenom,date_naissance)
         p.ajouterPersonne()
         
    elif(repance == 2):
         solde =raw_input("donner le solde de cette compte :")
         cin_personne=raw_input("donner le ncompte de personne correspandent :")
         ncompte=raw_input("donner le nemuro de cette compte ")
         c=Compte()
         c.set_info(solde, cin_personne, ncompte)
         c.ajouterCompte()
    elif(repance == 3):
        ncompte=raw_input("donner votre ncompte : ")
        c=Compte()
        if c.afficherCompte(ncompte)==1:
            print(c)
        else :
            print("ce Compte n'est existe pas !")
    elif(repance == 4):
        ncompte=raw_input("donner votre cin : ")
        p=Personne()
        if p.afficherPersonne(ncompte)==1:
            print(p)
        else :
            print("Personne n'est existe pas !")
    elif(repance == 5):
        ncompte=raw_input("donner votre numero  compte : ")
        c=Compte()
        if c.afficherCompte(ncompte)==1:
            deb=raw_input("donner debit a retirer :")
            deb = float(deb)
            if c.debiter(deb) == 1:
                if(c.MiseAjourCompte()==1):
                    print("votre debit a retire")
                else :
                    print("votre debit n'est pas retire")
            else :
                print("votre debit n'est pas retire")
        else :
            print("ce Compte n'est existe pas !")
    elif(repance == 6):
        ncompte=raw_input("donner votre numero  compte : ")
        c=Compte()
        if c.afficherCompte(ncompte)==1:
            crd=raw_input("donner cridite a ajouter :")
            crd= float(crd)
            c.crediter(crd)
            c.MiseAjourCompte()
            print("votre cridite a ajouter ")
        else :
            print("ce compte n'existe pas")
            
    else :
        break
print("c'est la fin de ce programme by!!")

