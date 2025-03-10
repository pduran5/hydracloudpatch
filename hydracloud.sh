#!/bin/bash

# Descomprimir paquete app.asar
echo '>> Descomprimiendo app.asar...'
asar e app.asar app.asar.extract

echo '>> Parcheando Hydra...'
python3 patch.py

# Comprimir paquete app.asar
echo '>> Comprimiendo app.asar modificado...'
asar pack app.asar.extract app.asar

# Eliminar directorio app.asar.extract
echo '>> Eliminando directorio app.asar.extract...'
rm -rf app.asar.extract

echo '>> FINALIZADO!'