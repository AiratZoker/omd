import math


class CountVectorizer:
    """
    Класс CountVectorizer предназначен для создания
    терм-документной матрицы, представляющей частоту встречаемости
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
            words = [word.lower() for word in words]
            for word in words:
                if word in self.dictionary:
                    self.dictionary[word] += 1
                else:
                    self.dictionary[word] = 1

        self.feature_names = list(self.dictionary.keys())

        vectors = []
        for sentence in sentences:
            vector = [0] * len(self.feature_names)
            words = sentence.split()
            words = [word.lower() for word in words]
            for word in words:
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


class TfidfTransformer:
    """Класс для преобразования матрицы счетчиков
    слов в TF-IDF представление.
    """

    def tf_transform(self, count_matrix: list[list[float]]) -> list[list[float]]:
        """
        Принимает на вход матрицу счетчика
        (результат работы CountVectorizer)
        и преобразует ее в матрицу TF (частотность терминов),
        где каждый элемент делится на сумму всех элементов
        в этом документе.
        """
        vectors = []
        for sentence in count_matrix:
            sum_el = sum(sentence)
            vectors.append([round(el/sum_el, 3) for el in sentence])
        return vectors

    def idf_transform(self, count_matrix: list[list[float]]) -> list[float]:
        """
        Принимает на вход матрицу счетчика и преобразует
        ее в вектор IDF (обратная частотность документа),
        где каждый элемент является логарифмом отношения
        общего количества документов к количеству документов,
        содержащих соответствующее слово.
        """
        vector = []
        all_documents = len(count_matrix)
        for column in zip(*count_matrix):
            vector.append(
                round(
                    math.log(
                        (all_documents + 1) /
                        (len(column) - column.count(0) + 1)) + 1,
                    1)
            )
        return vector

    def fit_transform(self, count_matrix: list[list[float]])\
            -> list[list[float]]:
        """
        Принимает на вход матрицу счетчика
        и преобразует ее в матрицу TF-IDF,
        где каждый элемент является произведением
         соответствующих элементов матриц TF и IDF.
        """
        tf = self.tf_transform(count_matrix)
        idf = self.idf_transform(count_matrix)

        for i in range(len(tf)):
            tf[i] = [round(t * f, 3) for t, f in zip(tf[i], idf)]

        return tf


class TfidfVectorizer(CountVectorizer):
    """Класс для преобразования текстовых данных в TF-IDF представление."""

    def __init__(self, transformer: TfidfTransformer):
        """
        Инициализирует объект TfidfVectorizer.
        Наследует все атрибуты и методы CountVectorizer и
        добавляет атрибут transformer, который является объектом
        TfidfTransformer.
        """
        super().__init__()
        self.transformer = transformer

    def fit_transform(self, corpus: list[str]) -> list[list[float]]:
        """
        Принимает на вход корпус документов. Сначала преобразует корпус
        в матрицу счетчиков слов с помощью метода fit_transform
        родительского класса CountVectorizer. Затем преобразует
        матрицу счетчиков в TF-IDF представление с помощью метода
        fit_transform класса TfidfTransformer.
        """
        count_matrix = super().fit_transform(corpus)
        return self.transformer.fit_transform(count_matrix)


if __name__ == "__main__":
    corpus = [
        "Crock Pot Pasta Never boil pasta again",
        "Pasta Pomodoro Fresh ingredients Parmesan to taste",
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(count_matrix)
    transformer = TfidfTransformer()
    tfidf_matrix = transformer.fit_transform(count_matrix)
    print(tfidf_matrix)
    vectorizer = TfidfVectorizer(transformer)
    tfidf_matrix = vectorizer.fit_transform(corpus)
    print(tfidf_matrix)
