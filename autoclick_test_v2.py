import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

# Ajusta estos valores
url = "https://xxx"
selector = "#btnrefrescar"
chromedriver_path = r"C:\chromedriver\chromedriver.exe"  # pon ruta correcta a chromedriver

delay_seconds = 1800  # 30 minutos
delay_test = 10  # para pruebas rápidas, usa 10s y luego cambia a 1800

print("Iniciando navegador (versión 2)...")
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
# options.add_argument("--headless")  # opcional para ejecución sin ventana

service = Service(chromedriver_path)

with webdriver.Chrome(service=service, options=options) as driver:
    print(f"Navegando a: {url}")
    driver.get(url)

    print(f"Esperando {delay_test} segundos antes de hacer clic...")
    time.sleep(delay_test)

    try:
        boton = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
        )
    except Exception as e:
        raise SystemExit(f"No se encontró el botón {selector} en {url}: {e}")

    boton.click()
    print("Clic realizado en el botón")

    # espera un poco para ver cambios en la página, ajustar según necesidad
    time.sleep(5)

    print("Listo. Conservando ventana 5 seg antes de cerrar...")
    time.sleep(5)
