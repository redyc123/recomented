from typing import List
from embeddings.vectorstore import VecStore
from film.film import Film
from film.store import FilmStore
from logic.request_model import RequestLogic


class Logic:
    def __init__(
        self,
        collection_name: str,
        path_films: str
    ) -> None:
        self.filmstore = FilmStore(path=path_films)
        self.vecstore = VecStore(
            collection_name,
            self.filmstore.make_docs()
        )

    def run(self, request: RequestLogic):
        result: List[Film] = []
        if request.filter == "all":
            result = self.filmstore.show(self.filmstore.films)
        if request.filter == "title":
            result = self.filmstore.filter_title(request.search)
        if request.filter == "genere":
            result = self.filmstore.filter_genere(request.search)
        if request.filter == "actor":
            result = self.filmstore.filter_actor(request.search)
        if request.filter == "desc":
            films = self.vecstore.search(request.search)
            if films:
                return [f for f in films]
        return [f.title for f in result] if result else []


logic = Logic("films", "/data/store.json")
