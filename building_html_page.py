import webbrowser
import os
import youtube_search

# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Movie Gallery Python</title>
    <!-- Bootstrap 3 -->
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
  <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        #trailer .modal-dialog {
            margin-top: 100px;
            width: 1280px;
            height: 720px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 30px;
            padding-top: 30px;
            padding-bottom: 30px;
            height: 850px;
        }
        .movie-tile:hover {

        }

        .image-poster:hover {
            -webkit-transform: scale(1.1);
            transform: scale(1.1);
            -webkit-transition: .3s ease-in-out;
            transition: .3s ease-in-out;
            background-color: #EEE;
            cursor: pointer;
        }

        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile > .image-poster', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'width': '1280',
              'height': '720',
              'rel': '0',
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'allowfullscreen': 'allowfullscreen',
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''
# <iframe width="1280" height="720" src="https://www.youtube.com/embed/qaS7L--2d48?rel=0&amp;controls=0" frameborder="0" allowfullscreen></iframe>

# The main page layout and title bar
main_page_content = '''
  <body>

  <!-- for the header items
  <h2> Arrange By </h2>

    <div class="dropdown">
    <button class="btn btn-primary dropdown-toggle" type="button" data-toggle="dropdown">Dropdown Example
    <span class="caret"></span></button>
    <ul class="dropdown-menu">
      <li><a href="#">Year</a></li>
      <li><a href="#">CSS</a></li>
      <li><a href="#">JavaScript</a></li>
    </ul>
  </div>
-->





    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>



    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Movie Gallery Python</a>





<!--

                </div>
    <ul class="nav navbar-nav">
      <li class="active"><a href="#">Home</a></li>
      <li><a href="#">Page 1</a></li>
      <li><a href="#">Page 2</a></li>
      <li><a href="#">Page 3</a></li>
    </ul>
  </div>

-->






          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>

  </body>
</html>
'''

# <div class="col-md-6 col-lg-3 movie-tile text-center">
# <div class="image-poster" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">

# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-3 movie-tile text-center">
<div class="image-poster" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" width="254" height="350">
    </div>
    <h3>{movie_title} {movie_year} </h3>




    <div class="text-left">
    <div><p>R | {movie_runtime} | {movie_genre}</p></div>
    <div><p><b>Rated:</b> {movie_rated} of {movie_imdb_votes} votes</p></div>
    <div><p><b>Awards:</b> {movie_awards}</p></div>
    <div><p><b>Actors:</b> {movie_actors}</p></div>
    <div><p><b>Director:</b> {movie_director}</p></div>
    <div><p><b>Plot:</b> {movie_plot}</p></div>
    <div><p><b>IMDB Link:</b> <a href="{movie_imdb_link}" target="_blank">Link</a></p></div>





</div>
</div>





'''



# def create_clickable_links(link):
#     html_code = """<a href="">HTML Images</a>"""
#     clickable_link = ''link
#
#     return clickable_link

def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:


        # Extract the youtube ID from the url
        # youtube_id_match = re.search(
        #     r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        # youtube_id_match = youtube_id_match or re.search(
        #     r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        # trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
        #                       else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            movie_year=movie.year,

            movie_runtime=movie.runtime,
            movie_genre=movie.genre,
            movie_rated=movie.imdb_rating,
            movie_imdb_votes=movie.imdb_votes,
            movie_type=movie.type,
            movie_language=movie.language,
            movie_awards=movie.awards,
            movie_actors=movie.actors,
            movie_director=movie.director,
            movie_writer=movie.writer,
            movie_imdb_link=movie.link_id,

            poster_image_url=movie.poster_link,
            trailer_youtube_id=youtube_search.get_youtube_id_trailer(movie.title),
            movie_plot=movie.plot
        )
    return content


def create_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('movie_gallery_python.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
