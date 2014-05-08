#coding: utf-8
from __future__ import absolute_import, unicode_literals
from tekton import router
from cadastro.model import Cadastro

def index(_write_tmpl):
    _write_tmpl('/templates/cadastro.html', {'salvar_cadastro': '/cadastro/salvar'})

def salvar(_handler, firstname, user, email, senha, dia, mes, ano, sex):
    cadastrar = Cadastro(firstname=firstname, user=user, email=email, senha=senha, dia=dia, mes=mes, ano=ano, sex=sex)
    cadastrar.put()

    _handler.redirect('/cadastro/index')
