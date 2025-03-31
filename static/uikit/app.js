// Invoke Functions Call on Document Loaded
document.addEventListener('DOMContentLoaded', function () {
  hljs.highlightAll();
});


// This script was missing from the github repo, but could be seen
// in the video. Allows for flash messages to be cleared by the user
// by clicking the 'x' button of the message.
let alertWrapper = document.querySelector('.alert')
let alertClose = document.querySelector('.alert__close')

if (alertWrapper) {
    console.log('Alert Wrapper clicked')
    alertClose.addEventListener('click', () => alertWrapper.style.display = 'none')
}