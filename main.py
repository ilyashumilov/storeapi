from fastapi import Body, Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from models import session, apples, faces

from pydantic import BaseModel
app = FastAPI()
auth = HTTPBasic()

class response(BaseModel):
    amount: int

@app.post("/")
def main(payload: response,auth_data: HTTPBasicCredentials = Depends(auth)):
    s = session()
    users = s.query(faces)

    for i in users:

        if auth_data.username == i.username and auth_data.password == i.password and i.role == 'seller':

            item = s.query(apples).first()
            item.amount = int(item.amount) + payload.amount
            s.commit()

            return 'Added to store:' + str(item.amount) + 'items'

        elif auth_data.username == i.username and auth_data.password == i.password and i.role == 'buyer':

            s = session()
            item = s.query(apples).first()
            if item.amount == 0 or item.amount - payload.amount <0:
                raise HTTPException(status_code=404, detail="Incorrect credentials")
            item.amount = int(item.amount) - payload.amount
            s.commit()
            return 'Sold:', item.amount + 'items'

        raise HTTPException(status_code=403, detail="Incorrect credentials")

