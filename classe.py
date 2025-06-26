from PyQt5.QtWidgets import (
    QVBoxLayout, QHBoxLayout,QGridLayout,
    QLabel, QFrame, QPushButton, QLineEdit,
    QDialog, QVBoxLayout, QLabel, QLineEdit, 
    QPushButton, QHBoxLayout
)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QFont, QTextCharFormat
import logs as lg
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QGridLayout, QPushButton, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt


class LienDialog(QDialog):
    def __init__(self, texte=""):
        super().__init__()
        self.setWindowTitle("Ajouter un lien")
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setStyleSheet("""
            QDialog{
                background-color: #181818; 
                color: white; 
                border: 1px solid #2B2B2B;
            }
            QPushButton {
                background-color: #1F1F1F;
                border: none;
                font-family: Inter;
                font-size: 22px;
                padding: 12px 16px;
                border-radius: 5px;
                color: #90A4AE;
            }
            QPushButton:hover {
                background-color: #0089CD;
                color: white;
            }
            QLabel {
                color: #90A4AE;
                font-family: Inter;
                font-size: 22px;
            }
            QLineEdit {
                background-color: #1F1F1F;
                color: white;
                font-family: Inter;
                font-size: 22px;
                padding: 12px 16px;
                border-radius: 5px;
                border: 1px solid #2B2B2B;
            }
        """)

        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(40, 40, 40, 40)

        self.texte_input = QLineEdit(texte)
        self.texte_input.setPlaceholderText("Texte à afficher")
        self.url_input = QLineEdit("https://")
        self.url_input.setPlaceholderText("URL")

        self.layout.addWidget(QLabel("Texte :", self))
        self.layout.addWidget(self.texte_input)
        self.layout.addWidget(QLabel("Lien :", self))
        self.layout.addWidget(self.url_input)

        btn_layout = QHBoxLayout()
        self.ok_btn = QPushButton("Ajouter")
        self.cancel_btn = QPushButton("Annuler")
        self.ok_btn.clicked.connect(self.accept)
        self.cancel_btn.clicked.connect(self.reject)
        btn_layout.addWidget(self.ok_btn)
        btn_layout.addWidget(self.cancel_btn)
        self.layout.addLayout(btn_layout)

    def get_data(self):
        return self.texte_input.text(), self.url_input.text()
         
class TableauDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inserer un tableau")
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setStyleSheet("""
            QDialog {
                background-color: #181818; 
                color: white; 
                border: 1px solid #2B2B2B;
            }
            QPushButton {
                background-color: #1F1F1F;
                border: none;
                font-family: Inter;
                font-size: 22px;
                padding: 12px 16px;
                border-radius: 5px;
                color: #90A4AE;
            }
            QPushButton:hover {
                background-color: #0089CD;
                color: white;
            }
            QLabel {
                color: #90A4AE;
                font-family: Inter;
                font-size: 22px;
            }
            QLineEdit {
                background-color: #1F1F1F;
                color: white;
                font-family: Inter;
                font-size: 22px;
                padding: 12px 16px;
                border-radius: 5px;
                border: 1px solid #2B2B2B;
            }
        """)

        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(40, 40, 40, 40)

        # Champs pour lignes et colonnes
        self.lignes_input = QLineEdit("2")
        self.lignes_input.setPlaceholderText("Nombre de lignes")
        self.colonnes_input = QLineEdit("2")
        self.colonnes_input.setPlaceholderText("Nombre de colonnes")

        self.layout.addWidget(QLabel("Lignes :", self))
        self.layout.addWidget(self.lignes_input)
        self.layout.addWidget(QLabel("Colonnes :", self))
        self.layout.addWidget(self.colonnes_input)

        # Boutons
        btn_layout = QHBoxLayout()
        self.ok_btn = QPushButton("Inserer")
        self.cancel_btn = QPushButton("Annuler")
        self.ok_btn.clicked.connect(self.accept)
        self.cancel_btn.clicked.connect(self.reject)
        btn_layout.addWidget(self.ok_btn)
        btn_layout.addWidget(self.cancel_btn)
        self.layout.addLayout(btn_layout)

    def get_data(self):
        return int(self.lignes_input.text()), int(self.colonnes_input.text())

class BarreTitre(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        lg.logging.info("Initialisation de la barre de titre")
        self.setFixedHeight(40)
        self.setStyleSheet("""
            QFrame {
                background-color: #121212;
                border-bottom: 1px solid #2B2B2B;
            }
            QLineEdit {
                background: transparent;
                border: none;
                color: #90A4AE;
                font-size: 18px;
                padding-left: 10px;
            }
            QPushButton {
                border: none;
                color: #90A4AE;
                font-size: 16px;
                padding: 0 10px;
            }
            QPushButton:hover {
                background-color: #0089CD;
                color: white;
            }
        """)

        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(10, 0, 0, 0)

        # Champ pour nom du fichier
        self.input_nom = QLineEdit("Sans titre")
        self.input_nom.setFixedWidth(250)
        self.input_nom.setToolTip("Nom du document - modifiable")
        self.input_nom.setStyleSheet("""
            QLineEdit {
                background-color: #1F1F1F;
                color: #90A4AE;
                border: 1px solid #2B2B2B;
                border-radius: 5px;
                font-size: 18px;
                padding-left: 10px;
            }
        """)
        self.layout.addWidget(self.input_nom)

        self.layout.addStretch()

        # Boutons de fenetre
        # Bouton : reduire
        self.btn_min = QPushButton()
        self.btn_min.setIcon(QIcon("ui/icons/minimize.png"))  # icone "-"
        self.btn_min.clicked.connect(lambda: lg.logging.debug("Fenetre reduite"))
        self.btn_min.setToolTip("Reduire")

        # Bouton : plein ecran / restaurer
        self.btn_max = QPushButton()
        self.btn_max.setIcon(QIcon("ui/icons/expand.png"))  # icone "□"
        self.btn_max.setToolTip("Plein ecran")

        # Bouton : fermer
        self.btn_close = QPushButton()
        self.btn_close.setIcon(QIcon("ui/icons/close.png"))  # icone "×"
        self.btn_close.clicked.connect(lambda: lg.logging.debug("Application fermee"))
        self.btn_close.setToolTip("Fermer")

        self.layout.addWidget(self.btn_min)
        self.layout.addWidget(self.btn_max)
        self.layout.addWidget(self.btn_close)

        # Connexions
        self.btn_min.clicked.connect(self.parent().showMinimized)        
        self.btn_max.clicked.connect(self.toggle_max_restore)
        self.btn_close.clicked.connect(self.parent().close)

        # Pour le deplacement
        self.old_pos = None
        self._maximized = False
    
    def toggle_max_restore(self):
        if self._maximized:
            lg.logging.debug("Restaurer la fenetre")
            self.parent().showNormal()
            self._maximized = False
            self.btn_max.setIcon(QIcon("ui/icons/expand.png"))
        else:
            lg.logging.debug("Maximiser la fenetre")
            self.parent().showMaximized()
            self._maximized = True
            self.btn_max.setIcon(QIcon("ui/icons/restore.png"))

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.old_pos = event.globalPos()

    def mouseMoveEvent(self, event):
        if self.old_pos:
            delta = event.globalPos() - self.old_pos
            self.parent().move(self.parent().pos() + delta)
            self.old_pos = event.globalPos()

    def mouseReleaseEvent(self, event):
        self.old_pos = None

class Tool(QFrame):
    def __init__(self, colonnes=2, parent=None):
        super().__init__(parent)
        self.colonnes = colonnes
        self.boutons = []
        lg.logging.info(f"Creation du Tool avec {colonnes} colonnes")

        self.setStyleSheet("""
            QFrame {
                border-right: 1px solid #2B2B2B;
                border-bottom: 1px solid #2B2B2B;
            }
            QPushButton {
                background-color: #1F1F1F;
                border: none;
                padding: 12px 16px;
                font-family: Inter;
                font-size: 18px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #181818;
            }
            QPushButton:checked {
                background-color: #0089CD;
                color: white;
            }
        """)

        self.layout = QGridLayout()
        self.layout.setSpacing(10)
        self.setLayout(self.layout)

    def ajouter_bouton(self, texte, fonction=None, tooltip=None, icon_path=None, tag=None):
        lg.logging.info(f"Ajout du bouton '{texte}'")
        bouton = QPushButton(texte)
        bouton.tag = tag  # stocker le style (gras, italic...)
        if tag and tag != "image":
            bouton.setCheckable(True)

        # Ajout de l’icone si un chemin est fourni
        if icon_path:
            lg.logging.debug(f"Ajout icone a '{texte}': {icon_path}")
            icon = QIcon(icon_path)
            bouton.setIcon(icon)
            bouton.setIconSize(QSize(24, 24))  # taille de l'icone

        # Tooltip (si fourni)
        if tooltip:
            lg.logging.debug(f"Ajout tooltip a '{texte}': {tooltip}")
            bouton.setToolTip(tooltip)

        # Connexion a la fonction cliquee
        if fonction:
            bouton.clicked.connect(fonction)
            lg.logging.debug(f"Connexion de la fonction au bouton '{texte}'")

        # Placement automatique dans la grille
        index = len(self.boutons)
        ligne = index // self.colonnes
        colonne = index % self.colonnes
        self.layout.addWidget(bouton, ligne, colonne)

        self.boutons.append(bouton)
        lg.logging.debug(f"Bouton '{texte}' ajoute en position ({ligne}, {colonne})")

    def mettre_a_jour_etat_boutons(self, char_format: QTextCharFormat):
        for bouton in self.boutons:
            if not hasattr(bouton, "tag") or bouton.tag is None:
                continue
            
            tag = bouton.tag
            if tag == "bold":
                bouton.setChecked(char_format.fontWeight() > QFont.Normal)
            elif tag == "italic":
                bouton.setChecked(char_format.fontItalic())
            elif tag == "underline":
                bouton.setChecked(char_format.fontUnderline())
            elif tag == "strike":
                bouton.setChecked(char_format.fontStrikeOut())
            elif tag == "h1":
                bouton.setChecked(int(char_format.fontPointSize()) >= 32)
            elif tag == "h2":
                bouton.setChecked(32 > int(char_format.fontPointSize()) >= 26)
            elif tag == "h3":
                bouton.setChecked(26 > int(char_format.fontPointSize()) >= 22)
            elif tag == "h4":
                bouton.setChecked(22 > int(char_format.fontPointSize()) >= 18)
            
            # elif tag == "num":
            #     bouton.setChecked()
            # elif tag == "puce":
            #     bouton.setChecked()
    
class EmojiDialog(QDialog):
    def __init__(self, emojis_per_page=15):
        super().__init__()
        self.setWindowTitle("Ajouter un emoji")
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setStyleSheet("""
            QDialog {
                background-color: #181818; 
                color: white; 
                border: 1px solid #2B2B2B;
            }
            QPushButton {
                background-color: #1F1F1F;
                border: none;
                font-family: Inter;
                font-size: 24px;
                padding: 12px 16px;
                border-radius: 5px;
                color: #90A4AE;
            }
            QPushButton:hover {
                background-color: #0089CD;
                color: white;
            }
        """)

        # Liste complète des emojis
        self.emojis = [
           "😀","😁","😂","🤣","😃","😄","😅","😆","😉","😊",
           "😋","😎","😍","😘","😗","😙","😚","☺️","🙂","🤗",
           "🤩","🤔","🤨","😐","😑","😶","🙄","😏","😣","😥",
           "😮","🤐","😯","😪","😫","😴","😌","😛","😜","😝",
           "🤤","😒","😓","😔","😕","🙃","🤑","😲","☹️","🙁"
        ]

        self.emojis_per_page = emojis_per_page
        self.current_page = 0
        self.total_pages = (len(self.emojis) - 1) // self.emojis_per_page + 1

        self.selected_emoji = None

        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(20, 20, 20, 20)

        # Zone pour le grid emojis
        self.grid = QGridLayout()
        self.grid.setSpacing(10)
        self.layout.addLayout(self.grid)

        # Navigation + Annuler
        nav_layout = QHBoxLayout()
        self.prev_btn = QPushButton("←")
        self.prev_btn.clicked.connect(self.page_precedente)
        self.next_btn = QPushButton("→")
        self.next_btn.clicked.connect(self.page_suivante)
        nav_layout.addWidget(self.prev_btn)
        nav_layout.addStretch()
        cancel_btn = QPushButton("Annuler")
        cancel_btn.clicked.connect(self.reject)
        nav_layout.addWidget(cancel_btn)
        nav_layout.addStretch()
        nav_layout.addWidget(self.next_btn)

        self.layout.addLayout(nav_layout)

        self.update_page()

    def update_page(self):
        # Vider l'ancien contenu
        for i in reversed(range(self.grid.count())):
            widget = self.grid.itemAt(i).widget()
            if widget:
                widget.setParent(None)

        # Calcul des emojis à afficher
        start = self.current_page * self.emojis_per_page
        end = start + self.emojis_per_page
        page_emojis = self.emojis[start:end]

        row, col = 0, 0
        for emoji in page_emojis:
            btn = QPushButton(emoji)
            btn.clicked.connect(lambda _, e=emoji: self.select_emoji(e))
            btn.setFixedSize(60, 60)
            self.grid.addWidget(btn, row, col)
            col += 1
            if col >= 5:
                col = 0
                row += 1

        # Gestion des boutons suivant/precedent
        self.prev_btn.setEnabled(self.current_page > 0)
        self.next_btn.setEnabled(self.current_page < self.total_pages - 1)

    def page_precedente(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.update_page()

    def page_suivante(self):
        if self.current_page < self.total_pages - 1:
            self.current_page += 1
            self.update_page()

    def select_emoji(self, emoji):
        self.selected_emoji = emoji
        self.accept()

    def get_emoji(self):
        return self.selected_emoji

class Info(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ajouter un lien")
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setStyleSheet("""
            QDialog{
                background-color: #181818; 
                color: white; 
                border: 1px solid #2B2B2B;
            }
            QLabel {
                color: #90A4AE;
                font-family: Inter;
                font-size: 22px;
            }
            QPushButton {
                background-color: #1F1F1F;
                border: none;
                font-family: Inter;
                font-size: 22px;
                padding: 12px 16px;
                border-radius: 5px;
                color: #90A4AE;
            }
            QPushButton:hover {
                background-color: #0089CD;
                color: white;
            }
        """)

        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(40, 40, 40, 40)

        inf = QLabel("Informations")
        inf.setStyleSheet("font-size: 32px;font-weight:600;")
        self.layout.addWidget(inf)
        self.layout.addWidget(QLabel("📄 Nom : Document.md (non enregistré → 'Sans titre' sinon)"))
        self.layout.addWidget(QLabel("📁 Chemin : C:/Users/Utilisateur/Desktop/Document.md (ou 'Non enregistré')"))
        self.layout.addWidget(QLabel("🛠️ Format : HTML enrichi (compatible Markdown)"))
        self.layout.addWidget(QLabel("📦 Taille : 12.4 Ko"))
        self.layout.addWidget(QLabel("🔠 Caractères : 1 523"))
        self.layout.addWidget(QLabel("📝 Mots : 248"))
        self.layout.addWidget(QLabel("🌐 Langue détectée : Français (France)"))
        self.layout.addWidget(QLabel("⏰ Dernière modification : 22/06/2025 à 23:45"))
        self.layout.addWidget(QLabel("⏳ Temps écoulé : 14 min 32 s"))
        self.layout.addWidget(QLabel("🔁 Modifications : 42 actions"))
        
        self.cancel_btn = QPushButton("Fermer")
        self.cancel_btn.clicked.connect(self.reject)
        self.layout.addWidget(self.cancel_btn)