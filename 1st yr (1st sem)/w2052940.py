# I declare that my work contains no examples of misconduct, such as plagiarism, orcollusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w2052940
# Date: 13.12.2023


# Importing from the graphics.py module
from graphics import *

# Result outcomes dictionary
OUTCOME_RESULTS = {
    (120, 0, 0): "Progress",
    (100, 20, 0): "Progress (module trailer)",
    (100, 0, 20): "Progress (module trailer)",
    (80, 40, 0): "Module retriever",
    (80, 20, 20): "Module retriever",
    (80, 0, 40): "Module retriever",
    (60, 60, 0): "Module retriever",
    (60, 40, 20): "Module retriever",
    (60, 20, 40): "Module retriever",
    (60, 0, 60): "Module retriever",
    (40, 80, 0): "Module retriever",
    (40, 60, 20): "Module retriever",
    (40, 40, 40): "Module retriever",
    (40, 20, 60): "Module retriever",
    (40, 0, 80): "Exclude",
    (20, 100, 0): "Module retriever",
    (20, 80, 20): "Module retriever",
    (20, 60, 40): "Module retriever",
    (20, 40, 60): "Module retriever",
    (20, 20, 80): "Exclude",
    (20, 0, 100): "Exclude",
    (0, 120, 0): "Module retriever",
    (0, 100, 20): "Module retriever",
    (0, 80, 40): "Module retriever",
    (0, 60, 60): "Module retriever",
    (0, 40, 80): "Exclude",
    (0, 20, 100): "Exclude",
    (0, 0, 120): "Exclude"
}

# Function to get a valid integer as an input
def get_input(prompt, valid_values):
    user_input = None

    while user_input not in valid_values:
        try:
            user_input = int(input(prompt))
            if user_input not in valid_values:
                print("Out of range")
            else:
                break  # Break the loop when a valid input is received
        except ValueError:
            print("Integer required")

    return user_input


# Function to predict the progression outcome based on the student's credit
def predict_progression(pass_credits, defer_credits, fail_credits):

    total_credits = pass_credits + defer_credits + fail_credits
    input_condition = (pass_credits, defer_credits, fail_credits)

    if total_credits != 120:
        return "Total incorrect"
    
    return OUTCOME_RESULTS.get(input_condition, "Outcome not defined")

# Function to create a histogram as a summary using graphics library

def create_histogram(data):
    # Graph window size and window name
    win = GraphWin("Histogram", 580, 420)
    # Window background colour
    win.setBackground("#E9EFE7")

    bar_width = 90
    spacing = 39
    base_height = 320

    categories = ["Progress", "Trailer", "Retriever", "Excluded"]

    category_map = {
        "Progress" : "Progress",
        "Progress (module trailer)" : "Trailer",
        "Module retriever" : "Retriever",
        "Exclude" : "Excluded"
    }

    updated_data = {category_map[category]: data[category] for category in data if category in category_map}

    total_students = sum(updated_data.values())

        # Bars in the histogram
    for i, category in enumerate(categories):
        bar_height = updated_data.get(category, 0)
        bar = Rectangle(Point(i * (bar_width + spacing) + spacing, base_height),
                        Point((i + 1.25) * (bar_width + spacing), base_height - (bar_height * 20)))
        bar.setFill(get_fill_color(category))
        bar.draw(win)

        # Text on top 
        topic = Text(Point(290, 30), "Histogram Results")
        topic.setSize(23)
        topic.draw(win)

        # Text on the top of bars
        text2 = Text(Point((i + 0.5) * (bar_width + spacing) + spacing, base_height - (bar_height * 20) - 10),
                    f"{bar_height}")
        text2.setSize(15)
        text2.draw(win)

        # Category names under the bars
        text3 = Text(Point((i + 0.5) * (bar_width + spacing) + spacing, base_height - (bar_height) + 15),
                    f"{category}")
        text3.setSize(15)
        text3.draw(win)

    # Total outcomes text
    total_text = Text(Point(150,380), f"{total_students} Total outcomes")
    total_text.setSize(20)
    total_text.draw(win)

    win.getMouse()
    win.close()

# Function to get fill color based on category
def get_fill_color(category):
    color_map = {
        "Progress": "#A6F98C",
        "Trailer": "#93BC74",
        "Retriever": "#99B061",
        "Excluded": "#C6A6A6"
    }
    return color_map.get(category, "white")

# Main function
def main():
    # Initialization
    progression_data = []
    continue_input = 'y'
    outcome_data = {
        "progress": 0,
        "Trailer": 0,
        "Retriever": 0,
        "Excluded": 0
    }

    while continue_input.lower() == 'y':
        # Get input from the user
        pass_credits = get_input("\nEnter your total PASS credits: ", valid_values=[0, 20, 40, 60, 80, 100, 120])
        defer_credits = get_input("Enter your total DEFER credits: ", valid_values=[0, 20, 40, 60, 80, 100, 120])
        fail_credits = get_input("Enter your total FAIL credits: ", valid_values=[0, 20, 40, 60, 80, 100, 120])

        # Predict progression outcome
        outcome = predict_progression(pass_credits, defer_credits, fail_credits)
        print(outcome)
        outcome_data[outcome] = outcome_data.get(outcome, 0)+1

        # Store progression data
        progression_data.append((outcome, pass_credits, defer_credits, fail_credits))

        #Ask if the user wants to continue
        continue_input = input("\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ")

    if continue_input.lower() == 'q':

        # Display the outcomes
        print("\nPart 2:")
        for data in progression_data:
            print(f"{data[0]} - {data[1]}, {data[2]}, {data[3]}")

        # Save outcomes as a text file
        with open("progression_data.txt", "w") as file:
            file.write("Part 3:\n")
            for data in progression_data:
                file.write(f"{data[0]} - {data[1]}, {data[2]}, {data[3]}\n")

        # creating histogram
        create_histogram(outcome_data)

# Entry point of the script
if __name__ == "__main__":
    main()

