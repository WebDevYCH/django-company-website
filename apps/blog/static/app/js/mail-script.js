    // -------   Mail Send ajax

     $(document).ready(function() {
        var form = $('#myForm'); // contact form
        var submit = $('.submit-btn'); // submit button
        var alert = $('.alert-msg'); // alert div for show alert message

        // form submit event
        form.on('submit', function(e) {
            e.preventDefault(); // prevent default form submit

            $.ajax({
                url: form.attr('action'), // form action url
                type: 'POST', // form submit method get/post// request type html/json/xml
                data: form.serialize(),
                beforeSend: function() {
                    alert.html('Sending....'); // change submit button text
                },
                success: function(data) {// reset form
                    alert.html('thanks for subscribing....'); // reset submit button text
                },
                error: function(e) {
                    var r = jQuery.parseJSON(e.responseText);
                    alert.html(r.email+"..");
                }
            });
            return false;
        });
    });