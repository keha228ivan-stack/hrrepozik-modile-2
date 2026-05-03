from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRaisedButton

from data import get_report_text, get_report_titles

KV = """
<ReportsScreen>:
    name: "reports"
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 0.93, 0.94, 0.96, 1

        MDTopAppBar:
            title: "Отчеты"
            md_bg_color: 1, 1, 1, 1
            specific_text_color: 0.08, 0.12, 0.22, 1

        ScrollView:
            MDBoxLayout:
                orientation: "vertical"
                adaptive_height: True
                spacing: "10dp"
                padding: "12dp"

                MDLabel:
                    text: "Выберите период"
                    bold: True

                MDBoxLayout:
                    adaptive_height: True
                    spacing: "8dp"

                    MDRaisedButton:
                        id: period_month
                        text: "Месяц"
                        on_release: root.set_period("Месяц")

                    MDRaisedButton:
                        id: period_quarter
                        text: "Квартал"
                        on_release: root.set_period("Квартал")

                    MDRaisedButton:
                        id: period_year
                        text: "Год"
                        on_release: root.set_period("Год")

                MDLabel:
                    id: selected_period_label
                    text: "Текущий период: Месяц"

                MDLabel:
                    text: "Выберите отчет"
                    bold: True

                MDBoxLayout:
                    id: reports_box
                    orientation: "vertical"
                    adaptive_height: True
                    spacing: "8dp"

                MDCard:
                    orientation: "vertical"
                    padding: "12dp"
                    size_hint_y: None
                    height: "220dp"
                    radius: [16, 16, 16, 16]

                    MDLabel:
                        text: "Краткая сводка"
                        bold: True
                    MDLabel:
                        id: report_text
                        text: "Нажмите на отчет, чтобы увидеть сводку"
"""
Builder.load_string(KV)


class ReportsScreen(Screen):
    selected_period = "Месяц"

    def on_pre_enter(self, *args):
        """Создает список доступных отчетов и обработчики клика."""
        self.ids.reports_box.clear_widgets()
        for title in get_report_titles():
            button = MDRaisedButton(text=title, on_release=lambda _, t=title: self.open_report(t))
            self.ids.reports_box.add_widget(button)

    def set_period(self, period):
        """Устанавливает период отчета."""
        self.selected_period = period
        self.ids.selected_period_label.text = f"Текущий период: {period}"

    def open_report(self, title):
        """Показывает текст выбранного отчета с учетом периода."""
        report = get_report_text(title)
        self.ids.report_text.text = f"Период: {self.selected_period}\n\n{report}"
