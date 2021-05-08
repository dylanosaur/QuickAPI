from flask import Blueprint
from flask_cors import cross_origin
from services import run_json, run_ping

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
            'benchmarks': {
                'ping': 47.06,
                'json': 301942.17,
                'google': 119382.43
            }
         },
    ]


@dashboard_bp.route('/test/<uri>')
def run_all(uri):
    run_ping(uri, 100000)
    run_json(uri, 100000)


