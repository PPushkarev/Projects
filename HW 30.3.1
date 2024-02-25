import pytest
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# Фикстура для создания и закрытия драйвера
@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Chrome()
    # Устанавливаем размер окна браузера
    driver.set_window_size(1200, 800)
    # Переходим на страницу авторизации
    driver.get('https://petfriends.skillfactory.ru/login')

    yield driver

    driver.quit()


# Тест для проверки отображения списка питомцев
def test_show_all_pets(driver):
    try:
        # Вводим email
        driver.find_element(By.ID, 'email').send_keys('peternsk@gmail.com')
        # Вводим пароль
        driver.find_element(By.ID, 'pass').send_keys('455000')
        # Нажимаем на кнопку входа в аккаунт
        driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        # Кликаем по ссылке "Мои питомцы"
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[contains(@class, "nav-link") and contains(@href, "/my_pets")]'))
        )
        element.click()


        # Находим все строки таблицы с питомцами
        rows = driver.find_elements(By.XPATH, "//tbody/tr")

        # Подсчитываем количество строк
        row_count = len(rows)

        # Находим элемент с текстом о питомцах
        pet_count_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
                                              "//div[contains(@class, 'col-sm-4') and contains(@class, 'left')]/h2[contains(text(), 'Peternsk')]/following-sibling::text()[1]/.."))
        )

        # Получаем текст элемента
        pet_count_text = pet_count_element.text.strip()

        # Извлекаем число  питомцев из текста
        pet_count = re.findall(r'\d+', pet_count_text)[0]

        #Локаторы

        images = driver.find_elements(By.CSS_SELECTOR, 'tr th img')
        names = driver.find_elements(By.XPATH, '//tbody/tr/td[1]')
        breeds = driver.find_elements(By.CSS_SELECTOR, 'td:nth-of-type(2)')
        ages = driver.find_elements (By.XPATH, '//tbody/tr/td[3]')


        # Получаем список имен питомцев для сравнения уникальности
        pet_names = [name.text for name in names]


        # Тест 1 Присутствуют все Питомцы
        try:
            element_present = EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr"))
            WebDriverWait(driver, 10).until(element_present)
            rows = driver.find_elements(By.XPATH, "//tbody/tr")
            row_count = len(rows)
            assert row_count == int(pet_count), "Присутствуют не все питомцы"
            print("Тест 1 Присутствие всех питомцы пройден успешно")

        except Exception as e:
            print("Произошла ошибка при выполнении теста 1:", e)


        # Тест 2 Сравниваем количество фотографий с атрибутом src и количество питомцев
        try:
            # Явное ожидание, чтобы дождаться загрузки всех изображений
            WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tr th img[src]')))

            # Считаем количество изображений с непустым атрибутом src
            pets_with_photo_count = sum(1 for img in images if img.get_attribute('src'))

            # Проверяем, что количество питомцев с фото хотя бы половина от общего количества питомцев
            assert pets_with_photo_count >= int(pet_count) / 2, "Хотя бы у половины питомцев должно быть фото"

            print("Тест 2 наличия фотографий у питомцев пройден успешно")

        except Exception as e:
            print("Произошла ошибка при выполнении теста 2:", e)



        # Тест 3 Проверяем, что у всех питомцев есть имена, возраст и порода
        try:
            driver.implicitly_wait(10)
            assert all(name.text != '' for name in names), "У питомца отсутствует имя"
            assert all(age.text != '' for age in ages), "У питомца отсутствует возраст"
            assert all(breed.text != '' for breed in breeds), "У питомца отсутствует порода"
            print("Тест 3 наличия имени, возраста, породы питомцев пройден успешно")

        except Exception as e:
            print("Произошла ошибка при выполнении теста 3:", e)


        # Тест 4 Проверяем, что все имена питомцев разные
        try:
            driver.implicitly_wait(10)
            assert len(set(pet_names)) == len(pet_names), "Имена питомцев не уникальны"
            print("Тест 4 наличия разных имен питомцев пройден успешно")

        except Exception as e:
            print("Произошла ошибка при выполнении теста 4:", e)


        # Тест 5 В списке нет повторяющихся питомцев
        try:
            driver.implicitly_wait(10)
            pet_info = [(name.text, age.text, breed.text) for name, age, breed in zip(names, ages, breeds)]
            assert len(pet_info) == len(set(pet_info)), "Обнаружены повторяющиеся питомцы"
            print("Тест 5 отсутствие повторяющихся питомцев пройден успешно")

        except Exception as e:
            print("Произошла ошибка при выполнении теста 5:", e)

        #
        # # Выводим количество строк и количество питомцев для отладки
        # print("Количество строк в таблице:", row_count)
        # print("Количество питомцев на странице:", pet_count)
        # print("Количество фото на странице:", images_with_src_count)


    except Exception as e:
        print("Произошла ошибка:", e)
