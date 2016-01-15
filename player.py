import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", 
						"A Story of a boy and his toys that come to life",
						"http://www.gstatic.com/tv/thumb/movieposters/17420/p17420_p_v7_ab.jpg",
						"https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie("Avatar",
					"A marine on an alien planet",
					"http://cafmp.com/wp-content/uploads/2012/11/avatar.jpg",
					"https://www.youtube.com/watch?v=5PSNL1qE6VY")
thefall = media.Movie("The Fall",
					"A moive about a girl and a druggy",
					"http://media.aintitcool.com/media/legacy/images2008/THE_FALL_FINAL.jpg",
					"www.youtube.com/watch?v=4YIEjqOzyP8")
mr_nobody = media.Movie("Mr. Nobody",
					"The last mortal man on earth is about to die",
					"http://dl9fvu4r30qs1.cloudfront.net/37/ae/b355f58c45e0beee2892a8c0925d/mr-nobody-poster.jpg",
					"https://www.youtube.com/watch?v=mpi0qsp3v_w")
serenity = media.Movie("Serenity",
					"The greatest moive ever",
					"http://images.moviepostershop.com/serenity-movie-poster-2005-1010310953.jpg",
					"https://www.youtube.com/watch?v=JY3u7bB7dZk")
battle_royale = media.Movie("Battle Royale",
					"A class of students fight to the death",
					"http://www.kawaiikakkoiisugoi.com/wp-content/uploads/2015/12/ncbUwOyJRSaZRucSzbcz_James-Bratten-Battle-Roayle-Poster.jpg",
					"https://www.youtube.com/watch?v=hCoPbkvyWEI")

movies = [toy_story, avatar, thefall, mr_nobody, serenity, battle_royale]
fresh_tomatoes.open_movies_page(movies)
