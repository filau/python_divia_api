# «&nbsp;API&nbsp;» Divia&nbsp;—&nbsp;Python

Ce module servant  d’«&nbsp;API&nbsp;» vous permet d’accéder aux horaires des prochains bus et tram du réseau dijonnais *Divia*, en temps réel, grâce au service *TOTEM*, et ce directement depuis un script Python&nbsp;!  
Cette bibliothèque est très largement inspirée (aussi bien sur le principe que dans la logique et les techniques utilisées) de [**divia-api** par **@gauthier-th**](https://github.com/gauthier-th/divia-api) (en JavaScript).

## Démo

Une démo de l’API est disponible en cliquant ici&nbsp;: [Démo](https://pda.firminlaunay.me/) (est c’est aussi [open-source](https://github.com/filau/pda_demo)&nbsp;!)

## Installation

Cette bibliothèque est disponible pour Python 3.6 et versions postérieures.  
  
* Depuis [PyPI](https://pypi.org), avec [pip](https://pypi.org/project/pip/)&nbsp;:
```
$  pip install divia-api
```

* Manuellement, dans un dossier où vous avez décompressé [la dernière version](https://github.com/filau/python_divia_api/releases/latest) du module&nbsp;:
```
$  python setup.py install
```

## Exemple d’utilisation

```python
from divia_api import DiviaAPI

api = DiviaAPI()

line = api.find_line("T2", 'R')  # Récupération de la ligne 2 du tram, dans la direction « R » (« A » étant la valeur par défaut).
line = api.get_line("185")  # Récupération de la ligne par son identifiant unique (ici le 185, qui correspond à la ligne 2 du tram, dans la direction « R ».

stop = line.find_stop("Darcy")  # Récupération de l’arrêt « Darcy » pour cette ligne.
stop = line.get_stop("1494")  # Récupération de l’arrêt « Darcy » pour cette ligne, à partir de son identifiant unique.

stop = api.find_stop("T2", "Darcy", 'R')  # Les étapes précédentes (récupération de la ligne et de l’arrêt) peuvent également être combinées.

totem_result = stop.totem()  # Interrogation du service TOTEM et récupération des prochains horaires. C’est une liste d’objets « datetime.datetime » qui est retournée par la fonction.

print(totem_result)  # Affichage du résultat.
```

## __________

*Divia* est une marque déposée de *Keolis Dijon*. Nous ne sommes en aucun cas affiliés à *Keolis* ou à ses filiales et succursales.  
  
Cette bibliothèque est ditribuée sous la [License publique générale GNU amoindrie, version 3](https://www.gnu.org/licenses/lgpl-3.0.fr.html).  
© 2021, Firmin Launay ([hey@firminlaunay.me](mailto:hey@firminlaunay.me))
