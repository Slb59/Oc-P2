# Oc-P2 : Analyse de marché pour Books Online

---

![logo](logo/Logo.png)

## Objectif
Ce programme est un exercice proposé par [OpenClassRooms](https://openclassrooms.com/fr/) dans le cadre de la formation :
Développeur d'applications Python
Il s'agit d'une version bêta d'un système de suivi de prix des livres en ligne.
Cette version scrute le site [Books to Scrape](http://books.toscrape.com/) un revendeur de livres en ligne, 
pour en extraire les données sur les livres

## Fonctionnement
Les informations sont extraites dans des fichiers CSV (un fichier par catégorie) dans le répertoire ''_csv_'',
les images (couverture des livres) sont stockées dans le répertoire ''_img_''

---

## Installation
```bash
# Creer l'environnement virtuel
python -m venv env
source env/bin/activate

# cloner le projet
git clone https://github.com/Slb59/Oc-P2.git
cd Oc-P2

# installer les dépendances
pip install -r requirements.txt

# executer le programme
python books_to_scrape.py
```
---

## Utilisation

Le programme peut s'executer sans paramètre
??? ou ajouter les directories de sortie ???

```shell
python books_to_scrape.py
```
---

## License



