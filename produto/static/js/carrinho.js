function disableButtons() {
    let buttons = document.querySelectorAll('button#delete-button');
    buttons.setAttribute('desabled', '');
}

const quantityProduct = document.getElementsByClassName('qtd-prod');

for (let i = 0; i < quantityProduct.length; i++) {
    quantityProduct[i].addEventListener('change', updateTotalPage)
}

function updateTotalPage() {
    let totalCart = 0

    const cartProducts = document.getElementsByClassName('cart-prod') 
    for (let i = 0; i < cartProducts.length; i++) {
        const productPrice = cartProducts[i].getElementsByClassName('prod-price')[0].innerText.replace('R$', '').replace(',', '.');
        const productQuantity = cartProducts[i].getElementsByClassName('qtd-prod')[0].value;
        const productId = cartProducts[i].getElementsByClassName('prodId')[0].value;
        
        totalCart += (productPrice * productQuantity)
        updateItem(productId, productQuantity);
    } console.log("total carrinho:" + totalCart)

    updateTotal(totalCart)
    

    totalCart = totalCart.toFixed(2)
    totalCart = totalCart.replace('.', ',')

    document.querySelector('.total-cart').innerText = "R$ " + totalCart
    
}



function updateItem(productId, productQuantity) {
    let csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0].value;
    
    const request = new XMLHttpRequest();
    request.open('POST', '/updateitem/');
    request.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    request.setRequestHeader('X-CSRFToken', csrfToken);
    request.send(`productId=${productId}&productQuantity=${productQuantity}`);
  }

function updateTotal(total) {
    let csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0].value;
    
    const request = new XMLHttpRequest();
    request.open('POST', '/updatetotalcart/');
    request.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    request.setRequestHeader('X-CSRFToken', csrfToken);
    request.send(`total=${total}`);
}