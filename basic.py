from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    # name = "Jose"
    # letters = list(name)
    # human_dict = {"name": 'Taimoor', "marks": 88}
    student_names = ["Taimoor", "Ali", "Hamza", "Shahzaib", "Numan", "Ashraf"]
    # return render_template('basic.html', my_variable=name, letters=letters, human_dict=human_dict)
    return render_template('basic.html', student_names=student_names)


if __name__ == '__main__':
    app.run(debug=True)
