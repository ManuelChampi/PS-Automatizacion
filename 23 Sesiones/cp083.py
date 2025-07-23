from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# Configurar Chrome con perfil del instructor
options = webdriver.ChromeOptions()
options.add_argument(r'user-data-dir=C:\Users\sailax\chrome_instructor')  # ruta a tu perfil de Chrome
driver = webdriver.Chrome(options=options)

# Ir directamente al enlace de edición con modo de edición activado
driver.get("https://teammates-escarabajo-462900.uc.r.appspot.com/web/instructor/sessions/edit?courseid=IS-2025Semestre_1&fsname=example&editingMode=true")

try:
    time.sleep(5)  # Esperar carga completa

    # Buscar el botón con texto "Save Changes"
    save_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Save Changes')]")

    if save_button.is_displayed():
        print("✅ El botón 'Save Changes' está presente y visible.")
    else:
        print("⚠️ El botón 'Save Changes' está presente pero no visible.")

except Exception as e:
    print(f"❌ No se encontró el botón 'Save Changes': {e}")

input("Presiona ENTER para cerrar el navegador...")
driver.quit()
