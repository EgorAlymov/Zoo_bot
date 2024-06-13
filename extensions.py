import config


def quiz_result(data: list) -> dict:
    animal_scores = dict.fromkeys(config.quiz_result, 0)

    for i in range(len(data)):
        for animal, animal_data in config.quiz_result.items():
            if data[i] == animal_data['answer'][i]:
                animal_scores[animal] += 1

    max_in_animal_scores = max(animal_scores, key=animal_scores.get)

    return config.quiz_result[max_in_animal_scores]