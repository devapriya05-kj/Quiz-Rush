
from nicegui import ui

ui.label('Quiz Rush - Leaderboard').classes('text-h4')
ui.label('Top Players').classes('text-h5')

players = [
    {'name': 'Rahul', 'score': 750},
    {'name': 'Arun', 'score': 950},
    {'name': 'Meera', 'score': 850},
]

players = sorted(players, key=lambda player: player['score'], reverse=True)

ui.table(
    columns=[
        {'name': 'rank', 'label': 'Rank', 'field': 'rank'},
        {'name': 'name', 'label': 'Player', 'field': 'name'},
        {'name': 'score', 'label': 'Score', 'field': 'score'},
    ],
    rows=[
        {
            'rank': rank,
            'name': player['name'],
            'score': player['score']
        }
        for rank, player in enumerate(players, start=1)
    ]
)

score = 8

results = [
    {
        'player': 'Arun',
        'quiz': 'Python Basics',
        'score': 8,
        'total': 10
    },
    {
        'player': 'Meera',
        'quiz': 'Python Basics',
        'score': 9,
        'total': 10
    },
]

ui.label('Quiz Results').classes('text-h5')

for result in results:
    correct_answers = result['score']
    wrong_answers = result['total'] - correct_answers
    percentage = (result['score'] / result['total']) * 100

    with ui.card():
        ui.label(f"Player: {result['player']}")
        ui.label(f"Quiz: {result['quiz']}")
        ui.label(f"Score: {result['score']} / {result['total']}")
        ui.label(f"Correct Answers: {correct_answers}")
        ui.label(f"Wrong Answers: {wrong_answers}")
        ui.label(f"Percentage: {percentage}%")

        ui.linear_progress(percentage / 100)


ui.run()
