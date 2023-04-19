function sender() {
    var name = document.getElementById('name').value;
    var email = document.getElementById('email').value;
    var message = document.getElementsByName('message')[0].value;
    var csrf_token = document.getElementsByName('csrfmiddlewaretoken')[0].value;

    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/send_telegram_message/');
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.setRequestHeader('X-CSRFToken', csrf_token);
    xhr.onload = function() {
        if (xhr.status === 200) {
            alert('Thank you for your message! We will get back to you soon.');
        } else {
            alert('There was a problem submitting your message. Please try again later.');
        }
    };
    xhr.send(encodeURI('name=' + name + '&email=' + email + '&message=' + message));

    return false;
}
