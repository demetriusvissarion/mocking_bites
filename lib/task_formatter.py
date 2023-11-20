class TaskFormatter:
    def __init__(self, task): # task is an instance of Task
        self.task = task

    def format(self):
        # Returns the task formatted as a string.
        # If the task is not complete, the format is:
        # - [ ] Task title
        # If the task is complete, the format is:
        # - [x] Task title
        if self.task.complete == False:
            return '[ ] ' + self.task.title
        else:
            return '[X] ' + self.task.title