const imgs = document.getElementById('img');
const img = document.querySelectorAll('#img img');

let idx = 0;


function carrossel() {
    idx++;

    if (idx > img.length - 1) {
        idx = 0;
    }
    if (window.innerWidth <= 768) {
        imgs.style.transform = `translateX(${-idx * 383}px)`;
    } else {
        imgs.style.transform = `translateX(${-idx * 900}px)`;
    }
    
}


setInterval(carrossel, 1300);