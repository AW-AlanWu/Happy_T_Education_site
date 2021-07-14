/* class html */
$(function(){
    $('.btn1').click(function(e){
        e.preventDefault();
        $('.class .chinese').addClass('active');
        $('.class .math').removeClass('active');
        $('.class .english').removeClass('active');
        $('.class .physical').removeClass('active');
        $('.class .sociaty').removeClass('active');
        
    });
    $('.btn2').click(function(e){
        e.preventDefault();
        $('.class .chinese').removeClass('active');
        $('.class .math').addClass('active');
        $('.class .english').removeClass('active');
        $('.class .physical').removeClass('active');
        $('.class .sociaty').removeClass('active');
        
    });
    $('.btn3').click(function(e){
        e.preventDefault();
        $('.class .chinese').removeClass('active');
        $('.class .math').removeClass('active');
        $('.class .english').addClass('active');
        $('.class .physical').removeClass('active');
        $('.class .sociaty').removeClass('active');
    });
    $('.btn4').click(function(e){
        e.preventDefault();
        $('.class .chinese').removeClass('active');
        $('.class .math').removeClass('active');
        $('.class .english').removeClass('active');
        $('.class .physical').addClass('active');
        $('.class .sociaty').removeClass('active');
        
    });
    $('.btn5').click(function(e){
        e.preventDefault();
        $('.class .chinese').removeClass('active');
        $('.class .math').removeClass('active');
        $('.class .english').removeClass('active');
        $('.class .physical').removeClass('active');
        $('.class .sociaty').addClass('active');
        
    });
    $('.btnall').click(function(e){
        e.preventDefault();
        $('.class .chinese').addClass('active');
        $('.class .math').addClass('active');
        $('.class .english').addClass('active');
        $('.class .physical').addClass('active');
        $('.class .sociaty').addClass('active');
        
    });
    $('btn6').click(function(e){
        e.preventDefault();
        $('.class .chinese').removeClass('active');
        $('.class .math').removeClass('active');
        $('.class .english').removeClass('active');
        $('.class .physical').removeClass('active');
        $('.class .sociaty').removeClass('active');
    });
});