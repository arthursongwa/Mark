from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,QGridLayout,
    QLabel, QTextEdit, QFrame, QPushButton, QLineEdit, QFileDialog, QInputDialog, QMessageBox
)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QFont, QTextCursor, QTextCharFormat, QTextTableFormat, QTextBlockFormat

from classe import LienDialog, TableauDialog, BarreTitre, Tool, EmojiDialog, Info
from random import randint
import sys
import logs as lg
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QHBoxLayout

class MarkdownEditor(QWidget):
    def __init__(self):
        super().__init__()
        lg.logging.info("Initialisation de la fenetre principale")

        # Fenetre principale
        self.setWindowTitle("Mark")
        self.setGeometry(randint(0, 300), 50, 1600, 980)
        self.setStyleSheet("background-color: #181818; color: #90A4AE;")
        self.setWindowFlags(Qt.FramelessWindowHint)
        lg.logging.debug("Configuration fenetre principale appliquee")

        self.barre_titre = BarreTitre(self)
        self.style_copied = None
        self.pinceau_actif = False
        lg.logging.debug("Barre de titre creee")

        # ─────────────── HEADER ───────────────
        self.tool1 = Tool(colonnes=2)
        self.tool1.ajouter_bouton("Nouveau.", self.nouveau_fichier, tooltip="Creer un nouveau fichier")
        self.tool1.ajouter_bouton("Ouvrir.", self.ouvrir_fichier, tooltip="Ouvrir un fichier .md")
        self.tool1.ajouter_bouton("Sauvegarder.", self.save, tooltip="Sauvegarder le fichier")
        self.tool1.ajouter_bouton("Informations.", self.show_info, tooltip="Afficher les informations du document")
        lg.logging.debug("Tool1 (fichier) initialise")

        self.tool2 = Tool(colonnes=2)
        self.tool2.ajouter_bouton("G.", lambda: self.toggle_style("bold"), tooltip="Gras", tag="bold")
        self.tool2.ajouter_bouton("I.", lambda: self.toggle_style("italic"), tooltip="Italique", tag="italic")
        self.tool2.ajouter_bouton("S.", lambda: self.toggle_style("underline"), tooltip="Souligne", tag="underline")
        self.tool2.ajouter_bouton("ab.", lambda: self.toggle_style("strike"), tooltip="Barre", tag="strike")
        lg.logging.debug("Tool2 (styles texte) initialise")

        self.tool3 = Tool(colonnes=2)
        self.tool3.ajouter_bouton("Lien.", self.inserer_lien, "Inserer un lien", "ui/icons/add_link.png")
        self.tool3.ajouter_bouton("Tableau.", self.inserer_tableau, "Inserer un tableau", "ui/icons/table.png")
        self.tool3.ajouter_bouton("Image.", self.inserer_image, "Inserer une image", "ui/icons/add_photo.png", tag="image")
        lg.logging.debug("Tool3 (insertion) initialise")

        self.tool4 = Tool(colonnes=2)
        self.tool4.ajouter_bouton(".", lambda: self.alignement(Qt.AlignLeft), "Aligner a gauche", "ui/icons/align_left.png", tag="left")
        self.tool4.ajouter_bouton(".", lambda: self.alignement(Qt.AlignCenter), "Centrer le texte", "ui/icons/align_center.png", tag="center")
        self.tool4.ajouter_bouton(".", lambda: self.alignement(Qt.AlignRight), "Aligner a droite", "ui/icons/align_right.png", tag="right")
        self.tool4.ajouter_bouton(".", lambda: self.alignement(Qt.AlignJustify), "Justifier le texte", "ui/icons/align_justify.png", tag="justify")
        lg.logging.debug("Tool4 (alignement) initialise")

        self.tool5 = Tool(colonnes=2)
        self.tool5.ajouter_bouton(".", lambda: self.changer_indentation(-1), "Diminuer le retrait", "ui/icons/indent_decrease.png")
        self.tool5.ajouter_bouton(".", lambda: self.changer_indentation(1), "Augmenter le retrait", "ui/icons/indent_increase.png")
        self.tool5.ajouter_bouton(".", self.inserer_liste_num, "Creer une liste numerotee", "ui/icons/list_numbered.png", tag="num")
        self.tool5.ajouter_bouton(".", self.inserer_liste_puce, "Creer une liste a puces", "ui/icons/list_bulleted.png", tag="puce")
        lg.logging.debug("Tool5 (listes et retraits) initialise")

        self.tool6 = Tool(colonnes=2)
        self.tool6.ajouter_bouton(".", self.coller, "Coller", "ui/icons/paste.png")
        self.tool6.ajouter_bouton(".", self.couper, "Couper", "ui/icons/cut.png")
        self.tool6.ajouter_bouton(".", self.copier, "Copier", "ui/icons/copy.png")
        # self.tool6.ajouter_bouton("", self.activer_pinceau, "Appliquer le style (pinceau)", "ui/icons/paint.png")
        lg.logging.debug("Tool6 (edition) initialise")

        self.tool7 = Tool(colonnes=2)
        self.tool7.ajouter_bouton("H1.", lambda: self.toggle_style("h1"), tooltip="Titre 1", tag="h1")
        self.tool7.ajouter_bouton("H2.", lambda: self.toggle_style("h2"), tooltip="Titre 2", tag="h2")
        self.tool7.ajouter_bouton("H3.", lambda: self.toggle_style("h3"), tooltip="Titre 3", tag="h3")
        self.tool7.ajouter_bouton("H4.", lambda: self.toggle_style("h4"), tooltip="Titre 4", tag="h4")
        lg.logging.debug("Tool7 (titres) initialise")

        self.tool8 = Tool(colonnes=2)
        self.tool8.ajouter_bouton(".", self.inserer_citation, tooltip="Ajouter une note", icon_path="ui/icons/note_add.png")
        # self.tool8.ajouter_bouton("", lambda: self.toggle_style("h2"), tooltip="Ajouter une checklist", icon_path="ui/icons/checklist.png")
        self.tool8.ajouter_bouton(".", self.inserer_emoji, tooltip="Ajouter un emoji", icon_path="ui/icons/add_reaction.png")
        self.tool8.ajouter_bouton(".", self.inserer_separateur, tooltip="Ajouter une ligne de separateur", icon_path="ui/icons/flip.png")
        lg.logging.debug("Tool8 (ajout de contenu : note, checklist, section, emoji) initialise")

        self.tool_with_tags = [self.tool2, self.tool7, self.tool4, self.tool5]  # Ajoute ici tous les Tool contenant des boutons de style

        self.header = QFrame()
        self.header.setFixedHeight(150)
        self.header.setStyleSheet("""
            QFrame {
                border-bottom: 1px solid #2B2B2B;
                font-family: Inter;
                font-size: 24px;
            }
            QLabel {
                border: 0;
            }
        """)
        self.header_layout = QHBoxLayout()
        self.header_layout.setContentsMargins(0, 0, 0, 0)
        self.header_layout.addWidget(self.tool1)
        self.header_layout.addStretch()
        self.header_layout.addWidget(self.tool2)
        self.header_layout.addStretch()
        self.header_layout.addWidget(self.tool7)
        self.header_layout.addStretch()
        self.header_layout.addWidget(self.tool3)
        self.header_layout.addStretch()
        self.header_layout.addWidget(self.tool8)
        self.header_layout.addStretch()
        self.header_layout.addWidget(self.tool4)
        self.header_layout.addStretch()
        self.header_layout.addWidget(self.tool5)
        self.header_layout.addStretch()
        self.header_layout.addWidget(self.tool6)
        self.header_layout.addStretch()
        self.header.setLayout(self.header_layout)
        lg.logging.debug("Header configure et widgets ajoutes")

        # ─────────────── TEXT EDITOR ───────────────
        self.text_edit = QTextEdit()
        self.text_edit.setFont(QFont("Inter", 14)) 
        self.text_edit.cursorPositionChanged.connect(self.mettre_a_jour_etat_boutons)
        self.text_edit.cursorPositionChanged.connect(self.mettre_a_jour_etat_alignement)
        self.text_edit.textChanged.connect(lambda: self.footer_nbrMot.setText(f"{len(self.text_edit.toPlainText().split())} mots"))
        self.text_edit.setStyleSheet("""
            QTextEdit {
                background-color: #1F1F1F;
                color: #90A4AE;
                border: 1px solid #2B2B2B;
                border-bottom: 0;
                border-bottom-left-radius: 0px;
                border-bottom-right-radius: 0px;
                border-top-left-radius: 5px;
                border-top-right-radius: 5px;
                padding: 100px;
            }
            hr{ border: 1px solid #90A4AE;}
            QScrollBar:vertical {
                background: #181818;
                width: 14px;
                margin: 0px;
                border: none;
            }

            QScrollBar::handle:vertical {
                background: #0089CD;
                min-height: 30px;
                border-radius: 5px;
            }

            QScrollBar::add-line:vertical,
            QScrollBar::sub-line:vertical {
                background: none;
                height: 0px;
            }

            QScrollBar::add-page:vertical,
            QScrollBar::sub-page:vertical {
                background: none;
            }
        """)
        lg.logging.debug("editeur de texte initialise")

        # ─────────────── CONTAINER CENTRAL ───────────────
        self.container = QFrame()
        self.container.setContentsMargins(0, 0, 0, 0)

        self.container_layout = QVBoxLayout()
        self.container_layout.setContentsMargins(100, 30, 100, 0)
        self.container_layout.addWidget(self.text_edit)

        self.container.setLayout(self.container_layout)
        lg.logging.debug("Container central configure")

        # ─────────────── FOOTER ───────────────
        self.footer = QFrame()
        self.footer.setStyleSheet("""
            QFrame {
                border-top: 1px solid #2B2B2B;
                font-family: Inter;
                font-size: 16px;
            }
            QLabel {
                border: 0;
            }
        """)

        self.footer_layout = QHBoxLayout()
        self.footer_layout.setContentsMargins(50, 10, 50, 10)
        self.footer_nbrMot = QLabel("0 mot")    
        self.footer_layout.addWidget(self.footer_nbrMot)
        self.footer_layout.addStretch()
        self.footer_layout.addWidget(QLabel("0% ---- 100% ---- 200%"))
        self.footer_layout.addStretch()
        self.footer_layout.addWidget(QLabel("Français (France)"))
        self.footer.setLayout(self.footer_layout)
        lg.logging.debug("Footer configure")

        # ─────────────── LAYOUT PRINCIPAL ───────────────
        self.main_layout = QVBoxLayout()
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.addWidget(self.barre_titre)
        self.main_layout.addWidget(self.header)
        self.main_layout.addWidget(self.container)
        self.main_layout.addWidget(self.footer)

        self.setLayout(self.main_layout)
        lg.logging.info("Initialisation complete de la fenetre principale terminee")
    
    def mettre_a_jour_etat_boutons(self):
        fmt = self.text_edit.currentCharFormat()
        for tool in self.tool_with_tags:
            tool.mettre_a_jour_etat_boutons(fmt)
    
    def mettre_a_jour_etat_alignement(self):
        alignment = self.text_edit.textCursor().blockFormat().alignment()
        
        self.tool4.boutons[0].setChecked(alignment == Qt.AlignLeft)
        self.tool4.boutons[1].setChecked(alignment == Qt.AlignCenter)
        self.tool4.boutons[2].setChecked(alignment == Qt.AlignRight)
        self.tool4.boutons[3].setChecked(alignment == Qt.AlignJustify)
        
        lg.logging.debug("Etat des boutons mis a jour")
        
    def toggle_style(self, style: str):
        lg.logging.debug(f"Toggling style : {style}")
        cursor = self.text_edit.textCursor()
        if not cursor.hasSelection():
            lg.logging.debug("Aucune selection, selection du mot sous le curseur")
            cursor.select(QTextCursor.WordUnderCursor)

        char_format = cursor.charFormat()
        new_format = QTextCharFormat(char_format)

        # ─── STYLES BASIQUES ───────────────────────────────────────────────
        if style == "bold":
            etat = QFont.Normal if char_format.fontWeight() > QFont.Normal else QFont.Bold
            new_format.setFontWeight(etat)
            lg.logging.debug(f"Changement fontWeight : {etat}")

        elif style == "italic":
            lg.logging.debug(f"Changement italic : {not char_format.fontItalic()}")
            new_format.setFontItalic(not char_format.fontItalic())

        elif style == "underline":
            lg.logging.debug(f"Changement underline : {not char_format.fontUnderline()}")
            new_format.setFontUnderline(not char_format.fontUnderline())

        elif style == "strike":
            lg.logging.debug(f"Changement strikeout : {not char_format.fontStrikeOut()}")
            new_format.setFontStrikeOut(not char_format.fontStrikeOut())

        # ─── TITRES (H1 a H4) ──────────────────────────────────────────────
        elif style == "h1":
            new_format.setFontPointSize(32 if char_format.fontPointSize() < 32 else 14)
            new_format.setFontWeight(QFont.Bold)
            lg.logging.debug("Changement titre H1")

        elif style == "h2":
            new_format.setFontPointSize(26 if char_format.fontPointSize() < 26 else 14)
            new_format.setFontWeight(QFont.Bold)
            lg.logging.debug("Changement titre H2")

        elif style == "h3":
            new_format.setFontPointSize(22 if char_format.fontPointSize() < 22 else 14)
            new_format.setFontWeight(QFont.Bold)
            lg.logging.debug("Changement titre H3")

        elif style == "h4":
            new_format.setFontPointSize(18 if char_format.fontPointSize() < 18 else 14)
            new_format.setFontWeight(QFont.Bold)
            lg.logging.debug("Changement titre H4")

        # ─── APPLICATION ───────────────────────────────────────────────────
        cursor.mergeCharFormat(new_format)
        self.text_edit.mergeCurrentCharFormat(new_format)
        self.text_edit.setFocus()
        lg.logging.debug("Style applique avec succes")

    def show_info(self):
        info = Info()
        if info.exec_() == QDialog.Accepted:
            pass
        else:
            lg.logging.debug("Insertion de lien annulee par l'utilisateur")
    
    def inserer_image(self):
        lg.logging.debug("Ouverture de la boîte de dialogue pour choisir une image")
        chemin_image, _ = QFileDialog.getOpenFileName(
            self,
            "Choisir une image",
            "",
            "Images (*.png *.jpg *.jpeg *.bmp *.gif);;Tous les fichiers (*)"
        )
        
        if chemin_image:
            lg.logging.debug(f"Image selectionnee : {chemin_image}")
            cursor = self.text_edit.textCursor()
            balise_img = f'<img src="{chemin_image}" width="300" />'
            cursor.insertHtml(balise_img)
            self.text_edit.setFocus()
            lg.logging.debug("Image inseree dans le QTextEdit")
        else:
            lg.logging.debug("Aucune image selectionnee")

    def inserer_lien(self):
        lg.logging.debug("Demande d'insertion de lien")

        cursor = self.text_edit.textCursor()
        texte_selectionne = cursor.selectedText().strip()

           
        # Lancement du popup
        dlg = LienDialog(texte_selectionne)
        if dlg.exec_() == QDialog.Accepted:
            texte, url = dlg.get_data()
            if texte and url:
                lg.logging.debug(f"Insertion lien : Texte='{texte}', URL='{url}'")
                lien_html = f'<a href="{url}" style="color: #90A4AE; cursor: pointer;">{texte}</a>'
                cursor.insertHtml(lien_html)
            else:
                lg.logging.debug("Texte ou URL vide - insertion annulee")
        else:
            lg.logging.debug("Insertion de lien annulee par l'utilisateur")
    
    def inserer_tableau(self):
        dialog = TableauDialog()
        if dialog.exec_() == QDialog.Accepted:
            lignes, colonnes = dialog.get_data()
            lg.logging.debug(f"Insertion tableau {lignes}x{colonnes}")

            html = '<table border="2" cellspacing="0" cellpadding="6" style="border-collapse: collapse; width: 100%; color: #90A4AE; font-family: Inter;">'
            for _ in range(lignes):
                html += '<tr>'
                for _ in range(colonnes):
                    html += '<td style="border: 2px solid #90A4AE;"> Value </td>'
                html += '</tr>'
            html += '</table><br>'

            cursor = self.text_edit.textCursor()
            cursor.insertHtml(html)
            self.text_edit.setFocus()
        else:
            lg.logging.debug("Insertion tableau annulee")
        # dlg = TableauDialog()
        # if dlg.exec_():
        #     rows, cols = dlg.get_data()
        #     lg.logging.debug(f"Insertion tableau {rows}x{cols}")
        #     cursor = self.text_edit.textCursor()
        #     fmt = QTextTableFormat()
        #     fmt.setBorder(1)
        #     fmt.setBorderStyle(QTextTableFormat.BorderStyle_Solid)
        #     fmt.setCellPadding(6)
        #     fmt.setCellSpacing(2)
        #     fmt.setAlignment(Qt.AlignLeft)
        #     cursor.insertTable(rows, cols, fmt)
        # else:
        #     lg.logging.debug("Insertion tableau annulee")
    
    def inserer_separateur(self):
        lg.logging.debug("Insertion d'une ligne de separation (table HTML)")

        html = """
        <table width="100%" cellspacing="0" cellpadding="0" style="margin-top: 8px; margin-bottom: 8px;">
            <tr><td style="border-bottom: 1px solid #90A4AE;"></td></tr>
        </table>
        """
        cursor = self.text_edit.textCursor()
        cursor.insertHtml(html)
        self.text_edit.setFocus()
    
    def inserer_citation(self):
        lg.logging.debug("Insertion d'une citation")

        cursor = self.text_edit.textCursor()
        if cursor.hasSelection():
            texte = cursor.selectedText()
        else:
            texte = "Votre citation ici..."

        # Encapsule dans un tableau a 1 cellule avec style bloc
        citation_html = f"""
        <table width="100%" cellspacing="0" cellpadding="0" style="margin: 16px 0;">
            <tr>
                <td style="
                    background-color: #181818;
                    border-left: 4px solid #0089CD;
                    padding: 12px 16px;
                    color: #90A4AE;
                    font-style: italic;
                    border-radius: 5px;
                ">
                    {texte}
                </td>
            </tr>
        </table>
        """
        cursor.insertHtml(citation_html)
        self.text_edit.setFocus()

    def exporter_en_markdown(self):
        with open("chemin.html", "w", encoding="utf-8") as f:
            f.write(self.text_edit.toHtml())
    
    def nouveau_fichier(self):
        lg.logging.info("Ouverture d'un nouveau fichier")
        self.nouveau_fichier_instance = MarkdownEditor()  # Cree une nouvelle instance
        self.nouveau_fichier_instance.show()
    
    def ouvrir_fichier(self):
        chemin_fichier, _ = QFileDialog.getOpenFileName(
            self,
            "Ouvrir un fichier Markdown",
            "",
            "Fichiers Markdown (*.md);;Tous les fichiers (*)"
        )

        if chemin_fichier:
            try:
                with open(chemin_fichier, "r", encoding="utf-8") as f:
                    contenu = f.read()
                    self.text_edit.setPlainText(contenu)
                    lg.logging.info(f"Fichier ouvert : {chemin_fichier}")
            except Exception as e:
                lg.logging.error(f"Erreur lors de l'ouverture du fichier : {e}")
                QMessageBox.critical(self, "Erreur", f"Impossible d'ouvrir le fichier :\n{e}")

    def inserer_emoji(self):
        lg.logging.debug("Demande d'insertion d'emoji")
        dialog = EmojiDialog()
        if dialog.exec_():
            emoji = dialog.get_emoji()
            if emoji:
                self.text_edit.insertPlainText(emoji)
                self.text_edit.setFocus()
                lg.logging.info(f"Emoji insere : {emoji}")
    
    def copier(self):
        self.text_edit.copy()
        lg.logging.debug("Texte copie dans le presse-papiers")

    def coller(self):
        self.text_edit.paste()
        lg.logging.debug("Texte colle depuis le presse-papiers")

    def couper(self):
        self.text_edit.cut()
        lg.logging.debug("Texte coupe et copie dans le presse-papiers")

    def save(self):
        with open(f"{self.barre_titre.input_nom.text()}.md", "w", encoding="utf-8") as file:
            file.write(self.text_edit.toHtml())
        lg.logging.info(f"Fichier sauvegarder sous le nom de {self.barre_titre.input_nom.text()}")

    def inserer_liste_puce(self):
        cursor = self.text_edit.textCursor()
        lg.logging.debug("Insertion de liste a puces")

        if not cursor.hasSelection():
            # Si aucune selection, insère une liste vide prête a remplir
            cursor.insertHtml("<ul><li>element</li></ul>")
        else:
            # Transforme chaque ligne selectionnee en <li>
            texte = cursor.selectedText()
            lignes = texte.split('\u2029')  # Separation de paragraphes dans QTextEdit
            html = "<ul>" + "".join(f"<li>{ligne}</li>" for ligne in lignes if ligne.strip()) + "</ul>"
            cursor.insertHtml(html)

        self.text_edit.setFocus()

    def inserer_liste_num(self):
        cursor = self.text_edit.textCursor()
        lg.logging.debug("Insertion de liste numerotee")

        if not cursor.hasSelection():
            cursor.insertHtml("<ol><li>element</li></ol>")
        else:
            texte = cursor.selectedText()
            lignes = texte.split('\u2029')
            html = "<ol>" + "".join(f"<li>{ligne}</li>" for ligne in lignes if ligne.strip()) + "</ol>"
            cursor.insertHtml(html)

        self.text_edit.setFocus()

    def alignement(self, mode):
        lg.logging.debug(f"Alignement demande : {mode}")
        cursor = self.text_edit.textCursor()
        block_format = cursor.blockFormat()
        block_format.setAlignment(mode)
        cursor.mergeBlockFormat(block_format)
        self.text_edit.setTextCursor(cursor)
        self.text_edit.setFocus()

        self.mettre_a_jour_etat_alignement()

    def changer_indentation(self, direction: int):
        """
        direction = +1 pour augmenter, -1 pour diminuer
        """
        cursor = self.text_edit.textCursor()
        block_format = cursor.blockFormat()

        current_indent = block_format.leftMargin()
        step = 20  # px par clic
        new_indent = max(0, current_indent + direction * step)

        block_format.setLeftMargin(new_indent)
        cursor.mergeBlockFormat(block_format)
        self.text_edit.setTextCursor(cursor)

        lg.logging.debug(f"Indentation {'augmentee' if direction > 0 else 'diminuee'} a {new_indent}px")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    editor = MarkdownEditor()
    editor.show()
    sys.exit(app.exec_())
