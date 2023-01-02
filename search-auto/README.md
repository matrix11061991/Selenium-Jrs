# Selenium pour ouvrir un navigateur
Un exemple de script Python qui utilise Selenium pour ouvrir un navigateur, naviguer sur la page Google et effectuer une recherche sur le mot-clé "Selenium":
```python
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
```
Ce script ouvrira Firefox, naviguera jusqu'à la page Google, entrera "Selenium" dans le champ de recherche et soumettra le formulaire de recherche. 
Ensuite, il fermera le navigateur.
