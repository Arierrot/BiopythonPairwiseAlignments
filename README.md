# BiopythonPairwiseAlignments
Se han implementado varios algoritmos de alineamiento utilizando la biblioteca **Biopython**, con el objetivo de dar respuesta a algunos de los problemas de entrenamiento planteados por **Rosalind** Team en el contexto de análisis de secuencias biológicas.

## Descripción

El objetivo de esta práctica es resolver problemas de alineamiento de secuencias biológicas propuestos en **[Rosalind](https://rosalind.info/problems/locations/)**, una plataforma de problemas bioinformáticos. Cada script en este repositorio implementa un método diferente de alineamiento, utilizando distintas penalizaciones y matrices de sustitución.

### Problemas resueltos

Los ejercicios se basan en los problemas de Rosalind, disponibles en los siguientes enlaces:

- **[BA5E](https://rosalind.info/problems/ba5e/)** - Encuentra el alineamiento global con la mayor puntuación.
- **[BA5F](https://rosalind.info/problems/ba5f/)** - Encuentra el alineamiento local con la mayor puntuación.
- **[BA5G](https://rosalind.info/problems/ba5g/)** - Calcula la distancia de edición entre dos secuencias.
- **[BA5J](https://rosalind.info/problems/ba5j/)** - Alinea dos secuencias usando penalizaciones afines para huecos.

Cada uno de estos problemas se ha implementado en un script independiente.

## Requisitos

Antes de ejecutar los scripts, es necesario instalar las dependencias. Se pueden instalar ejecutando:
```
pip install -r requirements.txt
```
## Uso

Cada script toma como entrada un archivo en formato **FASTA** con varias secuencias. La primera secuencia se usa como **target** y las siguientes como **query**.

Para ejecutar un script, utiliza el siguiente comando:
```
python nombre_del_script.py entrada.fasta salida.fasta
```
Por ejemplo, para ejecutar el alineamiento global con `ba5e.py`:
```
python ba5e.py entrada.fasta salida.fasta
```
Donde:
- `entrada.fasta` es el archivo que contiene las secuencias en formato FASTA.
- `salida.fasta` es el archivo donde se guardarán los alineamientos resultantes.

## Salida Esperada

Cada script imprime en pantalla:
- La cantidad de alineamientos encontrados.
- La puntuación del alineamiento.
- Si hay caracteres inválidos en alguna secuencia, se mostrará un aviso.
