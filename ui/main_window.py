import os
import subprocess
from PySide6.QtWidgets import QMessageBox, QFileDialog
from PySide6.QtGui import QPixmap
from PIL import Image
from PIL.ImageQt import ImageQt

from core.pipeline import process_images
from utils.helpers import resize_with_padding
from ui.window import AugmentationWindow

TARGET_SIZE = (128, 128)


class MainWindow(AugmentationWindow):
    def __init__(self):
        super().__init__()

        self.output_dir = None
        self.image_paths = []

        style = super()._get_button_style()
        self.load_button.setStyleSheet(style)
        self.select_output_button.setStyleSheet(style)
        self.augment_button.setStyleSheet(style)
        self.open_output_button.setStyleSheet(style)

        self.load_button.clicked.connect(self.load_images)
        self.select_output_button.clicked.connect(self.select_output_folder)
        self.augment_button.clicked.connect(self.apply_selected_augmentation)
        self.open_output_button.clicked.connect(self.open_output_directory)

    def load_images(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Выберите папку с изображениями")
        if folder_path:
            self.image_paths = [os.path.join(folder_path, f) for f in os.listdir(folder_path)
                                if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))]
            self.image_count = len(self.image_paths)

            if self.image_count == 0:
                QMessageBox.warning(self, "Ошибка", "Нет изображений в выбранной папке.")
            else:
                self.label.setText(f"Изображений загружено: {self.image_count}")
                self.show_image_preview(self.image_paths[0])
                self.preview_label.clear()
                self.preview_label.setText("После")

    def select_output_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Выберите папку для сохранения результатов")
        if folder:
            self.output_dir = folder
            self.info_label.setText(f"Сохранение: {self.output_dir}")

    def open_output_directory(self):
        if self.output_dir and os.path.exists(self.output_dir):
            if os.name == 'nt':
                os.startfile(self.output_dir)
            elif os.name == 'posix':
                subprocess.run(['xdg-open', self.output_dir])
        else:
            QMessageBox.warning(self, "Ошибка", "Сначала выберите папку для сохранения результатов.")

    def show_image_preview(self, path):
        image = Image.open(path).convert("L")
        resized = resize_with_padding(image, TARGET_SIZE)
        qimage = ImageQt(resized)
        pixmap = QPixmap.fromImage(qimage)
        self.image_label.setPixmap(pixmap)

    def show_augmented_preview(self, pil_image):
        qimage = ImageQt(pil_image)
        pixmap = QPixmap.fromImage(qimage)
        self.preview_label.setPixmap(pixmap)

    def apply_selected_augmentation(self):
        if not self.image_paths:
            QMessageBox.warning(self, "Ошибка", "Сначала загрузите изображения.")
            return

        if not self.output_dir:
            QMessageBox.warning(self, "Ошибка", "Сначала выберите папку для сохранения результатов.")
            return

        volume_level = self.level_combo.currentText()

        for i, image_path in enumerate(self.image_paths):
            image = Image.open(image_path).convert("L")
            resized = resize_with_padding(image, TARGET_SIZE)
            augmented_images = process_images(resized, TARGET_SIZE, volume_level=volume_level)

            base_name = os.path.splitext(os.path.basename(image_path))[0]

            for aug_type, augmented_image in augmented_images.items():
                output_filename = f"{base_name}_{aug_type}.jpg"
                output_path = os.path.join(self.output_dir, output_filename)
                augmented_image.save(output_path)

                if i == 0 and aug_type == 'rotate':
                    self.show_augmented_preview(augmented_image)

        QMessageBox.information(self, "Готово", "Аугментация завершена для всех изображений.")
