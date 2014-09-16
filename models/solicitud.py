# -*- coding:utf-8 -*-

from openerp.osv import osv, fields  


class solicitud (osv.osv):
	_name = 'co.solicitud'
	_description = 'CO Solicitud'

	_columns = {
		'suscriptor_id' : fields.many2one('co.suscriptor', 'Afiliado'),
		'multimedia_id' : fields.many2one('co.multimedia', 'Multimedia'),
		'medio_id' : fields.many2one('co.tipo.medios', 'Tipos Medios'),
		'tienda_id' : fields.many2one('co.tienda', 'Tienda'),
		'fecha_soli' : fields.date('Fecha solicitud'),
		'duracion_dias' : fields.integer('Duración en Días'),
	}	

solicitud ()