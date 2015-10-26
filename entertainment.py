import media
import fresh_tomatoes

toy_story = media.Movie("toy_story", "a boy and his toys which came to life!", "http://www.impawards.com/1995/posters/toy_story_ver1.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("avatar", "a marine on an alien island", "http://www.impawards.com/2009/posters/avatar_ver5_xlg.jpg", "https://youtu.be/cRdxXPV9GNQ")

batman = media.Movie("batman", "storyline", "http://www.impawards.com/2005/posters/batman_begins.jpg", "https://youtu.be/neY2xVmOfUM")

brave = media.Movie("brave", "storyline", "http://www.impawards.com/2012/posters/brave_ver2.jpg", "https://youtu.be/TEHWDA_6e3M")

frozen = media.Movie("frozen", "storyline", "http://www.impawards.com/2013/posters/frozen_ver2.jpg", "https://youtu.be/TbQm5doF_Uc")

prestige = media.Movie("prestige", "storyline", "http://www.impawards.com/2006/posters/prestige.jpg", "https://youtu.be/o4gHCmTQDVI")

movies = [toy_story, avatar, batman, brave, frozen, prestige]
fresh_tomatoes.open_movies_page(movies)