# -*- coding:utf-8 -*-

from openerp.osv import osv, fields


class categoria_pelicula (osv.osv):
	_name = 'co.categoria_pelicula'
	_description = 'CO Categoria pelicula'

	_colums = {
		'nombre_cat' : fields.char('Nombre de la Categoría'),
		'descripcion' : fields.date('Descripción'),
		'padre_id' : fields.many2one('co.categoria_pelicula', 'Padre'),
		'hijo_id' : fields.one2many(
			'co.categoria_pelicula',
			'padre_id',
			'SubCategoria'),
 		
	}


categoria_pelicula ()

#por ejemplo:  se tiene  una categoria series y esta tiene una subcategoria ficcion... 
#entonces no creamos otro objeto subcategorias, sino reutilizamos la misma clase categoria.
#esto lo hacemos en las lineas 13 y 14
