from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

def index(request):
    html = """
       <html>
       <head>
       <title>Home page</title>
       </head>
       <body>
       <h1>Welcome!!!</h1>
       </body>
       </html>
       """
    logger.info(f'Home page: {html}')
    return HttpResponse(html)


def about(request):
    html = """
          <html>
          <head>
          <title>About Me</title>
          </head>
          <body>
          <h1>I'm learning development</h1>
          </body>
          </html>
          """
    logger.info(f'Home page: {html}')
    return HttpResponse(html)

