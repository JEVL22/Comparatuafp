import pandas as pd

# Ruta del Excel
file_path = "AFP Comparador VF.xlsx"

# Leer hoja completa
df = pd.read_excel(file_path, sheet_name="Fondo 3", header=None)

# ========================
# SOLO TABLA: Porcentajes (Y:AE)
# ========================
porcentajes = df.iloc[31:, 25:32]  # desde fila 32 (índice 31), columnas Y (24) hasta AE (30)
porcentajes.columns = ["Fecha", "Habitat", "Integra", "Prima", "Profuturo", "Comparativo" , "Promedios AFPs"]
porcentajes = porcentajes.dropna(subset=["Fecha"])

# Exportar solo porcentajes
porcentajes.to_csv("fondo3_porcentajes.csv", index=False)

print("✅ Archivo exportado: fondo3_porcentajes.csv")
print(porcentajes.head())
