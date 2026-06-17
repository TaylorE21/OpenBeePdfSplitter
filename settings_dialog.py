SettingsDialog(QDialog)
-------------------------------------------------
                Configuration

Regex OCR

[ Num\s*Commande...                    ]

Langue OCR

[ fra                    ▼ ]

DPI OCR

[ 300 ]

Dossier de sortie

[C:\Output....................][Parcourir]

                    [Enregistrer]
                    [Annuler]

-------------------------------------------------
QLineEdit    regex

QComboBox    langue

QSpinBox     dpi

QLineEdit    output

QPushButton  Parcourir

QDialogButtonBox
[⚙ Configuration]
dialog = SettingsDialog(self)

dialog.exec()
[OCR]

language=fra
dpi=300

[SEARCH]

pattern=Num\s*Commande\s*Open\s*Bee[\s:]*([A-Za-z0-9\-/]+)

[OUTPUT]

directory=C:\OpenBee\Output
-----------------------------------------------------

PDF : 148 pages

███████████████░░░░░░░░░ 63 %

Page 93 / 148

PDF créés : 27

-----------------------------------------------------
  +------------------------------------------------+

Traitement | Journal

-----------------------------------------------

14:20:15 Ouverture du PDF

14:20:15 Regex détectée

14:20:16 Page 1 -> P06050-25

14:20:16 Création P06050-25.pdf

...

------------------------------------------------+
[ Effacer ]

[ Ouvrir le fichier log ]

[ Exporter le log ]
+----------------------------------------+

Déposez un ou plusieurs PDF ici

----------------------------------------

✓ fichier1.pdf

✓ fichier2.pdf

✓ fichier3.pdf

                [Découper]

+----------------------------------------+
