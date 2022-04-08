from fastapi import Body, Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from models import session, apples, faces

from pydantic import BaseModel
app = FastAPI()
auth = HTTPBasic()

class response(BaseModel):
    amount: int
s = session()

@app.post("/")
def main(payload: response,auth_data: HTTPBasicCredentials = Depends(auth))
    users = s.query(faces)
    
    print(auth_data.username,auth_data.password)
    
    for i in users:
        print(i.username,i.password)
        
        if auth_data.username == i.username and auth_data.password == i.password:
            
            if i.role == 'seller':
                item = s.query(apples).first()
                item.amount = int(item.amount) + payload.amount
                s.commit()
                
                item = s.query(apples).first()
                
                return 'Added to store: ' + str(payload.amount) + 'items' + '  Amount awailable:'+ str(item.amount)
            
            if i.role == 'buyer':
                item = s.query(apples).first()
                
                if item.amount == 0 or item.amount - payload.amount <0:
                    raise HTTPException(status_code=404, detail="Not enough items")
                
                item.amount = int(item.amount) - payload.amount
                s.commit()
                
                item = s.query(apples).first()
                return 'Sold: ' + str(payload.amount) + 'items' + '  Amount awailable:'+ str(item.amount)

    raise HTTPException(status_code=403, detail='Auth error')

#buyer  | Frabian  | Frabian