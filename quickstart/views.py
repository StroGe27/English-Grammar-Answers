from rest_framework.response import Response
from rest_framework.views import APIView

import requests
import codecs

from quickstart.serializers import RouteToResSerializer
from quickstart.models import RouteToRes

class main_list_questions(APIView):
    # Введите URL 
    def get(self, request, format=None):
        tmp = requests.get("https://www.english-grammar.at/online_exercises/tenses/t139-all-tenses.htm")
        with open("web_content.html", "w", encoding="utf-8") as file:
            file.write(tmp.text)
        tmp = str(tmp.text)
        
        start_answers = "I = new Array();"
        end_answers = "State = new Array();"

        start_index = tmp.find(start_answers)
        end_index = tmp.find(end_answers)

        a = tmp[start_index:end_index].split("\n\n")
        self._give_me_answer(a[1:])
        return Response([{
            "text": request.text
        }])
    def _give_me_list():
        pass
    
class get_answer(APIView):
    model_class = RouteToRes
    serializer_class = RouteToResSerializer

    def post(self, request, format=None):
        request = request.data
        if "https://www.english-grammar.at/online_exercises/tenses/" not in request["payload"]:
            return Response([{
                "error": "wrong URL",
            }])  
        tmp = requests.get(request["payload"])
        tmp = str(tmp.text)

        start_index = tmp.find("I = new Array();")
        end_index = tmp.find("State = new Array();")

        a = tmp[start_index:end_index].split("\n\n")
        arr_answers, len_arr = self._give_me_answer(a[1:])
        return Response([{
            "answers": arr_answers,
            "count_of_answers": len_arr,
        }])
    
    def _give_me_answer(self, arr_test):
        arr_split_n = []
        arr_correct_answers = []
        index_comma = 0
        for i in arr_test:
            arr_split_n = i.split("\n")
            for j in arr_split_n:
                result = ''.join(char for char in j if not char.isdigit())
                if '[][][][]' in result:
                    index_comma = j.find("'")
                    arr_correct_answers.append(j[index_comma+1:-2])

        arr_correct_answers = [codecs.decode(arr_correct_answers[i], 'unicode_escape') for i in range(len(arr_correct_answers))]      
        return arr_correct_answers, len(arr_test)
