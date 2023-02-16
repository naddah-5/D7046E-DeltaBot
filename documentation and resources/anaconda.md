# Anaconda environment
This is a guide on how to set up the anaconda environment used for development in this code base.
## Pre-requisites
It is assumed that anaconda is installed on the system already, anaconda is available for download [here](https://www.anaconda.com/products/distribution).

## Installation
From the anaconda navigator, navigate to the environments overview. 

<img src="images\anaconda_environment.PNG"  width="250" height="300">

Then create a new environment by selecting "create".

<img src="images\anaconda_create.PNG" width="300" height="300">

You will then be prompted to choose a name for the environment and which python version you wish to use. For this project we will use Python 3.10.

<img src="images\anaconda_prompt.PNG" width="350" height="200">

Once the environment has been created verify that openssl has been installed.

<img src="images\anaconda_openssl.PNG" width="400" height="300">

Now *close* the anaconda navigator and open the anaconda prompt. Both the standard or powershell will work. Activate the environment by using the command:
> conda activate -n \<the name of the environment>

In order to then install pytorch in the environment, enter the command:
> conda install pytorch torchvision torchaudio pytorch-cuda=11.6 -c pytorch -c nvidia

This will take some time since it solves for version conflicts in the libraries and all their dependencies. Once this process is complete a set of compatible versions will be suggested and you are prompted to decide if you want to install them. Simply press enter.

After the base environment is installed, install the remaining pip dependencies by running the following command from the projects root folder:
> pip install -r requirements.txt