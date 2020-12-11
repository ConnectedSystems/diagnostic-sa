
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

# Structure

The main set of code is found in the `diagnostic_sa` directory.

These are:
* li_2010.py

  Example implementations of the linear function taken from [Li et al., (2010)](https://doi.org/10.1021/jp9096919)

* li_2010_diagnostic_morris_incorrect.py

Analysis of the incorrectly implemented model

* li_2010_diagnostic_morris_inactive.py

Analysis of the model with an inactive parameter


Tests intended for use with the `pytest` framework is found in `tests/test_li.py`.

These produce the error messages as shown in the paper.

Code and analysis from an earlier revision is included here as currently the [Open Science Framework](https://osf.io) cannot associate multiple repositories associated with a project.

These produce the figures included in Appendix A.

The original repository may be found [here](https://github.com/ConnectedSystems/oat-use).





