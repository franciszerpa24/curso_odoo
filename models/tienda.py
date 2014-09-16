# -*- coding:utf-8 -*-


from openerp.osv import osv, fields  


class tienda (osv.osv):
	_name = 'co.tienda'
	_description = 'CO tienda'

	_columns = {
		'nombre' : fields.char('Nombre'),
		'direccion' : fields.selection('Direccion'),
	}	

tienda ()