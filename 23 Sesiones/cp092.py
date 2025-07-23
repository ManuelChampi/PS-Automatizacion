from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Configurar Chrome con perfil del instructor
options = webdriver.ChromeOptions()
options.add_argument(r'user-data-dir=C:\Users\sailax\chrome_instructor')  # ruta de tu perfil
driver = webdriver.Chrome(options=options)

# Ir a la página de sesiones del instructor
driver.get("https://teammates-escarabajo-462900.uc.r.appspot.com/web/instructor/sessions")

time.sleep(5)  # Esperar que cargue la tabla

# Buscar el botón Delete correspondiente al primer feedback (ajustable)
delete_button = driver.find_element(By.CSS_SELECTOR, "button.btn-soft-delete-0")
delete_button.click()

print("✅ Se hizo clic en el botón Delete.")

input("Presiona ENTER para cerrar el navegador...")
driver.quit()
