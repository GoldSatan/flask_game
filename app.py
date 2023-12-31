from flask import Flask, render_template, redirect, session, request, jsonify

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asd1!__cj!)'

@app.route('/')
def indexView():
    if 'game' in session:
        del session['game']

    return render_template('index.html')


@app.route('/game')
def gameView():
    if 'game' not in session:
        session['game'] = {
			'cells': [ 
       			[0, 0, 0],
       			[0, 0, 0],
       			[0, 0, 0],
            ],
			'if_win': 'no',
			'who_step': 'cross',
			'win': None
		}
    
    return render_template('game.html', session=session['game'])


@app.route('/game/update_game/row=<int:row_id>&col=<int:col_id>', methods=['POST'])
def updateGameView(row_id, col_id):
	if request.method == 'POST':
		if 'game' in session:
			game = session['game']
			if game['cells'][row_id][col_id] == 1 or game['cells'][row_id][col_id] == 2:
				pass
			else:
				if game['who_step'] == 'cross':
					game['cells'][row_id][col_id] = 1
					game['who_step'] = 'circle'
					
				elif game['who_step'] == 'circle':
					game['cells'][row_id][col_id] = 2
					game['who_step'] = 'cross'
			
			if ((game['cells'][0][0] == 1 and game['cells'][0][1] == 1 and game['cells'][0][2] == 1) or 
   				(game['cells'][1][0] == 1 and game['cells'][1][1] == 1 and game['cells'][1][2] == 1) or
   				(game['cells'][2][0] == 1 and game['cells'][2][1] == 1 and game['cells'][2][2] == 1) or
       			(game['cells'][0][0] == 1 and game['cells'][1][0] == 1 and game['cells'][2][0] == 1) or
       			(game['cells'][0][1] == 1 and game['cells'][1][1] == 1 and game['cells'][2][1] == 1) or
       			(game['cells'][0][2] == 1 and game['cells'][1][2] == 1 and game['cells'][2][2] == 1) or
       			(game['cells'][0][0] == 1 and game['cells'][1][1] == 1 and game['cells'][2][2] == 1) or
       			(game['cells'][0][2] == 1 and game['cells'][1][1] == 1 and game['cells'][2][0] == 1) 
        	):
				game['if_win'] = 'yes'
				game['win'] = 'cross'
    
			elif ((game['cells'][0][0] == 2 and game['cells'][0][1] == 2 and game['cells'][0][2] == 2) or 
   				  (game['cells'][1][0] == 2 and game['cells'][1][1] == 2 and game['cells'][1][2] == 2) or
   				  (game['cells'][2][0] == 2 and game['cells'][2][1] == 2 and game['cells'][2][2] == 2) or
       			  (game['cells'][0][0] == 2 and game['cells'][1][0] == 2 and game['cells'][2][0] == 2) or
       			  (game['cells'][0][1] == 2 and game['cells'][1][1] == 2 and game['cells'][2][1] == 2) or
       			  (game['cells'][0][2] == 2 and game['cells'][1][2] == 2 and game['cells'][2][2] == 2) or
          		  (game['cells'][0][0] == 2 and game['cells'][1][1] == 2 and game['cells'][2][2] == 2) or
       			  (game['cells'][0][2] == 2 and game['cells'][1][1] == 2 and game['cells'][2][0] == 2) 
        	):
				game['if_win'] = 'yes'
				game['win'] = 'circle'
   
   
			session['game'] = game 
			
			return jsonify({'status': 'success', 'session': session['game']})
        


@app.route('/game/restart', methods=['POST'])
def restartView():
	if request.method == 'POST':
		if 'game' in session:
			del session['game']
			
			session['game'] = {
				'cells': [ 
					[0, 0, 0],
					[0, 0, 0],
					[0, 0, 0],
				],
				'if_win': 'no',
				'who_step': 'cross',
				'win': None
			}
			
			return jsonify({'status': 'success', 'session': session['game']})

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')

