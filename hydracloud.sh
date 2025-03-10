#!/bin/bash

cd resources

# Descomprimir paquete app.asar
echo '>> Descomprimiendo app.asar...'
asar e app.asar app.asar.extract

echo '>> Parcheando Hydra...'
cd ../hydracloudpatch
python3 patch.py

# Comprimir paquete app.asar
echo '>> Comprimiendo app.asar modificado...'
cd ../resources
asar pack app.asar.extract app.asar

# Eliminar directorio app.asar.extract
echo '>> Eliminando directorio app.asar.extract...'
rm -rf app.asar.extract

echo '>> FINALIZADO!'