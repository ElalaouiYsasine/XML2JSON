from flask import Flask , render_template ,request ,url_for
import xmltodict
import json
import dicttoxml

app = Flask(__name__)

@app.route('/')

def home() :
    return render_template('index.html'  , data="")

@app.route('/getxml', methods=['POST']) #cette route réagira uniquement aux requêtes POST
def getxml() :
    xml_text = request.form['xml2']
    json_data = xml2json(xml_text)
    return render_template('index.html', data=json_data, input_text=xml_text)

def xml2json(xml_text) :
    try :
        if  xml_text is None or xml_text.strip() == "" :
            return "{}"
        else:
            xmlcode = xmltodict.parse(xml_text.strip())
            jsoncode = json.dumps(xmlcode, indent=4)
            return jsoncode
    except Exception as e :
        return f"Erreur de conversion : {str(e)}"

if __name__ == "__main__" :
    app.run(debug=True)