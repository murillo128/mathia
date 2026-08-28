# PF-088 — the `1/4` threshold is a one-dimensional propagation threshold, not a prime-specific spectral signature

**Status:** `NEGATIVE/CONTROL-EXPERIMENT` + `EXACT-DERIVED` + correction to the interpretation of PF-084/PF-086/PF-087.

## Claim

The sharp boundary

\[
\operatorname{Re}s=\frac14
\]

found in

- PF-084 for the all-block exact/reference Ruelle sector, and
- PF-086/PF-087 for the exact/reference direct cusp-scattering kernel,

is **not prime-specific**.

Exactly the same boundary occurs if the prime sequence is replaced by the featureless integer sequence

\[
x_n^0=n,\qquad n\ge N>2,
\]

while retaining the same exact prime-circle/projective map

\[
x_n^E=V(n)=\pi\cot\frac{\pi}{n}.
\]

For this integer control:

\[
D_{\mathbb Z}(s)\in\mathcal S_1
\quad\Longleftrightarrow\quad
\operatorname{Re}s>\frac14,
\]

in the same sense as PF-087: above `1/4` the direct exact/reference scattering defect is trace class, whereas for

\[
0<\operatorname{Re}s\le\frac14
\]

a single row is not in `ell^2`, so the matrix has no bounded extension on `ell^2`.

Likewise, the integer-control analogue of the all-block relative Ruelle product has sharp absolute-convergence boundary `Re s=1/4`.

Therefore the exponent `1/4` comes from the combination

```text
one-dimensional ordered channel tail
+ propagation amplitude |i-j|^(-2s)
+ Hilbert-space / two-pass squaring
```

rather than from prime-gap fluctuations.

The prime sequence changes coefficients, slowly varying weights, and subleading structure, but it is not responsible for the quarter exponent itself.

---

## 1. Why this is the right control

The comparison used in PF-082--PF-087 is

\[
V(x)=\pi\cot\frac{\pi}{x}
\qquad\text{versus}\qquad
V_0(x)=x.
\]

Nothing in the orthogonal-circle algebra requires the sample points to be prime in order to define the corresponding ordered endpoint geometry. Replacing `p_n` by `n` therefore gives a clean null model:

- same exact orthogonal-circle map `V`;
- same exact/projective comparison;
- same zero-twist ordered flute combinatorics;
- no prime gaps at all.

The ambient interior/exterior inversion remains exactly the same and, as in PF-017, is not promoted to an intrinsic spectral symmetry.

---

## 2. Exact asymptotics of the integer-circle tail

The standard cotangent expansion gives

\[
V(x)
=x-\frac{\pi^2}{3x}-\frac{\pi^4}{45x^3}+O(x^{-5}),
\]

and

\[
V'(x)
=\frac{\pi^2}{x^2}\csc^2\frac{\pi}{x}>1,
\]

because `sin y<y` for `0<y<pi/2`.

Hence the exact integer gaps

\[
\Delta_n^E=V(n+1)-V(n)
\]

satisfy

\[
\Delta_n^E
=1+\frac{\pi^2}{3n(n+1)}+O(n^{-4})>1.
\]

For the projective reference `Delta_n^0=1`. The canonically normalized cusp-width factors are

\[
W_n^\bullet
=2\left(\frac1{\Delta_{n-1}^\bullet}+\frac1{\Delta_n^\bullet}\right).
\]

Therefore

\[
W_n^0=4,
\]

while

\[
W_n^E
=4-\frac{4\pi^2}{3(n^2-1)}+O(n^{-4})<4.
\]

In particular

\[
\sqrt{\frac{W_n^E}{W_n^0}}
=1+O(n^{-2}),
\]

with a strictly smaller-than-one value for every fixed sufficiently large `n`.

For `i<j`, the long divided difference obeys

\[
\frac{V(j)-V(i)}{j-i}=1+O(i^{-2}),
\]

uniformly in `j>i`, by the mean-value theorem and `V'(x)-1=O(x^{-2})`.

For fixed `i`, moreover,

\[
\frac{V(j)-V(i)}{j-i}\longrightarrow1
\qquad(j\to\infty).
\]

---

## 3. Integer-control direct scattering kernel

After the same width-one cusp normalization as PF-086/PF-087, define

\[
C_{ij}^\bullet
=\sqrt{W_i^\bullet W_j^\bullet}\,
 |x_j^\bullet-x_i^\bullet|.
\]

For the integer reference,

\[
\boxed{C_{ij}^0=4|j-i|.}
\]

Let

\[
R_{ij}:=\frac{C_{ij}^E}{C_{ij}^0}.
\]

The estimates above imply, for `i<j`,

\[
\boxed{|\log R_{ij}|\le C i^{-2}.}
\tag{1}
\]

For fixed `i`,

\[
R_{ij}\longrightarrow
\rho_i:=\sqrt{\frac{W_i^E}{4}}\in(0,1).
\tag{2}
\]

Now define the relative direct-channel kernel

\[
D_{\mathbb Z}(s)_{ij}
=
\begin{cases}
(C_{ij}^E)^{-2s}-(C_{ij}^0)^{-2s},&i\ne j,\\
0,&i=j.
\end{cases}
\]

This is exactly the same identity-double-coset construction used in PF-086/PF-087, but with no prime sampling.

---

## 4. Trace class above `1/4`

Fix a compact `K` contained in `Re s>1/4`, and choose

\[
\sigma_0>\frac14,
\qquad
\sigma_0<\inf_{s\in K}\operatorname{Re}s.
\]

From (1) and the mean-value estimate for `r -> r^(-2s)`,

\[
|D_{\mathbb Z}(s)_{ij}|
\le
C_K i^{-2}|j-i|^{-2\sigma_0},
\qquad i<j.
\tag{3}
\]

Let `r_i` be the strict upper-triangular row. Then

\[
\begin{aligned}
\|r_i\|_2^2
&\le
C_K i^{-4}
\sum_{m\ge1}m^{-4\sigma_0}.
\end{aligned}
\]

The sum over `m` is finite exactly because

\[
4\sigma_0>1.
\]

Thus

\[
\|r_i\|_2\le C_K i^{-2},
\]

and therefore

\[
\sum_i\|r_i\|_2<\infty.
\]

As in PF-087, the strict upper triangle has the nuclear decomposition

\[
U(s)=\sum_i e_i\otimes r_i^*,
\]

so

\[
U(s)\in\mathcal S_1.
\]

Since

\[
D_{\mathbb Z}(s)=U(s)+U(s)^T,
\]

we obtain

\[
\boxed{
D_{\mathbb Z}(s)\in\mathcal S_1
\qquad(\operatorname{Re}s>1/4).
}
\]

An ordinary Fredholm determinant therefore exists in exactly the same quarter-plane as for the prime control:

\[
\det(I+D_{\mathbb Z}(s)).
\]

---

## 5. A single row becomes non-square-summable at and below `1/4`

Fix `i`. From (2), for every `s` with `Re s>0`,

\[
R_{ij}^{-2s}-1
\longrightarrow
\rho_i^{-2s}-1\ne0.
\]

The last inequality holds because `0<rho_i<1`; `rho_i^{-2s}=1` is impossible when `Re s>0`.

Consequently there are `c_{i,s}>0` and `J` such that

\[
|D_{\mathbb Z}(s)_{ij}|
\ge
c_{i,s}|j-i|^{-2\operatorname{Re}s}
\qquad(j\ge J).
\]

Hence

\[
\sum_j|D_{\mathbb Z}(s)_{ij}|^2
\ge
c_{i,s}^2
\sum_{m\ge J-i}m^{-4\operatorname{Re}s}.
\]

This diverges exactly when

\[
4\operatorname{Re}s\le1.
\]

Therefore

\[
\boxed{
D_{\mathbb Z}(s)
\text{ has no bounded extension on }\ell^2
\quad
(0<\operatorname{Re}s\le1/4).
}
\]

So the exact same sharp transition as PF-087 occurs without primes:

\[
\boxed{
\begin{array}{ll}
\operatorname{Re}s>1/4:&D_{\mathbb Z}(s)\in\mathcal S_1,\\[1mm]
0<\operatorname{Re}s\le1/4:&D_{\mathbb Z}(s)\text{ is not bounded on }\ell^2.
\end{array}}
\]

---

## 6. The all-block Ruelle `1/4` threshold is also reproduced by integers

The same control test applies to PF-084.

Fix a left edge

\[
a=m-1<b=m
\]

and let the right edge run to infinity,

\[
c=n<d=n+1.
\]

For the projective integer reference,

\[
Y=n-m,
\qquad
\chi_{m,n}^0=Y(Y+2).
\]

Thus

\[
L_{m,n}^0
=4\operatorname{arsinh}\sqrt{Y(Y+2)}
=4\log(2Y)+o(1).
\]

For the exact endpoints `V(k)`, the two long divided differences and the far right unit gap tend to their projective values, while the fixed left gap is

\[
\Delta_{m-1}^E=V(m)-V(m-1)>1.
\]

Therefore

\[
\frac{\chi_{m,n}^E}{\chi_{m,n}^0}
\longrightarrow
\frac1{\Delta_{m-1}^E},
\]

and hence

\[
\boxed{
L_{m,n}^E-L_{m,n}^0
\longrightarrow
-2\log\Delta_{m-1}^E<0.
}
\tag{4}
\]

For the relative Ruelle factor,

\[
F_{m,n}(s)
=
\log
\frac{1-e^{-sL_{m,n}^E}}
     {1-e^{-sL_{m,n}^0}},
\]

(4) gives, for fixed `m` and `Re s>0`,

\[
|F_{m,n}(s)|
\asymp_{m,s}
e^{-\operatorname{Re}s L_{m,n}^0}
\asymp
(n-m)^{-4\operatorname{Re}s}.
\]

Hence even one fixed-left subproduct has the exact boundary

\[
\sum_n|F_{m,n}(s)|<\infty
\quad\Longleftrightarrow\quad
\operatorname{Re}s>\frac14.
\]

Conversely, the uniform projective-defect estimate

\[
|L_{m,n}^E-L_{m,n}^0|\ll m^{-2}
\]

and the reference decay

\[
e^{-\operatorname{Re}s L_{m,n}^0}
\ll (1+n-m)^{-4\operatorname{Re}s}
\]

give

\[
\sum_m\sum_{n>m}|F_{m,n}(s)|<\infty
\]

for `Re s>1/4` because

\[
\sum_m m^{-2}<\infty,
\qquad
\sum_{k\ge1}k^{-4\operatorname{Re}s}<\infty.
\]

Thus the PF-084 quarter boundary is reproduced exactly by the integer control as well.

---

## 7. What the quarter exponent is actually measuring

For a long channel in the integer control,

\[
(C_{ij}^0)^{-2s}
=4^{-2s}|i-j|^{-2s}.
\]

The row-square condition is therefore simply

\[
\sum_{m\ge1}m^{-4\operatorname{Re}s}<\infty.
\]

The threshold

\[
\operatorname{Re}s=\frac14
\]

is the one-dimensional power-law threshold produced by squaring a propagation amplitude of order `distance^(-2s)`.

The prime case replaces the regular lattice by

\[
p_n\sim n\log n
\]

and introduces the harmonic-mean gap weights

\[
H_n
=\frac{g_{n-1}g_n}{2(g_{n-1}+g_n)},
\]

but those slowly varying factors do not change the critical power. At the endpoint they turn the elementary harmonic divergence into a prime/gap-weighted harmonic divergence, but the exponent itself was already present before any arithmetic information was inserted.

This also explains why PF-084 and PF-087 independently found the same number: both are long-range propagation on an ordered one-dimensional tail.

---

## 8. Consequence for the research program

The following interpretation is ruled out:

```text
prime gaps
  -> exact/reference quarter-plane
  -> a prime-specific spectral exponent 1/4.
```

The correct interpretation is

```text
one-dimensional flute ordering
  -> long-channel power law
  -> universal quarter threshold,

prime gaps
  -> coefficients / fluctuations / subleading structure inside that regime.
```

So PF-084/PF-086/PF-087 remain mathematically natural constructions, but **their `1/4` boundary itself is not evidence of arithmetic spectral structure**.

Any prime-specific candidate based on these operators must now survive subtraction of the integer (or another featureless regularly spaced) control. Promising quantities would have to involve, for example,

- the relative determinant after dividing by the control determinant;
- subleading singular behavior at `1/4` that depends on the `H_n` fluctuations;
- non-direct scattering terms whose behavior differs genuinely from the regular lattice;
- multiscale Feshbach coefficients tied to nontrivial prime-gap ratios rather than the ambient one-dimensional channel count.

Merely recovering `1/4` again is no longer a substantive positive signal.

---

## 9. Literature / novelty audit

No new general theorem about Schatten classes is claimed here. Polynomial-decay kernels, discrete Riesz-type operators, and Schatten thresholds for structured infinite matrices are standard operator-theoretic phenomena. Recent work continues to characterize Schatten membership for concrete infinite matrix classes; for example Bellavita--Dellepiane--Stylogiannis, *Boundedness, compactness and Schatten class for Rhaly matrices*, J. London Math. Soc. 112 (2025), e70304, treats this general kind of ideal-class transition for another structured matrix family. Discrete Riesz potentials on `Z^n` are likewise a standard power-law propagation model.

The project-specific content is the **control experiment** above: the exact same `V(x)=pi cot(pi/x)` orthogonal-circle deformation and the same canonical scattering/Ruelle constructions reproduce the PF-084/PF-087 `1/4` transition on the completely non-prime sequence `n`.

That is a decisive novelty correction rather than a claim that the p-series argument itself is new.

---

## 10. Audit boundary

The conclusions above concern exactly the two sectors already isolated in PF-084 and PF-087:

1. the all-consecutive-block relative Ruelle sector;
2. the identity-double-coset/direct relative cusp-scattering kernel.

They do **not** rule out a prime-specific effect in the full non-direct scattering operator, in a genuine relative Laplacian determinant, or in the multiscale low-energy Feshbach corrections of PF-080/PF-081.

Rather, they sharpen the gate:

\[
\boxed{
\text{future candidates must beat the integer-control flute.}
}
\]
