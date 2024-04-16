import os
import time
import threading
import json

from datetime import datetime
from dotenv import load_dotenv
from services.web_scraper_service import WebScraper
from services.database_service import DatabaseService
from services.filter_service import FilterService
from models.submission_model import Submission
from models.scraper_configuration_model import ScraperConfig

load_dotenv()

def load_dashboard_data(ids: list):
    scraper = WebScraper()
    filter = FilterService()
    output = []

    current_date = datetime.now().strftime("%Y-%m-%d")

    for id in ids:
        filter = FilterService()
        try:
            data = scraper.get_dashboard_information(id)
        except Exception as e:
            # Print error message in red 
            print("\033[91m", f"Error loading {id}", "\033[0m")            
            continue

        for value in data:
            task = value[0]
            status = value[1]
            score = value[2]

            details = {
                "task_name": filter.get_task_name(task),
                "task_number": filter.get_task_number(task),
                "submission_date": current_date,
                "submission_status": status,
                "submission_score": filter.get_score(score)
            }
            
            output.append(details)

        # print f"Loaded {id}" in green 
        print("\033[92m", f"Loaded {id}", "\033[0m")
        
            
    return output


def handle_data_storage_operations(datbase_service: DatabaseService, data: dict, bootcamp_name: str):
    # Step 1: Check if bootcamp and tasks exist
    bootcamp_exists = datbase_service.is_bootcamp_exists(bootcamp_name)
    task_exists = datbase_service.is_task_exists(data['task_name'])

    # Step 2: Link bootcamp and task
    if not bootcamp_exists:
        datbase_service.create_bootcamp(bootcamp_name)

    if not task_exists:
        datbase_service.create_task(data['task_name'])

    datbase_service.create_bootcamp_task(bootcamp_name, data['task_name'], data['task_number'])
    
    # Step 3: get the bootcamp_task ID
    bootcamp_task_id = database_service.get_bootcamp_task_id(bootcamp_name, data['task_name'])

    # Step 4: Enter the submission information 
    submission = Submission(bootcamp_task_id=bootcamp_task_id, 
                            score=data["submission_score"], 
                            date=data["submission_date"], 
                            status=data["submission_status"])
    
    
    database_service.create_submission(submission)

def get_scraping_details(file_name: str):    
    if not os.path.exists(file_name):
        print("File does not exist")
        exit()

    with open(file_name) as file:
        data = json.load(file)

    bootcamps = [ScraperConfig(**detail) for detail in data]    
    return bootcamps

def loading_animation():
    emojis = ['⚫','🔵','🟢','🟡','🟠','🔴']
    idx = 0
    while not stopAnimation:
        print(f'{emojis[idx % len(emojis)]}', end='\r')
        idx += 1
        time.sleep(0.5)    

def write_to_temp(dashboard_data: list):
    with open(f"temp_data.json", "w") as file:
        json.dump(dashboard_data, file)
    

if __name__ == '__main__':    
    global stopAnimation 

    stopAnimation = False

    # database_service = DatabaseService()        

    bootcamps = get_scraping_details("config.json")

    animation_thread = threading.Thread(target=loading_animation)
    animation_thread.start()

    output = []

    for bootcamp in bootcamps:
        bootcamp_name = bootcamp.bootcamp
        numbers = bootcamp.students

        print("Started Scraping")
        data = load_dashboard_data(numbers)
        print("Done Scraping")

        temp_value = {
            "bootcamp": bootcamp_name,
            "review_data": data
        }

        output.append(temp_value)    
        
        # for value in data:
        #     handle_data_storage_operations(database_service, value, bootcamp_name)

        print("Done uploading")
    
    write_to_temp(output)

    stopAnimation = True
    animation_thread.join()    

    print("Done")