from typing import Any, Dict, List, Literal


class Film:
    title: str
    desc: str
    date: str
    actors: List[str]
    genres: List[Literal[
        "horror",
        "comedy",
        "drama",
        "family",
        "adventure"
    ]]

    def unpuck(self, data: Dict[str, Any]):
        self.title, self.desc, self.date, self.actors, self.genres = (
            data["title"],
            data["desc"],
            data["date"],
            data["actors"],
            data["genres"]
        )
        return self
