# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import test_loader
from base import GAETestCase
from web import cadastro
from cadastro.model import Cadastro
from google.appengine.ext import ndb
from mock.mock import Mock

class RestTests(GAETestCase):
    def test_listar(self):
        cadastros = [Cadastro(firstname='Bruna', user='buh', email='bruna@gmail.com', senha='trovao', dia='29', mes='Abril', ano='1994', sex='F'),
                    Cadastro(firstname='Ariane', user='arya', email='ariane@gmail.com', senha='diana', dia='17', mes='Junho', ano='1993', sex='F')]

        ndb.put_multi(cadastros)
        resp = Mock()
        cadastro.listar(resp)
        resp.write.assert_called_once_with('[{"firstname":"ari", "user":"arya", "email":"ariane@gmail.com", "senha":"diana", "dia":"17", "mes":"Junho", "ano":"1993", "sex":"F"}, {"firstname":"Bruna", "user":"buh", "email":"bruna@gmail.com", "senha":"trovao", "dia":"29", "mes":"Abril", "ano":"1994", "sex":"F"}]')
        #resp.write.assert_called_once_with('[{"mes": "Abril", "user": "buh", "firstname": "Bruna", "idCadastro": 1, "ano": "1994", "sex": "F", "email": "bruna@gmail.com", "senha": "trovao", "dia": "29"}, {"mes": "Junho", "user": "arya", "firstname": "Ariane", "idCadastro": 2, "ano": "1993", "sex": "F", "email": "ariane@gmail.com", "senha": "diana", "dia": "17"}]')

    def test_salvar(self):
        resp = Mock()
        cadastro.salvar(resp, 'buh', 'buh', 'buh@gmail.com', 'senha', '29', 'Abril', '1994', 'M')
        lista = Cadastro.query().fetch()
        self.assertEquals(1, len(lista))
        cont = lista[0]
        self.assertEqual('buh', cont.firstname)
        self.assertEqual('buh@gmail.com', cont.email)



