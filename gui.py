from pathlib import Path

from PySide6.QtWidgets import (
    QWidget,
    QFileDialog,
    QPushButton,
    QTextEdit,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QProgressBar
)


class MainWindow(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("OpenBee PDF Splitter")

        self.resize(900, 650)

        self.pdf = QLineEdit()

        self.output = QLineEdit(str(Path("output").absolute()))

        self.log = QTextEdit()

        self.log.setReadOnly(True)

        self.progress = QProgressBar()

        self.init_ui()

    def init_ui(self):

        layout = QVBoxLayout()

        row1 = QHBoxLayout()

        row1.addWidget(QLabel("PDF"))

        row1.addWidget(self.pdf)

        button = QPushButton("Ouvrir")

        button.clicked.connect(self.open_pdf)

        row1.addWidget(button)

        layout.addLayout(row1)

        row2 = QHBoxLayout()

        row2.addWidget(QLabel("Sortie"))

        row2.addWidget(self.output)

        button2 = QPushButton("Choisir")

        button2.clicked.connect(self.select_folder)

        row2.addWidget(button2)

        layout.addLayout(row2)

        layout.addWidget(self.progress)

        self.start = QPushButton("Découper")

        self.start.clicked.connect(self.start_process)

        layout.addWidget(self.start)

        layout.addWidget(self.log)

        self.setLayout(layout)

    def open_pdf(self):

        file, _ = QFileDialog.getOpenFileName(
            self,
            "Sélectionner un PDF",
            "",
            "*.pdf"
        )

        if file:

            self.pdf.setText(file)

            self.log.append(file)

    def select_folder(self):

        folder = QFileDialog.getExistingDirectory(
            self,
            "Dossier de sortie"
        )

        if folder:

            self.output.setText(folder)

    def start_process(self):

        self.progress.setValue(0)

        self.log.append("Début du traitement")

        # moteur OCR + découpage
        # sera ajouté dans le prochain commit

        self.progress.setValue(100)

        self.log.append("Traitement terminé")
