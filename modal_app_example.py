import modal

# Create Modal app
app = modal.App("my-app")

# Define image with dependencies
image = modal.Image.debian_slim().pip_install([
    "fastapi",
    "uvicorn",
])

@app.function(
    image=image,
    keep_warm=1,  # Keep 1 container warm
)
@modal.web_endpoint(method="GET")
def hello():
    return {"message": "Hello from Modal!"}

@app.function(image=image)
@modal.web_endpoint(method="POST")
def process_data(data: dict):
    # Your processing logic here
    return {"processed": data, "status": "success"}

# For local testing
if __name__ == "__main__":
    with app.run():
        print("App is running locally...")