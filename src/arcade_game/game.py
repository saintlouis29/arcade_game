"""
le module principal du projet arcade_game

                  :: ::::: ::
                  :: ::::: ::
                  :: ::::: ::
                  :: ::::: ::
                  :: ::::: ::


                 .:: ::::: ::.
                .::: ::::: :::.
               .:::' ::::: ':::.
              .::::' ::::: '::::.
             .::::'  :::::  '::::.
           .:::::'   :::::   ':::::.
         .::::::'    :::::    '::::::.
    ...:::::::'      :::::      ':::::::...
    :::::::''        :::::        '':::::::
    ::::''           :::::           ''::::

      _______ _______ _______ ______  ___
     |   _   |       |   _   |   _  \|   |(R)
     |.  1   |.|   | |.  1   |.  l   |.  |
     |.  _   `-|.  |-|.  _   |.  _  <|.  |
     |:  |   | |:  | |:  |   |:  |   |:  |
     |::.|:. | |::.| |::.|:. |::.|:. |::.|
     `--- ---' `---' `--- ---`--- ---`---'

"""

import random
import pyxel

from arcade_game.spaceship import Spaceship
from arcade_game.enemy import Enemy

class Game:
    """
    Une classe pour notre jeu
    """
    def __init__(self):
        """
        Initialisation du jeu
        """
        self.w = 128 #largeur de l'écran
        self.h = 256 #hauteur de l'écran
        self.spaceship = Spaceship(self, self.w//2, self.h-8) #instanciation du vaisseau
        self.enemies = []
        pyxel.init(self.w, self.h, title="Arcade Game")
        # chargement des images
        pyxel.load("images.pyxres")
        # --> appel de la fonction principale
        pyxel.run(self.update, self.draw)

    # =====================================================
    # == UPDATE (30FPS)
    # =====================================================
    def update(self):
        """mise à jour des variables (30 fois par seconde)"""

        # deplacement du vaisseau
        self.spaceship.update()
        # déplacement des tirs
        for shoot in self.spaceship.shoots:
            shoot.update()
        # mise à jour de la liste des tirs
        self.update_shoots()
        # création des ennemis
        self.create_enemy()
        # déplacement des ennemis
        for enemy in self.enemies:
            enemy.update()
        # mise à jour des ennemis
        self.update_enemies()

    def update_shoots(self):
        """
        Retire les tirs invisibles de la liste
        """
        visible_shoots = []
        for shoot in self.spaceship.shoots:
            # si la position du tir est in
            if shoot.y + shoot.h > 0:
                visible_shoots.append(shoot)
        self.spaceship.shoots = visible_shoots

    def create_enemy(self):
        """Création d'un ennemi
        """
        jeu = self
        # un ennemi par seconde
        if (pyxel.frame_count % 30 == 0):
            enemy = Enemy(jeu, random.randint(0, 120), -8)
            self.enemies.append(enemy)

    def update_enemies(self):
        """Suppression des ennemis hors écran
        """
        to_keep=[]
        for enemy in self.enemies:
            if enemy.y < self.h:
                to_keep.append(enemy)
        self.enemies = to_keep
    # =====================================================
    # == DRAW (30FPS)
    # =====================================================
    def draw(self):
        """création et positionnement des objets (30 fois par seconde)"""

        # vide la fenetre 30 fois par seconde
        pyxel.cls(0)
        for shoot in self.spaceship.shoots:
            shoot.draw()
        self.spaceship.draw()
        for enemy in self.enemies:
            enemy.draw()

# instanciation de notre classe
Game()