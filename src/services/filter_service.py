from models import *
import re


class FilterService():

    def get_task_information(self, task_name: str):
        return (self.__get_task_number(task_name), self.__get_task_name(task_name))

    def get_task_number(self, task_name: str):
        dash_index = task_name.index('-')
        task_number = task_name[:dash_index]
        task_number = re.sub(r'\D', '', task_number)
        
        return int(task_number)
    
    def get_task_name(self, task_name: str):
        dash_index = task_name.index('-')
        task_name = task_name[dash_index+1:]

        return task_name.strip()
    
    def get_score(self, score: str):
        try:
            return int(score)
        except:
            return None
    
