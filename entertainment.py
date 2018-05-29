#import modules
import media
import fresh_tomatoes

#create multiple instances of class movie
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://images-na.ssl-images-amazon.com/images/I/91g2fEXursL._RI_SX200_.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")


jumpstreet = media.Movie("21 Jump Street",
                           "Comedy and Cops hit Jump Street",
                           "https://ia.media-imdb.com/images/M/MV5BMTc3NzQ3OTg3NF5BMl5BanBnXkFtZTcwMjk5OTcxNw@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                           "https://www.youtube.com/watch?v=RLoKtb4c4W0")

school_of_rock = media.Movie("School of Rock",
                   "Overly enthusiastic guitarist Dewey Finn (Jack Black) gets thrown out of his bar band and finds himself in desperate need of work.",
                   "https://lh3.ggpht.com/w60u7fTrzb6Sgrf0Atg3UY1rOA0cK8VB-BE6ItGxov-ePzEGuwZbhjbTQ6G-ahzO8tUW=w200-h300",
                   "https://www.youtube.com/watch?v=wZdpNglLbt8")

nemo = media.Movie("Finding Nemo",
                   "When Nemo swims too close to the surface to prove himself, he is caught by a diver, and horrified Marlin must set out to find him.",
                   "https://ia.media-imdb.com/images/M/MV5BZjMxYzBiNjUtZDliNC00MDAyLTg3N2QtOWNjNmNhZGQzNDg5XkEyXkFqcGdeQXVyNjE2MjQwNjc@._V1_UY268_CR1,0,182,268_AL_.jpg",
                   "https://www.youtube.com/watch?v=wZdpNglLbt8")

warrior = media.Movie("Warrior",
                      "An estranged family finds redemption in the unlikeliest of places",
                      "https://ia.media-imdb.com/images/M/MV5BMTk4ODk5MTMyNV5BMl5BanBnXkFtZTcwMDMyNTg0Ng@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                      "https://www.youtube.com/watch?v=I5kzcwcQA1Q")

#create an array of all instances of movie
movies = [toy_story, avatar, jumpstreet, school_of_rock, nemo, warrior]
#open movie page
fresh_tomatoes.open_movies_page(movies)



