# Automatización: clic en página web después de 30 min

## 1) Archivo de prueba
- `testpage.html` con un botón `#botonPrueba` y un `div#status`.

## 2) Script de prueba
- `autoclick_test.py` utiliza Selenium para abrir el HTML local y clicar el botón.
- Para pruebas rápidas, `delay_test = 10` segundos.
- Para producción, cambia `delay_test = 1800` (30 minutos).

## 3) Requisitos
- Python 3.x
- Selenium: `pip install selenium`
- Chrome + ChromeDriver (mismo Chrome ver.)
- Ajustar `chromedriver_path` en el script.

## 4) Ejecución básica
1. Abrir PowerShell en `K:` o `C:`.
2. `cd "C:\Users\carmijos.ext\Desktop\VSC-Workspace\Automatizacion"`
3. `python autoclick_test.py`

## 5) Pasos siguientes para suspender/activar
- Configurar tarea de Windows Task Scheduler con "Wake the computer to run this task".
- Ejecuta el script desde la tarea 30 min después.
- Suspender equipo manual con `rundll32.exe powrprof.dll,SetSuspendState 0,1,0`.
