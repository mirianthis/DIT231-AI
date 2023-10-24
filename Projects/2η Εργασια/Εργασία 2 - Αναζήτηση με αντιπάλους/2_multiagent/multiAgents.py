# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 1)
    """

    def minimax(self, state, depth, agent = 0, maximizing = True):
        if depth == 0 or state.isWin() or state.isLose():
            return self.evaluationFunction(state), Directions.STOP
        actions = state.getLegalActions(agent)
        if maximizing:
            scores = [self.minimax(state.generateSuccessor(agent, action), depth - 1, 1, False)[0] for action in actions]
            bestScore = max(scores)
            bestIndices = [i for i in range(len(scores)) if scores[i] == bestScore]
            return bestScore, actions[random.choice(bestIndices)]
        else:
            scores = []
            if agent == state.getNumAgents() - 1: # last ghost
                scores = [self.minimax(state.generateSuccessor(agent, action), depth - 1, 0, True)[0] for action in actions]
            else:
                scores = [self.minimax(state.generateSuccessor(agent, action), depth, agent + 1, False)[0] for action in actions]
            bestScore = min(scores)
            bestIndices = [i for i in range(len(scores)) if scores[i] == bestScore]
            return bestScore, actions[random.choice(bestIndices)]

    def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"

        return self.minimax(gameState, self.depth * 2, 0, True)[1]

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 2)
    """
    def minimax(self, state, depth, a, b, agent = 0, maximizing = True):
        if depth == 0 or state.isWin() or state.isLose():
            return self.evaluationFunction(state), Directions.STOP
        actions = state.getLegalActions(agent)
        if maximizing:
            bestScore = -1e100
            bestActions = []
            for action in actions:
                score = self.minimax(state.generateSuccessor(agent, action), depth - 1, a, b, 1, False)[0]
                a = max(a, score)
                if score > bestScore:
                    bestScore = score
                    bestActions = [action]
                elif score == bestScore:
                    bestActions.append(action)
                if bestScore > b: break
            return bestScore, random.choice(bestActions)
        else:
            bestScore = 1e100
            bestActions = []
            if agent == state.getNumAgents() - 1: # last ghost
                for action in actions:
                    score = self.minimax(state.generateSuccessor(agent, action), depth - 1, a, b, 0, True)[0]
                    b = min(b, score)
                    if score < bestScore:
                        bestScore = score
                        bestActions = [action]
                    elif score == bestScore:
                        bestActions.append(action)
                    if a > bestScore: break
            else:
                for action in actions:
                    score = self.minimax(state.generateSuccessor(agent, action), depth, a, b, agent + 1, False)[0]
                    b = min(b, score)
                    if score < bestScore:
                        bestScore = score
                        bestActions = [action]
                    elif score == bestScore:
                        bestActions.append(action)
                    if a > bestScore: break
            return bestScore, random.choice(bestActions)

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        return self.minimax(gameState, self.depth * 2, -1e100, 1e100, 0, True)[1]

        util.raiseNotDefined()

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 3)
    """

    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"

        def expHelper(gameState, deepness, agent):
            if agent >= gameState.getNumAgents():
                agent = 0
                deepness += 1
            if (deepness == self.depth or gameState.isWin() or gameState.isLose()):
                return self.evaluationFunction(gameState)
            elif (agent == 0):
                return maxFinder(gameState, deepness, agent)
            else:
                return expFinder(gameState, deepness, agent)

        def maxFinder(gameState, deepness, agent):
            output = ["meow", -float("inf")]
            pacActions = gameState.getLegalActions(agent)

            if not pacActions:
                return self.evaluationFunction(gameState)

            for action in pacActions:
                currState = gameState.generateSuccessor(agent, action)
                currValue = expHelper(currState, deepness, agent + 1)
                if type(currValue) is list:
                    testVal = currValue[1]
                else:
                    testVal = currValue
                if testVal > output[1]:
                    output = [action, testVal]
            return output

        def expFinder(gameState, deepness, agent):
            output = ["meow", 0]
            ghostActions = gameState.getLegalActions(agent)

            if not ghostActions:
                return self.evaluationFunction(gameState)

            probability = 1.0 / len(ghostActions)

            for action in ghostActions:
                currState = gameState.generateSuccessor(agent, action)
                currValue = expHelper(currState, deepness, agent + 1)
                if type(currValue) is list:
                    val = currValue[1]
                else:
                    val = currValue
                output[0] = action
                output[1] += val * probability
            return output

        outputList = expHelper(gameState, 0, 0)
        return outputList[0]

def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 4).

     DESCRIPTION: <Basically this algorithm really focuses on moving towards food.>
    """
    "*** YOUR CODE HERE ***"

    foodPos = currentGameState.getFood().asList()
    foodDist = []
    ghostStates = currentGameState.getGhostStates()
    capPos = currentGameState.getCapsules()
    currentPos = list(currentGameState.getPacmanPosition())

    for food in foodPos:
        food2pacmanDist = manhattanDistance(food, currentPos)
        foodDist.append(-1*food2pacmanDist)

    if not foodDist:
        foodDist.append(0)

    return max(foodDist) + currentGameState.getScore()

# Abbreviation
better = betterEvaluationFunction
