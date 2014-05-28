var myApp = angular.module('myApp', [], function($interpolateProvider) {
    $interpolateProvider.startSymbol('{_');
    $interpolateProvider.endSymbol('_}');
});

myApp.controller('myAppCtrl', controller);

function controller($scope, $http){

    $scope.lista = g_listaBlah;

    $scope.cadastro = [];
    $http.get('/cadastro/listar').success(function (json){
      $scope.cadastro = json;
    })

    $scope.editarCadastro = function(cadastro){
        cadastro.editando = true;
    }

    $scope.salvarCadastro = function(){

        var cadastro = {"firstname":$scope.inputFirstname,
            "user":$scope.inputUser,
            "email":$scope.inputEmail,
            "senha":$scope.inputSenha,
            "dia":$scope.inputDia,
            "mes":$scope.inputMes,
            "ano":$scope.inputAno,
            "sex":$scope.inputSex};

        $http.post('/cadastro/salvar', cadastro).success(function (json){

            cadastro.idCadastro = json.idCadastro;
            cadastro.editando = false;
            $scope.cadastro.push(cadastro);

            $scope.inputFirstname = "";
            $scope.inputUser = "";
            $scope.inputEmail = "";
            $scope.inputSenha = "";
            $scope.inputDia = "";
            $scope.inputMes = "";
            $scope.inputAno = "";
            $scope.inputSex = "";

        });

    }

    $scope.confirmarEdicao = function(cadastro){
        cadastro.editando = false;

        params = {"idCadastro":cadastro.idCadastro,
            "firstname":cadastro.firstname,
            "user":cadastro.user,
            "email":cadastro.email,
            "senha":cadastro.senha,
            "dia":cadastro.dia,
            "mes":cadastro.mes,
            "ano":cadastro.ano,
            "sex":cadastro.sex}

        $http.post('/cadastro/editar', params);
    }

    $scope.removerElemento = function(cadastro, index){
        $scope.cadastro.splice(index, 1);
        cadastro.editando = false;

        $http.post('/cadastro/remover', {"idCadastro":cadastro.idCadastro});
    }

}

/**
 * Created by ariane on 5/19/14.
 */
