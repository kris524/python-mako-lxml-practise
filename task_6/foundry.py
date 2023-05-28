from dataclasses import dataclass
from collections.abc import Iterable
from typing import List
from mako.template import Template
from lxml import html


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
        <title>Foundry: ${foundry.name}</title> <br>
    </head>

    <body>
        The processes in the foundry are: <br>
        % for process in foundry:
            <h2>Process ID: ${process.id}</h2>
            <p>Process description: ${process.description}</p>
        <ul>
            % for p_step in process:
            <h2>${p_step.id}</h2>
            <p>${p_step.step_descirption}</p>
            <li>${p_step.parameters}</li>
            % endfor
        </ul>
        % endfor
    </body>
    """
    )
    return template.render(foundry=foundry)


def verify_html_contents(html_res, foundry):
    tree = html.fromstring(html_res)
    assert tree.xpath("//head/title/text()")[0] == f"Foundry: {foundry.name}"
    limit = -3
    for index, process in enumerate(foundry):
        k=0
        limit+=3
        
        print(tree.xpath(f"//body/h2[{index+1}]/text()")[0])

        assert (
            tree.xpath(f"//body/h2[{index+1}]/text()")[0] == f"Process ID: {process.id}"
        )

        print(tree.xpath(f"//body/p[{index+1}]/text()")[0])
        assert (
            tree.xpath(f"//body/p[{index+1}]/text()")[0]
            == f"Process description: {process.description}"
        )
        #TODO: Fix iteration of process steps
        # for index, step in enumerate(process, start=1):
        #     step_xpath = "//body/ul"
        #     print(tree.xpath(f'{step_xpath}/h2[{index}]/text()')[0])
            # assert tree.xpath(f'{step_xpath}/h2[{index}]/text()')[0] == step.id

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

    res = generate_html(tsmc)

    verify_html_contents(res, tsmc)
