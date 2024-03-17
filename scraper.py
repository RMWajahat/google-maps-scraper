import xlsxwriter
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from webdriver_manager.chrome import ChromeDriverManager

query=""
def CreateExcel(dataMatrix):
    workbook = xlsxwriter.Workbook(f"{query}.xlsx")
    worksheet = workbook.add_worksheet()
    worksheet.write(0, 0, "Name")
    worksheet.write(0, 1, "Rating")
    worksheet.write(0, 2, "Reviews")
    worksheet.write(0, 3, "Phone no")
    worksheet.write(0, 4, "Link")
    worksheet.write(0, 5, "Address")
    for i in range(len(dataMatrix)):
        for j in range(len(dataMatrix[0])):
            worksheet.write(i + 1, j, str(dataMatrix[i][j]))

    workbook.close()


def get_details(driver,comp, wait):
    wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "bfIbhd")))
    details = driver.find_elements(By.CLASS_NAME, "bfIbhd")
    name = comp.find_elements(By.CLASS_NAME, "rgnuSb")[0].text
    try:
        rating = comp.find_elements(By.CLASS_NAME, "rGaJuf")[0].text
    except IndexError:
        rating = "None"
    try:
        reviews = comp.find_elements(By.CLASS_NAME, "leIgTe")[0].text
    except IndexError:
        reviews = "None"
    try:
        phone_no = details[0].find_elements(By.CLASS_NAME, "eigqqc")[0].text
    except IndexError:
        phone_no = "None"
    try:
        link = details[0].find_elements(By.CLASS_NAME, "Gx8NHe")[0].text
    except IndexError:
        link = "None"
    try:
        addr = details[0].find_elements(By.CLASS_NAME, "hgRN0")[0].text
    except IndexError:
        addr = "None"


    return [name, rating, reviews, phone_no, link, addr]


def parseInfo(driver,wait):
    dataMatrix = []
    companies = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "DVBRsc")))
    for comp in companies:
        comp.click()
        print(f"getting details of page {page_no}...")
        data = get_details(driver,comp, wait)
        dataMatrix.append(data)

    return dataMatrix


if __name__ == '__main__': 
    # -------------- setup driver ------------
    url = "https://www.google.com/localservices/prolist?g2lbs=ANTchaPs6k7V2N3dSAjw2bqnw-Ur5HHQ1kMxoX5TkSzQOkRoviax6FINJTtDMn-B_r9OQlmFm838w-lf48qWfMHgZ2Kl-TCKiRsRF7P4ulNLEcknlZKRUWFs-2HusUdoFyU1aj95Q4BF&hl=en-IN&gl=in&cs=1&ssta=1&oq=&src=2&sa=X&scp=CgASABoAKgA%3D&q=&ved=2ahUKEwi719zgtOyBAxVF4Y4KHecABb0QjdcJegQIABAF&slp=MgBAAVIECAIgAIgBAJoBBgoCFxkQAA%3D%3D"
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)
    wait = WebDriverWait(driver, timeout=15)
    # -----------------------------------------


    query = input("Search query : ")
    search_bar = driver.find_element(By.XPATH, '//*[@id="qjZKOb"]').send_keys(query+Keys.ENTER)
    print("showing results for query")
    page_no = 0
    dataMatrix = []
    endreached = False
    while not endreached:
        try:
            wait.until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="yDmH0d"]')))
            print("on page -", page_no)
            button = driver.find_element(By.XPATH, '//[@id="yDmH0d"]//[text()[contains(.,"Next >")]]') 
            dataMatrix.extend(parseInfo(driver, wait, page_no))
            button.click()
            page_no += 1
        except:
            dataMatrix.extend(parseInfo(driver, wait))
            print("-end-")
            endreached = True

    print("creating Data Set ...")
    CreateExcel(dataMatrix)
    print(f"[JOB Completed] {query}.xlxs file has been created!")
    driver.quit()
    