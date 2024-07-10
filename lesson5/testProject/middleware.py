def DisableCSRFCheck(get_response): # CSRF: Cross Site Request Forgery
    def middleware(request):
        request._dont_enforce_csrf_checks = True
        response = get_response(request)
        return response
    
    return middleware