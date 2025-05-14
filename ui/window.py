from PySide6.QtWidgets import (
    QMainWindow, QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout, QComboBox
)
from PySide6.QtCore import Qt


class AugmentationWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Аугментация изображений")
        self.setFixedSize(420, 720)

        self.label = QLabel("Выберите папку с изображениями")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 16pt; font-weight: bold; color: #333;")

        self.image_label = QLabel("До")
        self.image_label.setFixedSize(128, 128)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setStyleSheet("border: 1px solid #ccc;")

        self.preview_label = QLabel("После")
        self.preview_label.setFixedSize(128, 128)
        self.preview_label.setAlignment(Qt.AlignCenter)
        self.preview_label.setStyleSheet("border: 1px solid #ccc;")

        self.load_button = QPushButton("Загрузить папку")
        self.load_button.setFixedHeight(40)

        self.select_output_button = QPushButton("Выбрать папку для сохранения")
        self.select_output_button.setFixedHeight(40)

        self.open_output_button = QPushButton("Открыть папку с результатами")
        self.open_output_button.setFixedHeight(40)

        self.augment_button = QPushButton("Применить аугментацию")
        self.augment_button.setFixedHeight(40)

        self.level_combo = QComboBox()
        self.level_combo.addItems(['low', 'medium', 'high'])
        self.level_combo.setStyleSheet("font-size: 12pt; padding: 5px;")

        self.info_label = QLabel()
        self.info_label.setAlignment(Qt.AlignCenter)
        self.info_label.setStyleSheet("font-size: 12pt; color: #666;")

        preview_layout = QHBoxLayout()
        preview_layout.addWidget(self.image_label)
        preview_layout.addWidget(self.preview_label)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addLayout(preview_layout)
        layout.addWidget(self.load_button)
        layout.addWidget(QLabel("Выберите уровень аугментации:"))
        layout.addWidget(self.level_combo)
        layout.addWidget(self.select_output_button)
        layout.addWidget(self.augment_button)
        layout.addWidget(self.open_output_button)
        layout.addWidget(self.info_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def _get_button_style(self):
        return """
        QPushButton {
            background-color: #4CAF50;
            color: white;
            font-size: 14pt;
            font-weight: bold;
            border-radius: 8px;
            border: none;
        }
        QPushButton:hover {
            background-color: #45a049;
        }
        QPushButton:pressed {
            background-color: #388e3c;
        }
        """
