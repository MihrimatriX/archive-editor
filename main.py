import sys
import os
from PySide6.QtWidgets import QApplication
from src.ui.main_window import MainWindow

def main():
    # Uygulama dizinini Python yoluna ekle
    app_dir = os.path.dirname(os.path.abspath(__file__))
    if app_dir not in sys.path:
        sys.path.insert(0, app_dir)

    # Uygulamayı başlat
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main() 