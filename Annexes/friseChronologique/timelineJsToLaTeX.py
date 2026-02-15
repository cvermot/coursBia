import csv
import requests
import time
import os
import json
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF
from datetime import date

import re
cleanHtmlRe = re.compile('<.*?>')

from PIL import Image
size = 1280, 1280

import locale
locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')

#py -m pip install requests svglib reportlab Image
nbErreurs = 0

def cleanHtml(raw_html):
    cleantext = re.sub(cleanHtmlRe, '', raw_html).replace("#", "").replace("_", "\\_").replace("&amp;","et")#.replace("\"", "\\\" ")
    return cleantext.encode("utf-8").decode("utf-8") #.encode('ascii', 'ignore').decode("utf-8")

def telechargerImage(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    noms = url.split("/")
    nomPropre = noms[-1]
    nomPropre = nomPropre.replace("%", "")
    nomPropre = nomPropre.replace(":", "")
    nomPropre = nomPropre.replace(",", "")
    chemin = 'img/' + nomPropre
    if url == "" or "youtube" in url or ".webm" in url or ".tif" in url:
        return ""
    elif not os.path.exists(chemin):
        print("    Téléchargement infos Wikimedia... " )
        urlMedia = "https://commons.wikimedia.org/wiki/File:"+noms[-1]
        urlWikimedia = "https://commons.wikimedia.org/w/api.php?action=query&titles=File:"+noms[-1]+"&format=json&prop=imageinfo&iiprop=extmetadata"
        reponseUrlWikimedia = requests.get(urlWikimedia, headers=headers)
        if reponseUrlWikimedia.status_code == 200:
            infosWikimedia = json.loads(reponseUrlWikimedia.text)
            infoMedia = infosWikimedia["query"]["pages"]
            auteur = "Inconnu"
            for keys in infoMedia:
                licence = infoMedia[keys]["imageinfo"][0]["extmetadata"]["LicenseShortName"]["value"]
                date = (infoMedia[keys]["imageinfo"][0]["extmetadata"]["DateTime"]["value"].split(" "))[0]
                description = cleanHtml(infoMedia[keys]["imageinfo"][0]["extmetadata"]["ImageDescription"]["value"])
                if "Artist" in infoMedia[keys]["imageinfo"][0]["extmetadata"]:
                    auteur = cleanHtml(infoMedia[keys]["imageinfo"][0]["extmetadata"]["Artist"]["value"])
        else:
            print("    Erreur de téléchargements crédits")
            return ""
        
        print("    Téléchargement illustration... " )
        reponse = requests.get(url, headers=headers)
        
        if reponse.status_code == 429:
            print("    Erreur 429 sur URL " + url + ".")
            global nbErreurs
            nbErreurs = nbErreurs + 1
            #time.sleep(5)
            #reponse = requests.get(url, headers=headers)

        if reponse.status_code == 200:
            with open(chemin, 'wb') as image:
                image.write(reponse.content)
            print("    Fichier enregistré")
            
            if url.split(".")[-1] == "svg":
                cheminPdf = chemin.replace(".svg", ".pdf")
                nomPropre = nomPropre.replace(".svg", ".pdf")
                drawing = svg2rlg(chemin)
                renderPDF.drawToFile(drawing, cheminPdf)
                chemin = cheminPdf
            else :
                try:
                    im = Image.open(chemin)
                    im.thumbnail(size, Image.Resampling.LANCZOS)
                    im.save(chemin, "JPEG")
                except IOError:
                    print ("    Impossible de redimenssionner " + chemin)
            
            print("        Génération biblio pour : " + noms[-1]) 
            #Generation biblio
            with open("biblio.bib", "a", encoding='UTF-8') as biblio:
                biblio.write("@misc{frise:"+nomPropre+",\n")
                biblio.write("author    = {"+auteur.replace(",", " et ")+"},\n")
                biblio.write("title     = {"+description+"},\n")
                biblio.write("year      = "+date.split("-")[0]+",\n")
                biblio.write("url       = {"+urlMedia+"},\n")
                biblio.write("urldate   = {"+date+"},\n")
                biblio.write("note      = {Licence : "+licence+"}\n")
                biblio.write("}\n")
            return chemin
        else:
            print("    Impossible de télécharger l'image. URL : " + url + "\n    Code :  " + str(reponse.status_code))
    return chemin.replace(".svg", ".pdf")

#main
with open("frise.tex", "w", encoding='UTF-8') as friseLaTeX:
    with open('FriseBIA.csv', newline='', encoding='UTF-8') as csvfile:
        frise = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        for row in frise:
            time.sleep(0.1)
            print(row['Year'] + " " + row['Headline'])
            if row['Type'] == "era":
                friseLaTeX.write("\\section{"+row['Headline']+"}\n")
                friseLaTeX.write(row['Text']+"\n")
            elif row['Type'] == "":
                drapeau = telechargerImage(row['Media Thumbnail']);
                image = telechargerImage(row['Media']);
                friseLaTeX.write("\\begin{table}[H]\n")
                friseLaTeX.write("    \\centering\n")
                friseLaTeX.write("    \\begin{tabular}{c l c}\n")
                friseLaTeX.write("        \\begin{minipage}{.075\\textwidth}\n")
                if drapeau != "":
                    friseLaTeX.write("            \\begin{figure}[H]\n")
                    friseLaTeX.write("                \\centering\n")
                    friseLaTeX.write("                \\includegraphics[width=1.0\\linewidth]{Annexes/friseChronologique/"+drapeau+"}\n")
                    friseLaTeX.write("                \\captionsetup{labelformat=empty}\\refDrapeau{"+drapeau.split("/")[-1].replace("Flag_of","Drapeau").replace("_"," ").replace(".pdf","")+"}{frise:"+drapeau.split("/")[-1]+"}\n")
                    friseLaTeX.write("            \\end{figure}\n")
                if row['Group'] == "Les femmes de l'air":
                    friseLaTeX.write("            \n            \\centering\\mdiFemale\n")
                if row['Icone'] != "":
                    listeIcone = row['Icone'].split(",")
                    for icone in listeIcone:
                        friseLaTeX.write("            \n            \\centering"+icone+"\n")
                friseLaTeX.write("        \\end{minipage}\n")
                friseLaTeX.write("    &\n")
                friseLaTeX.write("        \\begin{minipage}{.65\\textwidth}\n")
                dateTexte = row['Year']
                if row['Month'] != "" and row['Day'] != "":
                    dateTmp = date(int(row['Year']),int(row['Month']),int(row['Day']))
                    dateTexte = dateTmp.strftime("%d %B %Y")
                friseLaTeX.write("            \\textbf{"+dateTexte+"} - \\textbf{"+row['Headline']+"}\n")
                friseLaTeX.write("            \n            ")
                friseLaTeX.write(row['Text']+"\n")
                if image != "":
                    friseLaTeX.write("            \\begin{figure}[H]\n")
                    friseLaTeX.write("                \\legende{"+row['Media Caption']+"}{frise:"+image.split("/")[-1]+"}\n")
                    friseLaTeX.write("            \\end{figure}\n")
                friseLaTeX.write("        \\end{minipage}\n")
                friseLaTeX.write("    &\n")
                friseLaTeX.write("        \\begin{minipage}{.275\\textwidth}\n")
                friseLaTeX.write("            \\begin{figure}[H]\n")
                friseLaTeX.write("                \\centering\n")
                if image != "":
                    friseLaTeX.write("                \\includegraphics[width=1.0\\linewidth]{Annexes/friseChronologique/"+image+"}\n")
                else:
                    friseLaTeX.write("                \\includegraphics[width=1.0\\linewidth]{Annexes/friseChronologique/vide.pdf}\n")
                friseLaTeX.write("            \\end{figure}\n")
                friseLaTeX.write("        \\end{minipage}\n")
                #friseLaTeX.write("        \\\\ \\hline\n")
                friseLaTeX.write("    \\end{tabular}\n")
                friseLaTeX.write("\\end{table}\n")
if nbErreurs != 0:
    print ("\nNombre de téléchargements en erreur : " + str(nbErreurs) + ". Relancez le script pour retenter")
else:
    print ("\nFin sans erreur")
