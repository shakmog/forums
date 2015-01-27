class ajax(object):

	def process_request( self, request ):

		request.context_dict = {

			'base_template' : 'base.html'
		
		}

		if request.is_ajax():
		
			request.context_dict[ 'base_template' ] = 'ajax.html'