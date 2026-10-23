from pathlib import Path

#Busca datos/productos.txt a partir de donde está este archivo, así funciona desde cualquier carpeta (Terminal o boton de VS Code

carpeta_proyecto = Path(__file__).parent.parent
archivo = carpeta_proyecto / "datos" / "productos.txt"
lineas = archivo.read_text(encoding="utf-8").splitlines()

print("=== Inventario Tienda Don Pedro ===")

for productos in lineas[2:]:
    print("-", productos)


contador_productos = 0
total = 0

for linea in lineas[2:]:
    if "$" in linea:
        valor=linea.split("$")[1].strip()
        precio = valor.replace(".","")
        total += int(precio)
    contador_productos += 1

print(f"\nTotal de productos: {contador_productos}")
print(f"Total valor del inventario: ${total}")


