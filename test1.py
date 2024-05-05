import base64
from flask import Flask, request, jsonify
from inference_sdk import InferenceHTTPClient

app = Flask(__name__)

# initialize the client
CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="b8MX4715oE8Tp0Gt9hnA"
)

def image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        # Read the image file in binary mode
        image_binary = img_file.read()
        # Encode the binary data into base64
        base64_encoded = base64.b64encode(image_binary)
        # Decode the bytes object to a string
        base64_string = base64_encoded.decode('utf-8')
    return base64_string

@app.route('/infer', methods=['POST'])
def infer_image():
    # Check if the request contains an image
    if 'files' not in request.files:
        return jsonify({'error': 'No image provided'})
    
    image_file = request.files['files'].filename
    print("degycgjyfcyf", image_file)
    
    # Save the image file temporarily
    # image_path = 'temp_image.jpg'  # You can use any temporary path here
    # image_file.save(image_path)

    # Convert the image to base64
    base64_image = image_to_base64(image_file)

    # Pass the base64-encoded image to the inference SDK
    result = CLIENT.infer(base64_image, model_id="dogs-xysua/1")

    # Remove the temporary image file
 #   os.remove(image_path)

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
