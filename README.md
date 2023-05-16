# ElephantLLM

ElephantLLM is a Python library for dealing with increasing the input length of LLM by appending memory management system.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install ElephantLLM.

```bash
pip install elephantllm
```

## Usage

```python
from elephantllm import ElephantLLM
import CustomModel # your model

# append memory to your model
model = CustomModel()
model_with_memory = ElephantLLM(model)
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)