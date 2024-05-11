knowledge_base = {
    'malaria': ['chest pain', 'vomiting', 'fever', 'fatigue', 'headache', 'diarrhea'],
    'dengue': ['headache', 'joint pain', 'pain behind the eyes', 'rash', 'fever', 'vomiting'],
    'yellow fever': ['chills', 'muscle aches', 'loss of appetite', 'fever', 'nausea', 'headache']
}

def inference(user_symptoms):
    probability = {}

    for disease in knowledge_base.keys():
        count = 0
        for symptom in knowledge_base[disease]:
            if symptom in user_symptoms:
                count += 1
        probability[disease] = count / len(knowledge_base[disease])

    return probability

def ques_set():
    user_symptoms = []
    questions = []

    for disease in knowledge_base.keys():
        questions += knowledge_base[disease]

    questions = list(set(questions))

    print('Answer the following questions:')
    for question in questions:
        answer = input(f'Do you have {question}? [Y/N]: ')
        if answer.lower() == 'y':
            user_symptoms.append(question)

    return user_symptoms

def make_decision():
    max_questions = 3  # Maximum number of questions to ask
    ques_count = 0
    user_symptoms = []

    while ques_count < max_questions:
        user_symptoms += ques_set()
        ques_count += 1
        if user_symptoms:
            break

    if not user_symptoms:
        print('Maximum number of questions reached. Unable to make a decision based on the given information.')
    else:
        probabilities = inference(user_symptoms)
        max_probability = max(probabilities.values())
        likely_diseases = [disease for disease, prob in probabilities.items() if prob == max_probability]

        print("\n")
        if max_probability == 1:
            print('You are likely having ' + ', '.join(likely_diseases) + '.')
        elif max_probability > 0:
            print('You may have ' + ', '.join(likely_diseases) + '.')
        else:
            print('You are not having any disease.')

make_decision()
