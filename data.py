"""Модуль с тестовыми данными и простым провайдером данных."""

from copy import deepcopy

_CURRENT_USER = {
    "login": "director",
    "password": "1234",
    "full_name": "Директор Компании",
    "email": "director@company.local",
    "role": "Руководитель",
}

employees = [
    {"id": 1, "name": "Иванов Иван", "department": "Отдел продаж", "course": "Техника продаж", "progress": 45, "test_score": 58, "overdue": True},
    {"id": 2, "name": "Петрова Анна", "department": "Бухгалтерия", "course": "Финансовая отчетность", "progress": 88, "test_score": 91, "overdue": False},
    {"id": 3, "name": "Сидоров Максим", "department": "IT-отдел", "course": "Кибербезопасность", "progress": 72, "test_score": 77, "overdue": False},
    {"id": 4, "name": "Кузнецова Ольга", "department": "Производство", "course": "Охрана труда", "progress": 39, "test_score": 66, "overdue": True},
]

departments = [
    {"name": "Отдел продаж", "employees_count": 12, "average_progress": 64, "average_score": 72, "completed_courses": 18, "overdue_courses": 5, "kpi": 61},
    {"name": "Бухгалтерия", "employees_count": 8, "average_progress": 84, "average_score": 89, "completed_courses": 16, "overdue_courses": 1, "kpi": 87},
    {"name": "IT-отдел", "employees_count": 15, "average_progress": 79, "average_score": 81, "completed_courses": 22, "overdue_courses": 2, "kpi": 78},
    {"name": "Производство", "employees_count": 20, "average_progress": 58, "average_score": 63, "completed_courses": 24, "overdue_courses": 7, "kpi": 56},
    {"name": "HR-отдел", "employees_count": 6, "average_progress": 90, "average_score": 92, "completed_courses": 12, "overdue_courses": 0, "kpi": 93},
]

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
    "Отчет по среднему баллу тестирования": "Средний балл тестирования по компании — 72%.",
    "Отчет по просроченным курсам": "Всего просрочено 15 курсов. Наибольшее число просрочек в Производстве.",
}


def get_test_user():
    return deepcopy(_CURRENT_USER)


def register_user(login, password, full_name, email):
    global _CURRENT_USER
    _CURRENT_USER = {
        "login": login,
        "password": password,
        "full_name": full_name,
        "email": email,
        "role": "Руководитель",
    }
    return deepcopy(_CURRENT_USER)


def get_profile_data():
    return {
        "full_name": _CURRENT_USER["full_name"],
        "email": _CURRENT_USER["email"],
        "role": _CURRENT_USER["role"],
        "login": _CURRENT_USER["login"],
    }


def get_employees(): return deepcopy(employees)

def get_departments(): return deepcopy(departments)

def get_kpi_metrics(): return deepcopy(kpi_metrics)

def get_report_titles(): return list(report_templates.keys())

def get_report_text(title): return report_templates.get(title, "Отчет не найден.")
