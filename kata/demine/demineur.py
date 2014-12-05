class Demineur:
    def __init__(self, entree):
        dimensions = entree.split("\n")[0]
        nbr_lignes = int(dimensions.split(" ")[0])
        nbr_colonnes = int(dimensions.split(" ")[1])
        grille = entree.split("\n")[1]

        self.mines = [(int(idx / nbr_colonnes), (idx % nbr_colonnes)/nbr_lignes) for idx, val in enumerate(grille) if val == "*"]

    def __str__(self):
        return ""

    def calculer_representation_console_du_champ_de_mine_qu_on_a_mis_dans_le_constructeur_au_moment_de_la_creation_de_l_instance_de_la_classe_demineur_j_aime_les_pates(self):
        return "0"