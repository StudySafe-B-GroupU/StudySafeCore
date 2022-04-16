from django import Jsonresponse


def get_venue(request):
    res = {
        'success': True,
        'message': 'You have sucessfully get the venues'
    }
    return Jsonresponse(res)


def create_venue(request):
    if request.method == "POST":
        res = {
            'success': True,
            'message': 'You have sucessfully create a venue'
        }
    else:
        res = {
            'success': False,
            'message': 'Error in creating a venue'
        }
    return Jsonresponse(res)


def update_venue(request):
    if request.method == "PUT":
        res = {
            'success': True,
            'message': 'You have sucessfully update a venue'
        }
    else:
        res = {
            'success': False,
            'message': 'Error in update a venue'
        }
    return Jsonresponse(res)


def modify_venue(request):
    if request.method == "PATCH":
        res = {
            'success': True,
            'message': 'You have sucessfully modify a venue'
        }
    else:
        res = {
            'success': False,
            'message': 'Error in modify a venue'
        }
    return Jsonresponse(res)

def delete_venue(request):
    if request.method == "DELETE":
        res = {
            'success': True,
            'message': 'You have sucessfully delete a venue'
        }
    else:
        res = {
            'success': False,
            'message': 'Error in delete a venue'
        }
    return Jsonresponse(res)
