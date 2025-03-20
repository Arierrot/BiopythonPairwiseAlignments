# BA5F - Find a Highest-Scoring Local Alignment of Two Strings

Este script encuentra el alineamiento local con la puntuación más alta entre una secuencia objetivo y varias secuencias query utilizando la matriz de sustitución PAM250.

## Requisitos
Instala las dependencias necesarias con:

pip install -r requirements.txt

## Uso

python ba5f.py entrada.fasta salida.fasta

Donde:
- `entrada.fasta` es el archivo con las secuencias en formato FASTA.
- `salida.fasta` es el archivo donde se guardarán los alineamientos.

## Salida
- Muestra en pantalla la cantidad de alineamientos y su puntuación.
- Guarda los alineamientos en el archivo de salida en formato FASTA.
- Si hay caracteres inválidos, se notifica.