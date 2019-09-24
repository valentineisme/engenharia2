//cpf
function VerificaCPF() {
    if (vercpf(document.usuarioform.cpf.value)) {
        document.getElementById("msgcpf").innerHTML = "";
    } else {
        errors = "1";
        document.getElementById("msgcpf").innerHTML = "<font color='red'>CPF invalido </font>";
        document.retorno = (errors == '');
    }
}

function vercpf(cpf) {
    if (cpf.length != 11 || cpf == "00000000000" || cpf == "11111111111" || cpf == "22222222222" || cpf == "33333333333" || cpf == "44444444444" || cpf == "55555555555" || cpf == "66666666666" || cpf == "77777777777" || cpf == "88888888888" || cpf == "99999999999")
        return false;
    add = 0;
    for (i = 0; i < 9; i++)
        add += parseInt(cpf.charAt(i)) * (10 - i);
    rev = 11 - (add % 11);
    if (rev == 10 || rev == 11)
        rev = 0;
    if (rev != parseInt(cpf.charAt(9)))
        return false;
    add = 0;
    for (i = 0; i < 10; i++)
        add += parseInt(cpf.charAt(i)) * (11 - i);
    rev = 11 - (add % 11);
    if (rev == 10 || rev == 11)
        rev = 0;
    if (rev != parseInt(cpf.charAt(10)))
        return false;
    // alert('O CPF INFORMADO É VÁLIDO.');
    return true;
}


//data_nascimento
function VerificaData() {
    if (validardataDeNascimento(document.usuarioform.data_nascimento.value)) {
        document.getElementById("msgdata").innerHTML = "";
    } else {
        errors = "1";
        document.getElementById("msgdata").innerHTML = "<font color='red'>Data Invalida </font>";
        document.retorno = (errors == '');
    }
}

// function VerificaData_Edit() {
//     if (validardataDeNascimento(document.usuarioform_edit.data_nascimento.value)) {
//         document.getElementById("msgdata").innerHTML = "";
//     } else {
//         errors = "1";
//         document.getElementById("msgdata").innerHTML = "<font color='red'>Data Invalida </font>";
//         document.retorno = (errors == '');
//     }
// }

function validardataDeNascimento(data) {

    dataAtual = new Date();
    data = new Date(data);
    if ((data < dataAtual)){
        console.log("Data Válida");
        return true;
    } else {
        console.log("Data Inválida");
        return false;
    }
}

//telefone
function mascara(o, f) {
    v_obj = o
    v_fun = f
    setTimeout("execmascara()", 1)
}

function execmascara() {
    v_obj.value = v_fun(v_obj.value)
}

function mtel(v) {
    v = v.replace(/\D/g, "");             //Remove tudo o que não é dígito
    v = v.replace(/^(\d{2})(\d)/g, "($1) $2"); //Coloca parênteses em volta dos dois primeiros dígitos
    v = v.replace(/(\d)(\d{4})$/, "$1-$2");    //Coloca hífen entre o quarto e o quinto dígitos
    return v;
}

function id(el) {
    return document.getElementById(el);
}

window.onload = function () {
    id('id_telefone').onkeyup = function () {
        mascara(this, mtel);
    }
}

//email

function VerificaEmail() {
    if (validacaoEmail(document.usuarioform.email.value)) {
        document.getElementById("msgemail").innerHTML = "";
    } else {
        errors = "1";
        document.getElementById("msgemail").innerHTML = "<font color='red'>E-mail invalido </font>";
        document.retorno = (errors == '');
    }
}

function validacaoEmail(email) {
    usuario = email.substring(0, email.indexOf("@"));
    dominio = email.substring(email.indexOf("@") + 1, email.length);

    if ((usuario.length >= 1) &&
        (dominio.length >= 3) &&
        (usuario.search("@") == -1) &&
        (dominio.search("@") == -1) &&
        (usuario.search(" ") == -1) &&
        (dominio.search(" ") == -1) &&
        (dominio.search(".") != -1) &&
        (dominio.indexOf(".") >= 1) &&
        (dominio.lastIndexOf(".") < dominio.length - 1)) {
        return true;
    } else {
        return false;
    }
}

function validarSenha(){
   NovaSenha = document.getElementById('id_senha').value;
   CNovaSenha = document.getElementById('senha').value;
   if (NovaSenha != CNovaSenha) {
      alert("Senhas Diferentes!");
   }else{
       if (NovaSenha.length < 8){
           alert("Senha tem que ter 8 ou mais digitos.");
       }

   }
}

function usuario_editar(id) {
    $.ajax({
        type: 'GET',
        url: '/perfil/editar/',
        data: {
            us: id,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        dataType: 'json',
        success: function (data) {
            $("input#id_nome").attr('value', data[0].fields['nome']);
            $("input#id_telefone").attr('value', data[0].fields['telefone']);
            $("input#id_data_nascimento").attr('value', data[0].fields['data_nascimento']);
            $("input#id_usuario").attr('value', data[0].pk);
        },
        error: function (xhr, errmsg) {
            console.log(xhr.status + ": " + xhr.responseText + "Error: " + errmsg);
        }
    });
}