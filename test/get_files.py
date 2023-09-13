import os
import fnmatch

def find_files_by_extensions(directory, extensions):
    """
    Busca todos los archivos con las extensiones dadas en un directorio de forma recursiva.
    
    :param directory: Ruta del directorio donde se iniciará la búsqueda.
    :param extensions: Lista de extensiones de archivo (por ejemplo, ['txt', 'jpg', 'py', etc.]).
    :return: Lista de rutas absolutas de los archivos que coinciden con las extensiones dadas.
    """
    matching_files = []

    # Usamos un bucle for para recorrer todos los elementos del directorio, incluidos subdirectorios
    for root, _, files in os.walk(directory):
        for filename in files:
            for extension in extensions:
                if filename.endswith(f".{extension}"):
                    # Obtenemos la ruta absoluta de cada archivo coincidente y la agregamos a la lista
                    file_path = os.path.abspath(os.path.join(root, filename))
                    matching_files.append(file_path)
                    break  # Salimos del bucle interior para evitar duplicados

    return matching_files

# Ejemplo de uso:
directorios_con_archivos_txt = find_files_by_extensions('/home/rafa/work/kege/Next', ['cpp', 'txt'])
print(directorios_con_archivos_txt)