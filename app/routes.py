import logging
from flask import jsonify, render_template, request
from app import APP


@APP.route('/')
def root():
    logging.info(request.headers)
    return 'root'
