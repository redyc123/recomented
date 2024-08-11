from typing import List, Literal
from film.film import Film
from langchain_core.documents import Document
import json


class FilmStore:
    films: List[Film]

    def __init__(self, path: str) -> None:
        films = json.load(open(path, "r"))
        self.films = [Film().unpuck(f) for f in films["films"]]

    def filter_genere(
        self,
        genere: Literal[
            "horror",
            "comedy",
            "drama",
            "family",
            "adventure"
        ]
    ) -> List[Film]:
        return [f for f in self.films if genere in f.genres]

    def filter_title(self, title: str) -> List[Film]:
        return [f for f in self.films if title in f.title]

    def filter_actor(self, actor: str) -> List[Film]:
        return [f for f in self.films if actor in f.actors]

    def make_docs(self) -> List[Document]:
        return [Document(
            page_content=f.desc,
            metadata={
                "title": f.title,
                "date": f.date,
                "actors": f.actors,
                "genres": f.genres
            }
        ) for f in self.films]

    def show(self, films: List[Film]) -> str:
        return "\n".join([f.title for f in films])
