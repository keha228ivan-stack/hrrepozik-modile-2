"""Модуль с тестовыми данными и простым провайдером данных.

В будущем функции этого модуля можно заменить на запросы к API,
не меняя экраны и бизнес-логику приложения.
"""

from copy import deepcopy

# Тестовый пользователь для авторизации руководителя.
TEST_USER = {"login": "director", "password": "1234"}

# Мок-данные по сотрудникам.
employees = [
    {
        "id": 1,
        "name": "Иванов Иван",
        "department": "Отдел продаж",
        "course": "Техника продаж",
        "progress": 45,
        "test_score": 58,
        "overdue": True,
    },
    {
        "id": 2,
        "name": "Петрова Анна",
        "department": "Бухгалтерия",
        "course": "Финансовая отчетность",
        "progress": 88,
        "test_score": 91,
        "overdue": False,
    },
    {
        "id": 3,
        "name": "Сидоров Максим",
        "department": "IT-отдел",
        "course": "Кибербезопасность",
        "progress": 72,
        "test_score": 77,
        "overdue": False,
    },
    {
        "id": 4,
        "name": "Кузнецова Ольга",
        "department": "Производство",
        "course": "Охрана труда",
        "progress": 39,
        "test_score": 66,
        "overdue": True,
    },
    {
        "id": 5,
        "name": "Смирнов Денис",
        "department": "HR-отдел",
        "course": "Оценка компетенций",
        "progress": 82,
        "test_score": 74,
        "overdue": False,
    },
    {
        "id": 6,
        "name": "Орлова Мария",
        "department": "Отдел продаж",
        "course": "Работа с возражениями",
        "progress": 52,
        "test_score": 55,
        "overdue": False,
    },
    {
        "id": 7,
        "name": "Федоров Артем",
        "department": "IT-отдел",
        "course": "DevOps основы",
        "progress": 93,
        "test_score": 95,
        "overdue": False,
    },
    {
        "id": 8,
        "name": "Васильева Елена",
        "department": "Производство",
        "course": "Стандарты качества",
        "progress": 61,
        "test_score": 59,
        "overdue": True,
    },
]

# Мок-данные по отделам.
departments = [
    {
        "name": "Отдел продаж",
        "employees_count": 12,
        "average_progress": 64,
        "average_score": 72,
        "completed_courses": 18,
        "overdue_courses": 5,
        "kpi": 61,
    },
    {
        "name": "Бухгалтерия",
        "employees_count": 8,
        "average_progress": 84,
        "average_score": 89,
        "completed_courses": 16,
        "overdue_courses": 1,
        "kpi": 87,
    },
    {
        "name": "IT-отдел",
        "employees_count": 15,
        "average_progress": 79,
        "average_score": 81,
        "completed_courses": 22,
        "overdue_courses": 2,
        "kpi": 78,
    },
    {
        "name": "Производство",
        "employees_count": 20,
        "average_progress": 58,
        "average_score": 63,
        "completed_courses": 24,
        "overdue_courses": 7,
        "kpi": 56,
    },
    {
        "name": "HR-отдел",
        "employees_count": 6,
        "average_progress": 90,
        "average_score": 92,
        "completed_courses": 12,
        "overdue_courses": 0,
        "kpi": 93,
    },
]

# KPI-показатели для отдельного экрана.
kpi_metrics = [
    {"name": "Общий KPI обучения", "value": 76},
    {"name": "KPI завершения курсов", "value": 74},
    {"name": "KPI среднего балла тестирования", "value": 80},
    {"name": "KPI соблюдения сроков", "value": 68},
    {"name": "KPI активности сотрудников", "value": 71},
]

report_templates = {
    "Отчет по выполнению курсов": "За период назначено 42 курса, завершено 31. Средний прогресс обучения — 76%.",
    "Отчет по отделам": "Лучший KPI у HR-отдела (93%). Зона роста: Производство (56%) и Отдел продаж (61%).",
    "Отчет по сотрудникам в зоне риска": "В зоне риска 4 сотрудника. Основные причины: просрочки и низкий прогресс.",
    "Отчет по среднему баллу тестирования": "Средний балл тестирования по компании — 72%. В IT-отделе и Бухгалтерии показатели выше 80%.",
    "Отчет по просроченным курсам": "Всего просрочено 15 курсов. Наибольшее число просрочек в Производстве и Отделе продаж.",
}


def get_test_user():
    """Возвращает тестового пользователя для авторизации."""
    return deepcopy(TEST_USER)


def get_employees():
    """Возвращает копию списка сотрудников."""
    return deepcopy(employees)


def get_departments():
    """Возвращает копию списка отделов."""
    return deepcopy(departments)


def get_kpi_metrics():
    """Возвращает KPI-метрики для экрана KPI."""
    return deepcopy(kpi_metrics)


def get_report_titles():
    """Возвращает список доступных названий отчетов."""
    return list(report_templates.keys())


def get_report_text(title):
    """Возвращает текст отчета по его названию."""
    return report_templates.get(title, "Отчет не найден.")
