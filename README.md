# 🎮 MiniGame -- TicTacToe & Four Connect

Dieses Projekt implementiert ein kleines Konsolen-Spiel in Python:\
- **TicTacToe (3x3)** - **Vier Gewinnt (5x5, vereinfachte Version)**

Das Spielfeld wird mithilfe von **pandas.DataFrame** dargestellt und in
der Konsole ausgegeben.

------------------------------------------------------------------------

## 📂 Inhalt

-   **Spielstart**: Auswahl zwischen TicTacToe und Vier Gewinnt
-   **Spielerwechsel**: Spieler 1 (Standard: `x`) und Spieler 2
    (Standard: `o`)
-   **Züge**:
    -   TicTacToe → Eingabe z. B. `A1`, `B3`
    -   Vier Gewinnt → Eingabe Spalte, z. B. `A`, `C`
-   **Spiellogik**:
    -   Abwechselnde Züge
    -   Figuren fallen in Spalten herunter (bei Vier Gewinnt)
    -   Belegte Felder können nicht überschrieben werden
-   **Konfiguration**: Spielerfiguren können zu Beginn angepasst werden

------------------------------------------------------------------------

## ⚙️ Installation

### 1. Repository klonen

    git clone https://github.com/deinusername/minigame.git
    cd minigame

### 2. Virtuelle Umgebung erstellen (optional, empfohlen)

    python -m venv venv
    source venv/bin/activate   # Linux/Mac
    venv\Scripts\activate      # Windows

### 3. Abhängigkeiten installieren

    pip install -r requirements.txt

------------------------------------------------------------------------

## 📊 Verwendung

    python minigame.py

-   Zuerst wird das Spiellayout abgefragt (1 = TicTacToe, 2 = Vier
    Gewinnt).
-   Danach können die Spieler optional ihre Spielfiguren konfigurieren.
-   Anschließend läuft das Spiel rundenbasiert im Terminal.

------------------------------------------------------------------------

## 📦 Benötigte Libraries

-   pandas\
-   numpy

------------------------------------------------------------------------

## 🚀 Nächste Schritte / Ideen

-   Gewinnlogik implementieren (aktuell nur Spielfelder, keine
    automatische Gewinnerkennung).\
-   Erweiterung von Vier Gewinnt auf echtes 6x7-Brett.\
-   GUI-Version mit Tkinter oder Pygame.

------------------------------------------------------------------------

## 📜 Lizenz

Dieses Projekt steht unter der **MIT Lizenz**.
