$(documet).ready(function() {
    let count = $('.news .row > div').lenght,
        start = 3,
        show = 3;

    $('.news .row > div').addClass('d-none')
    $('.news .row > div:lt(' + start + ')').removeClass('d-none');

    $('.show-more').click(function(e) {
        e.preventDefault();

        start = (start + show <= count) ? start + show : count;

        $('.news .row > div:lt(' + start + ')').removeClass('d-none');
    })
})