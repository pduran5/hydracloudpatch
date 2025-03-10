# Hydra Launcher Cloud Patch
Programa para parchear Hydra Launcher y añadir funciones de guardado de partidas, trofeos y configuraciones de juegos en la nube (p.ej. Google Drive).

- Abrir `wsl --cd %localappdata%\Programs\Hydra`
- Instalar asar (sólo la 1a vez): `sudo snap install asar`
- Ejecutar:
```
git clone https://github.com/pduran5/hydracloudpatch
sh ./hydracloudpatch/hydracloud.sh
```

# Configurar guardado de partidas en Google Drive
- Descargar [rclone](https://rclone.org/downloads/) y descomprimir `rclone.exe` en `C:\Windows`
- Ejecutar `%localappdata%\Programs\Hydra\resources\ludusavi\ludusavi.exe`
  - Cuando pida actualizar dar a Cancel
  - Ir a OTHER y en el apartado de Cloud seleccionar en Remote Google Drive y logarse en la web que abre
  - Cerrar ludusavi