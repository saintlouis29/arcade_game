"""
Un module pour le vaisseau
                                   _     _
                                  | |   (_)
     ___ _ __   __ _  ___ ___  ___| |__  _ _ __
    / __| '_ \ / _` |/ __/ _ \/ __| '_ \| | '_ \.
    \__ \ |_) | (_| | (_|  __/\__ \ | | | | |_) |
    |___/ .__/ \__,_|\___\___||___/_| |_|_| .__/
        | |                               | |
        |_|                               |_|
                     `. ___
                    __,' __`.                _..----....____
        __...--.'``;.   ,.   ;``--..__     .'    ,-._    _.-'
  _..-''-------'   `'   `'   `'     O ``-''._   (,;') _,'
,'________________                          \`-._`-','
 `._              ```````````------...___   '-.._'-:
    ```--.._      ,.                     ````--...__\-.
            `.--. `-`                       ____    |  |`
              `. `.                       ,'`````.  ;  ;`
                `._`.        __________   `.      \'__/`
                   `-:._____/______/___/____`.     \  `
                               |       `._    `.    \.
                               `._________`-.   `.   `.___
                                                  `------'`
"""

import pyxel

# =====================================================
# SPACESHIP
# =====================================================

class Spaceship :
    """
    Une classe pour notre vaisseau
    """
    def __init__(self, game, x, y):
        """Initialisation du vaisseau
        :param game: L'instance du jeu
        :type game: Game
        :param x: L'abscisse du coin supérieur gauche
        :type x: int
        :param y: L'ordonnée du coin supérieur gauche
        :type y: int
        """
        self.game = game
        # position initiale du vaisseau
        self.x = x
        self.y = y
        # largeur (width) et hauteur du vaisseau (height)
        self.w = 8
        self.h = 8
        self.shoots = []

    # =====================================================
    # == UPDATE
    # =====================================================
    def update(self):
        """Mise à jour du vaisseau (30FPS)
        """
        self._move()
        self._shoot()

    def _move(self):
        """déplacement avec les touches de directions"""
        if pyxel.btn(pyxel.KEY_RIGHT) and self.x < self.game.w - self.w:
            self.x += 2
        if pyxel.btn(pyxel.KEY_LEFT) and self.x > 0:
            self.x -= 2
        if pyxel.btn(pyxel.KEY_UP) and self.y > 0:
            self.y -= 2
        if pyxel.btn(pyxel.KEY_DOWN) and self.y < self.game.h - self.h:
            self.y += 2

    def _shoot(self):
        if pyxel.btn(pyxel.KEY_SPACE):
            shoot = Shoot(self, self.x, self.y)
            self.shoots.append(shoot)

    # =====================================================
    # == DRAW
    # =====================================================
    def draw(self):
        """
        Dessin du vaisseau
        """
        pyxel.blt(self.x, self.y, 0, 0, 0, 8, 8)

# =====================================================
# SHOOT
# =====================================================

class Shoot:
    """
    Une classe pour nos tirs
    """
    def __init__(self, spaceship, x, y):
        """Une classe pour les tirs du vaisseau

        :param spaceship: le vaisseau d'où provient le tir
        :type spaceship: SpaceShip
        :param x: L'abscisse du coin supérieur gauche
        :type x: int
        :param y: L'ordonnée du coin supérieur gauche
        :type y: int
        """
        self.spaceship = spaceship
        # position initiale du vaisseau
        self.x = x+2
        self.y = y
        # largeur (width) et hauteur du vaisseau (height)
        self.w = 4
        self.h = 6

    # =====================================================
    # == UPDATE
    # =====================================================
    def update(self):
        """Mise à jour
        """
        self._move()

    def _move(self):
        """déplacement"""
        self.y -= 2

    # =====================================================
    # == DRAW
    # =====================================================
    def draw(self):
        """
        Dessin du tir
        """
        pyxel.blt(self.x, self.y, 0, 10, 1, self.w, self.h)
