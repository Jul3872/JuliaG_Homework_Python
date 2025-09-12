from project_YouGile import ProjectYouGile

api = ProjectYouGile('https://ru.yougile.com/api-v2/')


def test_create_project_():
    # количество проектов до
    login = "jul381972@gmail.com",
    password = "Yulya1427!",
    name = "Тестировщик"
    projects_before = api.get_project_list(login=login,
                                           password=password,
                                           name=name)
    len_before = len(projects_before)

    # создание проекта
    title = 'New_Project_Test'
    users = {"95bb52b4-fa9e-44bd-80b3-84a437b66df5": "admin"}
    companyID = "0712b0a4-65ec-4443-ac24-0fd40742d8eb"
    result = api.create_project(title, users, login, password, companyID)
    new_id = result['id']

    # количество проектов после
    projects_after = api.get_project_list(login=login,
                                          password=password,
                                          name=name)
    len_after = len(projects_after)

    assert len_after - len_before == 1
    assert projects_after[-1]['title'] == title
    assert projects_after[-1]['id'] == new_id


def test_get_project_with_id():
    # создание проекта
    login = "jul381972@gmail.com",
    password = "Yulya1427!",
    companyID = "0712b0a4-65ec-4443-ac24-0fd40742d8eb"
    title = 'Get_Project_Test'
    users = {"95bb52b4-fa9e-44bd-80b3-84a437b66df5": "admin"}
    result = api.create_project(title, users, login, password, companyID)
    project_id = result['id']

    # обращаемся к проекту
    new_project = api.get_project_with_id(project_id)

    assert new_project['title'] == title
    assert new_project['users'] == users


def test_edit_project():
    login = "jul381972@gmail.com",
    password = "Yulya1427!",
    companyID = "0712b0a4-65ec-4443-ac24-0fd40742d8eb"
    title = 'Edit_Project_Test'
    users = {"95bb52b4-fa9e-44bd-80b3-84a437b66df5": "admin"}

    result = api.create_project(title, users, login, password, companyID)

    project_id = result['id']
    new_deleted = 'false'
    new_title = 'Edited_Project_Test'
    new_users = {"95bb52b4-fa9e-44bd-80b3-84a437b66df5": "admin"}

    edited = api.edit_project(project_id, new_deleted, new_title, new_users)

    assert edited['title'] == new_title
