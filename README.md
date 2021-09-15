# FAST API ESSENTIALS

The following packages are necessary to run any FastAPI scripts<br> 
- fastapi (pip install fastapi)
- uvicorn (pip install uvicorn)

The code must be run in the command prompt through the following command:<br><br>
```uvicorn Index:app --reload```

**uvicorn** : Uvicorn is a fast web server.<br>
**Index:app** : Index is the module where the FastAPI is initialized. app is the name of the variable which is assigned with the instance of FastAPI.<br>
**--reload** : Reload is a flag for development purposes only. This will automatically restart the uvicorn server with any changes made in the code while in development.

Once the server is running. Open your browser and paste the following URL:<br><br>
``` http://127.0.0.1:8000/ ```

# ABOUT THE REPOSITORY

In this repository, we will demonstrate three techniques in FastAPI.
- **Communication through "JSON Payload"**<br>
A payload is the actual data pack sent in an HTTP request. It is a piece of critical information when we make an API request. 
This payload can be in several formats. We will look into the JSON format in particular as a majority of APIs communicate via a JSON 
payload.

- **Uploading a file**<br>
Uploading a file can be done with the UploadFile and File class from the FastAPI library. Let us keep this simple by just 
creating a method that allows the user to upload a file. Once uploaded, we will display the name of the file as a response as well as 
print it for verification in the command prompt.

- **A combination of accepting data and file uploads**<br>
We can create a function that supports a combination of accepting data and file uploads with the help of the "Depends" class. 
A function may have dependencies for several reasons, such as code reusability, security, database connections, etc. 
A Dependant function is a function that uses another function/class to carry out its activities.