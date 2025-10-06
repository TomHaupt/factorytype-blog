---
title: "The Space Rⁿ and its Topology"
date: 2025-10-04T12:00:00-06:00
draft: false
tags: ["workflow", "debug"]
---

### The Distance Function in Rⁿ
Points in the space Rⁿ are represented as n-tuples of real numbers, denoted as (x₁, x₂, ..., xₙ), where each xᵢ is a real number. The space Rⁿ is equipped with the standard Euclidean topology, which is defined using a distance function (or metric) that measures the distance between two points in Rⁿ. The distance function d: Rⁿ × Rⁿ → R is given by:
$$d((x₁, x₂, ..., xₙ), (y₁, y₂, ..., yₙ)) = √((x₁ - y₁)² + (x₂ - y₂)² + ... + (xₙ - yₙ)²)$$
This metric induces a topology on Rⁿ.<br>
<img src="/images/d(A,B).png" alt="d(A,B)" width="200"/>
If the space is R², the distance between the points A and B is given by:
d((0,0), (3,4)) = √((0-3)² + (0-4)²) = √(9 + 16) = √25 = 5<br>

### Open Sets in $\mathbb{R}^n$
In the topology of Rⁿ, a set U ⊆ Rⁿ is considered open if for every point x in U, there exists a positive radius r such that the open ball centered at x with radius r is entirely contained within U. An open ball B(x, r) in Rⁿ is defined as:
$$
B(x, r) = \lbrace{ y \in \mathbb{R}^n \mid d(x, y) < r \rbrace}
$$
This means that for any point in the open set, you can find a small "neighborhood" around that point that is also contained within the set.<br>
<img src="/images/O(A).png" alt="O(A)" width="200"/><br>
For example, in R², an open ball centered at (1,1) with radius 1 would include all points (x,y) such that the distance from (1,1) to (x,y) is less than 1.<br>


