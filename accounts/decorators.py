from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func

def allowed_users(allowed_user_roles = []):
    def decorator_func(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None

            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            
            if group in allowed_user_roles:    
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page!')

        return wrapper_func
    return decorator_func

def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None

        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'Customer':
            return redirect('user_page')
        
        if group == 'Admin':
            return view_func(request, *args, **kwargs)
            
    return wrapper_func


