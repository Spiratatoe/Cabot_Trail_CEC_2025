# Introduction
Bienvenue au concours de programmation CEC 2025 ! Tout ce dont vous avez besoin se trouve dans ce Github, et nous vous recommandons de suivre les étapes suivantes pour commencer :

1. Lisez le reste de ce README.md
2. Lisez le tutoriel lié à githubHowToUseGithubDesktop.txt
3. Lisez le tutoriel lié à githubHowToFork.txt
4. Débloquer ce repo
5. Clonez votre repo forké localement sur votre machine
6. Commencez à coder !

   
# Obtenir de l'aide
Veuillez suivre les étapes suivantes si vous avez besoin d'aide :

1. Consultez la documentation incluse pour les questions de logistique et de notation
2. Consultez le dossier du concours de programmation pour les questions relatives au concours
3. Consultez le discord pour les questions auxquelles vous avez déjà répondu
4. Si vous avez fait tout cela, demandez de l'aide aux directeurs. Si nous pouvons répondre à votre question, elle sera postée sur le discord en anglais et en français.
   
# Notes importantes
Dans votre README.md, veuillez spécifier :

- Comment exécuter votre code
- Le langage et la version que votre code utilise (ie. Python 3.11)
- Une liste des paquets requis (i.e. Pandas, NumPy), avec la version si nécessaire (ie. pytorch==2.1.116)
- Si nécessaire, le système d'exploitation sur lequel votre code doit être exécuté Toute spécification de ce type non incluse dans votre README ne peut être considérée comme étant sur la (les) machine(s) des directeurs. 
machine(s) des administrateurs.

# Fichiers d'information
Les fichiers suivants fournissent toutes les informations relatives au concours. 
Il s'agit des fichiers suivants
- Le document de cas
- la présentation
- Exemple de production
- Info GitHub

# Test
Votre code sera testé en comparant les résultats de votre algorythme aux résultats corrects. Un dossier (auquel seuls les directeurs ont accès) intitulé « CEC_test » contiendra un certain nombre d'images correspondant à oui ou non. Le format de fichier de ces images sera le png, le nom de chaque image étant « test_xxx.png ». Dans ce cas, x représente le nombre de fichiers testés, comme dans les répertoires « oui » et « non ». 

Les résultats seront comparés aux résultats corrects dans Excel. Il est nécessaire que les concurrents produisent leurs résultats dans un fichier csv, xlsx, ou google sheet (ou similaire). Bien que d'autres interfaces utilisateur soient encouragées, un fichier .csv ou quelque chose de similaire pour sortir les résultats bruts est nécessaire à des fins de test ! Vous pouvez consulter l'exemple de sortie dans le dossier info pour plus de détails à ce sujet !

# Informations potentiellement utiles :
Nous vous avons donné accès aux images via le lien OneDrive ici : 
https://dalu-my.sharepoint.com/:f:/g/personal/or942416_dal_ca/EnQWMWAfUMZFvSOX0s12eyIBUcl52LuIB1posYqPujOtzw?e=CSkuKl

Nous vous suggérons d'enregistrer le dossier via un fichier zip et de le décompresser localement sur votre ordinateur. En moyenne, cette méthode prend environ 20 minutes (en supposant un débit de ~400KB/s). Vous pouvez essayer de synchroniser le dossier OneDrive, mais nous trouvons que cela prend plus de temps pour télécharger les fichiers.

## Récupérer l'ensemble de données
Voici un exemple de code qui accède à ce dossier et qui s'exécute en utilisant le répertoire racine.

``ruby
import os
from os import path

dataset_dir = r"/Users/orionwiersma/Documents/CEC_2025 »

# Initialiser les listes pour contenir les données
image_paths = []
targets = []

total_images = 0

# Carte pour les étiquettes des cibles
label_map = {'no':0, 'yes':1}

for subdir in listdir(dataset_dir) :
  subdir_path = path.join(dataset_dir, subdir)
  if path.isdir(subdir_path) :
    subdir_path_list = listdir(subdir_path)
    for image in subdir_path_list :
      image_paths.append(path.join(subdir_path, image))
      targets.append(label_map[subdir])
    total_images += len(subdir_path_list)
    print(f « Nombre d'images dans le répertoire “{subdir}” : {len(subdir_path_list)}")
print(f'Nombre total d'images : {total_images}')
```
Cela devrait donner quelque chose comme ceci :
```
Nombre d'images dans le répertoire 'no' : 9546
Nombre d'images dans le répertoire 'yes' : 9828
Nombre total d'images : 19374
```
## Vérification des chemins d'accès aux fichiers
Vous pouvez également vérifier les chemins d'accès aux fichiers de vos images :
``Ruby
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'image_path' : image_paths,
    'target' : targets
}, index=np.arange(0, total_images))

print(df.head())
```

Ce qui devrait donner quelque chose comme ceci :
```
                                          image_path target
0 /Users/orionwiersma/Documents/augmented/no/no_...       0
1 /Users/orionwiersma/Documents/augmented/no/no_...       0
2 /Users/orionwiersma/Documents/augmentés/no/no_...       0
3 /Users/orionwiersma/Documents/augmentés/no/no_...       0
4 /Users/orionwiersma/Documents/augmentés/no/no_...       0
```
