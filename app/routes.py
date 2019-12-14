import logging
from flask import jsonify, request
from app import APP, jobs


@APP.route('/')
def root():
    return 'root'


@APP.route('/github')
def github():
    job = jobs.github_users.queue()
    logging.info(job)
    return jsonify({'job_id': job.id})
