
class CountVectorizer:
    """
    Класс CountVectorizer предназначен для создания
    терм-документной матрицы,представляющей частоту встречаемости
    слов (терминов) в коллекции документов.
    """

    def __init__(self):
        """
        Инициализирует объект класса CountVectorizer.
        """
        self.dictionary = {}
        self.feature_names = []

    def fit_transform(self, sentences: list[str]) -> list[list[int]]:
        """
        Метод анализирует коллекцию предложений
        и строит терм-документную матрицу,
        представляющую частоту встречаемости слов в каждом предложении.

        :param sentences: Список предложений, которые будут проанализированы.
        :return: Терм-документная матрица в виде списка векторов.
        """
        for sentence in sentences:
            words = sentence.split()
            for word in words:
                word = word.lower()
                if word in self.dictionary:
                    self.dictionary[word] += 1
                else:
                    self.dictionary[word] = 1

        self.feature_names = list(self.dictionary.keys())

        vectors = []
        for sentence in sentences:
            vector = [0] * len(self.feature_names)
            words = sentence.split()
            for word in words:
                word = word.lower()

                index = self.feature_names.index(word)
                vector[index] += 1
            vectors.append(vector)

        return vectors

    def get_feature_names(self) -> list[str]:
        """
        Возвращает список уникальных слов (терминов),
        используемых в коллекции документов.

        :return: Список уникальных слов.
        """
        return self.feature_names


if __name__ == '__main__':

    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())

    print(count_matrix)
