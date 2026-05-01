from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp

from screens.dashboard_screen import DashboardScreen
from screens.departments_screen import DepartmentsScreen
from screens.kpi_screen import KpiScreen
from screens.login_screen import LoginScreen
from screens.reports_screen import ReportsScreen
from screens.risk_screen import RiskScreen

KV = """
#:import dp kivy.metrics.dp

MDScreen:
    MDBoxLayout:
        orientation: "vertical"

        ScreenManager:
            id: screen_manager

        MDBoxLayout:
            id: nav_bar
            size_hint_y: None
            height: dp(62)
            spacing: "6dp"
            padding: "6dp"
            md_bg_color: 0.94, 0.94, 0.94, 1

            MDRaisedButton:
                text: "Главная"
                on_release: app.switch_screen("dashboard")
            MDRaisedButton:
                text: "Отделы"
                on_release: app.switch_screen("departments")
            MDRaisedButton:
                text: "KPI"
                on_release: app.switch_screen("kpi")
            MDRaisedButton:
                text: "Риски"
                on_release: app.switch_screen("risk")
            MDRaisedButton:
                text: "Отчеты"
                on_release: app.switch_screen("reports")
            MDRaisedButton:
                text: "Выход"
                md_bg_color: 0.85, 0.25, 0.25, 1
                on_release: app.logout()
"""


class HrMobileApp(MDApp):
    """Мобильный аналитический клиент для руководства."""

    def build(self):
        self.title = "HR Analytics Mobile"
        root = Builder.load_string(KV)
        self.sm = root.ids.screen_manager

        # Регистрируем все экраны приложения.
        self.sm.add_widget(LoginScreen())
        self.sm.add_widget(DashboardScreen())
        self.sm.add_widget(DepartmentsScreen())
        self.sm.add_widget(KpiScreen())
        self.sm.add_widget(RiskScreen())
        self.sm.add_widget(ReportsScreen())

        self.sm.current = "login"
        root.ids.nav_bar.disabled = True
        root.ids.nav_bar.opacity = 0
        self.root_widget = root
        return root

    def switch_screen(self, name):
        """Переход между экранами через нижнюю навигацию."""
        self.sm.current = name

    def on_start(self):
        """Подписываемся на событие смены экрана."""
        self.sm.bind(current=self.on_screen_changed)

    def on_screen_changed(self, _, current):
        """Скрывает навигацию на логине и показывает после входа."""
        is_login = current == "login"
        self.root_widget.ids.nav_bar.disabled = is_login
        self.root_widget.ids.nav_bar.opacity = 0 if is_login else 1

    def logout(self):
        """Выход пользователя на экран авторизации."""
        self.sm.current = "login"


if __name__ == "__main__":
    HrMobileApp().run()
