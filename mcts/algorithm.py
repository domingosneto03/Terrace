import math
import random
import pygame
import time

class MCTSNode:
    def __init__(self, state):
        self.state = state
        self.children = []
        self.visits = 0
        self.wins = 0

def mcts_search(root_state, num_iterations):
    root_node = MCTSNode(root_state)

    for _ in range(num_iterations):
        node = root_node
        # Selection
        while node.children:
            node = select_child(node)

        # Expansion
        if not node.state.is_game_over():
            node.children = expand(node)

        # Simulation
        simulation_state = node.state.clone()
        simulate(simulation_state)

        # Backpropagation
        result = simulate(simulation_state)
        backpropagate(node, result)

    return best_child(root_node)

def select_child(node):
    # Calculate UCB1 scores for each child node
    ucb1_scores = [
        (child.wins / child.visits) + math.sqrt(2 * math.log(node.visits) / child.visits)
        if child.visits > 0 else float('inf')
        for child in node.children
    ]
    # Select the child with the highest UCB1 score
    selected_index = ucb1_scores.index(max(ucb1_scores))
    return node.children[selected_index]


def expand(node):
    # Get all possible actions from the current state
    actions = node.state.get_possible_actions()
    # Create child nodes for each action
    children = [MCTSNode(node.state.apply_action(action)) for action in actions]
    return children

def simulate(state):
    while not state.is_game_over():
        # Perform a random action
        action = state.get_random_action()
        state.apply_action(action)
    return state.get_winner()  # Return the winner of the simulated game

def backpropagate(node, result):
    # Update visit count and win count of nodes along the path
    while node is not None:
        node.visits += 1
        if result == node.state.get_winner():
            node.wins += 1
        node = node.parent

def best_child(node):
    # Select the child with the highest win rate
    best_child = max(node.children, key=lambda child: child.wins / child.visits)
    return best_child

