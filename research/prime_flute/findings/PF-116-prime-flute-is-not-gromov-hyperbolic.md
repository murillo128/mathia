# PF-116 — the exact prime flute is not Gromov hyperbolic

**Status:** `LITERATURE+DERIVED + DECISIVE-NEGATIVE/BOUNDARY`. Portilla--Rodríguez--Tourís' train criterion and Baker--Harman--Pintz's short-interval bound are classical inputs. The project-specific result is that the exact zero-twist prime flute fails the Gromov-hyperbolicity criterion. By PF-115, the exact all-composite shift clone `p_n -> p_n+1` fails it as well. This closes the coarse Gromov-hyperbolicity/boundary route; it does not decide compact relative resolvent, quasiconformal equivalence, wave/scattering equivalence, or finer Laplace invariants.

## Claim

Let `X` be the exact zero-twist prime flute with endpoints

\[
u_n=\cot\frac{\pi}{p_n},
\]

and distinguished cuff lengths `ell_n`. Put

\[
l_n:=\frac{\ell_n}{2},
\qquad
h_n:=\log\frac{u_n}{u_{n-1}}.
\]

Then

\[
\boxed{X\text{ is not Gromov hyperbolic}.}
\tag{1}
\]

Moreover, if `X^+` is the exact all-composite shift clone of PF-106, obtained from `p_n+1` and normalized by the hyperbolic translation `z -> z-1`, then

\[
\boxed{X^+\text{ is not Gromov hyperbolic}.}
\tag{2}
\]

The second statement is an immediate consequence of PF-115 once (1) is proved: the prime flute and the shift clone have the same Gromov-hyperbolicity class under the bounded-perturbation theorem for flute/train length data.

## 1. The train coordinate is the half-cuff length

For a flute in the sense of Portilla--Rodríguez--Tourís, the second fundamental geodesics are punctures, so their train coordinates satisfy

\[
r_n=0.
\]

The fundamental geodesics are the successive separating cuffs. Thus, up to the harmless finite indexing convention at the first pant,

\[
2l_n=\ell_n.
\]

PF-001 gives the exact prime-flute identity

\[
\boxed{
e^{-l_n}=\tanh\frac{h_n}{4}.}
\tag{3}
\]

This is the only special hyperbolic identity needed below.

## 2. An unconditional logarithmic lower envelope for `l_n`

Write

\[
F(x)=\log\cot\frac{\pi}{x}.
\]

Then

\[
F'(x)=\frac{2\pi}{x^2\sin(2\pi/x)}\asymp\frac1x
\qquad (x\to\infty).
\tag{4}
\]

Let

\[
g_{n-1}=p_n-p_{n-1}.
\]

Baker--Harman--Pintz give unconditionally

\[
g_{n-1}\ll p_{n-1}^{0.525}.
\tag{5}
\]

In particular `g_{n-1}=o(p_{n-1})`, hence `p_n/p_{n-1}->1`. By the mean-value theorem and (4)--(5),

\[
h_n
=F(p_n)-F(p_{n-1})
\ll \frac{g_{n-1}}{p_{n-1}}
\ll p_n^{-0.475}.
\tag{6}
\]

Since `tanh y <= y` for `y>0`, (3) gives

\[
e^{-l_n}\le\frac{h_n}{4}\ll p_n^{-0.475},
\]

and therefore

\[
\boxed{
l_n\ge0.475\log p_n-O(1).}
\tag{7}
\]

For the later case split it is convenient to weaken this to the uniform tail bound

\[
\boxed{
l_n\ge\frac25\log p_n}
\tag{8}
\]

for all sufficiently large `n`.

No conjectural prime-gap input is used.

## 3. The inverse-length weights have an exact cumulative lower bound

Because (6) implies `h_n->0`, eventually `h_n/4<1/4`. On that interval the elementary inequality

\[
\tanh y\ge\frac y2
\]

holds, so from (3)

\[
e^{-l_n}\ge\frac{h_n}{8}
\tag{9}
\]

on a fixed tail.

The logarithmic mesh telescopes exactly. Hence for sufficiently large `r<s`,

\[
\begin{aligned}
\sum_{k=r+1}^{s}e^{-l_k}
&\ge\frac18\sum_{k=r+1}^{s}h_k\\
&=\frac18\log\frac{u_s}{u_r}.
\end{aligned}
\tag{10}
\]

Since

\[
u_j=\cot\frac{\pi}{p_j}\asymp p_j,
\]

there are absolute tail constants `c_0>0,C_0` such that

\[
\boxed{
\sum_{k=r+1}^{s}e^{-l_k}
\ge
c_0\left(\log\frac{p_s}{p_r}-C_0\right).
}
\tag{11}
\]

The important feature is that (11) is a **finite-interval** lower bound. It is stronger for the present purpose than merely knowing the global divergence `sum e^{-l_n}=infinity` from PF-012.

## 4. Portilla--Rodríguez--Tourís' criterion diverges

For trains with bounded second-fundamental data `r_n`, Theorem 3.12 of Portilla--Rodríguez--Tourís characterizes Gromov hyperbolicity by finiteness of

\[
K^0
=
\sup_n\sup_{h\in[0,l_n]}
\min_m \Gamma^0_{nm}(h).
\tag{12}
\]

Their Proposition 3.13 allows the minimum to be taken over all `m>=1`. For a flute `r_n=0`, the relevant pieces of their simplified function are

\[
\Gamma^0_{nm}(h)=
\begin{cases}
e^h\displaystyle\sum_{k=m+1}^{n}e^{-l_k},
& m<n,\ l_m\le h,\\[2mm]
l_m-h+e^h\displaystyle\sum_{k=m}^{n}e^{-l_k},
& m<n,\ l_m>h,\\[2mm]
\min(h,l_n-h),&m=n,\\[2mm]
l_m-h+e^h\displaystyle\sum_{k=n}^{m}e^{-l_k},
&m>n,\ l_m>h.
\end{cases}
\tag{13}
\]

(The remaining `m>n,l_m<=h` branch is not needed below.)

Choose the admissible test height

\[
H_n:=\frac1{10}\log p_n.
\tag{14}
\]

By (8), for all sufficiently large `n`,

\[
0<H_n<l_n.
\]

We now lower-bound (13) uniformly in `m`.

### Case A: `m=n`

Using (8),

\[
\Gamma^0_{nn}(H_n)
=\min(H_n,l_n-H_n)
\ge\frac1{10}\log p_n.
\tag{15}
\]

### Case B: `m>n`

For every sufficiently large `n`, all `m>n` lie in the tail of (8), and

\[
l_m\ge\frac25\log p_m
\ge\frac25\log p_n
>H_n.
\]

Therefore the fourth branch of (13) applies and

\[
\Gamma^0_{nm}(H_n)
\ge l_m-H_n
\ge\frac3{10}\log p_n.
\tag{16}
\]

### Case C: `m<n` and `p_m>=p_n^{1/2}`

For large `n`, such `m` is itself in the tail of (8). Then

\[
l_m-H_n
\ge
\frac25\log p_m-rac1{10}\log p_n
\ge\frac1{10}\log p_n.
\tag{17}
\]

In particular `l_m>H_n`, so the second branch of (13) applies and

\[
\Gamma^0_{nm}(H_n)
\ge\frac1{10}\log p_n.
\tag{18}
\]

### Case D: `m<n` and `p_m<p_n^{1/2}`

Whichever of the first two `m<n` branches of (13) applies, the expression contains at least

\[
e^{H_n}\sum_{k=m+1}^{n}e^{-l_k}.
\tag{19}
\]

If `m` is beyond the fixed threshold of (11), then

\[
\sum_{k=m+1}^{n}e^{-l_k}
\ge c_0\left(\frac12\log p_n-C_0\right).
\tag{20}
\]

If `m` lies in the finite pre-threshold prefix, simply discard that finite prefix and apply (11) from the fixed threshold onward; the same lower bound with changed constants follows. Since `e^{H_n}=p_n^{1/10}`,

\[
\Gamma^0_{nm}(H_n)
\gg p_n^{1/10}\log p_n.
\tag{21}
\]

Combining (15), (16), (18), and (21), there is a constant `c>0` such that

\[
\boxed{
\min_{m\ge1}\Gamma^0_{nm}(H_n)
\ge c\log p_n
\longrightarrow\infty.
}
\tag{22}
\]

Therefore `K^0=infinity`. Theorem 3.12 now gives (1).

## 5. The all-composite shift clone is non-hyperbolic too

PF-115 proves, using Theorem 3.8 of the same paper and PF-107's bounded cuff perturbation, that

\[
X\text{ is Gromov hyperbolic}
\iff
X^+\text{ is Gromov hyperbolic}.
\tag{23}
\]

Combining (1) and (23) proves (2).

This makes the clone control stronger than a mere equality of an unspecified binary class: the common class is now known explicitly.

## 6. Consequence for the RH search

The prime flute is a complete hyperbolic surface of curvature `-1`, but its intrinsic metric space is not Gromov hyperbolic. Thus a route of the form

\[
\text{prime gaps}
\longrightarrow
\text{coarse Gromov-hyperbolicity / Gromov-boundary structure}
\longrightarrow
\text{RH-specific spectral mechanism}
\]

fails already at the first coarse gate. The exact all-composite shift clone has the same negative answer.

The mechanism behind (1) is also not a delicate prime-gap fluctuation. It uses only an unconditional sublinear upper bound on every sufficiently large consecutive gap together with the exact telescoping of the logarithmic endpoint mesh. The obstruction is therefore a large-scale geometric feature of this zero-twist construction, not evidence that primality selects a special coarse boundary class.

This does **not** resolve the accepted relative-operator clue. Non-Gromov-hyperbolicity neither proves nor disproves a strong common-manifold metric comparison, compactness of a relative resolvent, equality of essential spectra, wave/scattering equivalence, Schatten membership, or any finer nonlocal Laplace invariant. Those questions remain strictly finer than the coarse binary invariant closed here.

## 7. Prior art and novelty audit

The imported ingredients are established literature:

- A. Portilla, J. M. Rodríguez, E. Tourís, *A real variable characterization of Gromov hyperbolicity of flute surfaces*, Osaka Journal of Mathematics **48** (2011), 179--207, DOI `10.18910/9158`, arXiv:0806.0093. Theorem 3.12 and Proposition 3.13 supply the `K^0/Gamma^0` criterion used in (12)--(13); Theorem 3.8 is the bounded-perturbation stability already used in PF-115.
- R. C. Baker, G. Harman, J. Pintz, *The Difference Between Consecutive Primes, II*, Proceedings of the London Mathematical Society **83** (2001), 532--562, DOI `10.1112/S0024611501012690`. Only the unconditional exponent `0.525` is used.
- PF-001 supplies the exact cuff coordinate (3), and PF-115 supplies the shift-clone corollary.

No novelty is claimed for the train criterion, the short-interval theorem, elementary `tanh` inequalities, or logarithmic telescoping. Directed searches for `prime flute`, `cot(pi/p)` flute surfaces, prime gaps together with Gromov hyperbolicity, and the exact endpoint construction located no published statement deciding this prime-specific surface's Gromov-hyperbolicity class.

The durable Mathia contribution is the project-specific bridge

\[
\boxed{
\text{exact cotangent cuff law}
+
\text{BHP sublinear gap envelope}
+
\text{Portilla--Rodríguez--Tourís train criterion}
\Longrightarrow
\text{the exact prime flute is not Gromov hyperbolic}.}
\]

This is a negative/boundary result for the prime-flute program, not a new theorem about arbitrary flute surfaces and not evidence for RH.

## 8. Audit / falsification core

The proof can be challenged at a small number of explicit gates:

1. verify the identification `l_n=ell_n/2`, `r_n=0` with the flute/train coordinates of Portilla--Rodríguez--Tourís;
2. verify PF-001's exact identity `e^{-l_n}=tanh(h_n/4)`;
3. combine `F'(x)asymp1/x` with the BHP exponent to obtain the tail lower envelope (8);
4. verify the elementary tail bound `tanh(h_n/4)>=h_n/8` and the exact telescoping identity leading to (11);
5. read Theorem 3.12 and Proposition 3.13 with the simplified `Gamma^0` branches in (13);
6. check the four-case lower bound (15)--(21) at the admissible height `H_n=(1/10)log p_n`;
7. conclude `K^0=infinity`, hence non-Gromov-hyperbolicity;
8. use PF-115 only after (1) to transfer the class to the all-composite shift clone.

A refutation would need to break one of these gates. Neither parabolicity from PF-012 nor zero systole from PF-005 is used as a substitute for the Portilla criterion, so no invalid implication between conformal type, systole, and Gromov hyperbolicity is assumed.