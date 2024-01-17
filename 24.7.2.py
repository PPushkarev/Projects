
from api import PetFriends
from settings import valid_email, valid_password
import os


pf = PetFriends()


def test__successful_add_new_pet_simple(name='Терминатор', animal_type='kedi',
                                     age='2024'):
    """Тест 1 Проверяем что можно добавить питомца без фото"""


    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_simple(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test__successful_add_set_photo(pet_photo='photo/cat.jpg'):
    """Тест 2 Проверяем что можно добавить фото питомца"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    pet_id = my_pets['pets'][0]['id']
       # Добавляем фото
    status, result = pf.add_set_photo(auth_key, pet_id, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200


def test_negative_get_api_key_for_valid_user(email= valid_email2, password= valid_password2):
    """ Тест 3 Проверяем что запрос api ключа возвращает статус 403 при отсутствии пользователя в базе данных"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert 'key' not in result


def test_negative_get_api_key_for_valid_user_with_empty_credentials():
    """Тест 4 Проверяем, что запрос API ключа для действительного пользователя с пустыми учетными данными возвращает статус 403."""
    status, _ = pf.get_api_key("", "")
    assert status == 403



def test_negative_add_new_pet_with_empty_name():
    """Тест 5 Проверяем, что нельзя добавить питомца с пустым именем."""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, _ = pf.add_new_pet(auth_key, '', 'cetuscatus', '5', 'photo/cat.jpg')

    # Предполагаемый статус для отрицательного возраста
    # Проверяем что статус ответа = 400
    assert status == 400


def test_negative_add_new_pet_with_negative_age():
    """Тест 6 Проверяем, что нельзя добавить питомца с отрицательным возрастом."""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, _ = pf.add_new_pet(auth_key, 'Фулька2', 'cetuscatus', '-5', 'photo/cat.jpg')

    # Предполагаемый статус для отрицательного возраста
    # Проверяем что статус ответа = 400
    assert status == 400


def test_negative_update_noexisted_pet(name='Мурзик', animal_type='Котэ', age=5):
    """Тест 7 Проверяем возможность обновления информации о питомце которого не существует"""

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    nonexistent_pet_id = "999999"
    status, result = pf.update_pet_info(auth_key, nonexistent_pet_id, name, animal_type, age)

        # Проверяем что статус ответа = 400
    assert status == 400


def test_negative_add_new_pet_with_empty_name(animal_type='собака', age='4'):
    """Тест 8 Проверяем, что нельзя добавить питомца с пустым именем"""

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Пытаемся добавить питомца с пустым именем
    status, _ = pf.add_new_pet_simple(auth_key, '', animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом (должен быть статус 400)
    assert status == 400


def test_negative_delete_self_pet():
    """Тест  9 Проверяем возможность удаления не существующего питомца"""

    # Получаем ключ auth_key и запрашиваем список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    nonexistent_pet_id = "999999"
    status, _ = pf.delete_pet(auth_key, nonexistent_pet_id)

    # Проверяем что статус ответа равен 200
    assert status == 200

def test_negative_get_all_pets_with_invalid_filter(filter='58'):
    """ Тест 10 Проверяем выведение списка питомцев с не правильным фильтром и ломаем сервер"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)

    # Проверяем что статус ответа равен 403
    assert status == 403
    assert len(result['pets']) > 0
