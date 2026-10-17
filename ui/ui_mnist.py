import customtkinter as ctk
from .drawingcanvas import DrawingCanvas
from .utils import get_input


# --- Palette ---
BG        = "#0f0f1a"   # fond quasi-noir bleuté
PANEL     = "#1a1a2e"   # panneau gauche, légèrement plus clair
CANVAS_BG = "#f8f8f5"   # zone de dessin blanc cassé
ACCENT    = "#7c6af7"   # violet doux — couleur principale
TEXT_DIM  = "#6b7280"   # texte secondaire
TEXT_MAIN = "#e8e8f0"   # texte principal


class KoalaMNIST(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("KOALA — MNIST")
        self.minsize(760, 520)
        self.configure(fg_color=BG)

        ctk.set_appearance_mode("dark")

        self._build_left_panel()
        self._build_right_panel()

    # ------------------------------------------------------------------ #
    #  Panneau gauche — zone de dessin
    # ------------------------------------------------------------------ #
    def _build_left_panel(self):
        panel = ctk.CTkFrame(
            self,
            fg_color=PANEL,
            corner_radius=16,
        )
        panel.pack(side="left", fill="y", padx=(20, 10), pady=20)

        # Titre du panneau
        ctk.CTkLabel(
            panel,
            text="Zone de dessin",
            font=("Inter", 11),
            text_color=TEXT_DIM,
        ).pack(side="top", pady=(18, 2))

        ctk.CTkLabel(
            panel,
            text="Dessine un chiffre",
            font=("Inter", 16, "bold"),
            text_color=TEXT_MAIN,
        ).pack(side="top", pady=(0, 12))

        # Wrapper avec bordure colorée simulée via un CTkFrame
        canvas_border = ctk.CTkFrame(
            panel,
            fg_color=ACCENT,
            corner_radius=12,
        )
        canvas_border.pack(side="top", padx=16, pady=0)

        # Canvas lui-même à l'intérieur (padding de 2px = l'épaisseur de la bordure)
        self.canvas = DrawingCanvas(canvas_border)
        self.canvas.pack(padx=2, pady=2)

        # Boutons
        btn_frame = ctk.CTkFrame(panel, fg_color="transparent")
        btn_frame.pack(side="top", fill="x", padx=16, pady=(14, 18))

        ctk.CTkButton(
            btn_frame,
            text="Reconnaître",
            font=("Inter", 13, "bold"),
            fg_color=ACCENT,
            hover_color="#6356d4",
            corner_radius=10,
            height=38,
            command=self.find_number,
        ).pack(side="left", expand=True, fill="x", padx=(0, 6))

        ctk.CTkButton(
            btn_frame,
            text="Effacer",
            font=("Inter", 13),
            fg_color="#2a2a3e",
            hover_color="#33334d",
            corner_radius=10,
            height=38,
            command=self.clear_canvas,
        ).pack(side="left", expand=True, fill="x", padx=(6, 0))

    # ------------------------------------------------------------------ #
    #  Panneau droit — résultat
    # ------------------------------------------------------------------ #
    def _build_right_panel(self):
        panel = ctk.CTkFrame(self, fg_color="transparent")
        panel.pack(side="left", fill="both", expand=True, padx=(10, 20), pady=20)

        # Centrage vertical avec un frame intérieur
        inner = ctk.CTkFrame(panel, fg_color="transparent")
        inner.place(relx=0.5, rely=0.5, anchor="center")

        ctk.CTkLabel(
            inner,
            text="résultat",
            font=("Inter", 12),
            text_color=TEXT_DIM,
        ).pack()

        self.result_number = ctk.CTkLabel(
            inner,
            text="?",
            font=("Inter", 96, "bold"),
            text_color=ACCENT,
        )
        self.result_number.pack()

        self.result_sub = ctk.CTkLabel(
            inner,
            text="dessine quelque chose",
            font=("Inter", 13),
            text_color=TEXT_DIM,
        )
        self.result_sub.pack(pady=(4, 0))

    # ------------------------------------------------------------------ #
    #  Logique
    # ------------------------------------------------------------------ #
    def find_number(self):
        confiance ,num  = get_input(self.canvas.image)
        # nb = 4
        self.result_number.configure(text=str(num))
        self.result_sub.configure(text=f"confiance : {confiance}%")  # placeholder

    def clear_canvas(self):
        self.canvas.clear()
        self.result_number.configure(text="?")
        self.result_sub.configure(text="dessine quelque chose (un chiffre a la fois please)")


if __name__ == "__main__":
    app = KoalaMNIST()
    app.mainloop()