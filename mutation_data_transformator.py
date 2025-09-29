import csv
import os
import sys

def convertir_maf_a_tsv():
    entrada = "data_mutations.maf"
    salida = "mutaciones_tabla.tsv"

    # Mapa de columnas originales con claves que se extraen del MAF y nombres que queremos en el TSV
    desired_cols = {
        "Hugo_Symbol": "Gene",
        "Chromosome": "Chr",
        "Start_Position": "Start",
        "End_Position": "End",
        "Variant_Classification": "Mutation_Class",
        "Variant_Type": "Mutation_Type",
        "HGVSp_Short": "Protein_Change",       # preferimos HGVSp_Short
        "HGVSp": "Protein_Change_alt",         # si no existe HGVSp_Short, usamos HGVSp como respaldo
        "PolyPhen": "PolyPhen",
        "SIFT": "SIFT",
        "Tumor_Sample_Barcode": "Sample"
    }

    # Verificar existencia del archivo
    if not os.path.exists(entrada):
        print(f"Error: no se encontró el archivo '{entrada}'. Ponlo en la misma carpeta que este script.")
        sys.exit(1)

    # Abrir entrada y salida
    # Usamos errors='replace' para evitar que caracteres raros rompan la lectura
    with open(entrada, "r", encoding="utf-8", errors="replace") as maf_file, \
         open(salida, "w", encoding="utf-8", newline="") as tsv_file:

        reader = csv.reader(maf_file, delimiter="\t")
        writer = csv.writer(tsv_file, delimiter="\t")

        # 1) Encontrar la primera línea no-comentario
        header = None
        for row in reader:
            if not row:
                continue
            first_cell = row[0].strip()
            if first_cell.startswith("#"):
                # línea de metadatos; la saltamos
                continue
            # Esta es la fila de cabecera del MAF
            header = [col.strip() for col in row]
            break

        if header is None:
            print("No se encontró una línea de encabezado en el archivo MAF. ¿El archivo está corrupto?")
            sys.exit(1)

        # Mapa de nombre de columna -> índice
        header_index = {col: idx for idx, col in enumerate(header)}

        # Decidir columnas finales a escribir: preferimos HGVSp_Short; si no existe usamos HGVSp
        output_cols = []
        # guardamos la lista de claves originales que vamos a extraer (en ese orden)
        keys_to_extract = []
        # Evitamos duplicar "Protein_Change" si ambas claves existen
        used_protein_col = False

        for orig_col, out_name in desired_cols.items():
            # if orig_col is 'HGVSp' but HGVSp_Short exists, skip HGVSp as fallback
            if orig_col == "HGVSp":
                if "HGVSp_Short" in header_index:
                    continue  # ya tendremos HGVSp_Short
            if orig_col in header_index:
                # Si la salida ya incluye "Protein_Change" (por HGVSp_Short), y orig_col maps también a eso, evitamos duplicado
                if out_name == "Protein_Change" and used_protein_col:
                    continue
                output_cols.append(out_name)
                keys_to_extract.append(orig_col)
                if out_name == "Protein_Change":
                    used_protein_col = True

        # Si ninguna de las columnas deseadas existe, avisar y salir
        if not keys_to_extract:
            print("Ninguna de las columnas esperadas se encontró en el MAF.")
            print("Columnas disponibles (primeras 30):", header[:30])
            sys.exit(1)

        # Escribir cabecera del TSV (nombres amigables)
        writer.writerow(output_cols)

        # 2) Procesar filas restantes: cada row del reader corresponde a una mutación
        filas_leidas = 0
        filas_escritas = 0
        for row in reader:
            # Saltar filas vacías
            if not row:
                continue
            filas_leidas += 1

            # Construir salida consultando índices; si faltan datos, dejamos campo vacío
            out_row = []
            for key in keys_to_extract:
                idx = header_index.get(key)
                if idx is None or idx >= len(row):
                    out_row.append("")
                else:
                    out_row.append(row[idx].strip())
            writer.writerow(out_row)
            filas_escritas += 1

    # Resumen
    print("Conversión completada.")
    print(f"   Archivo de entrada: {entrada}")
    print(f"   Archivo generado:   {salida}")
    print(f"   Filas leídas (aprox): {filas_leidas}")
    print(f"   Filas escritas:       {filas_escritas}")
    print(f"   Columnas extraídas (en orden): {output_cols}")

if __name__ == "__main__":
    convertir_maf_a_tsv()