let usertab = document.querySelector('.opcao_candidato');
let emptab = document.querySelector('.opcao_empresa');
let loginuser = document.querySelector('.aba_candidato');
let loginemp = document.querySelector('.aba_empresa');


// função para que ao usuario clicar na div opcao_candidato o formulario correspondente ficar visivel
function trocarLogins1(){
    loginuser.style.display = 'none';
    loginemp.style.display = 'flex';
}
usertab.onclick = trocarLogins1

// função para que ao usuario clicar na div opcao_empresa o formulario correspondente ficar visivel

function trocarLogins2(){
    loginuser.style.display = 'flex';
    loginemp.style.display = 'none';
}
emptab.onclick = trocarLogins2

