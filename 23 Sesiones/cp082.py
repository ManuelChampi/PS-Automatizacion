from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# Configurar Chrome con perfil del instructor
options = webdriver.ChromeOptions()
options.add_argument(r'user-data-dir=C:\Users\sailax\chrome_instructor')  # ruta a tu perfil de Chrome
driver = webdriver.Chrome(options=options)

# Ir directamente al link de vista previa del instructor
driver.get("https://teammates-escarabajo-462900.uc.r.appspot.com/web/sessions/result?courseid=IS-2025Semestre_1&fsname=Sesi%C3%B3n%20de%20Feedback&previewas=mariochampi12@gmail.com")

try:
    time.sleep(5)  # Esperar que cargue bien la página

    # Verificar si el mensaje Note está presente
    note_alert = driver.find_element(By.CSS_SELECTOR, "div.alert.alert-primary")

    if "Questions without responses" in note_alert.text:
        print("✅ El mensaje 'Note: Questions without responses...' está presente.")
    else:
        print("⚠️ El div existe, pero el texto no coincide.")

except Exception as e:
    print(f"❌ No se encontró el mensaje esperado: {e}")

input("Presiona ENTER para cerrar el navegador...")
driver.quit()
