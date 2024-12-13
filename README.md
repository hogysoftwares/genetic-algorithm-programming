# genetic-algorithm-programming

This is a genetic algorithm designed to find the maxima and minima in any mathematical function. This particular case uses the six-hump camelback function, but the algorithm can be applied to any 3 dimensional function. Every generation has a population of ten, and the previous generation crossovers their binary strings representing their x,y position and the corresponding fitness score (the z position) to make the next generation. Mutations take place with a low probability at every bit of each agent. The population size and mutation rate can be changed to alter for best results.

Genetic algorithms are inspired from how crossovers and mutations happen in DNAs. However, they are a heuristics method alternative to random searchs. Basically, genetic algorithms are to be used when there are no better alternatives in terms of guarantee. It is still much better than random searchs, but they are also not guaranteed to find the most optimum solution.
