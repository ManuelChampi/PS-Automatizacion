from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Configurar Chrome con perfil del instructor
options = webdriver.ChromeOptions()
options.add_argument(r'user-data-dir=C:\Users\sailax\chrome_instructor')  # ruta de tu perfil
driver = webdriver.Chrome(options=options)

# Ir directamente al link del reporte
driver.get("https://teammates-escarabajo-462900.uc.r.appspot.com/web/instructor/sessions/report?courseid=IS-2025Semestre_1&fsname=Sesi%C3%B3n%20de%20Feedback")

time.sleep(5)  # Esperar a que cargue completamente

# Verificar que el contenido de la fecha sea "Not applicable"
result_visible_from = driver.find_element(By.XPATH, '//p[contains(@class, "form-control-static")]').text

if result_visible_from.strip() == "Not applicable":
    print("✅ El campo 'Result visible from' muestra: Not applicable")
else:
    print(f"⚠️ Valor inesperado en 'Result visible from': {result_visible_from}")

input("Presiona ENTER para cerrar el navegador...")
driver.quit()
