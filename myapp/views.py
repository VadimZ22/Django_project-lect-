import logging

# Create your views here.
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    return HttpResponse('Hello World')


def about(request):
    try:
        result = 1 / 0
    except Exception as e:
        logger.exception(f'Error in About page {e}')
        return HttpResponse('something went wrong')
    else:
        logger.info('About page accessed')
        return HttpResponse('about us')
