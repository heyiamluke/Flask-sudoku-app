from flask import Flask,render_template, request, flash, redirect, url_for, jsonify


from app.sudopy import Sudoku
from app.Sudokupy import random_puzzle
import os
from pprint import pprint

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/solution', methods=['POST'])
def solution():
    data = request.form
    data = clean_puzzle(data)
    S = Sudoku(data)
    if S.validate():
        T = S.solve()
        return render_template('solution.html', solved_puzzle=T.puzzle)
    else:
        flash('Invalid Sudoku')
        return redirect(url_for('index'))


def clean_puzzle(puzzle):
    """
    converts input from request.form to a string format readable by Sudoku
    """
    output = ''
    for val in puzzle.values():
        if val == '':
            output += '.'
        elif int(val) in range(1, 10):
            output += val
    return output


@app.route('/random', methods=['GET','POST'])
def random():
    if request.method == "POST":
            N=request.form.get('N')
            data=random_puzzle(int(N))
            S = Sudoku(data)
            return render_template('random.html', solved_puzzle=S.puzzle, slidervalue=N)
    
if __name__ == '__main__':
    app.run(threaded=True)