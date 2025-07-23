from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configurar Chrome con perfil del instructor
options = webdriver.ChromeOptions()
options.add_argument(r'user-data-dir=C:\Users\sailax\chrome_instructor')  # ruta de tu perfil
driver = webdriver.Chrome(options=options)

# Ir directamente al enlace de edición
driver.get("https://teammates-escarabajo-462900.uc.r.appspot.com/web/instructor/sessions/edit?courseid=IS-2025Semestre_1&fsname=example&editingMode=true")

try:
    wait = WebDriverWait(driver, 10)

    # Hacer clic en el botón "Edit"
    edit_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Edit')]")))
    edit_btn.click()
    print("✅ Se hizo clic en el botón 'Edit'.")

    # Esperar un breve momento para que cargue la interfaz de edición
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(., 'Cancel')]")))

    # Hacer clic en el botón "Cancel"
    cancel_btn = driver.find_element(By.XPATH, "//button[contains(., 'Cancel')]")
    cancel_btn.click()
    print("✅ Se hizo clic en el botón 'Cancel'.")

except Exception as e:
    print(f"❌ Ocurrió un error: {e}")

input("Presiona ENTER para cerrar el navegador...")
driver.quit()
