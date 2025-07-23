from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# Configurar Chrome con perfil del instructor
options = webdriver.ChromeOptions()
options.add_argument(r'user-data-dir=C:\Users\sailax\chrome_instructor')  # ruta de tu perfil
driver = webdriver.Chrome(options=options)

# Ir directamente al link de detalles del curso
driver.get("https://teammates-escarabajo-462900.uc.r.appspot.com/web/instructor/courses/details?courseid=IS-2025Semestre_1")

try:
    time.sleep(5)  # Esperar que cargue bien

    # Hacer clic en el botón "Remind Students to Join"
    remind_button = driver.find_element(By.ID, "btn-remind-all")
    remind_button.click()
    print("✅ Botón 'Remind Students to Join' clickeado correctamente.")

except Exception as e:
    print(f"❌ Error durante la automatización: {e}")

input("Presiona ENTER para cerrar el navegador...")
driver.quit()
