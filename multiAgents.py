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
from math import inf

import util
from game import Agent
from pacman import GameState


def scoreEvaluationFunction(currentGameState: GameState):
    score = currentGameState.getScore()

    pacmanPosition = currentGameState.getPacmanPosition()
    ghostPositions = currentGameState.getGhostPositions()
    capsulesPositions = currentGameState.getCapsules()
    foodPositions = currentGameState.getFood()

    if currentGameState.isLose():
        return score - 1000
    if currentGameState.isWin():
        return score + 1000
    elif currentGameState.getPacmanState().scaredTimer > 1 and pacmanPosition in ghostPositions:
        return score + 200
    elif pacmanPosition in capsulesPositions:
        return score + 150
    elif pacmanPosition in foodPositions:
        return score + 150

    return score


def shouldSelfEvaluate(gameState: GameState):
    pacmanPosition = gameState.getPacmanPosition()
    ghostPositions = gameState.getGhostPositions()
    capsulesPositions = gameState.getCapsules()
    foodPositions = gameState.getFood()

    return (gameState.isLose() or
            gameState.isWin() or
            ((gameState.getPacmanState().scaredTimer > 1) and (pacmanPosition in ghostPositions)) or
            pacmanPosition in capsulesPositions or
            pacmanPosition in foodPositions
            )


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

    def __init__(self, evalFn='scoreEvaluationFunction', depth='2'):
        self.index = 0  # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)


class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState: GameState):
        value, action = self.minimax(gameState, 0)
        return action

    def minimax(self, gameState: GameState, index):
        numAgents = gameState.getNumAgents()
        if index > self.depth * numAgents or shouldSelfEvaluate(gameState):
            return self.evaluationFunction(gameState), None

        agentIndex = index % numAgents

        if agentIndex == 0:
            # pacman -> Max
            bestValue = [-inf, None]
            for action in gameState.getLegalActions(agentIndex):
                nextState = gameState.generateSuccessor(agentIndex, action)

                value, childAction = self.minimax(nextState, index + 1)
                if value >= bestValue[0]:
                    bestValue = value, action
        else:
            # ghost -> Min
            bestValue = [inf, None]
            for action in gameState.getLegalActions(agentIndex):
                nextState = gameState.generateSuccessor(agentIndex, action)

                value, childAction = self.minimax(nextState, index + 1)
                if value < bestValue[0]:
                    bestValue = value, action

        return bestValue


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()


def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviation
better = betterEvaluationFunction
