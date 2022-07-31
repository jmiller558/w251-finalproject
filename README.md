<div align="center">
<p>
   <img width="850" src="https://github.com/jmiller558/w251finalproject/blob/master/utils/smarterchef.png"></a>
</p>

<br>
<p>
SmarterChef was developed by Gabriela May-Lagunes, Jesse Miller, Tal Segal, Varun Tanna, and Anil Tipirini as a final project for DATASCI W251 Deep Learning in the Cloud and at the Edge at UC Berkeley. It establishes the fundemental infrastructure for a system that recognizes food items, stores an inventory of those items, and recommends recipes based on the items in inventory. 
</p>

## <div align="left">Running The Program</div>

To run the program for the first time, navigate to the user-interface folder and execute the run script with:

```bash
sh run
```

The run script will execute set-up from building the docker image, to running the docker container and launching the program.

In subsquent runs, the container and program can be launched directly by navigating to the user_interface/w251_app folder and entering the commands:
```bash
docker rm w251_app
```
```bash
docker run --name w251_app -v $PWD:/app/ --device=/dev/video0:/dev/video0 -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY -p 8000:8000 w251_app
```

To reset the inventory prior to launching the program, simply navigate to the user_interface/w251_app folder and delete the ingredients.db file.

## <div align="left">Additional Repo Files</div>

Other files in the repo include:

1. custom_model_train.ipynb: a jupyter notebook showing the model training and validation process
2. train.py: script used for training
3. val.py: script used for validation
4. other supporting folders and files utilized the above scripts


