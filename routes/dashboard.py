from flask import Blueprint
from flask_cors import cross_origin
from ..services import run_json, run_ping
import asyncio

dashboard_bp = Blueprint('dashboard_bp', __name__)


@cross_origin()
@dashboard_bp.route('/json')
def dump_json():
    return '{"field":"values"}, {"field":"value2"}'


@dashboard_bp.route('/data')
def dump_data():
    return [
        {
            'name': 'pi',
            'config': 'flask',
            'benchmarks': {'/': 14.6}
        },
        {
            'name': 'vbox',
            'config': 'flask',
            'benchmarks': {'/': 212.01}
        },
        {
            'name': 'vbox',
            'config': 'express',
            'benchmarks': {'/': 218.68}
        },
        {
            'name': 'vbox',
            'config': 'springboot',
            'benchmarks': {'/': 260.09}
        },
        {
            'name': 'vbox',
            'config': '.net',
            'benchmarks': {'/': 276.61}
        },
    ]


@dashboard_bp.route('/test/<uri>')
def run_all(uri):
    # ping_result = run_ping(uri, 10000)
    json_result = run_json(uri, 100)
    return json_result

