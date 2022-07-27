# Simplified Perlin Noise

Perlin noise (also sometimes classical Perlin noise) is a mathematical algorithm for generating a procedural texture by a pseudo-random method. It is used in computer graphics to increase the realism or graphical complexity of the surface of geometric objects. It can also be used to generate smoke, fog, etc. effects, *__but in this algoritm we use full random and matrix__*.


# How to use

There are many applications of Perlin noise. I saw a wood texture obtained by using modular arithmetic. I used it to create a path through a roguelike forest. You can easily get clouds by trimming the noise to an arbitrary level. The smoke in Under Construction is Perlin's noise, with the positive values corresponding to smoke and the negative values thrown out.

### Download and install

```bash
  git clone https://github.com/Numbers-Technologies/Perlin-Noise.git
  cd Perlin-Noise
  pip3 install -r requirements.txt
```

### Run as program

```bash
  python3 noise.py -s /path/to/file
```


### Run as a module

```python3
import noise

noise.start("/path/to/save")
```


# How does it works?

We create a matrix (64x64 for example) and fill it with units. Then, after selecting a random variable ( secret value ) and a random matrix element, random variables are generated around the random variable (1<x<sv]. Thus, we have like a mountain around the random variable (secret value). We do some number of iterations, after which we get "mountains"


# Screenshots

# License

GPL-3.0 license
