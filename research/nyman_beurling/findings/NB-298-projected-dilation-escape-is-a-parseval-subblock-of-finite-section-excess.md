# NB-298 — projected dilation escape is a Parseval subblock of finite-section excess

- **Date:** 2026-09-23
- **Status:** proved
- **Research line:** `nyman_beurling`
- **Depends on:** NB-284, NB-285, NB-287, NB-297
- **Classification:** `EXACT-DERIVED + CLOSED-QUOTIENT-SOURCE + FIRST-FREE-SAMPLING + PROJECTED-DILATION-ESCAPE + REPRESENTer-TAIL-OCCUPATION + NULLSPACE-PARSEVAL-SUBBLOCK + PRINCIPAL-ANGLE-CANCELLATION + FIXED-PACKET-UNIFORM-NO-GO + MOVING-PACKET-ROUTE-NARROWING + PRIOR-ART-AUDITED`

## Claim

`NB-297` isolates a canonical positive block

\[
\Xi_{m,n,Z}=L_ZP_{R_{m,n,Z}}L_Z^*
\preceq
K_{mn-1,Z}-K_{n-1,Z},
\]

inside the **ordinary** finite-section enrichment, where

\[
R_{m,n,Z}
=
(V_{n-1,Z}+S_mV_{n-1,Z})\ominus V_{n-1,Z}.
\]

That removes the transported-baseline artifact exposed by `NB-296`. The remaining question is whether the projected dilation escape can supply genuinely new coercivity beyond the finite-section obstruction already isolated in `NB-284`--`NB-287`.

It cannot do so for free. For a fixed zero packet, the `NB-297` block is exactly a subblock of the **pre-existing representer tail**, and the corresponding target gain is exactly a Parseval subblock of the **pre-existing finite-section excess**.

More precisely, work in the closed quotient-source space

\[
\mathcal H:=\mathcal H_Z^\infty
=
\overline{\bigcup_M V_{M,Z}},
\]

write

\[
U:=V_{n-1,Z},
\qquad
L:=L_Z:\mathcal H\to\mathbb C^N,
\qquad
K:=LP_UL^*,
\]

and assume `L|_U` is onto. Let

\[
\mathcal T:=\mathcal H\ominus U
\]

be the full future source tail and

\[
E:=K_\infty-K
=L P_{\mathcal T}L^*,
\qquad
K_\infty:=LL^*.
\]

For every integer `m>=2`, the projected dilation escape

\[
R:=R_{m,n,Z}
=(U+S_mU)\ominus U
\]

satisfies

\[
R\subseteq\mathcal T.
\]

Hence

\[
\boxed{
E=\Xi+\Omega,
\qquad
\Xi:=LP_RL^*,
\qquad
\Omega:=LP_{\mathcal T\ominus R}L^*\succeq0,
}
\tag{1}
\]

and therefore

\[
\boxed{0\preceq\Xi\preceq E.}
\tag{2}
\]

Thus the entire baseline-free dilation block of `NB-297` already lives inside the representer tail `E` from `NB-285`.

There is an equally exact target-side statement. Let

\[
D_U:=U\cap\ker L,
\qquad
R_U:=P_UL^*K^{-1},
\]

so that `R_U` is the minimum-norm right inverse of `L|_U`. Define the **neutralized dilation escape**

\[
\boxed{
\mathcal N_R
:=
(I-R_UL)R.
}
\tag{3}
\]

Then

\[
\boxed{
(U+R)\cap\ker L
=
D_U\oplus\mathcal N_R,
}
\tag{4}
\]

orthogonally. If

\[
h_U:=R_Uy
\]

is the minimum-norm old-section interpolant for first-free datum `y`, then

\[
\boxed{
\mathcal C_U(y)-\mathcal C_{U+R}(y)
=
\|P_{\mathcal N_R}h_U\|^2
=
y^*\bigl[K^{-1}-(K+\Xi)^{-1}\bigr]y.
}
\tag{5}
\]

On the other hand, with

\[
D_\infty:=\mathcal H\cap\ker L,
\]

`NB-284`--`NB-287` give

\[
\boxed{
\mathfrak A_U(y)
:=
\mathcal C_U(y)-\mathcal C_\infty(y)
=
\|P_{D_\infty\ominus D_U}h_U\|^2.
}
\tag{6}
\]

Since

\[
\mathcal N_R\subseteq D_\infty\ominus D_U,
\]

the full excess splits orthogonally as

\[
\boxed{
\mathfrak A_U(y)
=
\bigl[\mathcal C_U(y)-\mathcal C_{U+R}(y)\bigr]
+
\left\|
P_{(D_\infty\ominus D_U)\ominus\mathcal N_R}h_U
\right\|^2.
}
\tag{7}
\]

So the projected dilation mechanism does not create a second source of finite-section coercivity. It selects a concrete finite-dimensional Parseval block from the nullspace tail already responsible for `A_U`.

A second consequence sharpens the role of the principal-angle matrix `Q` in `NB-297`. If

\[
F:=(I-P_U)S_mE_U,
\qquad
Q:=F^*F,
\qquad
Y:=LF,
\]

where `E_U:C^d->U` is any isometric synthesis map, then `NB-297` gives

\[
\Xi=YQ^+Y^*.
\]

But the polar decomposition of `F` gives

\[
F=JQ^{1/2},
\]

with `J` a partial isometry onto `R`, so

\[
\boxed{
YQ^+Y^*
=
LJJ^*L^*
=
LP_RL^*.
}
\tag{8}
\]

Consequently the **nonzero magnitudes** of the principal-angle defect eigenvalues in `Q` cancel after normalization. Their support controls how many escape directions survive, but quantitative sample mass is determined by the orientation of the normalized escape subspace `R` under `L`, not by the size of the nonzero eigenvalues of `Q` themselves.

For a fixed zero packet this produces a uniform no-go in the dilation parameter. Since `NB-284`--`NB-285` imply

\[
\|E_{n-1,Z}\|\longrightarrow0
\]

as `n->infinity`, `(2)` yields

\[
\boxed{
\sup_{m\ge2}
\|\Xi_{m,n,Z}\|
\le
\|E_{n-1,Z}\|
\longrightarrow0.
}
\tag{9}
\]

Likewise, for every fixed datum `y`, `(7)` gives

\[
\boxed{
0\le
\sup_{m\ge2}
\bigl[
\mathcal C_{n-1,Z}(y)
-
\mathcal C_{V_{n-1,Z}+S_mV_{n-1,Z}}(y)
\bigr]
\le
\mathfrak A_{n-1,Z}(y)
\longrightarrow0.
}
\tag{10}
\]

Thus increasing the multiplicative dilation cannot rescue a fixed-packet lower bound after the ordinary section is sufficiently deep, even though the source escape rank from `NB-297` can remain macroscopically large. Any surviving Ford-scale statement must be a **moving-packet occupation theorem**: the normalized projected dilation block must capture a non-negligible part of a representer/null tail that itself fails to vanish uniformly.

---

## 1. The projected dilation escape lies inside the full future tail

Fix the packet `Z` and suppress it from the notation. The closed quotient-source space is

\[
\mathcal H
=
\overline{\bigcup_MV_M}.
\tag{11}
\]

Take

\[
U=V_{n-1},
\qquad
\mathcal T=\mathcal H\ominus U.
\tag{12}
\]

Because the canonical sections are nested and the Nyman dilation obeys

\[
S_mU\subseteq V_{mn-1}\subseteq\mathcal H,
\tag{13}
\]

one has

\[
U+S_mU\subseteq\mathcal H.
\tag{14}
\]

By definition,

\[
R=(U+S_mU)\ominus U.
\tag{15}
\]

Therefore

\[
R\subseteq\mathcal H\cap U^\perp=\mathcal T.
\tag{16}
\]

Since `R` is finite-dimensional and closed,

\[
\mathcal T
=
R\oplus(\mathcal T\ominus R).
\tag{17}
\]

Applying `L P_(.) L*` gives

\[
LP_\mathcal TL^*
=
LP_RL^*
+
LP_{\mathcal T\ominus R}L^*.
\tag{18}
\]

But

\[
LP_\mathcal TL^*
=
L(I-P_U)L^*
=
K_\infty-K,
\tag{19}
\]

so `(1)` follows.

This is stronger than the finite-section bound from `NB-297`,

\[
\Xi
\preceq
K_{mn-1}-K_{n-1},
\tag{20}
\]

because `(2)` compares `Xi` directly with the **entire future representer tail**, independently of `m`.

A convenient way to expose the remaining degree of freedom is to define, on the support of `E`,

\[
\boxed{
\Theta_R
:=
E^{+/2}\Xi E^{+/2}.
}
\tag{21}
\]

From `0<=Xi<=E`,

\[
0\preceq\Theta_R\preceq P_{\operatorname{ran}E},
\tag{22}
\]

and

\[
\boxed{
\Xi
=
E^{1/2}\Theta_RE^{1/2}.
}
\tag{23}
\]

Thus `E` measures the absolute amount of sample-visible future tail available, while `Theta_R` measures what fraction/orientation of that pre-existing tail is occupied by the projected dilation escape.

The live moving-packet problem is therefore not simply to make `R` large. It is to control `Theta_R` on the target-relevant part of `E` while `E` itself varies with the packet and cutoff.

---

## 2. Principal-angle magnitudes cancel from the normalized sample Gram

Retain the finite-dimensional synthesis notation of `NB-297`. Let

\[
E_U:\mathbb C^d\to U
\]

be an isometry onto `U` and put

\[
F=(I-P_U)S_mE_U.
\tag{24}
\]

Then

\[
\operatorname{ran}F=R,
\qquad
Q=F^*F,
\qquad
Y=LF.
\tag{25}
\]

The standard Moore--Penrose formula for the orthogonal projector onto `ran F` is

\[
P_R=F(F^*F)^+F^*=FQ^+F^*.
\tag{26}
\]

Hence

\[
LP_RL^*
=
LFQ^+F^*L^*
=
YQ^+Y^*.
\tag{27}
\]

To see what `Q` is and is not contributing, write the polar decomposition

\[
F=JQ^{1/2},
\tag{28}
\]

where `J` is a partial isometry from `(ker Q)^perp` onto `R`. Then

\[
Y=LJQ^{1/2},
\tag{29}
\]

so

\[
YQ^+Y^*
=
LJ
Q^{1/2}Q^+Q^{1/2}
J^*L^*
=
LJ P_{(\ker Q)^\perp}J^*L^*.
\tag{30}
\]

Because `J` already has initial space `(ker Q)^perp`,

\[
J P_{(\ker Q)^\perp}J^*=JJ^*=P_R,
\tag{31}
\]

which proves `(8)`.

This gives a precise route restriction. Lower bounds on the **positive eigenvalues** of `Q` do not by themselves give lower bounds on `Xi`: after the escape vectors are normalized, those magnitudes cancel exactly. The kernel of `Q` still matters, because it fixes the escape rank, but beyond rank the missing information is the `L`-orientation of `R`.

So a theorem of the form "the dilation has many well-separated principal angles from the old section" is not yet a first-free sampling theorem. It must be coupled to a statement about how the corresponding normalized escape directions are seen by `L`.

---

## 3. Neutralizing the escape produces the exact new finite kernel

Let

\[
D_U:=U\cap\ker L.
\tag{32}
\]

Since `L|_U` is onto, its minimum-norm right inverse is

\[
R_U=P_UL^*K^{-1},
\qquad
K=LP_UL^*.
\tag{33}
\]

It satisfies

\[
LR_U=I_{\mathbb C^N},
\qquad
\operatorname{ran}R_U
=U\ominus D_U.
\tag{34}
\]

For `r in R`, define

\[
q_r:=r-R_ULr.
\tag{35}
\]

Then

\[
Lq_r=0,
\tag{36}
\]

and, because `r perp U` while `R_ULr in U\ominus D_U`,

\[
q_r\perp D_U.
\tag{37}
\]

The map

\[
r\mapsto q_r
\tag{38}
\]

is injective: if `q_r=0`, then `r=R_ULr in U`; but `r in R subset U^perp`, so `r=0`.

Define its range

\[
\mathcal N_R=(I-R_UL)R.
\tag{39}
\]

Then

\[
\mathcal N_R
\subseteq
(U+R)\cap\ker L,
\qquad
\mathcal N_R\perp D_U.
\tag{40}
\]

Conversely, take any

\[
q=u+r\in(U+R)\cap\ker L,
\qquad
u\in U,
\quad r\in R.
\tag{41}
\]

Since `Lu=-Lr`,

\[
d:=u+R_ULr
\tag{42}
\]

lies in `U` and satisfies `Ld=0`; hence `d in D_U`. Therefore

\[
q
=d+(r-R_ULr),
\tag{43}
\]

with the two summands orthogonal. This proves `(4)`.

In particular,

\[
\dim\mathcal N_R=\dim R.
\tag{44}
\]

The large source escape rank from `NB-297` therefore really does unlock the same number of new null directions after sample neutralization. What it does **not** determine is how much of the current minimum interpolant lies in those directions.

---

## 4. The ordinary gain is exactly the Parseval mass on that null block

For a datum `y`, let

\[
h_U:=R_Uy.
\tag{45}
\]

Then

\[
Lh_U=y,
\qquad
h_U\perp D_U,
\qquad
\|h_U\|^2=y^*K^{-1}y.
\tag{46}
\]

Because `h_U` is already feasible in `U+R`, every other feasible vector there is of the form

\[
h_U+d,
\qquad
d\in (U+R)\cap\ker L.
\tag{47}
\]

Using `(4)` and `h_U perp D_U`, the minimum-norm feasible vector in `U+R` is

\[
h_{U+R}
=
h_U-P_{\mathcal N_R}h_U.
\tag{48}
\]

Therefore Pythagoras gives

\[
\boxed{
\mathcal C_U(y)-\mathcal C_{U+R}(y)
=
\|P_{\mathcal N_R}h_U\|^2.
}
\tag{49}
\]

Since `U perp R`, the sampling Gram of `U+R` is

\[
K_{U+R}
=K+LP_RL^*
=K+\Xi.
\tag{50}
\]

Hence `(49)` is exactly equivalent to

\[
\boxed{
\|P_{\mathcal N_R}h_U\|^2
=
y^*\left[K^{-1}-(K+\Xi)^{-1}\right]y.
}
\tag{51}
\]

This is the full target-aware gain of the entire projected dilation block, not merely a one-direction Bessel certificate.

Now let

\[
D_\infty=\mathcal H\cap\ker L.
\tag{52}
\]

The infinite minimum-norm interpolant is

\[
h_\infty
=h_U-P_{D_\infty}h_U.
\tag{53}
\]

Because `D_U subset D_infty` and `h_U perp D_U`,

\[
P_{D_\infty}h_U
=
P_{D_\infty\ominus D_U}h_U.
\tag{54}
\]

Thus

\[
\mathfrak A_U(y)
=
\mathcal C_U(y)-\mathcal C_\infty(y)
=
\|P_{D_\infty\ominus D_U}h_U\|^2.
\tag{55}
\]

Moreover `(40)` implies

\[
\mathcal N_R
\subseteq D_\infty\ominus D_U.
\tag{56}
\]

Consequently

\[
D_\infty\ominus D_U
=
\mathcal N_R
\oplus
\left[(D_\infty\ominus D_U)\ominus\mathcal N_R\right],
\tag{57}
\]

and Parseval gives exactly `(7)`.

The matrix version follows at once from `(2)`. Since

\[
K+\Xi\preceq K+E=K_\infty,
\tag{58}
\]

matrix inversion reverses Loewner order:

\[
K^{-1}-(K+\Xi)^{-1}
\preceq
K^{-1}-K_\infty^{-1}.
\tag{59}
\]

Thus for every datum

\[
\boxed{
0\le
\mathcal C_U(y)-\mathcal C_{U+R}(y)
\le
\mathfrak A_U(y).
}
\tag{60}
\]

This inequality is not merely a comparison: `(7)` identifies the missing nonnegative term exactly as the Parseval mass on the rest of the future nullspace.

---

## 5. Fixed packets give a uniform-in-dilation no-go

For fixed `Z`, the canonical sections increase densely to `H`. Therefore

\[
P_{V_{n-1}}\to I_\mathcal H
\]

strongly. Since the sample space is finite-dimensional,

\[
E_{n-1}
=
L(I-P_{V_{n-1}})L^*
\longrightarrow0
\tag{61}
\]

in operator norm.

For every `m>=2`, the corresponding projected dilation escape lies in the same future tail, so `(2)` yields

\[
0\preceq\Xi_{m,n}\preceq E_{n-1}.
\tag{62}
\]

Hence

\[
\sup_{m\ge2}\|\Xi_{m,n}\|
\le
\|E_{n-1}\|
\to0.
\tag{63}
\]

This is uniform in the dilation factor, including choices `m=m_n` that grow arbitrarily rapidly with `n`.

Likewise, `NB-284`--`NB-287` give for each fixed `y`

\[
\mathfrak A_{n-1}(y)\to0.
\tag{64}
\]

Combining with `(60)`,

\[
\sup_{m\ge2}
\left[
\mathcal C_{n-1}(y)
-
\mathcal C_{V_{n-1}+S_mV_{n-1}}(y)
\right]
\le
\mathfrak A_{n-1}(y)
\to0.
\tag{65}
\]

There is therefore no fixed-packet theorem in which one first drives the ordinary section deep and then recovers an order-one target gain merely by choosing a sufficiently large multiplicative dilation.

This is compatible with the large rank estimate of `NB-297`. A subspace can have large dimension while carrying vanishing sample Gram, because normalized escape directions may increasingly lie in almost sample-null directions. Rank is not the missing scale.

The same conclusion applies to the whitened `NB-297` block. Put

\[
M_{\rm esc}
=K^{-1/2}\Xi K^{-1/2}.
\tag{66}
\]

For fixed `Z`,

\[
K_{n-1}\to K_\infty\succ0,
\tag{67}
\]

so `||K_{n-1}^{-1/2}||` stays bounded for large `n`. By `(63)`,

\[
\sup_{m\ge2}\|M_{\rm esc}(m,n,Z)\|
\to0.
\tag{68}
\]

Thus every target certificate derived solely from this fixed-packet whitened escape also vanishes uniformly in `m`.

---

## 6. Equality cases and the actual moving-packet target

The decomposition `(1)` makes the two endpoint cases transparent.

First,

\[
\Xi=0
\quad\Longleftrightarrow\quad
R\subseteq\ker L.
\tag{69}
\]

This is the sample-null escape case already isolated in `NB-297`.

Second,

\[
\Xi=E
\quad\Longleftrightarrow\quad
\mathcal T\ominus R\subseteq\ker L.
\tag{70}
\]

So `Xi=E` means that the projected dilation block captures **all sample-visible future representer tail**, even though there may still be many future source directions outside `R`.

At the target level,

\[
\mathcal C_U(y)-\mathcal C_{U+R}(y)
=
\mathfrak A_U(y)
\tag{71}
\]

if and only if

\[
P_{(D_\infty\ominus D_U)\ominus\mathcal N_R}h_U=0.
\tag{72}
\]

Thus full matrix occupation and full occupation for one target are distinct notions, as expected.

For a moving Ford family `(Z_X,n_X,m_X)`, the useful theorem can now be stated without ambiguity. One needs a lower estimate showing that the normalized projected dilation block captures a non-negligible portion of the **existing** finite-section tail in the target-relevant directions. Equivalently, one may work either with the sample-tail occupation operator

\[
\Theta_X
=E_X^{+/2}\Xi_XE_X^{+/2},
\tag{73}
\]

or with the nullspace occupation ratio

\[
\boxed{
\eta_X(y_X)
:=
\frac{\|P_{\mathcal N_{R_X}}h_{U_X}\|^2}
{\|P_{D_{\infty,X}\ominus D_{U_X}}h_{U_X}\|^2}
\in[0,1]
}
\tag{74}
\]

whenever the denominator is nonzero.

Then

\[
\mathcal C_{U_X}(y_X)-\mathcal C_{U_X+R_X}(y_X)
=
\eta_X(y_X)\,\mathfrak A_{U_X}(y_X).
\tag{75}
\]

This identity separates the two quantities that a successful Ford-scale argument must control:

1. a nonuniformly surviving finite-section excess `A_(U_X)`; and
2. nontrivial occupation `eta_X` of that excess by the dilation-generated null block.

Neither a large principal-angle defect, a large source escape rank, nor strong coercivity relative to the dilated old baseline supplies these two facts automatically.

---

## 7. Prior-art boundary

The operator identities used here are standard Hilbert-space facts: orthogonal decompositions, minimum-norm right inverses, Moore--Penrose projectors, polar decomposition, and Pythagoras. No novelty is claimed for those abstract ingredients.

The research-specific content is the identification of the `NB-297` Nyman projected-dilation block with three objects already developed independently in this line:

- the representer tail `E=K_infty-K` of `NB-285`;
- the future interpolation nullspace underlying the Parseval decomposition of `NB-287`; and
- the genuine finite-section excess isolated in `NB-284`.

This yields the exact subblock formula `(7)`, the principal-angle cancellation `(8)`, and the uniform-in-`m` fixed-packet no-go `(9)`--`(10)`. The literature audit did not reveal a Nyman--Beurling source stating this particular identification. Existing semigroup, Gram, and approximation results remain background rather than load-bearing inputs, so `SOURCES.md` requires no new dependency for this proof.

---

## Consequence for the research line

`NB-297` made projected dilation escape a legitimate baseline-free candidate. `NB-298` narrows that route: **projected dilation can only spend finite-section excess that was already present**.

The nonzero principal-angle scales of the source escape do not supply extra quantitative mass after normalization, and for every fixed packet the entire projected-dilation block vanishes uniformly over the dilation factor as the ordinary cutoff grows.

Therefore the next discriminating target is not another source-rank or principal-angle estimate. It is a moving-packet occupation estimate coupling the arithmetic dilation geometry to the pre-existing representer/null tail, for example a Ford-scale lower bound on `eta_X(y_X)` together with a nonvanishing lower bound on `A_(U_X)(y_X)`, or an equivalent target-aware lower bound formulated through `Theta_X`.

Without that coupling, projected dilation remains a structurally explicit selector of the finite-section obstruction, not a new mechanism that forces it.