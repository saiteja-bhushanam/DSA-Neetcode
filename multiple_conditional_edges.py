from langgraph.graph import StateGraph, START, END
from typing import TypedDict
from typing import TypedDict, Dict, Any

class GraphInput(TypedDict):
    num1: int
    num2: int
    num3: int
    num4: int
    final_output: int | None
    op1: str
    op2: str
    partial_output: int | None
    

def add_partial(input: GraphInput) -> GraphInput:
    input["partial_output"] = input["num1"] + input["num2"]
    return input

def add_final(input: GraphInput) -> GraphInput:
    input["final_output"] = input["partial_output"] + input["num3"] + input["num4"]
    return input

def multiply_partial(input: GraphInput) -> GraphInput:
    input["partial_output"] = input["num1"] * input["num2"]
    return input

def multiply_final(input: GraphInput) -> GraphInput:
    input["final_output"] = input["partial_output"] * input["num3"] * input["num4"]
    return input

def condition1(input: GraphInput) -> str:
    if input["op1"] == "+":
        return "add_partial"
    elif input["op1"] == "*":
        return "multiply_partial"
    
def condition2(input: GraphInput) -> str:
    if input["op2"] == "+":
        return "add_final"
    elif input["op2"] == "*":
        return "multiply_final"
    
def pass_through(input: GraphInput) -> GraphInput:
    return input
    
state_machine = StateGraph(GraphInput)

#create nodes
state_machine.add_node("add_partial", add_partial)
state_machine.add_node("multiply_partial", multiply_partial)
state_machine.add_node("add_final", add_final)
state_machine.add_node("multiply_final", multiply_final)
state_machine.add_node("pass_through", pass_through)

#create edges
state_machine.add_conditional_edges(START, condition1, {"add_partial": "add_partial", "multiply_partial": "multiply_partial"})
state_machine.add_edge("add_partial", "pass_through")
state_machine.add_edge("multiply_partial", "pass_through")
state_machine.add_conditional_edges("pass_through", condition2, {"add_final": "add_final", "multiply_final": "multiply_final"})
state_machine.add_edge("add_final", END)
state_machine.add_edge("multiply_final", END)

#compile the state machine
app = state_machine.compile()
#invoke the state machine
result = app.invoke({"num1": 1, "num2": 2, "num3": 3, "num4": 4, "final_output": None, "op1": "+", "op2": "*"})
print(result)
