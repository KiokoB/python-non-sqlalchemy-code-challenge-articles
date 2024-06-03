class Article:
    all = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
        

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance (title, str) and 5<= len(title) <= 50:
            self._title = title
            if hasattr(self, title):
                raise AttributeError ("Title cannot be changed after it is set.")
        
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise ValueError("Author must be an instance of Author")
        self._author = value

    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    # def magazine(self, new_magazine):
    #     if not isinstance(new_magazine, Magazine):
    #         raise TypeError("new_magazine must be an instance of Magazine")
    #     self._magazine = new_magazine
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise ValueError("Magazine must be an instance of Magazine")
        self._magazine = value

    
class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = name
        self._articles = []

    #property name
    @property
    def name(self):
        return self._name

    #Setter
    # @name.setter
    # def name(self,name):
    #     if isinstance(name, str) and len(name) > 0 :
    #         self._name = name
    #         if hasattr(self, name):
    #             raise AttributeError ("Name cannot be changed after it is set.")

    def articles(self):
        return self._articles

    
    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        return article

    def topic_areas(self):
        if not self._articles:
            return None
        return list(set(article.magazine.category for article in self._articles))

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._article = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        if isinstance (name, str) and 2<= len(name)<= 16:
            self._name = name

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        if isinstance (category, str) and len(category) > 0:
            self._category = category
    


    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]


    def contributing_authors(self):
        if not self._articles:
            return None
        authors_count = {}
        for article in self._articles:
            if article.author in authors_count:
                authors_count[article.author] += 1
            else:
                authors_count[article.author] = 1
        return [author for author, count in authors_count.items() if count > 2]

