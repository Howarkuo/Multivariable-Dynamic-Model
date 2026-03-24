# Competition Model Analysis

## The Competition Model Equations
To find the nullclines, we start by setting the population growth rates ($\frac{da}{dt}$ and $\frac{db}{dt}$) to zero.

**Species a:**
$$\frac{da}{dt} = 0.2a(1 - \frac{a+b}{1000}) = 0$$

**Species b:**
$$\frac{db}{dt} = 0.5b(1 - \frac{a+b}{500}) = 0$$

---

### 1. Carrying Capacities ($K_a$ and $K_b$)
These are the most important variables for the layout of the graph because they define the actual boundaries of the nullclines.

* **$K_a$ (Carrying Capacity of species a):** Determines the position of the **a-nullcline** (the line where $\frac{da}{dt} = 0$). By solving the equation, we get the line $a + b = 1000$. $K_a$ serves as both the x-intercept and the y-intercept for this boundary.
* **$K_b$ (Carrying Capacity of species b):** Dictates the position of the **b-nullcline** (the line where $\frac{db}{dt} = 0$). Solving this gives the line $a + b = 500$. $K_b$ serves as the intercepts for this line.

### 2. Growth Rates ($\mu$ and $\lambda$)
While they dictate how fast the populations multiply, they do not affect where the nullclines are drawn.

* **The Math:** In the model, the growth rates are $\mu = 0.2$ and $\lambda = 0.5$. Because the nullclines are found by setting the entire equation to $0$, the algebraic method divides both sides by the growth rate, removing it from the nullcline equations ($a+b=1000$ and $a+b=500$).
* **The Visual Effect:** Instead of moving the lines, these rates determine the behavior of the **direction arrows** inside the regions. They control the magnitude of the vectors—meaning they dictate how fast the populations increase or decrease in Regions I, II, and III.

### 3. Population Variables ($a$ and $b$)
* **The Axes:** The variables $a$ and $b$ represent the population sizes at any given time. They form the horizontal and vertical axes of the phase plane graph.
* **The Point in Space:** The specific values of $(a, b)$ at a specific time determine exactly which region (I, II, or III) the current ecosystem state falls into, dictating the trajectory of the populations.