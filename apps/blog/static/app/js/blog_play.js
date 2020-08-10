var init = function() {
    speechSynthesis.cancel();
};

$('#play-area').on('click', function() {

    if (!speechSynthesis.paused && speechSynthesis.speaking) {
        speechSynthesis.pause();
    } else if (speechSynthesis.paused && speechSynthesis.speaking) {
        speechSynthesis.resume();
    } else if (!speechSynthesis.speaking) {
        let voices = speechSynthesis.getVoices();
        let speech = new SpeechSynthesisUtterance();
        let tts = document.getElementById("textToSpeech");
        speech.text = tts.value;
        speech.voice = voices[1];
        
        speechSynthesis.speak(speech);
        speech.onend = function() {
            console.log('reaching end');
        };
        speech.onerror = function(event) {
            console.log('An error has occurred with the speech synthesis: ' + event.error);
        }
        speech.onstart = function(event) {
            $("#play-graphic").css('display', 'none');
            $(".pause-rectangle").css('display', 'block');
            $(".pause-rectangle-1").css('display', 'block');
            console.log('We have started uttering this speech: ');
        }
        speech.onmark = function(event) {
            console.log('A mark was reached: ' + event.name);
        }
        speech.onpause = function(event) {
            $("#play-graphic").css('display', 'block');
            $(".pause-rectangle").css('display', 'none');
            $(".pause-rectangle-1").css('display', 'none');
            console.log('Speech paused after ' + event.elapsedTime + ' milliseconds.');
        }
        speech.onresume = function(event) {
            $("#play-graphic").css('display', 'none');
            $(".pause-rectangle").css('display', 'block');
            $(".pause-rectangle-1").css('display', 'block');
            
            console.log('Speech resumed after ' + event.elapsedTime + ' milliseconds.');
        }

        function millisToMinutesAndSeconds(millis) {
            var minutes = Math.floor(millis / 60000);
            var seconds = ((millis % 60000) / 1000).toFixed(0);
            return minutes + ":" + (seconds < 10 ? '0' : '') + seconds;
        }
        speech.onboundary = function(event) {
            console.log(event.name + ' boundary reached after ' + speech.rate + ' ' + millisToMinutesAndSeconds(event.elapsedTime) + ' milliseconds.');
        }
        function setOption() {
            console.log(this.name, this.value);
            msg[this.name] = this.value;
        }

    }

});

window.onload = function() {

    init();
};