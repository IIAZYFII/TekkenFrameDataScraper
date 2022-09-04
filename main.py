from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import csv
s = Service("C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(service=s)


driver.get("https://rbnorway-t7.web.app/")


close_button = driver.find_element(By.CSS_SELECTOR, 'button.mat-focus-indicator.mat-button.mat-button-base')
close_button.click()

driver.implicitly_wait(20)
chars = driver.find_element(By.CLASS_NAME,"avatar-container")
character_elems = chars.find_elements(By.TAG_NAME, "a")
links = []
for character_elem in character_elems:
        links.append(character_elem.get_attribute('href'))

for i in range(len(links)):
    if (i >= 8):

        driver.get(links[i])
        driver.implicitly_wait(20)
        character_name  = driver.find_element(By.CLASS_NAME,"title").text
        table = driver.find_element(By.TAG_NAME, "table")
        rows = table.find_elements(By.CSS_SELECTOR, 'tr.mat-row.cdk-row.ng-star-inserted')
        with open(character_name + '.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Command', 'Hit Level', 'Damage', 'Startup', 'Block', 'Hit', 'Counter Hit', 'Notes'])
            print(character_name)
            for row in rows:
                container = row.find_element(By.CLASS_NAME, "move-container")
                command = container.find_element(By.TAG_NAME, "div")
                hit_level = row.find_element(By.CSS_SELECTOR, 'td.mat-cell.cdk-cell.cdk-column-hitLevel.mat-column-hitLevel.ng-star-inserted')
                damage = row.find_element(By.CSS_SELECTOR, 'td.mat-cell.cdk-cell.cdk-column-damage.mat-column-damage.ng-star-inserted')
                startup = row.find_element(By.CSS_SELECTOR,'td.mat-cell.cdk-cell.cdk-column-startup.mat-column-startup.ng-star-inserted')
                block = row.find_element(By.CSS_SELECTOR,'td.mat-cell.cdk-cell.cdk-column-block.mat-column-block.ng-star-inserted')
                hit = row.find_element(By.CSS_SELECTOR,
                                   'td.mat-cell.cdk-cell.cdk-column-hit.mat-column-hit.ng-star-inserted')
                counter_hit = row.find_element(By.CSS_SELECTOR,
                                   'td.mat-cell.cdk-cell.cdk-column-counterHit.mat-column-counterHit.ng-star-inserted')
                notes = row.find_element(By.CSS_SELECTOR,'td.mat-cell.cdk-cell.cdk-column-notes.mat-column-notes.ng-star-inserted')
                writer.writerow([command.text, hit_level.text, damage.text, startup.text, block.text, hit.text,
                             counter_hit.text, notes.text])
                print(command.text, hit_level.text, damage.text, startup.text, block.text, hit.text,
                             counter_hit.text, notes.text)


driver.quit()