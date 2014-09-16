# -*- coding:utf-8 -*-

from openerp.osv import osv, fields  


class tipo_medios (osv.osv):
	_name = 'co.tipo.medios'
	_description = 'CO Tipo Medios'

	_columns = {
		'nombre' : fields.char('Nombre'),
	}	

tipo_medios ()