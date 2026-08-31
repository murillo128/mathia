# WP-068 — full-root Hardy differences make the Mangoldt anchor functional unbounded

**Status:** `EXACT-DERIVED` + `DECISIVE-NEGATIVE` for the finite-scalar renormalization branch left open by WP-067. The cumulative-shell identity comes from PC-079, the anchor trace from PC-080/WP-067, and the norm estimate below is derived directly from the exact Hardy coefficients. No theorem-level historical novelty is claimed for the classical Hardy/local-Dirichlet identities used in the derivation.

WP-067 reduced every finite scalar repair of the canonical base-shell square to one exact functional-analytic question: is

\[
L(B)=\operatorname{Tr}(HB)
\]

bounded on the shell span under

\[
Q_H(B)=\operatorname{Tr}(B^*HB)?
\]

It is not. The canonical **full-root cumulative shells** supplied by PC-079 already give an explicit null sequence for the `Q_H` norm on which `L` stays nonzero.

For every integer `N>=2`, define

\[
\boxed{
B_N:=\sum_{\substack{d\mid N\\d>1}}\Gamma_d.
}
\]

Then

\[
\boxed{
L(B_N)=\log N
}
\]

while

\[
\boxed{
Q_H(B_N)=O(\log N).
}
\]

Consequently

\[
X_N:=\frac{B_N}{\log N}
\]

satisfies

\[
\boxed{
Q_H(X_N)\longrightarrow0,
\qquad
L(X_N)=1.
}
\]

Thus `L` is unbounded already on the algebraic shell span. In the notation of WP-067, for every finite real constant `c`,

\[
\boxed{
\inf_B\left(Q_H(B)-2\operatorname{Re}L(B)+c\right)=-\infty.
}
\]

The conditional Riesz branch in WP-067 therefore resolves on the **unbounded** side: subtracting the divergent anchor self-energy and then choosing any finite scalar counterterm cannot restore positivity.

## 1. PC-079 forces the cumulative full-root test sequence

Let

\[
H_{jk}=\frac1{j+k+1},
\qquad
\Gamma_1=-H.
\]

PC-079 proves the exact divisor-shell identity

\[
\sum_{d\mid N}\Gamma_d
=\mathfrak D_N\Gamma_1,
\]

where `\mathfrak D_N` is the canonical Hankel coefficient dilation. Therefore

\[
B_N
=\mathfrak D_N\Gamma_1-\Gamma_1.
\]

Writing `m=j+k+1`, its entries are

\[
\boxed{
(B_N)_{jk}
=b_N(m),
\qquad
b_N(m)=\frac{1-N\mathbf1_{N\mid m}}{m}.
}
\]

The analytic generating function of this Hankel sequence is consequently

\[
\begin{aligned}
F_N(z)
&:=\sum_{m\ge1}b_N(m)z^m\\
&=\log(1-z^N)-\log(1-z)\\
&=\boxed{\log\frac{1-z^N}{1-z}}.
\end{aligned}
\]

Put

\[
g(z):=-\log(1-z).
\]

Then the cancellation at the common anchor is especially transparent:

\[
\boxed{F_N(z)=g(z)-g(z^N).}
\]

The same cumulative-shell identity gives the anchor functional exactly. PC-080 gives

\[
L(\Gamma_d)=\operatorname{Tr}(H\Gamma_d)=\Lambda(d),
\qquad d>1,
\]

hence the classical divisor identity `\sum_{d\mid N}\Lambda(d)=\log N` yields

\[
\boxed{
L(B_N)
=\sum_{\substack{d\mid N\\d>1}}\Lambda(d)
=\log N.
}
\]

No primality assumption is being used: the obstruction is present along every integer full-root refinement level.

## 2. The `H`-Gram norm is an integrated local Dirichlet norm

Let

\[
C:\ell^2(\mathbb Z_{\ge0})\to L^2(0,1),
\qquad
Ce_j(t)=t^j.
\]

Then `C^*C=H`. Since `B_N` is self-adjoint,

\[
Q_H(B_N)
=\operatorname{Tr}(B_NHB_N)
=\|CB_N\|_{\mathcal S_2}^2.
\]

For fixed `t in (0,1)`, the `k`-th column of `CB_N` is

\[
\sum_{j\ge0}b_N(j+k+1)t^j.
\]

On the other hand,

\[
\frac{F_N(z)-F_N(t)}{z-t}
=\sum_{k\ge0}
\left(
\sum_{j\ge0}b_N(j+k+1)t^j
\right)z^k.
\]

Therefore, with the standard Hardy norm on the unit circle,

\[
\boxed{
Q_H(B_N)
=\int_0^1 D_t(F_N)\,dt,
}
\]

where

\[
\boxed{
D_t(F)
:=
\left\|
\frac{F(z)-F(t)}{z-t}
\right\|_{H^2}^2.
}
\]

This is the usual local-Dirichlet difference quotient, but no external theorem is needed here: the equality follows coefficient by coefficient from the Gram realization of the Hilbert matrix.

For real `0<=t<1`, let `P_t` denote the Poisson kernel at `t`. Since

\[
\frac1{|e^{i\theta}-t|^2}
=\frac{P_t(\theta)}{1-t^2},
\]

and the Poisson integral reproduces analytic Hardy functions,

\[
\boxed{
D_t(F)
=
\frac{P_t(|F|^2)-|F(t)|^2}{1-t^2}.
}
\]

Thus the problem is to control the Poisson variance of the exact cyclotomic logarithm `F_N`.

## 3. The bulk Poisson variance is uniformly bounded in `N`

The base logarithm

\[
g(z)=\sum_{m\ge1}\frac{z^m}{m}
\]

has an elementary exact Poisson variance. The nonnegative Fourier coefficients of its boundary square are

\[
\sum_{n\ge1}\frac1{n(n+k)}
=\frac{H_k}{k},
\qquad k\ge1.
\]

Hence

\[
P_t(|g|^2)
=\zeta(2)
+2\sum_{k\ge1}\frac{H_k}{k}t^k.
\]

Using the directly differentiated generating identity

\[
\sum_{k\ge1}\frac{H_k}{k}t^k
=\operatorname{Li}_2(t)
+\frac12\log^2(1-t),
\]

while `g(t)^2=\log^2(1-t)`, gives

\[
\boxed{
V_g(t)
:=P_t(|g|^2)-|g(t)|^2
=\zeta(2)+2\operatorname{Li}_2(t).
}
\]

For `0<=t<1`,

\[
0\le\operatorname{Li}_2(t)\le\zeta(2),
\]

so

\[
\boxed{V_g(t)\le3\zeta(2)=\frac{\pi^2}{2}.}
\]

Now put `g_N(z)=g(z^N)`. Its boundary Fourier modes are exactly the modes of `g` dilated by `N`, so Poisson weighting by `t^{|k|}` gives

\[
\boxed{
P_t(|g_N|^2)-|g_N(t)|^2
=V_g(t^N).
}
\]

Since `F_N=g-g_N`, the elementary variance inequality

\[
|u-v|^2\le2|u|^2+2|v|^2
\]

applied after subtracting the respective Poisson means yields

\[
\boxed{
P_t(|F_N|^2)-|F_N(t)|^2
\le
2V_g(t)+2V_g(t^N)
\le2\pi^2.
}
\]

Therefore

\[
D_t(F_N)
\le\frac{2\pi^2}{1-t^2}.
\]

On the bulk interval `0<=t<=1-1/N`,

\[
\begin{aligned}
\int_0^{1-1/N}D_t(F_N)\,dt
&\le
2\pi^2
\int_0^{1-1/N}\frac{dt}{1-t^2}\\
&=
\pi^2\log(2N-1)\\
&\le\boxed{\pi^2\log(2N)}.
\end{aligned}
\]

Thus all possible growth beyond logarithmic order is confined to a radial boundary layer of width `1/N` around the cancelled anchor.

## 4. The boundary layer contributes only `O(1)`

The cancellation in `F_N` gives a finite boundary value

\[
F_N(1)=\log N.
\]

Let

\[
s_j
:=
\sum_{m\ge j+1}b_N(m).
\]

Taking harmonic partial sums and using

\[
H_M-H_{\lfloor M/N\rfloor}\longrightarrow\log N
\]

gives the exact formula

\[
\boxed{
s_j=\log N+H_{\lfloor j/N\rfloor}-H_j.}
\]

The boundary local-Dirichlet norm is therefore

\[
\boxed{
D_1(F_N)
:=
\left\|
\frac{F_N(z)-F_N(1)}{z-1}
\right\|_{H^2}^2
=
\sum_{j\ge0}s_j^2.
}
\]

This is `O(N)`. Indeed, for `0<=j<N`,

\[
s_j=\log N-H_j,
\]

and

\[
\sum_{j=0}^{N-1}(\log N-H_j)^2=O(N)
\]

by comparison with `\sum_{j=1}^N\log^2(N/j)=O(N)`. For `j=qN+r` with `q>=1` and `0<=r<N`, the standard elementary estimate

\[
H_m=\log m+\gamma+O(m^{-1})
\]

gives, uniformly in `r`,

\[
\begin{aligned}
s_{qN+r}
&=\log N+H_q-H_{qN+r}\\
&=\log\frac{qN}{qN+r}+O(q^{-1})\\
&=O(q^{-1}).
\end{aligned}
\]

Hence

\[
\sum_{q\ge1}\sum_{r=0}^{N-1}s_{qN+r}^2
\ll
N\sum_{q\ge1}\frac1{q^2}
=O(N).
\]

So

\[
\boxed{D_1(F_N)=O(N).}
\]

It remains to transfer this endpoint bound uniformly to the thin radial layer. Put

\[
a_j=b_N(j+1),
\qquad
s=(s_j)_{j\ge0},
\]

and let `S^*` be the backward shift on `\ell^2`. Since

\[
a_j=s_j-s_{j+1},
\]

we have

\[
a=(I-S^*)s.
\]

The coefficient vector of the divided difference at `t` is

\[
(I-tS^*)^{-1}a.
\]

Using

\[
I-S^*
=(I-tS^*)-(1-t)S^*,
\]

we obtain

\[
(I-tS^*)^{-1}a
=s-(1-t)(I-tS^*)^{-1}S^*s.
\]

Because

\[
\|(I-tS^*)^{-1}\|\le\frac1{1-t},
\]

it follows that

\[
\boxed{
D_t(F_N)\le4\|s\|_2^2
=4D_1(F_N)
=O(N)
}
\]

for every `0<=t<1`. Therefore the final interval has bounded total contribution:

\[
\boxed{
\int_{1-1/N}^1D_t(F_N)\,dt
=O(1).
}
\]

Combining the bulk and boundary-layer estimates proves

\[
\boxed{Q_H(B_N)=O(\log N).}
\]

## 5. The WP-067 Riesz functional is unbounded

We have simultaneously

\[
L(B_N)=\log N
\]

and

\[
Q_H(B_N)\le C(1+\log N)
\]

for an absolute constant `C`. Consequently

\[
\frac{|L(B_N)|^2}{Q_H(B_N)}
\ge
\frac{(\log N)^2}{C(1+\log N)}
\longrightarrow\infty.
\]

Equivalently, with

\[
X_N=\frac{B_N}{\log N},
\]

we have

\[
Q_H(X_N)\longrightarrow0,
\qquad
L(X_N)=1.
\]

Thus `L` is not continuous for the `Q_H` norm and has no Riesz representer in the shell Hilbert-space completion considered in WP-067.

The finite-renormalization consequence is stronger than mere failure of positivity. For

\[
R_c(B)=Q_H(B)-2\operatorname{Re}L(B)+c,
\]

restrict to real multiples `B=lambda B_N`. Since `Q_H(B_N)>0`, optimizing over `lambda` gives

\[
\inf_{\lambda\in\mathbb R}R_c(\lambda B_N)
=
 c-\frac{(\log N)^2}{Q_H(B_N)}.
\]

The right-hand side tends to `-infinity`. Hence for every finite `c`,

\[
\boxed{
\inf_{B\in\mathcal A_0}R_c(B)=-\infty.
}
\]

This settles the exact alternative left open by WP-067.

## 6. Adversarial controls and boundaries

The argument survives the most obvious ways of weakening the claim.

1. **No prime-only tuning.** The test sequence works for every integer `N>=2`; it is the canonical cumulative full-root shell forced by PC-079. The divergence of the Riesz ratio is therefore not a hidden use of prime sparsity.
2. **No zero data or analytic continuation.** Every identity is inside the unit disk or on the positive radial interval. No zeta zero, RH hypothesis, completed zeta function, or continuation across a singular line enters.
3. **No arbitrary regularization.** `B_N` is an exact finite linear combination of existing shell operators, and `Q_H` and `L` are exactly the positive Gram form and anchor functional fixed in WP-067.
4. **The anchor cancellation is essential and checked exactly.** `F_N(1)=log N` while the two logarithmic singularities in `g(z)-g(z^N)` cancel at `z=1`. The endpoint tail formula `s_j=log N+H_floor(j/N)-H_j` is an independent coefficient-level audit of that cancellation.
5. **The estimate is stronger than a numerical asymptotic.** Only the upper bound `Q_H(B_N)=O(log N)` is needed; no conjectured constant or fitted asymptotic is used.

The result does **not** rule out a renormalization that changes the geometry before taking the limit: a non-scalar finite/archimedean coupling, a quotient or compression with an independent sign theorem, a different closed form/domain, or another genuinely global construction remains outside this theorem. What is ruled out is the entire branch

\[
\boxed{
\text{same }H\text{-Gram square}
\;-
\text{divergent scalar anchor energy}
\;+
\text{finite scalar counterterm}
\to
\text{positive global form}.
}
\]

## 7. Prior-art and novelty audit

The arithmetic/operator inputs are already canonical inside Mathia.

- PC-079 supplies the exact cumulative full-root identity and coefficient-dilation calculus.
- PC-080 supplies `Tr(H Gamma_n)=Lambda(n)` through the base-shell mixed Hardy trace.
- WP-067 is the immediate parent result: it identifies boundedness of `L` in the `Q_H` geometry as the only remaining finite-scalar repair condition.

The divided-difference quantity `D_t(F)` belongs to the classical local Dirichlet/Hardy framework, and the surrounding BMOA/local-Douglas theory provides much more general norm characterizations. Directed searches for local Dirichlet integrals of logarithmic/cyclotomic functions, BMOA logarithmic symbols, and cyclotomic Hankel products found that classical neighboring theory but no reason to treat the elementary identities above as a new abstract Hardy-space theorem. The proof here therefore keeps the needed specialization explicit: the decisive ingredient is the exact Mathia sequence

\[
F_N(z)=\log\frac{1-z^N}{1-z}
\]

and its interaction with the WP-067 `H`-Gram norm, not a novelty claim for local Dirichlet spaces.

## Research consequence

WP-067 no longer ends in a conditional dichotomy. The canonical shell functional carrying the Mangoldt anchor data is **provably unbounded** in the positive base-shell Gram geometry:

\[
\boxed{
B_N\xrightarrow[Q_H]{}0
\quad\text{after division by }\log N,
\qquad
L\left(\frac{B_N}{\log N}\right)=1.
}
\]

Therefore no finite scalar choice can complete the canonical zero-finite-part subtraction into a positive form. Any surviving Weil-positivity route must change something structural before the sign theorem is applied — for example the domain/quotient, the finite–archimedean coupling, or the positive geometry itself — rather than retain the same `H`-Gram square and repair it by a scalar normalization.