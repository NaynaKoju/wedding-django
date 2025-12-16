// Countdown Timer Script
(function($) {
    'use strict';

    $.fn.countdown = function(options) {
        var settings = $.extend({
            date: null,
            format: null
        }, options);

        if (!settings.date) {
            $.error('Date is not defined.');
            return;
        }

        if (!Date.parse(settings.date)) {
            $.error('Incorrect date format, it should look like this, 12/24/2012 12:00:00.');
            return;
        }

        var targetDate = Date.parse(settings.date) / 1000;
        var currentDate = Math.floor($.now() / 1000);
        var secondsLeft = targetDate - currentDate;

        if (secondsLeft < 0) {
            secondsLeft = 0;
        }

        var days = Math.floor(secondsLeft / 86400);
        secondsLeft = secondsLeft % 86400;

        var hours = Math.floor(secondsLeft / 3600);
        secondsLeft = secondsLeft % 3600;

        var minutes = Math.floor(secondsLeft / 60);
        var seconds = secondsLeft % 60;

        if (settings.format === "on") {
            days = (String(days).length >= 2) ? days : "0" + days;
            hours = (String(hours).length >= 2) ? hours : "0" + hours;
            minutes = (String(minutes).length >= 2) ? minutes : "0" + minutes;
            seconds = (String(seconds).length >= 2) ? seconds : "0" + seconds;
        }

        if (!isNaN(targetDate)) {
            this.html('<div class="days"><div class="number">' + days + '</div><div class="string">Days</div></div>' +
                     '<div class="hours"><div class="number">' + hours + '</div><div class="string">Hours</div></div>' +
                     '<div class="minutes"><div class="number">' + minutes + '</div><div class="string">Minutes</div></div>' +
                     '<div class="seconds"><div class="number">' + seconds + '</div><div class="string">Seconds</div></div>');
        } else {
            console.error('Invalid date format');
        }
    };

    // Initialize countdown on elements with data-date attribute
    $(document).ready(function() {
        $('[data-date]').each(function() {
            var $this = $(this);
            var date = $this.data('date');

            // Update countdown every second
            setInterval(function() {
                $this.countdown({
                    date: date,
                    format: "on"
                });
            }, 1000);
        });
    });

})(jQuery);