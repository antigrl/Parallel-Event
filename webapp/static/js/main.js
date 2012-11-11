$(document).ready(function(){
        $('#login-trigger').click(function(){
                $(this).next('#login-content').slideToggle();
                $(this).toggleClass('active');                                  

                if ($(this).hasClass('active')) $(this).find('span').html('▲')
                        else $(this).find('span').html('▼')
                })
});