
document.querySelectorAll('.rows .cols')[0].addEventListener('click', function () {
	window.open('/',"_self");
})


/* click cells */


const update_session = (row_id, col_id) => {
	var url = `/game/update_game/row=${row_id}&col=${col_id}`;

	fetch(url, 
	{method: 'POST'})

	window.open('/game',"_self");
}

document.querySelector('.main_grid .cell_1').addEventListener('click', function () {
	update_session(0, 0);
})
document.querySelector('.main_grid .cell_2').addEventListener('click', function () {
	update_session(0, 1);
})
document.querySelector('.main_grid .cell_3').addEventListener('click', function () {
	update_session(0, 2);
})
document.querySelector('.main_grid .cell_4').addEventListener('click', function () {
	update_session(1, 0);
})
document.querySelector('.main_grid .cell_5').addEventListener('click', function () {
	update_session(1, 1);
})
document.querySelector('.main_grid .cell_6').addEventListener('click', function () {
	update_session(1, 2);
})
document.querySelector('.main_grid .cell_7').addEventListener('click', function () {
	update_session(2, 0);
})
document.querySelector('.main_grid .cell_8').addEventListener('click', function () {
	update_session(2, 1);
})
document.querySelector('.main_grid .cell_9').addEventListener('click', function () {
	update_session(2, 2);
})



/* restart game */


const restart_game = () => {
	fetch('/game/restart', 
	{method: 'POST'})

	window.open('/game',"_self");
}

document.querySelector('a.restart').addEventListener('click', restart_game);