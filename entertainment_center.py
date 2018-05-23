#!/usr/bin/env python
import media
import fresh_tomatoes
# here we imported media and fresh_tomatoes python files.


tholiprema = media.Movie("THOLIPREMA",
                         "https://bit.ly/2GAqgKB",
                         "https://www.youtube.com/embed/xca_8P_6yM8")
padmavati = media.Movie("PADMAVATI",
                        "https://bit.ly/2wYIqX4",
                        "https://www.youtube.com/embed/X_5_BLt76c0")
vivegam = media.Movie("VIVEGAM",
                      "https://bit.ly/2ISTw4p",
                      "https://www.youtube.com/embed/yJdHR8nCYWk")

junglebook = media.Movie("JUNGLE BOOK",
                         "https://bit.ly/2rWSB8P",
                         "https://www.youtube.com/embed/5mkm22yO-bs")
mahanati = media.Movie("MAHANATI",
                       "https://bit.ly/2KD0hEP",
                       "https://www.youtube.com/embed/Dtp_0ahGSfY")
avengers = media.Movie("AVENGERS",
                       "https://bit.ly/2qzWJtk",
                       "https://www.youtube.com/embed/QwievZ1Tx-8")
movies = [tholiprema, padmavati, vivegam, junglebook, mahanati, avengers]
# different movies are stored in tuple format
fresh_tomatoes.open_movies_page(movies)
