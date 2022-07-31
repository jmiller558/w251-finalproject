import pymodels
import sys, os
import requests
from fastapi import FastAPI, Request, Depends, BackgroundTasks, UploadFile
from fastapi.templating import Jinja2Templates
from database import SessionLocal, engine
from pydantic import BaseModel 
from pymodels import Ingredient, Recipe
from sqlalchemy.orm import Session
from sqlalchemy import func
from PIL import ImageTk, Image
import tkinter as tk
from io import BytesIO
import cv2
import torch

app = FastAPI()

pymodels.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")

path = sys.path[0]
model = torch.hub.load(path, 'custom', path='../best.pt', source='local')
model.conf = .7


class IngredientRequest(BaseModel):
    name: str

def yes_button_cmd(img_window):
    food_found_var.set(1)
    img_window.destroy() 

def no_button_cmd(img_window):
    food_found_var.set(0)
    img_window.destroy()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.get("/")
def home(request: Request, db: Session = Depends(get_db)):
    """
    show all ingredients in the database
    """

    try: 
        ingredients = db.query(Ingredient.name, func.sum(Ingredient.quantity).label("quantity")).group_by(Ingredient.name).all() 
    except: 
        ingredients = db.query(Ingredient) 
        ingredients = ingredients.all()

    return templates.TemplateResponse("home.html", {
        "request": request, 
        "ingredients": ingredients
    })

@app.post("/")
async def create_ingredient(request: Request,  db: Session = Depends(get_db)):
#     """
#     add one or more ingredients to the database, and generate potential recipes 
#     """
    WINDOW_NAME = "Food Detector"
    food_found = 0
    while food_found == 0:
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            image = frame[..., ::-1]
            results = model(image, size=640)
            results_frame = results.render()[-1][..., ::-1]
            cv2.imshow(WINDOW_NAME, results_frame)
            cv2.waitKey(1)
            df_ingred = results.pandas().xyxy[-1]
            if not(df_ingred.empty):
                break
            if cv2.getWindowProperty(WINDOW_NAME, cv2.WND_PROP_VISIBLE) < 1:
                break

        cap.release()
        cv2.destroyAllWindows()
        img_window = tk.Tk()
        global food_found_var
        food_found_var = tk.StringVar()
        food_found_var.set(0)
        title = tk.Label(img_window, text="Food Detected")
        title.config(font=("Courier",14))
        text = tk.Text(img_window, height=2)
        text.insert("1.0","Has the food been correctly identified?")
        yes_button = tk.Button(img_window, text="Yes (Add Ingredients)", command = lambda: yes_button_cmd(img_window))
        no_button = tk.Button(img_window, text="No (Try Again)", command = lambda: no_button_cmd(img_window))
        results.render()
        img_raw = results.imgs[-1]
        img = ImageTk.PhotoImage(Image.fromarray(img_raw))
        panel = tk.Label(img_window, image=img)
        title.pack()
        text.pack()
        yes_button.pack()
        no_button.pack()
        panel.pack(side="bottom", fill="both",expand="yes")
        img_window.mainloop()
        food_found = int(food_found_var.get())

    ingredient_names = df_ingred["name"].values.tolist()
    for ing_name in ingredient_names:
        ingredient = Ingredient()
        ingredient.name = ing_name.replace('_',' ').lower()
        ingredient.quantity = 1
        db.add(ingredient)
        db.commit()

    try: 
        ingredients = db.query(Ingredient.name, func.sum(Ingredient.quantity).label("quantity")).group_by(Ingredient.name).all() 
    except: 
        ingredients = db.query(Ingredient) 
        ingredients = ingredients.all()
    
    recipes = []
    api_key= '973b4f2f29344bb4a1eefe04f6b8bf6b'
    
    ingredient_str = ''
    ingredient_lst = []
    if len(ingredients) > 0:
        ingredient_str = ingredients[0].name
        ingredient_lst = [ingredients[0].name]
        print(ingredient_str)
        if len(ingredients) > 1: 
            for ing in ingredients[1:]:
                ingredient_str = ingredient_str + ',+' + ing.name
                ingredient_lst.append(ing.name)

    r = requests.get(f'https://api.spoonacular.com/recipes/findByIngredients?ingredients={ingredient_str}&number=10&apiKey={api_key}')
    for j in range(len(r.json())):
        recipe = Recipe()
        missing_list = ""
        used_list = ""
        for i,ingred in enumerate(r.json()[j]["missedIngredients"]):
            if i == 0:
                missing_list = ingred["name"]
            else:
                missing_list = missing_list+', '+ ingred["name"]
        for i,ingred in enumerate(r.json()[j]["usedIngredients"]):
            used_ingred = next(ing for ing in ingredient_lst if ing.lower().strip() in ingred["name"].lower().strip())
            if i == 0:
                used_list = used_ingred
            elif used_ingred not in used_list:
                used_list = used_list+', '+used_ingred
        recipe.recipe_name = r.json()[j]["title"]
        recipe.used_ingredients = used_list
        recipe.missing_ingredients = missing_list
        recipe.image = r.json()[j]["image"]
        recipes.append(recipe)
    
    return templates.TemplateResponse("home.html", {
        "request": request, 
        "ingredients": ingredients, 
        "recipes": recipes
    })

@app.post("/reset")
async def rest_ing_db():
    if os.path.exists(f"{path}/ingredients.db"):
        os.remove(f"{path}/ingredients.db")
