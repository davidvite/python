import fresh_tomatoes
import media



toy_story = media.Movie("TOy Story",
						"Kid with toys",
						"https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg",
						"https://www.youtube.com/watch?v=KYz2wyBy3kc")



avatar = media.Movie("Avatar",
					"Blue, blue",
					"https://en.wikipedia.org/wiki/Avatar_(2009_film)#/media/File:Avatar-Teaser-Poster.jpg",
					"https://www.youtube.com/watch?v=5PSNL1qE6VY")

threeidiots = media.Movie("3 Idiots",
						"Some guys trying to do engineering",
						"https://upload.wikimedia.org/wikipedia/en/d/df/3_idiots_poster.jpg",
						"https://www.youtube.com/watch?v=xvszmNXdM4w")

ratatouille = media.Movie("Ratatouille",
							"Rata cook",
							"https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
							"https://www.youtube.com/watch?v=niD-jahFURU")

schoolofrock = media.Movie("School Of Rock",
							"Chavoruco playing rock",
							"https://en.wikipedia.org/wiki/School_of_Rock#/media/File:School_of_Rock_Poster.jpg",
							"https://www.youtube.com/watch?v=3PsUJFEBC74"
							)
			
movies = [toy_story , avatar, threeidiots, ratatouille, schoolofrock]
# fresh_tomatoes.open_movies_page(movies)
# print(avatar.storyline)
print(media.Movie.__doc__)