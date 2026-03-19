import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

# Ajusta estos valores
html_file = r"C:\Users\carmijos.ext\Desktop\VSC-Workspace\Automatizacion\testpage.html"
selector = "#botonPrueba"
chromedriver_path = r"C:\chromedriver\chromedriver.exe"  # pon ruta correcta a chromedriver

delay_seconds = 1800  # 30 minutos
delay_test = 10  # para pruebas rápidas, usa 10s y luego cambia a 1800

print("Iniciando navegador...")
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
# options.add_argument("--headless")  # opcional para no mostrar ventana

service = Service(chromedriver_path)

with webdriver.Chrome(service=service, options=options) as driver:
    driver.get("file:///" + html_file.replace("\\", "/"))
    print(f"Página cargada: {html_file}")

    wait_time = delay_test  # para primera prueba
    print(f"Esperando {wait_time} segundos antes de hacer clic...")
    time.sleep(wait_time)

    try:
        boton = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
        )
    except Exception as e:
        raise SystemExit(f"No se encontró el botón {selector}: {e}")

    boton.click()
    print("Clic realizado en el botón")

    # Ver resultado
    status_text = driver.find_element(By.ID, "status").text
    print("Status en la página:", status_text)

    print("Listo. Conservando ventana 5 seg antes de cerrar...")
    time.sleep(5)
