from __future__ import absolute_import, unicode_literals
import json
from tekton import router
from cadastro.model import Cadastro

def validateField(attr):
    if attr:
        return attr
    else:
        return ''

def index(_write_tmpl):
    cadastrados = Cadastro.query()
    cadastros_dict = []
    for cad in cadastrados:
        cad_dict = {'idCadastro': validateField(cad.key.id()),
                    'firstname': validateField(cad.firstname),
                    'user': validateField(cad.user),
                    'email': validateField(cad.email),
                    'senha': validateField(cad.senha),
                    'dia': validateField(cad.dia),
                    'mes': validateField(cad.mes),
                    'ano': validateField(cad.ano),
                    'editando': False
                    }
        cadastros_dict.append(cad_dict)

    _write_tmpl('templates/listar_cadastros.html', {'cad': json.dumps(cadastros_dict)})