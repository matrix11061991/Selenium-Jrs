from selenium import webdriver
# Ouvrir un navigateur
driver = webdriver.Firefox()
# Naviguer jusqu'à la page Google
driver.get("http://www.google.com")
# Trouver le champ de recherche sur la page
search_field = driver.find_element_by_name("q")
# Entrer "Selenium" dans le champ de recherche
search_field.send_keys("Selenium")
# Soumettre le formulaire de recherche
search_field.submit()
# Fermer le navigateur
driver.quit()
