# forloop
Forloop.ai platform - package containing public API commands
- most of the platform currently in private repositories

See our website for public release
www.forloop.ai


forloop is a Python library for easy automation and setting up of data preparation pipelines. Covering tasks from webscraping, API connectors to cleaning and exploratory data analysis.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install forloop.

```bash
pip install forloop
```

## Usage
Download our desktop APP directly from our website www.forloop.ai or use our platform directly from python as a library

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
![obrazek](https://user-images.githubusercontent.com/29150831/146663009-c569a3ea-0c6f-4b79-abb1-3221fb1e747c.png)


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

