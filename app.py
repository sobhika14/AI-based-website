import openai
import flask
# Set up the OpenAI API client
openai.api_key = "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"
# Set up the Flask app
app = flask.Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def generate_description():
 # Get the user's input text
 input_text = flask.request.form.get("input_text")

 # Use GPT-3 to generate a description for the Instagram post
 prompt = (
 f"Give me 2 line Quotes and 10 Hashtags for an Instagram post for the following text:\n{input_text}\n\n"
 "The description should be no more than 100 characters."
 )
 response = openai.Completion.create(
 engine="text-davinci-002", #text-davinci-002 #gpt2-small
 prompt=prompt,
 temperature=0.7,
 max_tokens=100,
 top_p=1,
 frequency_penalty=1,
 presence_penalty=1
 )
 description = response["choices"][0]["text"]

 # Render the generated description in the HTML template
 return flask.render_template("index.html", input_text=input_text, description=description)
if __name__ == "__main__":
 app.run()
