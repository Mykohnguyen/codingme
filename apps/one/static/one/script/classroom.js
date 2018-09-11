$(document).ready(function(){
    $('#pythonbutton').click(function(){
        $('#difficulty').slideToggle().css('display','inline-block');
        $('.difficulty_selection').remove();
        $('#difficulty').append("<div class='difficulty_selection'> <a href='/classroom/python/easy/1' class='green'> Easy </a> <br> </div>");
        $('#difficulty').append("<div class='difficulty_selection'><a href='/classroom/python/medium/1' class='yellow'> Medium </a> <br></div>");
        $('#difficulty').append("<div class='difficulty_selection'><a href='/classroom/python/hard/1' class='red'> Hard </a> <br></div>");
        $('#javabutton').slideToggle();
        $('#javascriptbutton').slideToggle();
    })
    $('#javabutton').click(function(){
        $('#difficulty').slideToggle().css('display','inline-block');
        $('.difficulty_selection').remove();
        $('#difficulty').append("<div class='difficulty_selection'> <a href='classroom/java/easy/1' class='green'> Easy </a> <br> </div>");
        $('#difficulty').append("<div class='difficulty_selection'><a href='classroom/java/medium/1' class='yellow'> Medium </a> <br></div>");
        $('#difficulty').append("<div class='difficulty_selection'><a href='classroom/java/hard/1' class='red'> Hard </a> <br></div>");
        $('#pythonbutton').slideToggle();
        $('#javascriptbutton').slideToggle();
    })
    $('#javascriptbutton').click(function(){
        $('#difficulty').slideToggle().css('display','inline-block');
        $('.difficulty_selection').remove();
        $('#difficulty').append("<div class='difficulty_selection'> <a href='classroom/javascript/easy/1' class='green'> Easy </a> <br> </div>");
        $('#difficulty').append("<div class='difficulty_selection'><a href='classroom/javascript/medium/1' class='yellow'> Medium </a> <br></div>");
        $('#difficulty').append("<div class='difficulty_selection'><a href='classroom/javascript/hard/1' class='red'> Hard </a> <br></div>");
        $('#javabutton').slideToggle();
        $('#pythonbutton').slideToggle();
    })
});