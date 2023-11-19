# Tic Tac Toe

## Introduction

 There is a board with 3 x 3 squares in this game. The two players take turns putting "x" and "o" on the board. One of the players have to get three same symbols in a row - horizontally, vertically or diagonally on a 3 x 3 board. The player who first gets 3 of his/her symbols (marks) in a row wins the game, and the other loses the game.  

## Overview
  
This document provides an overview of the testing strategy, resources used to develop the test cases, and justification for their selection in the context of the tictactoe game.

## Testing Strategy

The testing strategy for the TicTacToe game focuses on unit testing using the unittest framework in Python. The primary goal is to ensure that individual components of the code, especially functions within the TicTacToe class, behave as expected under various scenarios. The test cases cover functionalities such as player turns, win conditions, and caption updates.

## Test Resources

unittest Framework
The unittest framework is a built-in testing library in Python. It provides a test discovery mechanism and a set of conventions for organizing test cases. The framework is for supporting the creation of both simple and complex test cases, so that it validates different aspects of the tictactoe game implementation.

unittest.mock Module
The unittest.mock module is used for creating mock objects during testing. In this context, it is employed to simulate mouse clicks and positions in the test_run_game_process test case. This allows controlled testing of the game process without relying on actual user inputs.

## Justification

unittest Framework
The unittest framework is chosen for its integration with Python, providing a standardized approach to writing and executing test cases. It allows for the creation of test suites and provides clear reporting on test results. Its simplicity and compatibility with the Python standard library make it a suitable choice for this project.

unittest.mock Module
The unittest.mock module is employed to isolate the run_game_process function and simulate mouse inputs. This approach ensures that the test case focuses solely on the logic within the function without the need for user interaction. Mocking user inputs provides better control over test scenarios, allowing for comprehensive coverage of different conditions.

Ensure that the necessary dependencies, specifically pygame, are installed before running the tests.

## Additional Notes

The test cases cover essential functionalities, including player turns, win conditions, and caption updates. It also regularly updates the test suite as the code evolves to maintain the effectiveness of the testing strategy
