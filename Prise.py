from Connect import Connect


class Prise:
    "Modèle représentant les prise"

    def __init__(self, nom_prise):
        self.nom_prise = nom_prise

    def get_prise(self, nom_prise):
        connexion = Connect()
        co = connexion.connect()
        data = connexion.run(co, "SELECT * FROM prise")
        connexion.close(co)
        return data

    def set_prise(self, nom_prise):
        connexion = Connect()
        co = connexion.connect()
        #insert_data=['default', nom_prise]
        query = "INSERT INTO `prise` (`id`, `nom`) VALUES (default, '%s')" % nom_prise
        data = connexion.run(co, query)
        connexion.close(co)
        return data
    def delete_prise(self, nom_prise):
        connexion = Connect()
        co = connexion.connect()
        query = "DELETE FROM `prise` WHERE nom= '%s'" % nom_prise
        data = connexion.run(co, query)
        connexion.close(co)
        return data
