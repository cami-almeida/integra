let usertab = document.querySelector('.opcao_candidato');
let emptab = document.querySelector('.opcao_empresa');
let loginuser = document.querySelector('.aba_candidato');
let loginemp = document.querySelector('.aba_empresa');
let cadarea = document.querySelector('.area')
let cadoutrarea = document.querySelector('.area_outros')
let idiomaarea = document.querySelector('.idioma_outros')


// função para que ao usuario clicar na div opcao_candidato o formulario correspondente ficar visivel
function trocarLogins1(){
    loginuser.style.display = 'none';
    loginemp.style.display = 'flex';
}

// função para que ao usuario clicar na div opcao_empresa o formulario correspondente ficar visivel

function trocarLogins2(){
    loginuser.style.display = 'flex';
    loginemp.style.display = 'none';
}

function trocarLogins1(){
    loginuser.style.display = 'none';
    loginemp.style.display = 'flex';
}


function optionCheck(){
    let option = document.getElementById("opcoesarea").value;
    if(option == "OTR"){
        cadoutrarea.style.display = 'block';
    }
    else{
        cadoutrarea.style.display = 'none';
    }
}



function optionCheckIdiomas(){
    let option2 = document.getElementById("opcao_idioma").value;
    if(option2 == "OTR"){
        idiomaarea.style.display = 'block';
    }
    else{
        idiomaarea.style.display = 'none';
    }
}



emptab.onclick = trocarLogins1
usertab.onclick = trocarLogins2


