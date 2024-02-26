from django.shortcuts import redirect
from django.urls import reverse_lazy

class RedirectToTasksMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        # Check if user is authenticated
        if request.user.is_authenticated:
            # Check if the requested path is the root URL without the 'task' path
            if request.path == '/' and not request.path.startswith('/task/'):
                # Redirect to a different page, such as the tasks page
                return redirect(reverse_lazy('tasks'))
        
        return response

# """
# Project: Task Management System
# Developer: Sanket Sonar
# Contact:sonarsanket2001@gmail.com
# """ 
