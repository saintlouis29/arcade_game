"""Un module pour les ennemis"""


import pyxel

# =====================================================
# ENNEMY
# =====================================================

class Enemy :
    """
    Une classe pour les ennemis
    """
    def __init__(self, game, x, y):
        """Initialisation de l'ennemi
        :param game: L'instance du jeu
        :type game: Game
        :param x: L'abscisse du coin supérieur gauche
        :type x: int
        :param y: L'ordonnée du coin supérieur gauche
        :type y: int
        """
        self.game = game
        # position initiale de l'ennemi
        self.x = x
        self.y = y
        # largeur (width) et hauteur de l'ennemi (height)
        self.w = 8
        self.h = 8

    # =====================================================
    # == UPDATE
    # =====================================================
    def update(self):
        """Mise à jour de l'ennemi (30FPS)
        """
        self._move()

    def _move(self):
        """déplacement vers le bas de l'ennemi"""
        self.y +=2

    # =====================================================
    # == DRAW
    # =====================================================
    def draw(self):
        """
        Dessin d'un ennemi
        """
        pyxel.blt(self.x, self.y, 0, 0, 8, 8, 8)
