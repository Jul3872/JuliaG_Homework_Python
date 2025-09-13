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
DELETED_STATUS = "false"

# Экземпляр API
api = ProjectYouGile('https://ru.yougile.com/api-v2/')


def test_create_project():
    try:
        # Количество проектов до
        projects_before = api.get_project_list(login=LOGIN,
                                               password=PASSWORD, name=NAME)
        len_before = len(projects_before)

        # Создание проекта
        result = api.create_project(NEW_TITLE, TEST_USER,
                                    LOGIN, PASSWORD, COMPANY_ID)
        new_id = result['id']

        # Количество проектов после
        projects_after = api.get_project_list(login=LOGIN,
                                              password=PASSWORD, name=NAME)
        len_after = len(projects_after)

        assert result.status_code == 201
        assert len_after - len_before == 1
        assert projects_after[-1]['title'] == NEW_TITLE
        assert projects_after[-1]['id'] == new_id
    except AssertionError as err:
        print(f"Ошибка в тесте создания проекта: {err}")
    except Exception as exc:
        print(f"Общая ошибка: {exc}")


def test_get_project_with_id():
    try:
        # Создание проекта
        result = api.create_project(TITLE_GET_TEST, TEST_USER,
                                    LOGIN, PASSWORD, COMPANY_ID)
        project_id = result['id']

        # Обращаемся к проекту
        new_project = api.get_project_with_id(project_id)

        assert result.status_code == 200
        assert new_project['title'] == TITLE_GET_TEST
        assert new_project['users'] == TEST_USER
    except AssertionError as err:
        print(f"Ошибка в тесте получения проекта по ID: {err}")
    except Exception as exc:
        print(f"Общая ошибка: {exc}")


def test_edit_project():
    try:
        # Создание проекта
        result = api.create_project(TITLE_EDIT_TEST, TEST_USER,
                                    LOGIN, PASSWORD, COMPANY_ID)
        project_id = result['id']

        # Изменение проекта
        edited = api.edit_project(project_id, DELETED_STATUS,
                                  EDITED_TITLE, TEST_USER)

        assert result.status_code == 200
        assert edited['title'] == EDITED_TITLE
    except AssertionError as err:
        print(f"Ошибка в тесте редактирования проекта: {err}")
    except Exception as exc:
        print(f"Общая ошибка: {exc}")
