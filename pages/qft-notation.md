# Foundations

## Understanding Contravariant and Covariant Components

Consider how we find the length $l$ of a vector in a 3D Cartesian system with one end of the vector at the origin, i.e.,

$$
\begin{aligned}
    (l)^2 = (X_1)^2 +(X_2)^2 +(X_3)^2 = \\
    \sum_i X_i X_i =X_i X_i = \\
    \begin{bmatrix} X_1 & X_2 & X_3 \end{bmatrix}\begin{bmatrix} X_1 \cr X_2 \cr X_3 \end{bmatrix} = \\
    \begin{bmatrix} X_1 & X_2 & X_3 \end{bmatrix}\begin{bmatrix} 1 & 0 & 0 \cr 0 & 1 & 0 \cr 0 & 0 & 1 \end{bmatrix}\begin{bmatrix} X_1 \cr X_2 \cr X_3 \end{bmatrix} = X_i \delta_{ij} X_j
\end{aligned}
$$

where $\delta_{ij} X_j = \sum_j \delta_{ij} X_j = X_i$

Here, with a future purpose in mind, we insert an identity matrix, represented in index notation by
the Kronecker delta $\delta_{ij}$ (=0 if row i $\neq$ column j ; = 1 if i = j), on the RHS.

By the same reasoning, imagine a spatially 4D Cartesian system, where the length of a 4D vector is

$$
\begin{aligned}
    (l)^2 = (X_0)^2 +(X_1)^2 +(X_2)^2 + (X_3)^2 = \\
    \sum_i X_\mu X_\mu =X_\mu X_\mu = \\
    \begin{bmatrix} X_0 & X_1 & X_2 & X_3 \end{bmatrix}\begin{bmatrix} X_0 \cr X_1 \cr X_2 \cr X_3 \end{bmatrix} = \\
    \begin{bmatrix} X_0 & X_1 & X_2 & X_3 \end{bmatrix}\begin{bmatrix} 1 & 0 & 0 & 0 \cr 0 & 1 & 0 & 0 \cr 0 & 0 & 1  & 0 \cr 0 & 0 & 0 & 1 \end{bmatrix}\begin{bmatrix} X_0 \cr X_1 \cr X_2 \cr X_3 \end{bmatrix} = X_\mu \delta_{\mu\nu} X_\nu
\end{aligned}
$$

Going forward to 4D spacetime of special relativity theory (SRT), and the "length" of a 4D vector we have in mind is the proper time $\tau$ on an object passing by us. The $0^{th}$ coordinate is now time instead of a spatial $X_0$ coordinate. From SRT, we know

$$
\begin{aligned}
    (c\tau)^2 = (ct)^2 - (X_1)^2 - (X_2)^2 - (X_3)^2 = \\
    \begin{bmatrix} ct & X_1 & X_2 & X_3 \end{bmatrix}
    \begin{bmatrix} ct \cr -X_1 \cr -X_2 \cr -X_3 \end{bmatrix}
\end{aligned}
$$

## Covariant and Contravariant notation

We shall use a notation using contravariant components $x^{\mu}$ of the 4D position vector as 3D cartesian coordinates $X_i$ plus ct, i.e.

$$
x^{\mu} =
\begin{bmatrix} x^0 \cr x^1 \cr x^2 \cr x^3\end{bmatrix}=
\begin{bmatrix}ct \cr X_1 \cr X_2 \cr X_3\end{bmatrix}=
\begin{bmatrix}ct,X_i\end{bmatrix}^T
$$
