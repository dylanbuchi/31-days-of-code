import tkinter as tk
import urllib.request
import clipboard
import requests
import random
import re
import io
import sys

from urllib.error import HTTPError
from bs4 import BeautifulSoup
from PIL import Image, ImageTk
from tkinter import messagebox

MOVIE_FILE_PATH = 'src/day_30/movies.txt'


def paste_movie_title_to_clipboard(movie_title):
    messagebox.showinfo(message="The movie title was copied to the clipboard!")
    clipboard.copy(movie_title)


def ask_user_to_watch_or_skip(movies_and_images, image_label, movie_label):
    is_yes = messagebox.askyesno(message='Do you want to watch this movie?')
    if not is_yes:
        configure_image_and_movie_labels(movies_and_images, image_label,
                                         movie_label)
        return ask_user_to_watch_or_skip(movies_and_images, image_label,
                                         movie_label)
    else:
        return is_yes


def configure_image_and_movie_labels(movies_and_images, image_label,
                                     movie_label):
    movie, image_url = get_random_movie_and_image(movies_and_images)
    image = get_formated_image(image_url)
    image_label.configure(image=image)
    image_label.image = image
    movie_label.configure(text=movie)


def remove_unicode_characters_from(string):
    string_encode = string.encode("ascii", "ignore")
    string_decode = string_encode.decode()
    return string_decode


def get_url_images(soup):
    images = soup.find_all('img')
    image_list = []
    prev = ''

    for image in images:
        image_src = (image['src'])
        if image_src and image_src.endswith('jpg'):
            if len(image_src) <= 52:
                # skip if the current image is equal to the previous one
                if image_list:
                    prev = image_list[-1]
                if prev == image_src:
                    continue

                image_list.append(image_src)

    return image_list[0:100]


def get_movies(soup):
    movies = []
    movies_data = soup.find_all(name='a')

    for movie in movies_data:
        movie = movie.getText().strip()
        matches = re.match(r'[0-9]+', movie)
        if (matches):
            movie = remove_unicode_characters_from(movie)
            # format the string
            point_index = movie.index('.')
            movie = f"{movie[0:point_index]}. {movie[point_index+1:]}"
            movies.append(movie)
    return movies


def get_soup_data():
    url = "https://www.timeout.com/newyork/movies/best-movies-of-all-time"
    try:
        response = requests.get(url)
        response.raise_for_status()
        html_text = response.text
    except HTTPError:
        sys.exit()

    soup = BeautifulSoup(html_text, 'html.parser')
    return soup


def zip_movies_and_images():
    soup = get_soup_data()
    images = get_url_images(soup)
    movies = get_movies(soup)

    movies_and_images = zip(movies, images)
    return movies_and_images


def get_app_screen():
    screen = tk.Tk()
    screen.title('Best Movies of all time')
    screen.geometry('800x600')
    return screen


def get_formated_image(image_url):
    image_url_data = urllib.request.urlopen(image_url)
    raw_data = image_url_data.read()

    pilImage = Image.open(io.BytesIO(raw_data))
    pilImage = pilImage.resize((800, 600), Image.ANTIALIAS)

    image = ImageTk.PhotoImage(pilImage)
    return image


def save_movies_to_file(movies_and_images, filename):
    with open(filename, 'w') as movie_file:
        for movie, _ in movies_and_images:
            movie_file.write(f"{movie}\n")


def load_movies_from_file(filename):
    with open(filename) as movie_file:
        return movie_file.read().splitlines()


def get_random_movie_and_image(movies_and_images):
    return random.choice(movies_and_images)


def main():
    screen = get_app_screen()
    movies_and_images = list(zip_movies_and_images())
    save_movies_to_file(movies_and_images, MOVIE_FILE_PATH)

    movie, image_url = get_random_movie_and_image(movies_and_images)

    image = get_formated_image(image_url)

    movie_label = tk.Label(text=movie)
    movie_label.pack()

    image_label = tk.Label(image=image)
    image_label.pack()

    result = ask_user_to_watch_or_skip(movies_and_images, image_label,
                                       movie_label)
    if result:
        paste_movie_title_to_clipboard(movie)
        screen.after(3000, sys.exit)

    screen.mainloop()


if __name__ == "__main__":
    main()