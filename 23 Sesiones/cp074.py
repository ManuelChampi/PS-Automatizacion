from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configurar Chrome con perfil del instructor
options = webdriver.ChromeOptions()
options.add_argument(r'user-data-dir=C:\Users\sailax\chrome_instructor')  # ruta de tu perfil
driver = webdriver.Chrome(options=options)

# Ir a la página de sesiones
driver.get("https://teammates-escarabajo-462900.uc.r.appspot.com/web/instructor/sessions")

try:
    # Esperar y hacer clic en "Add New Feedback Session"
    btn_add_session = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID, "btn-add-session"))
    )
    btn_add_session.click()
    print("✅ Se hizo clic en 'Add New Feedback Session'.")

    # Esperar y hacer clic en "Copy from previous feedback sessions"
    btn_copy_session = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID, "btn-copy-session"))
    )
    btn_copy_session.click()
    print("✅ Se hizo clic en 'Copy from previous feedback sessions'.")

except Exception as e:
    print(f"❌ Error en la ejecución: {e}")

input("Presiona ENTER para cerrar el navegador...")
driver.quit()
