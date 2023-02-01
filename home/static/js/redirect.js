function produtoPage(id) {
    window.location.href = '/produto/' + id;
}

document.querySelector('form').addEventListener('submit', function(e) {
    e.preventDefault();
    const pesquisa = document.querySelector('input[name="search-bar"]').value;
    window.location.href = '/get/?search-bar=' + pesquisa;
});

function redirect(url) {
    window.location.href = '/' + url + '/';
}

/*function logar() {
    window.location.href = '/login/'
}

function registrar() {
    window.location.href = '/cadastro/'
}

function verCarrinho() {

}*/


