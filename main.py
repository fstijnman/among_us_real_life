from typing import Optional
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
import os
import psycopg2
import time

DATABASE_URL = os.environ["DATABASE_URL"]
conn = psycopg2.connect(DATABASE_URL, sslmode="require")
cursor = conn.cursor()

app = FastAPI()
templates = Jinja2Templates(directory="templates")


def is_task_done(task_number):
    postgresquery = "SELECT done FROM tasks WHERE task = 'task{}'".format(task_number)
    cursor.execute(postgresquery)
    result = cursor.fetchone()
    if result[0] == 0:
        done = "Not Done"
    else:
        done = "Done"
    return done


def update_task_done(task_number):
    postgresquery = "UPDATE tasks SET done = 1 WHERE task = 'task{}';".format(
        task_number
    )
    cursor.execute(postgresquery)
    conn.commit()


# TASK 1
@app.get("/gods-love")
def task1_get(request: Request):
    done = is_task_done(1)
    return templates.TemplateResponse(
        "task1.html", context={"request": request, "result": done}
    )


# TASK 1
@app.post("/gods-love")
def task1_post(request: Request, num: int = Form(...)):
    if num == 1892373650:
        update_task_done(1)
    done = is_task_done(1)
    return templates.TemplateResponse(
        "task1.html", context={"request": request, "result": done}
    )


# TASK 2
@app.get("/leg-less")
def task2_get(request: Request):
    done = is_task_done(2)
    return templates.TemplateResponse(
        "task2.html", context={"request": request, "result": done}
    )


# TASK 2
@app.post("/leg-less")
def task2_post(request: Request, name: str = Form(...)):
    result = name
    if "roosevelt" in result.lower():
        update_task_done(2)
    done = is_task_done(2)
    return templates.TemplateResponse(
        "task2.html", context={"request": request, "result": done}
    )


# TASK 3
@app.get("/big-joao")
def task3_get(request: Request):
    postgresquery = "SELECT done FROM tasks WHERE task = 'task{}'".format(3)
    cursor.execute(postgresquery)
    result = cursor.fetchone()
    if result[0] > 20:
        done = "Done"
    else:
        done = "Not Done"
    return templates.TemplateResponse(
        "task3.html", context={"request": request, "result": result[0], "done": done}
    )


# TASK 3
@app.post("/big-joao")
def task3_post(request: Request, tap: str = Form(...)):
    button_pressed = tap
    postgresquery = "SELECT done FROM tasks WHERE task = 'task{}'".format(3)
    cursor.execute(postgresquery)
    temp = cursor.fetchone()
    postgresquery = "UPDATE tasks SET done = {} WHERE task = 'task3';".format(
        temp[0] + 1
    )
    cursor.execute(postgresquery)
    conn.commit()
    postgresquery = "SELECT done FROM tasks WHERE task = 'task{}'".format(3)
    cursor.execute(postgresquery)
    result = cursor.fetchone()
    if result[0] > 49:
        done = "Done"
    else:
        done = "Not Done"
    time.sleep(1)
    return templates.TemplateResponse(
        "task3.html", context={"request": request, "result": result[0], "done": done}
    )


# TASK 4
@app.get("/pedro-bala")
def task4_get(request: Request):
    done = is_task_done(4)
    return templates.TemplateResponse(
        "task4.html", context={"request": request, "result": done}
    )


# TASK 4
@app.post("/pedro-bala")
def task4_post(request: Request, num: int = Form(...)):
    if num == 1077297:
        update_task_done(4)
    done = is_task_done(4)
    return templates.TemplateResponse(
        "task4.html", context={"request": request, "result": done}
    )


# TASK 5
@app.get("/jose-pedro")
def task5_get(request: Request):
    done = is_task_done(5)
    return templates.TemplateResponse(
        "task5.html", context={"request": request, "result": done}
    )


# TASK 5
@app.post("/jose-pedro")
def task5_post(request: Request, num: int = Form(...)):
    if num == 4:
        update_task_done(5)
    done = is_task_done(5)
    return templates.TemplateResponse(
        "task5.html", context={"request": request, "result": done}
    )


# TASK 6
@app.get("/jorge-amado")
def task6_get(request: Request):
    done = is_task_done(6)
    return templates.TemplateResponse(
        "task6.html", context={"request": request, "result": done}
    )


# TASK 6
@app.post("/jorge-amado")
def task6_post(request: Request, name: str = Form(...)):
    result = name
    if "spons" in result.lower():
        update_task_done(6)
    done = is_task_done(6)
    return templates.TemplateResponse(
        "task6.html", context={"request": request, "result": done}
    )


# TASK 7
@app.get("/don-aninha")
def task7_get(request: Request):
    done = is_task_done(7)
    return templates.TemplateResponse(
        "task7.html", context={"request": request, "result": done}
    )


# TASK 7
@app.post("/don-aninha")
def task7_post(request: Request, name: str = Form(...)):
    result = name
    if "theepot" in result.lower():
        update_task_done(7)
    done = is_task_done(7)
    return templates.TemplateResponse(
        "task7.html", context={"request": request, "result": done}
    )


# TASK 8
@app.get("/good-looking")
def task8_get(request: Request):
    done = is_task_done(8)
    return templates.TemplateResponse(
        "task8.html", context={"request": request, "result": done}
    )


# TASK 8
@app.post("/good-looking")
def task8_post(request: Request, num: int = Form(...)):
    result = num
    if result == 120:
        update_task_done(8)
    done = is_task_done(8)
    return templates.TemplateResponse(
        "task8.html", context={"request": request, "result": done}
    )


# TASK 9
@app.get("/cat")
def task9_get(request: Request):
    done = is_task_done(9)
    return templates.TemplateResponse(
        "task9.html", context={"request": request, "result": done}
    )


# TASK 9
@app.post("/cat")
def task9_post(request: Request, name: str = Form(...)):
    result = name
    if "watermelon sugar" in result.lower():
        update_task_done(9)
    done = is_task_done(9)
    return templates.TemplateResponse(
        "task9.html", context={"request": request, "result": done}
    )


# TASK 10
@app.get("/dora")
def task10_get(request: Request):
    done = is_task_done(10)
    return templates.TemplateResponse(
        "task10.html", context={"request": request, "result": done}
    )


# TASK 10
@app.post("/dora")
def task10_post(request: Request, num: float = Form(...)):
    result = num
    if result == 0.05:
        update_task_done(10)
    done = is_task_done(10)
    return templates.TemplateResponse(
        "task10.html", context={"request": request, "result": done}
    )


# main index.html
@app.get("/")
def read_root(request: Request):
    task_dict = {}
    for i in range(1, 11):
        if i == 3:
            postgresquery = "SELECT done FROM tasks WHERE task = 'task{}'".format(3)
            cursor.execute(postgresquery)
            temp = cursor.fetchone()
            if temp[0] > 20:
                task_dict["task_{}".format(i)] = "Done"
            else:
                task_dict["task_{}".format(i)] = "Not Done"
        else:
            task_dict["task_{}".format(i)] = is_task_done(i)
    return templates.TemplateResponse(
        "index.html", context={"request": request, "results": task_dict}
    )
