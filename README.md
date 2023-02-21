# Forloop

This is a public API repository allowing users to use [Forloop.ai](www.forloop.ai) platform directly as a Python library

Forloop is a new tool and a Python library focusing on easy automation and setting up of data extraction and data preparation pipelines. Covering tasks from webscraping, over cleaning, transformations and exploratory data analysis to orchestration and working with databases.

## Installation

In order to obtain a full version of Forloop including the no-code interface please register and download the platform from [app.forloop.ai](app.forloop.ai).

For simplified API version you can use the package manager [pip](https://pip.pypa.io/en/stable/) to install forloop as a Python library.

```bash
pip install forloop
```

## Demo

![pagegif_1_3](https://user-images.githubusercontent.com/29150831/199597423-a9888164-9eef-4e97-b822-18d8c79cd21b.gif)


## New cloud version (coming soon)

![obrazek](https://user-images.githubusercontent.com/29150831/220236250-46df2988-5af6-417f-a02b-6979da17c330.png)


## Getting started

Download our desktop app directly from our website [app.forloop.ai](app.forloop.ai) or use our platform directly from Python as a library

See our [documentation](http://app.forloop.ai/documentation/) to quickly start using Forloop.ai platform

Please join our [Slack community](https://join.slack.com/t/forloopaicommunity/shared_invite/zt-17bdp5hmc-Uu~IMg9F7W6uHUenUY_m5A) and ask questions, we will help you!

## Usage of Python library
Download our desktop app directly from our website [app.forloop.ai](app.forloop.ai) or use our platform directly from Python as a library

```python
import forloop.forloop_core as flcore

fc=flcore.ForloopClient(url="http://127.0.0.1:5000")

nodes=fc.get_nodes("pipeline1.flpl")
analyzed_data=fc.analyze_data("train.csv")
cleaned_data=fc.clean_data("train.csv")

print(nodes)
print(analyzed_data)
print(cleaned_data)
```

More examples will be gradually added in the folder Examples.

## More demos of the platform

(Downloadable at app.forloop.ai)

Intelligent data cleaning

![pagegif_2_3](https://user-images.githubusercontent.com/29150831/199597480-618785be-98f4-44ac-8294-7e31e2c8c5e7.gif)

Smooth mapping between code and no-code

![pagegif_3](https://user-images.githubusercontent.com/29150831/199597510-5a74d8eb-ba22-419e-86ae-372bb953a65a.gif)



## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change + feel free to join our community slack channel https://join.slack.com/t/forloopaicommunity/shared_invite/zt-10b6x45dz-joCPw3GQRgyZ6Z8srYxLog.

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Currently implemented

* Webscraping
* RPA
* Databases
* API connectors
* Pipelining
* Cleaning
* Launching of Python scripts
* Scheduling / Orchestration
* Google sheets integration
* Airtable integration
* Pipedrive Integration
* Code View
* Data Grid (Table-like) View
* Database View

