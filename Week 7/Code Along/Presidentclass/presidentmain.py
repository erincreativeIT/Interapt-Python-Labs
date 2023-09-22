from president_codealong import President

for term in 1, 26, 39, 45:
    p = President(term)

    print(f'{p.first_name} was born at {p.birth_place}, {p.birth_state} on {p.birth_date}')
