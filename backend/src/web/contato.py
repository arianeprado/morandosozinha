#coding: utf-8
from __future__ import absolute_import, unicode_literals
from web import my_form
from tekton import router

def index(_write_tmpl):
    url = router.to_path(my_form)
    _write_tmpl('/templates/contato.html', {'form_url': url})

def params(_resp, *args, **kwargs):
    _resp.write(args)
    _resp.write(kwargs)