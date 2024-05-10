from fastapi import FastAPI, Query

app = FastAPI()

approved_users = {}

@app.get("/approval")
async def approval_user(key: str = Query(None), name: str = Query(None)):
    if key is None or name is None:
        return {"message": "Hey its me Hussain Afridi.", "status": "false"}
    if key in approved_users and approved_users[key] == name:
        return {"message": "User already approved.", "status": "true"}
    elif key in approved_users and approved_users[key] != name:
        return {"message": "Hey kids you cant bypass me lol.", "status": "false"}
    else:
      return {"message": "Hey its me Hussain Afridi.", "status": "false"}
@app.get("/userapproval_by_mr_bunnyxd")
async def approve_user(key: str = Query(None), name: str = Query(None)):
    approved_users[key] = name
    return {"message": "User approved successfully."}
    
@app.get("/approve_status")
async def approve_status(key: str = Query(None), name: str = Query(None)):
    if key is None or name is None:
        return {"message": "Key and name are required."}
    
    if key in approved_users and approved_users[key] == name:
        return {"message": "Approved successfully."}
    else:
        return {"message": "Approval failed."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)