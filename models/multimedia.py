# -*- coding:utf-8 -*-

from openerp.osv import osv, fields


class multimedia (osv.osv):
	_name = 'co.multimedia'
	_description = 'CO Multimedia'
	_rec_name= 'titulo'
	_order = 'fecha_publicacion desc'

	_columns = {
		'titulo' : fields.char('Titulo', required=True),
		'fecha_publicacion' : fields.date('Fecha de publicacion'),
		'codigo' : fields.char('Código'), 
		'categoria_pelicula_id' : fields.many2one('co.categoria_pelicula','Categoria'),
		'medio_ids' : fields.many2many(
			'co.tipo.medios',
			'co_multimedia_medio_rel',
			'multimedia_id',
			'medio_id'),
	}


multimedia ()

#aqui hay una relacion de muchos a muchos
#por 