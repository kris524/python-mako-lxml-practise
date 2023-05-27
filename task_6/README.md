Consider a Semiconductor Foundry. In the foundry, there are many different manufacturing processes for creating various types of semiconductor devices (like CPUs, GPUs, ASICs, etc.). Each process has a unique Process ID, description, and a list of process steps. Each process step has a step ID, step description, and parameters.

Your task is to:

1. Create classes to represent the Foundry, Process, and ProcessStep using Python's object-oriented programming features.

2. Use the collections.abc package to ensure your Foundry can be iterated over, yielding all processes in the foundry. Similarly, make sure each Process can be iterated over to yield all ProcessSteps.

3. Generate a simple HTML report for each Process in the Foundry using the mako package. The report should contain the Process ID, description, and the IDs, descriptions and parameters of all steps in the Process.

4. Write a function using lxml to parse the generated HTML reports and verify that they contain the right information (i.e. the Process ID, description, ProcessStep IDs, descriptions, and parameters).