let slideIndex = 1;
let indice = 1;

function plusSlides(n) {
    mostrarSlides(indice += n);
}

function slideAtual(n) {
    mostrarSlides(indice= n);
}

function mostrarSlides(n){
    let i;
    let slides = document.getElementsByClassName('carousel');
    let btn = document.getElementsByClassName("btn");
    if (n> slides.length){indice= 1}
    if(n<1){indice = slides.length}
    for(i = 0 ; i<slides.length;i++) {
        slides[i].style.display = "none";
    }
    for(i=0; i < btn.length;i++){
        btn[i].className = btn[i].className.replace(" active", "");
    }
    slides[indice-1].style.display = "block";
    btn[indice-1].className += " active";
}
mostrarSlides(indice);
