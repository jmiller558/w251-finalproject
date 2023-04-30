<p align="center">
   <img width="850" src="https://github.com/jmiller558/w251-finalproject/blob/main/utils/smarterchef2.png"></a>
</p>

<br>
<p>
SmarterChef was developed by Gabriela May-Lagunes, Jesse Miller, Tal Segal, Varun Tanna, and Anil Tipirini as a final project for DATASCI W251 Deep Learning in the Cloud and at the Edge at UC Berkeley. It is a fully working end-to-end system that recognizes food items, maintains an inventory of those items, and recommends recipes based on the items in inventory. It establishes the fundamental infrastructure for more advanced food recognition programs, as well as for any system designed to track inventory via camera/image recognition and perform analysis/recommendations based on that inventory.

* You can read our final report [here](https://github.com/jmiller558/w251-finalproject/blob/b153e901555f0d82b293d731718bcf2a538abe29/W251-FinalReport-SmarterChef.pdf)
* You can view our final presentation (including a video demo) [here](https://docs.google.com/presentation/d/1hwfvzs1H4zhOsN7YDTPCyZFCEXOVjZ-zF9jXdp0Z_dc/edit?usp=sharing)
</p>
<p align="center">
   <img width="850" src="https://github.com/jmiller558/w251-finalproject/blob/main/utils/smarterchef1.png"></a>
</p>

## <div align="center">Running The Program</div>

<p align="left">
To run the program for the first time, navigate to the user-interface folder and execute the run script as follows:
</p>

```bash
cd user_interface
sh run
```

<p align="left">
The run script will execute the full initial set-up from building the docker image to running the docker container and launching the program.
<br>

In subsquent runs, the container and program can be launched directly by navigating to the user_interface/w251_app folder and entering the docker commands as follows:
</p>

```bash
cd user_interface/w251_app
docker rm w251_app
docker run --name w251_app -v $PWD:/app/ --device=/dev/video0:/dev/video0 -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY -p 8000:8000 w251_app
```

## <div align="center">Additional Repo Files</div>

Other files in the repo include:

1. custom_model_train.ipynb: a jupyter notebook showing the model training and validation process
2. train.py: script used for training
3. val.py: script used for validation
4. other supporting folders and files utilized in the above scripts


