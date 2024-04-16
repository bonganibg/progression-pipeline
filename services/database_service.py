from repository.postgres_repository import PostgresRepository
from models.bootcamp_model import Bootcamp
from models.bootcamp_task_model import BootcampTask
from models.submission_model import Submission
from models.task_model import Task

class DatabaseService():
    BOOTCAMP_TABLE = 'bootcamp'
    BOOTCAMP_TASK_TABLE = 'bootcamp_task'
    SUBMISSION_TABLE = 'submission'
    TASK_TABLE = 'task'

    __bootcamps = []
    __tasks = []

    def __init__(self):
        self.repository = PostgresRepository()
        self.__set_bootcamps()
        self.__set_tasks()
        
    def __set_bootcamps(self):
        bootcamps = self.repository.get_all(self.BOOTCAMP_TABLE, ["id", "name"])

        for bootcamp in bootcamps:
            print(bootcamp)
            self.__bootcamps.append(Bootcamp(**bootcamp))

    def __set_tasks(self):
        tasks = self.repository.get_all(self.TASK_TABLE, ["id", "name"])

        for task in tasks:
            self.__tasks.append(Task(**task))

    def is_bootcamp_exists(self, name: str):
        for bootcamp in self.__bootcamps:
            if bootcamp.name == name:
                return True
            
        return False               

    def is_task_exists(self, name: str):
        for task in self.__tasks:
            if task.name == name:
                return True

        return False

    def create_bootcamp(self, bootcamp: str):
        bootcamp = {'name': bootcamp}
        self.repository.insert(self.BOOTCAMP_TABLE, bootcamp)

        self.__set_bootcamps()

    def create_task(self, task: str):
        task = {'name': task}
        self.repository.insert(self.TASK_TABLE, task)

        self.__set_tasks()

    def create_bootcamp_task(self, bootcamp_name: str, task_name: str, number: int):
        bootcamp_id = self.__get_bootcamp_id(bootcamp_name)
        task_id = self.__get_task_id(task_name)

        print(bootcamp_id)
        print(task_id)

        bootcamp_task = BootcampTask(bootcamp_id=bootcamp_id,
                                     task_id=task_id, 
                                     number=number)
        
        data = bootcamp_task.model_dump()
        data.pop('id')

        self.repository.insert(self.BOOTCAMP_TASK_TABLE, data)

    def get_bootcamp_task_id(self, bootcamp_name: str, task_name: str):
        bootcamp_id = self.__get_bootcamp_id(bootcamp_name)
        task_id = self.__get_task_id(task_name)

        print(bootcamp_id)
        print(task_id)
        
        statement = f"SELECT id FROM {self.BOOTCAMP_TASK_TABLE} WHERE bootcamp_id = %s AND task_id = %s"
        data = (bootcamp_id, task_id)        

        result = self.repository.run_query(statement, data)        
        print("\033[91m" + str(result) + "\033[0m")
        return result[0][0]
    
    def __get_bootcamp_id(self, name: str):
        for bootcamp in self.__bootcamps:
            if bootcamp.name == name:                
                return bootcamp.id        
    
    def __get_task_id(self, name: str):
        for task in self.__tasks:
            if task.name == name:
                return task.id        
    
    def __get_task_bootcamp_id(self, bootcamp_name: str, task_name: str):
        bootcamp_id = None
        task_id = None

        for bootcamp in self.__bootcamps:
            if bootcamp.name == bootcamp_name:
                bootcamp_id = bootcamp.id                               
                break

        for task in self.__tasks:
            if task.name == task_name:
                task_id = task.id                
                break

        return bootcamp_id, task_id

    def create_submission(self, submission: Submission):
        submission = submission.model_dump()
        submission.pop('id')
        self.repository.insert(self.SUBMISSION_TABLE, submission)

