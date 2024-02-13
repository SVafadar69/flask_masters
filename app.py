from flask import Flask, request, render_template_string, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        input_text = request.form.get('user_input', '')
        return render_template_string('''
            <h1>Welcome to our website!</h1>
            <p>Please input your data in the field below. You can enter text, numbers, or a combination of both.</p>
            <p>You entered: {{ input_text }}</p>
            <form action="/" method="post">
                <label for="user_input">Please enter your data:</label><br>
                <input name="user_input" type="text" />
                <input type="submit" value="Submit!" />
            </form>
        ''', input_text=input_text)

    else:
        return '''
            <h1>Welcome to our website!</h1>
            <p>Please input your data in the field below. You can enter text, numbers, or a combination of both.</p>
            <form action="/" method="post">
                <label for="user_input">Please enter your data:</label><br>
                <input name="user_input" type="text" />
                <input type="submit" value="Submit!" />
            </form>
        '''
if __name__ == '__main__':
    app.run(debug=True)