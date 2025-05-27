from typing import Optional, List
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QListWidget, QListWidgetItem
)
from ..workers.pdf_generator import PDFGenerator

class PDFTab(QWidget):
    """PDF sekmesi widget'ı."""
    
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.resim_yollari: List[str] = []
        self._setup_ui()

    def _setup_ui(self) -> None:
        """UI bileşenlerini oluşturur."""
        layout: QVBoxLayout = QVBoxLayout(self)
        
        image_select_layout: QHBoxLayout = QHBoxLayout()
        self.resim_listesi: QListWidget = QListWidget()
        self.resim_sec_buton: QPushButton = QPushButton("Resim Seç")
        self.resim_sec_buton.clicked.connect(self.resim_sec)
        self.resim_temizle_buton: QPushButton = QPushButton("Listeyi Temizle")
        self.resim_temizle_buton.clicked.connect(self.resim_listesi.clear)
        
        image_select_layout.addWidget(self.resim_sec_buton)
        image_select_layout.addWidget(self.resim_temizle_buton)
        
        self.pdf_olustur_buton: QPushButton = QPushButton("PDF Oluştur")
        self.pdf_olustur_buton.clicked.connect(self.pdf_olustur)
        
        layout.addLayout(image_select_layout)
        layout.addWidget(self.resim_listesi)
        layout.addWidget(self.pdf_olustur_buton)

    def resim_sec(self) -> None:
        """Resim seçme işlemini başlatır."""
        from PySide6.QtWidgets import QFileDialog
        dosya_yollari, _ = QFileDialog.getOpenFileNames(
            self,
            "Resim Seç",
            "",
            "Resim Dosyaları (*.png *.jpg *.jpeg);;Tüm Dosyalar (*.*)"
        )

        if dosya_yollari:
            self.resim_yollari.extend(dosya_yollari)
            for dosya_yolu in dosya_yollari:
                item = QListWidgetItem(f"📷 {os.path.basename(dosya_yolu)}")
                item.setData(Qt.UserRole, dosya_yolu)
                self.resim_listesi.addItem(item)
            self.parent().log_yaz(f"{len(dosya_yollari)} resim eklendi", "normal")

    def pdf_olustur(self) -> None:
        """PDF oluşturma işlemini başlatır."""
        if not self.resim_yollari:
            self.parent().log_yaz("Lütfen önce resim seçin!", "kirmizi")
            return

        self.pdf_thread = PDFGenerator(self.resim_yollari)
        self.pdf_thread.log_signal.connect(self.parent().log_yaz)
        self.pdf_thread.finished_signal.connect(lambda: self.parent().log_yaz("PDF oluşturma tamamlandı!", "normal"))
        self.pdf_thread.start() 