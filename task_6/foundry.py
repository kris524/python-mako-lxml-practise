from dataclasses import dataclass
from collections.abc import Iterable
from typing import List
from mako.template import Template


class ProcessStep:
    def __init__(self, id: int, step_descirption: str, parameters: List[str]):
        self.id = id
        self.step_descirption = step_descirption
        self.parameters = parameters


class Process(Iterable):
    def __init__(self, id: int, description: str):
        self.id = id
        self.description = description
        self.steps = []

    def add_step(self, step: ProcessStep):
        self.steps.append(step)

    def __iter__(self):
        return iter(self.steps)


class Foundry(Iterable):
    def __init__(self, name):
        self.name = name
        self.processes = []

    def add_process(self, process):
        self.processes.append(process)

    def __iter__(self):
        return iter(self.processes)


def generate_html(foundry):
    template = Template(
        """
    <!DOCTYPE html>
    <html lang="en">

    <head>
        Foundry: ${foundry.name} <br>
    </head>

    <body>
        The processes in the foundry are: <br>
        % for process in foundry:
            Process ID: ${process.id}
            Process description: ${process.description}
        <ul>
            % for p_step in process:
            <li>${p_step.id}</li>
            <li>${p_step.step_descirption}</li>
            <li>${p_step.parameters}</li>
            % endfor
        </ul>
        % endfor
    </body>
    """
    )
    # return template.render(foundry=foundry)
    res = template.render(foundry=foundry)
    with open("task_6/output2.html", "w") as f:
        f.write(res)


if __name__ == "__main__":
    tsmc = Foundry("TSMC")
    process = Process(1, "CPU")
    process_gpu = Process(2, "GPU")

    process_step_1 = ProcessStep(1, "abc", ["a", "b", "c"])
    process_step_2 = ProcessStep(2, "gte", ["g", "t", "e"])
    process_step_3 = ProcessStep(3, "bgh", ["b", "g", "h"])

    process.add_step(process_step_1)
    process.add_step(process_step_2)
    process.add_step(process_step_3)

    process_step_gpu_1 = ProcessStep(1, "ywb", ["y", "w", "b"])
    process_step_gpu_2 = ProcessStep(2, "bsh", ["b", "s", "h"])
    process_step_gpu_3 = ProcessStep(3, "jte", ["j", "t", "e"])

    process_gpu.add_step(process_step_gpu_1)
    process_gpu.add_step(process_step_gpu_2)
    process_gpu.add_step(process_step_gpu_3)

    tsmc.add_process(process)
    tsmc.add_process(process_gpu)

    generate_html(tsmc)
