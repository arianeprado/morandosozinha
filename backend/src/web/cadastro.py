#coding: utf-8
from __future__ import absolute_import, unicode_literals
from tekton import router
from cadastro.model import Cadastro
import json

def index(_write_tmpl):

    _write_tmpl('/templates/cadastro.html', {'salvar_cadastro': '/cadastro/salvar'})

def salvar(_handler, firstname, user, email, senha, dia, mes, ano, sex):
    cadastrar = Cadastro(firstname=firstname, user=user, email=email, senha=senha, dia=dia, mes=mes, ano=ano, sex=sex)
    cadastrar.put()

def listar(_resp):
    json_struct = []

    cad = Cadastro.query()
    for m in cad:
        json_struct += \
        [{"firstname": m.firstname,
        "user": m.user,
        "email": m.email,
        "senha": m.senha,
        "dia": m.dia,
        "mes": m.mes,
        "ano": m.ano,
        "sex": m.sex,
        "idCadastro": m.key.id()}]

    json_str = json.dumps(json_struct)
    _resp.write(json_str)

def editar(_resp, idCadastro, firstname, user, email, senha, dia, mes, ano, sex):

    cadastrar = Cadastro.get_by_id(int(idCadastro))

    cadastrar.firstname = firstname
    cadastrar.user = user
    cadastrar.email = email
    cadastrar.senha = senha
    cadastrar.dia = dia
    cadastrar.mes = mes
    cadastrar.ano = ano
    cadastrar.sex = sex

    cadastrar.put()

def remover(_resp, idCadastro):

    cadastrar = Cadastro.get_by_id(int(idCadastro))

    cadastrar.key.delete()

