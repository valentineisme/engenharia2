$(document).ready(function () {

    //cadastro usuario
    $("body").on("click", ".abrir_cadastro_usuario", function () {
        $('.modalCadastroUsuario').modal('show');
    });
    $("body").on("click", ".editar_usuario", function () {
        $('.modalEditarUsuario').modal('show');
    });
});