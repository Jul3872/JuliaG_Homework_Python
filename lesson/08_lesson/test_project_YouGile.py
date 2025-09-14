from project_YouGile import ProjectYouGile

# Константы
LOGIN = "jul381972@gmail.com"
PASSWORD = "Yulya1427!"
NAME = "Тестировщик"
COMPANY_ID = "0712b0a4-65ec-4443-ac24-0fd40742d8eb"
USER_UUID = "95bb52b4-fa9e-44bd-80b3-84a437b66df5"
ADMIN_ROLE = "admin"
NEW_TITLE = "New_Project_Test"
TEST_USER = {USER_UUID: ADMIN_ROLE}
TITLE_GET_TEST = "Get_Project_Test"
TITLE_EDIT_TEST = "Edit_Project_Test"
EDITED_TITLE = "Edited_Project_Test"
DELETED_STATUS = False
NEW_TITLE_NEGATIVE = ""
USER_UUID_NEGATIVE = "95bb52b4-fa9e-44bd-80b3-84a437b66df"
TEST_USER_NEGATIVE = {USER_UUID_NEGATIVE: ADMIN_ROLE}

# Экземпляр API
api = ProjectYouGile('https://ru.yougile.com/api-v2/',
                     LOGIN, PASSWORD, COMPANY_ID)


def test_create_project_positive():
    # Количество проектов до
    projects_before = api.get_project_list()
    len_before = len(projects_before)

    # Создание проекта
    result = api.create_project(NEW_TITLE, TEST_USER)
    new_id = result.json()['id']

    # Количество проектов после
    projects_after = api.get_project_list()
    len_after = len(projects_after)

    assert result.status_code == 201
    assert len_after - len_before == 1
    assert projects_after[-1]['title'] == NEW_TITLE
    assert projects_after[-1]['id'] == new_id


def test_create_project_negative():
    projects_before = api.get_project_list()
    len_before = len(projects_before)

    # Создание проекта с пустым названием
    result = api.create_project(NEW_TITLE_NEGATIVE, TEST_USER)

    # Количество проектов после
    projects_after = api.get_project_list()
    len_after = len(projects_after)

    assert result.status_code == 400
    assert len_after - len_before == 0


def test_get_project_with_id_positive():
    result = api.create_project(TITLE_GET_TEST, TEST_USER)
    project_id = result.json()['id']

    # Обращаемся к проекту
    new_project = api.get_project_with_id(project_id)

    assert new_project.status_code == 200
    assert new_project.json()['title'] == TITLE_GET_TEST
    assert new_project.json()['users'] == TEST_USER

    # Очистка данных после теста
    api.edit_project(project_id, True,
                     TITLE_GET_TEST, TEST_USER)


def test_get_project_with_id_negative():
    # Обращаемся к проекту с несуществующим  id
    new_project = api.get_project_with_id("9999")

    assert new_project.status_code == 404


def test_edit_project_positive():
    # Создание проекта
    result = api.create_project(TITLE_EDIT_TEST, TEST_USER)
    project_id = result.json()['id']

    # Изменение проекта
    edited = api.edit_project(project_id, DELETED_STATUS,
                              EDITED_TITLE, TEST_USER)

    assert edited.status_code == 200
    project_title = api.get_project_with_id(project_id).json()['title']
    assert project_title == EDITED_TITLE

    # Очистка данных после теста
    api.edit_project(project_id, True,
                     EDITED_TITLE, TEST_USER)


def test_edit_project_negative():
    # Создание проекта
    result = api.create_project(TITLE_EDIT_TEST, TEST_USER)
    project_id = result.json()['id']

    # Попытка змененить проект с неверным идентификатором роли
    edited = api.edit_project(project_id, DELETED_STATUS,
                              EDITED_TITLE, TEST_USER_NEGATIVE)

    assert edited.status_code == 400

    # Очистка данных после теста
    api.edit_project(project_id, True,
                     EDITED_TITLE, TEST_USER)
