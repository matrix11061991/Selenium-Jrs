from selenium import webdriver

# Ouvre le navigateur Chrome
driver = webdriver.Chrome()

# Ouvre la page web
driver.get('http://www.example.com')

# Clique sur le bouton
button = driver.find_element_by_id('button')
button.click()

# Affiche le contenu de la page
print(driver.page_source)

# Ferme le navigateur
driver.quit()
