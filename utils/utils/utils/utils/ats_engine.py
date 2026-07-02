def calculate_ats_score(skills, match_percentage):
    score = (len(skills) * 5) + (match_percentage * 0.5)

    if score > 100:
        score = 100

    return round(score, 2)
