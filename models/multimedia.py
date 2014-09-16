# -*- coding:utf-8 -*-

from openerp.osv import osv, fields


class multimedia (osv.osv):
	_name = 'co.multimedia'
	_description = 'CO Multimedia'

	_colums = {
		'titulo' : fields.char('Titulo'),
		'fecha_plubilcacion' : fields.date('Fecha de publicacion'),
		'codigo' : fields.char('Código'), 
		'categoria_pelicula_id' : fields.many2one('co.categoria_pelicula','Categoria'),
		'medio_ids' : fields.many2many(
			'co.tipo.medios',
			'co_multimedia_medio_rel',
			'multimedia_id',
			'medios_id'),
	}


multimedia ()

#aqui hay una relacion de muchos a muchos
#por 