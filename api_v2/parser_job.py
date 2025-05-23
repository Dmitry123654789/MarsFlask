from flask_restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument('job', required=True)
parser.add_argument('work_size', required=True, type=int)
parser.add_argument('collaborators', required=True)
parser.add_argument('is_finished', required=True, type=bool)
parser.add_argument('start_date', required=True)
parser.add_argument('team_leader', required=True, type=int)
parser.add_argument('creator', required=True, type=int)
parser.add_argument('end_date', required=True)
parser.add_argument('is_finished', required=True, type=bool)
parser.add_argument('hazard_category_id', required=True, type=int)