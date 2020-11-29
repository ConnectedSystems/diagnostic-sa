
Companion code for a paper showcasing property-based sensitivity analysis as a useful approach in model development and quality assurance.


# Setup

Clone the necessary repositories

```bash
$ git clone https://github.com/ConnectedSystems/diagnostic-sa.git
$ git clone https://github.com/ConnectedSystems/SALib.git --branch radial-oat-method --single-branch salib-roat 
```

Create conda environment (the specification for Windows platforms is provided)

```bash
$ conda create --name <env> --file win_env.yml
```

Install as a locally editable package

```bash
$ cd diagnostic-sa
$ pip install -e .
$ cd ..
$ cd salib-roat
$ pip install -e .
```

Full instructions as above:

```bash
$ git clone https://github.com/ConnectedSystems/diagnostic-sa.git
$ git clone https://github.com/ConnectedSystems/SALib.git --branch radial-oat-method --single-branch salib-roat 

# Replace environment name with your own
$ conda create --name <env> --file win_env.yml

$ cd diagnostic-sa
$ pip install -e .
$ cd ../salib-roat
$ pip install -e .
$ cd ..
```


