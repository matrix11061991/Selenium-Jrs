from selenium import webdriver

# Ouvrez un navigateur web
driver = webdriver.Firefox()

# Naviguez vers une page web
driver.get("http://www.example.com")

# Cliquez sur un lien
link = driver.find_element_by_link_text("Click here")
link.click()

# Fermez le navigateur
driver.quit()
