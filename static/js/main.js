document.getElementById("main-div").style.display = "none";
setTimeout(function () {
    $('#main-div').fadeIn(500);
    document.getElementById("main-div").style.display = "block";
}, 1500);

$('.background').delay(1000).fadeOut(300).hide(500);

$("#scroll").click(function () {
    $('html, body').animate({
        scrollTop: $("#main").offset().top
    }, 1500);
});

$(document).ready(function () {
    var scrollTop = 0;
    $(window).scroll(function () {
        scrollTop = $(window).scrollTop();
        $('.counter').html(scrollTop);

        if (scrollTop >= 150) {
            $('.nav-link').addClass('scrolled-nav2');
            $('img').addClass('scrolled-nav1');
        } else if (scrollTop < 150) {
            $('img').removeClass('scrolled-nav1');
            $('.nav-link').removeClass('scrolled-nav2');
        }

    });

});

var btn = $('#button');

$(window).scroll(function () {
    if ($(window).scrollTop() > 300) {
        btn.addClass('show');
    } else {
        btn.removeClass('show');
    }
});

btn.on('click', function (e) {
    e.preventDefault();
    $('html, body').animate({ scrollTop: 0 }, '300');
});

$(function () {
    $(document).scroll(function () {
        var $nav = $(".navbar.fixed-top");
        $nav.toggleClass('scrolled', $(this).scrollTop() > $nav.height());
    });
});