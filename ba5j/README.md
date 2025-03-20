# BA5J - Align Two Strings Using Affine Gap Penalties

Este script realiza alineamientos globales entre una secuencia objetivo y varias secuencias query utilizando penalizaciones afines para los huecos y la matriz de sustitución BLOSUM62.

## Requisitos
Instala las dependencias necesarias con:
```
pip install -r requirements.txt
```
## Uso
```
python ba5j.py entrada.fasta salida.fasta
```
Donde:
- `entrada.fasta` es el archivo con las secuencias en formato FASTA.
- `salida.fasta` es el archivo donde se guardarán los alineamientos.

## Salida
- Muestra en pantalla la cantidad de alineamientos y su puntuación.
- Guarda los alineamientos en el archivo de salida en formato FASTA.
- Si hay caracteres inválidos, se notifica.
