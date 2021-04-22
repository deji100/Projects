const out = function() {
    const buts = document.getElementsByClassName('but');
    for (var i = 0; i < buts.length; i++) {
        buts[i].setAttribute('id', 'b');
    }
}
out()

function form() {
    const inputs = document.getElementsByTagName('input');
    inputs[1].placeholder = 'Username';
    inputs[2].placeholder = 'Gmail';
    inputs[3].placeholder = 'Password';
    inputs[4].placeholder = 'Confirm Password';
    }
form()

function input() {
    const inputs = document.getElementsByTagName('input');
    for (var i = 0; i < inputs.length; i++) {
        inputs[i].setAttribute('class', 'inp');
    }
}
input()