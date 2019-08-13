# DRS-cli
This repository contains a [bravado]-based client for modified GA4GH Data Repository Service (DRS) API services the 
[Open API specification] for which can be found in the [mock-DRS] repository.

# Installation

Install as a package on your chosen python environment.

Clone repository
```bash
git clone https://github.com/elixir-europe/DRS-cli.git
```

Traverse project repository 
```bash
cd DRS-cli
python setup.py install
```

To use the client import to the python script as follows
```python
from drs_client import Client
client = Client.Client("the-drs-uri")
```

**_or_**

Use the gihub -e git+https://github.com/elixir-europe/DRS-cli.git to this repository and add it to your requirements 

To test the working of the client you can run the main of the [client](drs_client/Client.py) script which currently 
returns a response from one of the live mock services.

# Usage

The client implemented in this module are solely to support the functioning of the [TEStribute] repository and are 
tested to work for the [mock-DRS] server.

[TESTribute]:https://github.com/elixir-europe/TEStribute 
[mock-DRS]:https://github.com/elixir-europe/mock-DRS
[bravado]:https://github.com/Yelp/bravado
[Open API specification]:https://github.com/elixir-europe/mock-DRS/blob/master/mock_drs/specs/schema.data_repository_service.cd0186f.openapi.modified.yaml
