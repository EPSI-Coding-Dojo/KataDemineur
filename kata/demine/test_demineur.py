from kata.demine.demineur import Demineur

__author__ = 'manu'

import unittest


class DemineurTestCase(unittest.TestCase):
    # def test_demine_1cas_pratique(self):
    #     input = "4 5\n" \
    #             "*..*." \
    #             "....." \
    #             ".*..*" \
    #             "..*.."
    #
    #     expected_output = "*11*1" \
    #                       "22222" \
    #                       "1*22*" \
    #                       "12*21"
    #     output = demineur(input)
    #     self.assertEqual(output, expected_output)

    def test_demine_vide(self):
        input = "0 0\n"
        demineur = Demineur(input)

        expected_output = ""
        self.assertEqual(demineur.__str__(), expected_output)

    def test_retourne_une_liste_vide_de_mine_quand_pas_de_mine(self):
        input = "1 1\n."
        demineur = Demineur(input)
        mines = demineur.mines
        self.assertEquals(mines, [])

    def test_retourne_la_liste_des_mines(self):
        input = "1 2\n**"
        demineur = Demineur(input)
        mines = demineur.mines
        self.assertEquals(mines, [(0, 0), (0, 1)])

    def test_retourne_le_caractere_zero_pour_une_grille_vide_de_1x1(self):
        input = "1 1\n."
        demineur = Demineur(input)
        output = demineur.calculer_representation_console_du_champ_de_mine_qu_on_a_mis_dans_le_constructeur_au_moment_de_la_creation_de_l_instance_de_la_classe_demineur_j_aime_les_pates()
        self.assertEquals(output, "0")

    # def test_retourne_une_string_de_taille_25_pour_une_grille_de_5x5(self):
    #     input = "5 5\n........................."
    #     demineur = Demineur(input)
    #     output = demineur.calculer_representation_console_du_champ_de_mine_qu_on_a_mis_dans_le_constructeur_au_moment_de_la_creation_de_l_instance_de_la_classe_demineur_j_aime_les_pates()

if __name__ == '__main__':
    unittest.main()
