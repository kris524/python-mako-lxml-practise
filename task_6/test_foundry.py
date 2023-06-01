import pytest
from foundry import Process, ProcessStep, Foundry
import unittest


class TestFoundry:
    def test_process_creation(self):
        process = Process(1, "ABC")
        assert process.id == 1
        assert process.description == "ABC"

    def test_process_step_creation(self):
        process_step = ProcessStep(3, "abv", ["a", "b", "v"])
        assert process_step.id == 3
        assert process_step.step_descirption == "abv"

    def test_add_process_step(self):
        process_step = ProcessStep(3, "abv", ["a", "b", "v"])
        process = Process(1, "ABC")
        process.add_step(process_step)
        assert process.steps == [process_step]
        for i in process:
            assert i == process_step

    def test_add_process_to_foundry(self):
        process_step = ProcessStep(3, "abv", ["a", "b", "v"])
        process = Process(1, "ABC")
        process.add_step(process_step)
        tsmc = Foundry("TSMC")
        tsmc.add_process(process)
        assert tsmc.processes == [process]
        for i in tsmc:
            assert i == process
