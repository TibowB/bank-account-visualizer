from fastapi import FastAPI
from security import add_cors_midddleware
from entities import init_db
import uvicorn


app = FastAPI()


# DATABASE
init_db()

# SECURITY
add_cors_midddleware(app)

# CONTROLLERS
from controllers.import_controller import *
from controllers.account_controller import *
from controllers.transaction_controller import *

if __name__ == '__main__':
    uvicorn.run("app:app", host="127.0.0.1", port=5000, reload=True)
