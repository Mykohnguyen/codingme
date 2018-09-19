$('#inventory').click(function() {
    $('.modal').slideToggle();
})
$('.closeinventory').click(function(){
    $('.modal').slideToggle();
})
$('#backgroundbutton').click(function() {
    $('.bmodal').slideToggle();
})
$('.closebackground').click(function(){
    $('.bmodal').slideToggle();
})
//  Updates user's favorite weapon without refreshing page
$('.favorite_weapon').click(function(event){
    event.preventDefault();
    var new_weapon = $(this).attr("alt-data")
    console.log('hi from js')
    $.ajax({
        type:'POST',
        url:'/favorite/weapon',
        data:{ 
            name:new_weapon,
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
        },
        success:function(){
            $('.weapon_image').attr('src',new_weapon)
        }
    })
})
$('.favorite_aura').click(function(event){
    event.preventDefault();
    var new_aura = $(this).attr("alt-data")
    $.ajax({
        type:'POST',
        url:'/favorite/aura',
        data:{ 
            name:new_aura,
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
        },
        success:function(){
            $('.aura_image').attr('src',new_aura)
        }
    })
})
$('.favorite_background').click(function(event){
    event.preventDefault();
    var new_background = $(this).attr("alt-data")
    $.ajax({
        type:'POST',
        url:'/favorite/background',
        data:{ 
            name:new_background,
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
        },
        success:function(){
            $('.background_image').attr('src',new_background)
        }
    })
})
