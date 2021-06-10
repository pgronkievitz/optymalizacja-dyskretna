## Problem szeregowania
_Gronkiewicz Patryk [@pgronkievitz](https://github.com/pgronkievitz), 
Piotr Krawiec [@finloop](https://github.com/finloop)_

Projekt ten jest przykładową implementacją algorytmu Łomnickiego. Więcej na 
jego temat można znaleźć w pliku `Opracowanie.pdf`, przykładowe rozwiązanie 
znajduje się w `Rozwiązanie.ods`. Natomiast przykłady użycia znajdują się w 
`examples/examples.py`.

<!-- GETTING STARTED -->
## Jak zacząć

Postępuj zgodnie z krokami poniżej.

### Instalacja

1. Sklonuj repozytorum
   ```sh
   git clone https://github.com/pgronkievitz/optymalizacja-dyskretna.git
   ```
2. Zainstaluj wymagane paczki
   ```sh
   pip3 install -r requirements.txt
   ```

## Przykłady użycia

| Maszyna    | Projekt 1 | Projekt 2 | Projekt 3 |
|------------|-----------|-----------|-----------|
| Tokarka    | 4         | 8         | 1         |
| Skrawarka  | 2         | 3         | 7         |
| Anodyzacja | 6         | 2         | 5         |

```python
import numpy as np
from src.lomnicki import lomnicki

# Zadanie przykładowe
dane = np.array([
   [4, 8, 1],
   [2, 3, 7],
   [6, 2, 5]
])
print(dane)
print(lomnicki(dane))
```

<!-- LICENSE -->
## Licencja

Oprogramowanie rozpowszechniane jest na licencji AGPL-3.0. Patrz 
`LICENSE`,aby uzyskać więcej informacji.
