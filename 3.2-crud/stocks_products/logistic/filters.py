from rest_framework import filters

class StockSearchFilter(filters.SearchFilter):
    
    def get_search_terms(self, request):
        search_param = request.query_params.get('products', '')
        if search_param:
            return search_param.split()
        return super().get_search_terms(request)

    def get_search_fields(self, view, request):
        search_param = request.query_params.get('products', '')
        if search_param:
            return ['positions__product__id', 'positions__product__title', 'positions__product__description']
        return ['address']
