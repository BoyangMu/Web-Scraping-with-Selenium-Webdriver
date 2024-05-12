from selenium import webdriver # allow launching browser
from selenium.webdriver.common.by import By # allow search with parameters
from selenium.webdriver.support.ui import WebDriverWait # allow waiting for page to load
from selenium.webdriver.support import expected_conditions as EC # determine whether the web page has loaded
from selenium.common.exceptions import TimeoutException # handling timeout situation

import pandas as pd


driver = webdriver.Chrome()
chromedriver_path = '/Users/stevenmu/Downloads/chromedriver-mac-arm64/chromedriver' # Change this to your own chromedriver path!
def create_webdriver():
 return webdriver.Chrome()

# Open the website
driver.get("https://github.com/collections/machine-learning")

projects = driver.find_elements("xpath", "//h1[@class='h3 lh-condensed']")

# Extract information for each project
project_list = {}
for proj in projects:
 proj_name = proj.text # Project name
 proj_url = proj.find_elements("xpath", "a")[0].get_attribute('href') # Project URL
 project_list[proj_name] = proj_url

 # Close connection
driver.quit()

# Extracting data
project_df = pd.DataFrame.from_dict(project_list, orient = 'index')
# Manipulate the table
project_df['project_name'] = project_df.index
project_df.columns = ['project_url', 'project_name']
project_df = project_df.reset_index(drop=True)

# Export project dataframe to CSV
project_df.to_csv('project_list.csv')