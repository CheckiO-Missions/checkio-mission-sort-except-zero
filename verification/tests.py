"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [[5, 3, 0, 0, 4, 1, 4, 0, 7]],
            "answer": [1, 3, 0, 0, 4, 4, 5, 0, 7],
        },
        {
            "input": [[0, 2, 3, 1, 0, 4, 5]],
            "answer": [0, 1, 2, 3, 0, 4, 5],
        },
        {
            "input": [[0, 0, 0, 1, 0]],
            "answer": [0, 0, 0, 1, 0],
        },
        {
            "input": [[4, 5, 3, 1, 1]],
            "answer": [1, 1, 3, 4, 5],
        },
        {
            "input": [[0, 0,]],
            "answer": [0, 0,],
        }
    ],
    "Extra": [
        {
            "input": [[5, 6, 0, 7, 10]],
            "answer": [5, 6, 0, 7, 10],
        },
        {
            "input": [[0, 0, 3, 0, 0, 1, 7]],
            "answer": [0, 0, 1, 0, 0, 3, 7],
        }
    ]
}
