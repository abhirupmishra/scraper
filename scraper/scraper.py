"""
Scraper
"""
from abc import ABC
from dataclasses import dataclass


@dataclass
class ScrapeResult:
    DOI: str
    wordscore: int
    frequency: list[tuple[str, int]]
    study_design: list[tuple[str, int]]


class Scraper(ABC):
    def scrape(self, search_text: str) -> ScrapeResult:
        ...
