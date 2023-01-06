import logging

import azure.functions as func

def mainPage(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    filename = f'templates/mainpage.html'
    with open(filename, 'rb') as f:
        return func.HttpResponse(
            body=f.read(),
            mimetype='text/html',
            status_code=200
        )