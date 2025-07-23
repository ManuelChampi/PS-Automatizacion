from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# Configurar Chrome con perfil del instructor o estudiante
options = webdriver.ChromeOptions()
options.add_argument(r'user-data-dir=C:\Users\sailax\chrome_instructor')  # usa el perfil adecuado si es diferente
driver = webdriver.Chrome(options=options)

# Ir directamente al home del estudiante
driver.get("https://teammates-escarabajo-462900.uc.r.appspot.com/web/student/home")

try:
    time.sleep(5)  # Espera a que cargue completamente

    # Hacer clic en el botón "View Responses"
    view_responses_btn = driver.find_element(By.ID, "view-responses-btn-0")
    view_responses_btn.click()
    print("✅ Botón 'View Responses' clickeado correctamente.")

except Exception as e:
    print(f"❌ Error durante la automatización: {e}")

input("Presiona ENTER para cerrar el navegador...")
driver.quit()
