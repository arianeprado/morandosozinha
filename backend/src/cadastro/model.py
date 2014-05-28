from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb

class Cadastro(ndb.Model):

	firstname = ndb.StringProperty();
	user = ndb.StringProperty();
	email = ndb.StringProperty();
	senha = ndb.StringProperty();
	dia = ndb.StringProperty();
	mes = ndb.StringProperty();
	ano = ndb.StringProperty();
	sex = ndb.StringProperty();
