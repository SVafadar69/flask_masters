#!/usr/bin/env python3

from flask import Flask, request, render_template_string, render_template


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        input_text = request.form.get('user_input', '')
        return render_template_string('''
            <p>You entered: {{ input_text }}</p>
            <form action="/" method="post">
                <input name="user_input" type="text" />
                <input type="submit" value="Submit!" />
            </form>
        ''', input_text=input_text)

    else:
        return '''
            <form action="/" method="post">
                <input name="user_input" type="text" />
                <input type="submit" value="Submit!" />
            </form>
        '''
if __name__ == '__main__':
    app.run(debug=True)