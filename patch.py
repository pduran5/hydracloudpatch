import os
import re

def read_file_content(file_path):
    """Lee el contenido de un archivo y lo devuelve como string"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"Error leyendo {file_path}: {e}")
        return None

def write_file_content(file_path, content):
    """Escribe contenido en un archivo"""
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
    except Exception as e:
        print(f"Error escribiendo {file_path}: {e}")

def get_pattern_replace_pairs():
    """Encuentra todos los pares patternX.txt y replaceX.txt en el directorio actual"""
    pairs = {}
    current_dir = os.getcwd()  # Directorio actual
    patch_dir = os.path.join(current_dir, 'patch')

    # Verifica si la carpeta patch existe
    if not os.path.exists(patch_dir):
        print("La carpeta 'patch' no existe en el directorio actual")
        return {}

    pairs = {}

    for filename in os.listdir(patch_dir):
        if filename.startswith('pattern') and filename.endswith('.txt'):
            number = filename[7:-4]  # Extrae el número entre 'pattern' y '.txt'
            pattern_path = os.path.join(patch_dir, filename)
            replace_path = os.path.join(patch_dir, f'replace{number}.txt')

            if os.path.exists(replace_path):
                pattern_content = read_file_content(pattern_path)
                replace_content = read_file_content(replace_path)
                if pattern_content is not None and replace_content is not None:
                    pairs[pattern_content] = replace_content
    return pairs

def process_js_files(directory, pattern_replace_pairs):
    """Procesa todos los archivos .js en el directorio y subdirectorios"""
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.js'):
                file_path = os.path.join(root, file)
                content = read_file_content(file_path)
                if content is not None:
                    modified = False
                    new_content = content

                    # Aplica cada reemplazo
                    for pattern, replacement in pattern_replace_pairs.items():
                        if pattern in new_content:
                            new_content = new_content.replace(pattern, replacement)
                            modified = True

                    # Si hubo modificaciones, escribimos el archivo
                    if modified:
                        write_file_content(file_path, new_content)
                        print(f"Modificado: {file_path}")
                    else:
                        print(f"Sin cambios: {file_path}")

def main():
    # Directorio actual para patterns/replace y búsqueda de .js
    base_directory = 'app.asar.extract/out'

    # Obtener pares pattern/replace del directorio actual
    pattern_replace_pairs = get_pattern_replace_pairs()

    if not pattern_replace_pairs:
        print("No se encontraron pares pattern/replace válidos en el directorio actual")
        return

    print(f"Encontrados {len(pattern_replace_pairs)} pares de patrones para reemplazar")

    # Procesar archivos .js desde el directorio actual y subdirectorios
    process_js_files(base_directory, pattern_replace_pairs)

    print("Proceso completado")

if __name__ == "__main__":
    main()
