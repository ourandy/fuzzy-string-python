from fuzzywuzzy import fuzz
from flask import Flask, g
from flask_restful import Resource, Api, reqparse
import Levenshtein as lev

app = Flask(__name__)

api = Api(app)


def calculate_levenshtein_distance(str_1, str_2):
    return levenshtein_distance(str_1, str_2)


class StringMatcher(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('text_one', required=True)
        parser.add_argument('text_two', required=True)

        args = parser.parse_args()

        return {'message': 'Really is excellent', 'ratio': fuzz.ratio(args.text_one, args.text_two), 'partial_ratio': fuzz.partial_ratio(args.text_one, args.text_two),
                'token_sort_ratio': fuzz.token_sort_ratio(args.text_one, args.text_two), 'token_set_ratio': fuzz.token_set_ratio(args.text_one, args.text_two)}, 200


class LevenshteinDistance(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('text_one', required=True)
        parser.add_argument('text_two', required=True)

        args = parser.parse_args()

        lev_distance = calculate_levenshtein_distance(
            args.text_one, args.text_two)

        return{'levenshtein_distance': lev_distance}, 200


api.add_resource(StringMatcher, '/stringmatcher')
