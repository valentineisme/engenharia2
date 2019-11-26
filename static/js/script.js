$(document).ready(function () {

    //cadastro usuario
    $("body").on("click", ".abrir_cadastro_usuario", function () {
        $('.modalCadastroUsuario').modal('show');
    });
    $("body").on("click", ".editar_usuario", function () {
        $('.modalEditarUsuario').modal('show');
    });
    $("body").on("click", ".abrir_veiculo", function () {
        $('.modalVeiculo').modal('show');
    });
    $("body").on("click", ".leiloarVeic", function () {
        $('.modalLeiloar').modal('show');
    });
    $("body").on("click", ".dar_lance", function () {
        $('.modalLeilaoAtivo').modal('show');
    });
});