#!/usr/bin/env python
import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width" initial-scaled="1.0">
<style>
.modal {
    display: none; /* Hidden by default */
    position: fixed; /* Stay in place */
    z-index: 1; /* Sit on top */
    padding-top: 100px; /* Location of the box */
    left: 0;
    top: 0;
    width: 100%; /* Full width */
    height: 100%; /* Full height */
    overflow: auto; /* Enable scroll if needed */
    background-color: rgb(0,0,0); /* Fallback color */
    background-color: rgba(0,0,0,0.4); /* Black w/ opacity */
}

/* Modal Content */
.modal-content {
    margin: 5% auto;
    padding: 20px;
    width: 40%;
}

/* The Close Button */
.close {
    color: #aaaaaa;
    float:right;
    font-size: 28px;
    font-weight: bold;
    color:black;
    margin-top:5px;
}

.close:hover,
.close:focus {
    color: white;
    background-color:black;
    text-decoration: none;
    cursor: pointer;
}
h1{color:white;text-align:center;background-color:black}
p{color:white;font-size:150%;}
p1{color:blue;}
body{background-color:white;}
.container{
     display:flex;
     flex-wrap:wrap;
}
.box{
    min-height:200px;
    width:100%;
}
div.one:hover{
    background-color:tomato;
    border-radius:200px;
}
div.two:hover{
    background-color:black;
    border-radius:200px;
}

div.three:hover{
    background-color:red;
    border-radius:200px;
}

div.four:hover{
    background-color:green;
    border-radius:200px;
}
div.five:hover{
    background-color:darkgoldenrod;
    border-radius:200px;
}
div.six:hover{
    background-color:deepskyblue;
    border-radius:200px;
}
@media screen and (min-width: 450px)
{
    .one, .two ,.three
    {
        width: 33.33%;
    }
        .four, .five,  .six
    {
        width: 33.33%;
    }
}
</style>
<div>
    <div id="myModal" class="modal">
        <div class="modal-content">
            <span class="close">&times;</span>
            <iframe id="fr" width="100%" height="315"
            src="https://www.youtube.com/embed/ZnVIUr_BQSs"
            frameborder="0" allow="autoplay; encrypted-media"
            allowfullscreen></iframe>
        </div>
        </div>
</div>
<script>
// Get the modal
var modal = document.getElementById('myModal');




// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];


onc= function(c) {
    modal.style.display="block";
    document.getElementById("fr").setAttribute("src",'https://www.youtube.com/embed/'+c);
}
span.onclick = function(){
            console.log("hello");
            var iframe = document.getElementById("fr");
            iframe.src = iframe.src;
            modal.style.display = "none";
        }


// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
</script>
</head>
'''
# The main page layout and title bar
main_page_content = '''
<body>

<h1>Movie Images</h1>
<p><p1>By clicking below images respective trailers are opened.</p1></p>
<hr>
<center>
<div class="container">
    <div class="box one" onclick="onc('xca_8P_6yM8')"><p>THOLIPREMA</p>
    <img vspace="20" src="https://bit.ly/2GAqgKB" style="width:45%"
    height="350" hspace="20"></a></div>

    <div class="box two" onclick="onc('X_5_BLt76c0')"><p>PADMAVATI</p>
    <img vspace="20" src="https://bit.ly/2wYIqX4" style="width:45%"
    height="350" hspace="20"><br></a></div>

    <div class="box three" onclick="onc('yJdHR8nCYWk')"><p>VIVEGAM</p>
    <img vspace="20" src="https://bit.ly/2ISTw4p" style="width:45%"
    height="350" hspace="20"></a></div>

    <div class="box four" onclick="onc('5mkm22yO-bs')"><p>JUNGLE BOOK</p>
    <img vspace="20" src="https://bit.ly/2rWSB8P" style="width:45%"
    height="350" hspace="20"></a><br></div>
    <div class="box five" onclick="onc('Dtp_0ahGSfY')"><p>MAHANATI</p>
    <img vspace="20" src="https://bit.ly/2KD0hEP" style="width:45%"
    height="350" hspace="20"></a><br></div>
    <div class="box six" onclick="onc('QwievZ1Tx-8')"><p>AVENGERS</p>
    <img vspace="20" src="https://bit.ly/2qzWJtk" style="width:45%"
    height="350" hspace="20"></a><br></div>
</div>
</center>
</body>
</html>
'''
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-title text-center"
data-trailer-youtube-id="{trailer_youtube_id}"
data-toggle="modal" data-target="#trailer">
<img src="{poster_image_url}"width="220" height="342">
<h2 style="color:white;">{movie_title}</h2>
</div>
'''


def create_movie_tiles_content(movies):
    content = ''
    for movie in movies:
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
              r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (
            youtube_id_match.group(0) if youtube_id_match else None)
        content+= movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content


def open_movies_page(movies):
    output_file = open('movie1.html', 'w')
    rendered_content = main_page_content.format(
        movie_tile=create_movie_tiles_content(movies))
    output_file.write(main_page_head + rendered_content)
    output_file.close()
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)

