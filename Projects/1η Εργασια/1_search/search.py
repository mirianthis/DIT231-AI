# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getInitialState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isFinalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getNextStates(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getActionCost(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getInitialState())
    print("Is the start a goal?", problem.isFinalState(problem.getInitialState()))
    print("Start's successors:", problem.getNextStates(problem.getInitialState()))
    """

    frontier = util.Stack()
    exploredNodes = []

    startState = problem.getInitialState()
    startNode = (startState, [])

    frontier.enqueue(startNode)

    while not frontier.isEmpty():

        currentState, actions = frontier.dequeue()

        if currentState not in exploredNodes:

            exploredNodes.append(currentState)

            if problem.isFinalState(currentState):
                return actions
            else:
                successors = problem.getNextStates(currentState)

                for succState, succAction, succCost in successors:
                    newAction = actions + [succAction]
                    newNode = (succState, newAction)
                    # frontier.push(newNode)
                    frontier.enqueue(newNode)

    return actions


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""

    frontier = util.Queue()
    exploredNodes = []

    startState = problem.getInitialState()
    startNode = (startState, [], 0)  # (state, action, cost)

    frontier.enqueue(startNode)

    while not frontier.isEmpty():

        currentState, actions, currentCost = frontier.dequeue()

        if currentState not in exploredNodes:

            exploredNodes.append(currentState)

            if problem.isFinalState(currentState):
                return actions
            else:
                successors = problem.getNextStates(currentState)

                for succState, succAction, succCost in successors:
                    newAction = actions + [succAction]
                    newCost = currentCost + succCost
                    newNode = (succState, newAction, newCost)

                    frontier.enqueue(newNode)

    return actions


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    frontier = util.PriorityQueue()
    exploredNodes = {}

    startState = problem.getInitialState()
    startNode = (startState, [], 0)  # (state, action, cost)

    frontier.enqueue(startNode, 0)

    while not frontier.isEmpty():
        currentState, actions, currentCost = frontier.dequeue()

        if (currentState not in exploredNodes) or (currentCost < exploredNodes[currentState]):
            exploredNodes[currentState] = currentCost

            if problem.isFinalState(currentState):
                return actions
            else:
                successors = problem.getNextStates(currentState)

                for succState, succAction, succCost in successors:
                    newAction = actions + [succAction]
                    newCost = currentCost + succCost
                    newNode = (succState, newAction, newCost)

                    frontier.update(newNode, newCost)

    return actions

    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    frontier = util.PriorityQueue()
    exploredNodes = []  # holds (state, cost)

    startState = problem.getInitialState()
    startNode = (startState, [], 0)  # (state, action, cost)

    frontier.enqueue(startNode, 0)

    while not frontier.isEmpty():

        currentState, actions, currentCost = frontier.dequeue()
        currentNode = (currentState, currentCost)
        exploredNodes.append((currentState, currentCost))

        if problem.isFinalState(currentState):
            return actions

        else:
            successors = problem.getNextStates(currentState)

            for succState, succAction, succCost in successors:
                newAction = actions + [succAction]
                newCost = problem.getActionCost(newAction)
                newNode = (succState, newAction, newCost)

                already_explored = False
                for explored in exploredNodes:
                    exploredState, exploredCost = explored

                    if (succState == exploredState) and (newCost >= exploredCost):
                        already_explored = True

                if not already_explored:
                    frontier.enqueue(newNode, newCost + heuristic(succState, problem))
                    exploredNodes.append((succState, newCost))

    return actions

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
