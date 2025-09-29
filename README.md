# BREAST-CANCER-MUTATION-DATA-EXTRACTOR
For this first assignment the goal is to create a python script for the development of a functional routine that extract some data from a breast cancer somatic mutations file named "Breast Cancer (CPTAC GDC, 2025)" from a clinical study reported at the clinicogenomic cancer dataset from cBioPortal and organize it in a tabular format output

# Transformador de Datos de Mutaciones Somáticas

Este repositorio contiene un flujo de trabajo en Python para convertir datos de mutaciones somáticas en cáncer desde un archivo `.maf` crudo a un archivo tabular `.tsv` fácilmente interpretable y visualizable.

---

## 📂 Contenido

- **data_mutations.maf** → Archivo de entrada crudo descargado desde la base de datos clinicogenómicos de cáncer.  
- **mutation_data_transformator.py** → Script de Python funcionalizado para la conversión de los datos.  
- **mutaciones_tabla.tsv** → Ejemplo de archivo convertido a formato `.tsv`.  
- **README.md** → Este archivo de descripción y documentación.  

---

## ⚙️ Requisitos

- **Python**: versión 3.8 o superior.  
- **Paquetes de Python necesarios**:  
  - Ninguno adicional.  
  - El script utiliza únicamente módulos estándar de Python (`csv`, `os`, `sys`), que ya vienen incluidos en la instalación base.  

---

## ▶️ Ejecución del script

1. Coloca el archivo `data_mutations.maf` en la misma carpeta donde está el script `mutation_data_transformator.py`.  
2. Ejecuta en la terminal:
```bash
python mutation_data_transformator.py
```
3. Se generará un archivo llamado mutaciones_tabla.tsv en la misma carpeta.

---

## 📌 Particularidades del código

- Lee un archivo .maf (Mutation Annotation Format) con información cruda de mutaciones somáticas.
- Identifica la cabecera del archivo ignorando líneas de metadatos que comienzan con #.
- Extrae columnas clave y las renombra a una versión más amigable:

  - Columna original (MAF)   →      Columna exportada (TSV)
  - Hugo_Symbol	             →              Gene
  - Chromosome	             →              Chr
  - Start_Position           →           	Start
  - End_Position	           →              End
  - Variant_Classification	 →          Mutation_Class
  - Variant_Type	           →          Mutation_Type
  - HGVSp_Short (preferida) o HGVSp	 →  Protein_Change
  - PolyPhen                 →           	PolyPhen
  - SIFT	                   →              SIFT
  - Tumor_Sample_Barcode	   →             Sample

- Si el archivo de entrada no existe, el script muestra un mensaje de error y se detiene.
- Al finalizar, imprime un resumen con número de filas leídas y escritas, además de las columnas extraídas.

---

## 📊 Contenido del archivo generado (.tsv)

El archivo de salida contiene columnas clave para análisis posteriores:
  - Gene → Nombre del gen mutado.
  - Chr → Cromosoma.
  - Start / End → Posición genómica de la mutación.
  - Mutation_Class → Clasificación de la mutación (ej. missense, nonsense, splice_site).
  - Mutation_Type → Tipo de variante (SNP, INS, DEL).
  - Protein_Change → Cambio aminoacídico reportado (ejemplo: p.G12D).
  - SIFT → Predicción del impacto funcional según SIFT.
  - PolyPhen → Predicción del impacto funcional según PolyPhen.
  - Sample → Identificador de la muestra tumoral.

### Ejemplo de salida (`mutaciones_tabla.tsv`)

| Gene    | Chr | Start     | End       | Mutation_Class    | Mutation_Type | Protein_Change | PolyPhen                   | SIFT             | Sample                                |
|---------|-----|-----------|-----------|------------------|---------------|----------------|----------------------------|------------------|---------------------------------------|
| KIF1B   | 1   | 10360976  | 10360976  | Missense_Mutation | SNP           | p.S1368C       | probably_damaging(0.916)   | tolerated(0.13)  | 94176301-9658-4151-9110-5139de        |
| ZMYND12 | 1   | 42439957  | 42439957  | Missense_Mutation | SNP           | p.D165H        | benign(0.003)              | tolerated(0.11)  | 94176301-9658-4151-9110-5139de        |

---

### 📈 Visualización del archivo generado

El archivo `mutaciones_tabla.tsv` puede abrirse y visualizarse de forma fácil y directa:

- **Excel o LibreOffice**: abrir directamente el archivo y seleccionar el separador de tabulación.

