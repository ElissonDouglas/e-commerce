var cepInput = document.querySelector('#id_cep');
var inputs = document.querySelectorAll('input')
var button = document.querySelector('input[type="submit"]');

cepInput.addEventListener('input', isValidCep)

function isValidCep(e) {
    var regex = /^[0-9]{5}-?[0-9]{3}$/
    let cep = cepInput.value
    if (regex.test(cep)) {
        button.disabled = false
    } else {
        button.disabled = true
    }
}