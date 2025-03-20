# BA5G - Compute the Edit Distance Between Two Strings

Este script calcula la distancia de edición entre una secuencia objetivo y varias secuencias query utilizando penalizaciones por coincidencias, desajustes e inserciones/eliminaciones.

## Requisitos
Instala las dependencias necesarias con:

pip install -r requirements.txt

## Uso

python ba5g.py entrada.fasta salida.fasta

Donde:
- `entrada.fasta` es el archivo con las secuencias en formato FASTA.
- `salida.fasta` es el archivo donde se guardarán los alineamientos.

## Salida
- Muestra en pantalla la distancia de edición entre las secuencias y el número de alineamientos posibles.
- Guarda los alineamientos en el archivo de salida en formato FASTA.
- Si hay caracteres inválidos, se notifica.