from podcast import Podcast_episode
from Book2 import Book

"""This class inherits from Podcast_episode and Book."""


class Audiobook(Podcast_episode, Book):
    audio_shelves = []

    def __init__(self, title, author, speaker, publish_year, pages, time, price, book_language, audio_language):
        Podcast_episode.__init__(self, title, speaker, publish_year, time, price, language=None)
        Book.__init__(self, title, author, publish_year, pages, price, language=None)
        self.audio_language = audio_language
        self.book_language = book_language


def get_data():
    """This function get information from user and build a object by them."""
    print('\033[35Enter information .')
    title = input("Enter title : ")
    speaker = input("Enter speaker : ")
    author = input("Enter author : ")
    publish_year = int(input("Enter publish_year :"))
    pages = int(input("Enter pages :"))
    book_Language = input("Enter book_language :")
    audio_Language = input("Enter audio_language :")
    time = int(input("Enter time :"))
    Price = float(input("Enter price : "))
    audio_book = Audiobook(title, author, speaker, publish_year, pages, time, Price, book_Language, audio_Language)
    Audiobook.audio_shelves.append(audio_book)
    return audio_book


