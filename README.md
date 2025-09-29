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
3. Se generará un archivo llamado mutaciones_tabla.tsv en la misma carpeta.

