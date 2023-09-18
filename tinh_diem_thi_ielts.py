def calculate_listening_reading_band_score(correct_answers):
    if correct_answers >= 39:
        return 9.0
    elif correct_answers >= 37:
        return 8.5
    elif correct_answers >= 35:
        return 8.0
    elif correct_answers >= 33:
        return 7.5
    elif correct_answers >= 30:
        return 7.0
    elif correct_answers >= 27:
        return 6.5
    elif correct_answers >= 23:
        return 6.0
    elif correct_answers >= 20:
        return 5.5
    elif correct_answers >= 16:
        return 5.0
    elif correct_answers >= 13:
        return 4.5
    elif correct_answers >= 10:
        return 4.0
    elif correct_answers >= 7:
        return 3.5
    elif correct_answers >= 5:
        return 3.0
    elif correct_answers >= 3:
        return 2.5
    else:
        return 0.0

# Function to calculate the overall IELTS band score
def calculate_overall_band_score(reading, listening, speaking, writing):
    listening_score = calculate_listening_reading_band_score(listening)
    reading_score = calculate_listening_reading_band_score(reading)

    overall_score = (listening_score + reading_score + speaking + writing) / 4
    
    check = overall_score - int(overall_score) 
    if(check >= 0.25 and check < 0.75):
        overall_score = int(overall_score) + 0.5
    elif(check >= 0.75):
        overall_score = int(overall_score) + 1.0
    else:
        overall_score = int(overall_score)
    
    return overall_score

# Number of test cases
T = int(input())

for _ in range(T):
    # Read the scores for Reading, Listening, Speaking, and Writing
    reading, listening, speaking, writing = map(float, input().split())
    
    # Calculate and print the overall IELTS band score
    overall_score = calculate_overall_band_score(reading, listening, speaking, writing)
    print(format(overall_score, '.1f'))




