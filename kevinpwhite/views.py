from django.shortcuts import render


def error_404(request, exception, template_name="404.html"):
    response = render_to_response(template_name)
    response.status_code = 404
    return response

def error_500(request):
        data = {}
        return render(request,'500.html', data)