from unicodedata import normalize

class TextUtil :
    """
    Classe com métodos para tratamento de texto
    """
	
    @staticmethod
    def remove_special_characters(text) :
        """
        Método para remover caracteres especiais do texto
        """
        return normalize('NFKD', text).encode('ASCII', 'ignore').decode('ASCII')