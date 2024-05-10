from fastapi import FastAPI, Query

app = FastAPI()

approved_users = {}

@app.get("/approval")
async def approval_user(key: str = Query(None)):
    if key is None :
        return {"message": "Hey its me Hussain Afridi.", "status": "rejected"}
    elif key in approved_users :
        return {"message": "Welcome to MR. BUNNY World", "status": "succesfull"}
    elif key not in approved_users :
        return {"message": "Hey kids you cant bypass me lol.", "status": "rejected"}
    else:
      return {"message": "Hey its me Hussain Afridi.", "status": "rejected"}

@app.get("/user")
async def approval_user(key: str = Query(None), name: str = Query(None)):
    if key is None or name is None:
        return {"message": "Hey its me Hussain Afridi.", "welcome": "false"}
    elif key in approved_users and approved_users[key] == name:
        return {"message": "Welcome to MR. BUNNY World", "welcome": "true"}
    elif key in approved_users and approved_users[key] != name:
        return {"message": "Hey kids you cant bypass me lol.", "welcome": "false"}
    else:
      return {"message": "Hey its me Hussain Afridi.", "welcome": "false"}
@app.delete("/user_removed_by_mr_bunnyxd")
async def remove_user(key: str = Query(None)):
    if key in approved_users:
      del approved_users[key]
      return {"message": "User removed successfully."}
    raise HTTPException(status_code=404,detail="User not found")
    
@app.get("/userapproval_by_mr_bunnyxd")
async def approve_user(key: str = Query(None), name: str = Query(None)):
    approved_users[key] = name
    return {"message": "User approved successfully."}
    
@app.get("/approve_status")
async def approve_status(key: str = Query(None), name: str = Query(None)):
    if key is None or name is None:
        return {"message": "Key and name are required."}
    
    if key in approved_users and approved_users[key] == name:
        return {"message": "User already Approved."}
    else:
        return {"message": "Approval failed."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
