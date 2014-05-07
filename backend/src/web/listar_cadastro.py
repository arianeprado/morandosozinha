from __future__ import absolute_import, unicode_literals
from tekton import router
from cadastro.model import Cadastro

def index(_write_tmpl):
    cadastrados = Cadastro.query()

    _write_tmpl('templates/listar_cadastros.html', {'cad': cadastrados})