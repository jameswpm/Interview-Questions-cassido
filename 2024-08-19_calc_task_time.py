"""
Given an array of function logs, where each log consists of a function name, 
a timestamp, and an event (either start or end), return the total execution time for each function. 
The timestamp is an integer representing milliseconds since the start of the program.

Example:

> calculateExecutionTimes([
    { name: "main", time: 0, event: "start" },
    { name: "subTask1", time: 5, event: "start" },
    { name: "subTask1", time: 10, event: "end" },
    { name: "subTask2", time: 15, event: "start" },
    { name: "subTask2", time: 20, event: "end" },
    { name: "main", time: 25, event: "end" }
])
> { main: 25, subTask1: 5, subTask2: 5 }

"""

def calcTaskTime(tasks):
    time_per_task = dict()
    idle_task = dict()
    for task in tasks:
        if task["name"] in time_per_task.keys():
            if task["event"] == "end":
               if task["name"] in idle_task.keys():
                   time_per_task[task["name"]] = (task["time"] - time_per_task[task["name"]]) + idle_task[task["name"]]
               else:
                    time_per_task[task["name"]] = task["time"] - time_per_task[task["name"]]
            if task["event"] == "start":
                idle_task[task["name"]] = time_per_task[task["name"]]
                time_per_task[task["name"]] = task["time"]

        else:
            time_per_task[task["name"]] = task["time"]

    print(time_per_task)
    return time_per_task

if __name__ == "__main__":
    assert calcTaskTime([
            { "name": "main", "time": 0, "event": "start" },
            { "name": "subTask1", "time": 5, "event": "start" },    
            { "name": "subTask1", "time": 10, "event": "end" },
            { "name": "subTask2", "time": 15, "event": "start" },
            { "name": "subTask2", "time": 20, "event": "end" },
            { "name": "main", "time": 25, "event": "end" }
        ]) == { "main": 25, "subTask1": 5, "subTask2": 5 }
    
    # Test case 2: Multiple nested functions
    assert calcTaskTime([
            { "name": "main", "time": 0, "event": "start" },
            { "name": "task1", "time": 5, "event": "start" },
            { "name": "task2", "time": 7, "event": "start" },
            { "name": "task2", "time": 12, "event": "end" },
            { "name": "task1", "time": 15, "event": "end" },
            { "name": "main", "time": 20, "event": "end" }
        ]) == { "main": 20, "task1": 10, "task2": 5 }

    # Test case 3: Tasks without nesting
    assert calcTaskTime([
            { "name": "task1", "time": 0, "event": "start" },
            { "name": "task1", "time": 5, "event": "end" },
            { "name": "task2", "time": 10, "event": "start" },
            { "name": "task2", "time": 15, "event": "end" },
            { "name": "task3", "time": 20, "event": "start" },
            { "name": "task3", "time": 25, "event": "end" }
        ]) == { "task1": 5, "task2": 5, "task3": 5 }

    # Test case 4: Single task
    assert calcTaskTime([
            { "name": "main", "time": 0, "event": "start" },
            { "name": "main", "time": 10, "event": "end" }
        ]) == { "main": 10 }

    # Test case 5: Overlapping tasks (incorrect sequence)
    assert calcTaskTime([
            { "name": "task1", "time": 0, "event": "start" },
            { "name": "task1", "time": 10, "event": "end" },
            { "name": "task1", "time": 5, "event": "start" },
            { "name": "task1", "time": 15, "event": "end" }
        ]) == { "task1": 20 }

    # Test case 6: Parallel tasks
    assert calcTaskTime([
            { "name": "task1", "time": 0, "event": "start" },
            { "name": "task2", "time": 5, "event": "start" },
            { "name": "task1", "time": 10, "event": "end" },
            { "name": "task2", "time": 15, "event": "end" }
        ]) == { "task1": 10, "task2": 10 }

    # Test case 7: Immediate start and end of the same task
    assert calcTaskTime([
            { "name": "task1", "time": 0, "event": "start" },
            { "name": "task1", "time": 0, "event": "end" }
        ]) == { "task1": 0 }

    # Test case 8: Complex nested tasks
    assert calcTaskTime([
            { "name": "main", "time": 0, "event": "start" },
            { "name": "sub1", "time": 5, "event": "start" },
            { "name": "sub2", "time": 7, "event": "start" },
            { "name": "sub3", "time": 10, "event": "start" },
            { "name": "sub3", "time": 15, "event": "end" },
            { "name": "sub2", "time": 20, "event": "end" },
            { "name": "sub1", "time": 25, "event": "end" },
            { "name": "main", "time": 30, "event": "end" }
        ]) == { "main": 30, "sub1": 20, "sub2": 13, "sub3": 5 }
    
    print("All tests passed")