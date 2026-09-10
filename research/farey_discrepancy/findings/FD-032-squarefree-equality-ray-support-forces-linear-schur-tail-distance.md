# FD-032 — squarefree equality-ray support forces linear Schur-tail distance

**Status:** `EXACT-DERIVED + EQUALITY-RAY-SUPPORT + LINEAR-PRIME-BREADTH + SCHUR-DISTANCE-LOWER-BOUND + SATURATION-ESCAPE-CLASSIFICATION`.

`FD-031` reduces every linear prime-prefix relaxation to a physical Mertens tail plus only finitely many synthetic head coordinates. Its remaining obstruction is projective: after Schur-eliminating the synthetic head, saturation of the sharp `FD-003` GCD-duality constant can occur only if that physical tail approaches one distinguished equality direction in the Schur metric.

There is an exact support mismatch hidden inside that direction. The `FD-003` equality vector `K_H^{-1}e_1` vanishes at every nonsquarefree coordinate, whereas the forced physical Mertens tail is identically `M(1)=1` on the whole terminal interval `H/2<d<=H`. Consequently the tail cannot become absolutely close to the extremal ray: **its squared Schur distance from that ray is always at least linear in `H`**, independently of every synthetic head choice.

More precisely, retain the `FD-031` notation

\[
K_H=
\begin{pmatrix}
K_D&P\\
P^T&B
\end{pmatrix},
\qquad
S=B-P^TK_D^{-1}P,
\tag{1}
\]

where

\[
D=\left\lfloor\frac{H}{Y+1}\right\rfloor,
\qquad
y_d=M\!\left(\left\lfloor\frac Hd\right\rfloor\right)
\quad(D<d\le H).
\tag{2}
\]

Put

\[
E:=y^TSy,
\qquad
w:=P^TK_D^{-1}e_1,
\qquad
t:=S^{-1}w,
\tag{3}
\]

\[
\Delta:=w^TS^{-1}w=C_H-C_D,
\qquad
\beta:=w^Ty,
\qquad
\mathfrak D:=\Delta-\frac{\beta^2}{E},
\tag{4}
\]

with

\[
C_n:=(K_n^{-1})_{11},
\qquad
Z:=\zeta(2).
\tag{5}
\]

Whenever `Delta>0`, define the squared projective residual

\[
\rho_{H,D}^2
:=\min_{c\in\mathbb R}(y-ct)^TS(y-ct)
=E-\frac{\beta^2}{\Delta}.
\tag{6}
\]

Then, as soon as `D<H/2`,

\[
\boxed{
\rho_{H,D}^2
\ge
\frac1Z
\left(
\left\lfloor\frac H4\right\rfloor
-
\left\lfloor\frac H8\right\rfloor
\right)
=
\frac{H}{8Z}+O(1).
}
\tag{7}
\]

Since `FD-031` gives

\[
\rho_{H,D}^2
=
\frac{E\mathfrak D}{\Delta},
\tag{8}
\]

one obtains the exact energy-defect tradeoff

\[
\boxed{
E\mathfrak D
\ge
\frac{\Delta}{Z}
\left(
\left\lfloor\frac H4\right\rfloor
-
\left\lfloor\frac H8\right\rfloor
\right).
}
\tag{9}
\]

Thus the angle defect in `FD-031` cannot become small by literal approach of the physical tail to the equality ray. It can become small only because the physical tail norm itself becomes large enough to dilute a compulsory macroscopic transverse component.

In particular, fix `0<lambda<1`. Along any sequence with

\[
H\to\infty,
\qquad
Y\ge\lambda H,
\qquad
Y<H,
\tag{10}
\]

and admissible horizon-dependent prime-prefix sources satisfying

\[
R_H(a)\longrightarrow Z,
\tag{11}
\]

one necessarily has

\[
\boxed{
\frac{E_{H,D(H,Y)}}{H}\longrightarrow\infty.
}
\tag{12}
\]

This conclusion makes no growth assumption on the synthetic source, its endpoint, or the finitely many Schur-eliminated head coordinates. The object forced to become superlinear is the **source-independent physical Mertens tail energy** selected by the linear prime-prefix breadth.

## 1. The unrestricted GCD equality vector is exactly squarefree-supported

Let

\[
u^{(H)}:=K_H^{-1}e_1.
\tag{13}
\]

The inverse factorization already derived in `FD-003` gives, for every `1<=d<=H`,

\[
\boxed{
u_d^{(H)}
=d\sum_{\substack{k\le H\\d\mid k}}
\frac{\mu(k/d)\mu(k)}{J_2(k)}.
}
\tag{14}
\]

If `d` is nonsquarefree, every multiple `k` of `d` is nonsquarefree, so `mu(k)=0`. Hence

\[
\boxed{
\mu(d)=0
\quad\Longrightarrow\quad
u_d^{(H)}=0.
}
\tag{15}
\]

For comparison, if `d` is squarefree, write `k=d\ell`. Only `(d,ell)=1` contributes, and multiplicativity gives the more explicit formula

\[
\nu_d^{(H)}
=
\frac{d\mu(d)}{J_2(d)}
\sum_{\substack{\ell\le H/d\\(\ell,d)=1}}
\frac{\mu(\ell)^2}{J_2(\ell)}.
\tag{16}
\]

The zero set (15), not the asymptotic size in (16), is the load-bearing fact below.

Block inversion of (1) identifies the tail of the same equality vector:

\[
\boxed{
\nu^{(H)}_{D+1:H}=-S^{-1}w=-t.
}
\tag{17}
\]

Therefore every nonsquarefree tail coordinate of the `FD-031` distinguished Schur direction vanishes exactly:

\[
\boxed{
D<d\le H,\ \mu(d)=0
\quad\Longrightarrow\quad
t_d=0.
}
\tag{18}
\]

This is stronger than a small-correlation statement. The unrestricted extremal direction literally has no coordinate support on nonsquarefree indices.

## 2. Multiples of four create a macroscopic transverse tail that no head can cancel

The physical tail in (2) behaves oppositely on the terminal floor-quotient fiber. For every

\[
\frac H2<d\le H,
\tag{19}
\]

one has `floor(H/d)=1`, hence

\[
\boxed{y_d=M(1)=1.}
\tag{20}
\]

Use the exact `FD-003` Jordan decomposition. For any full vector `q=(q_1,...,q_H)`,

\[
q^TK_Hq
=
\sum_{r\le H}J_2(r)
\left(
\sum_{\substack{d\le H\\r\mid d}}
\frac{q_d}{d}
\right)^2.
\tag{21}
\]

For a fixed tail vector `z`, the Schur complement has the variational identity

\[
\boxed{
z^TSz
=
\min_{x\in\mathbb R^D}
\binom{x}{z}^{\!T}
K_H
\binom{x}{z}.
}
\tag{22}
\]

Now let

\[
\mathcal R_H
:=
\left\{r:\frac H2<r\le H,\ 4\mid r\right\}.
\tag{23}
\]

Every `r in R_H` is nonsquarefree. If `D<H/2`, then also `r>D`, so no head index `d<=D` is divisible by `r`. Moreover `2r>H`, so among all tail indices only `d=r` is divisible by `r`.

Take any scalar `c` and put `z=y-ct`. Equations (18) and (20) give

\[
z_r=1
\qquad(r\in\mathcal R_H).
\tag{24}
\]

Consequently, for every possible head `x`, the `r`-th Jordan row in (21) is fixed:

\[
\sum_{\substack{d\le H\\r\mid d}}
\frac{q_d}{d}
=
\frac1r
\qquad(r\in\mathcal R_H).
\tag{25}
\]

These rows are positive squares, so (21)--(22) imply

\[
(y-ct)^TS(y-ct)
\ge
\sum_{r\in\mathcal R_H}\frac{J_2(r)}{r^2}.
\tag{26}
\]

The elementary Euler-product bound already used in `FD-003` is

\[
\frac{J_2(r)}{r^2}
=
\prod_{p\mid r}(1-p^{-2})
\ge
\prod_p(1-p^{-2})
=
\frac1Z.
\tag{27}
\]

Finally,

\[
|\mathcal R_H|
=
\left\lfloor\frac H4\right\rfloor
-
\left\lfloor\frac H8\right\rfloor.
\tag{28}
\]

Taking the minimum over `c` proves (7). Nothing about cancellation of `M(x)` for growing `x` enters: only `M(1)=1`, squarefree support of the GCD equality ray, and positivity of the Jordan rows are used.

The choice of multiples of four is deliberately conservative. Other nonsquarefree terminal indices also contribute, but (23) supplies a deterministic positive-density subset and an exact count without invoking squarefree-density asymptotics.

## 3. Linear-prefix saturation can escape only through superlinear physical-tail energy

Equation (6) is the ordinary projection formula in the `S` inner product. Since

\[
\|y\|_S^2=E,
\qquad
\|t\|_S^2=\Delta,
\qquad
\langle y,t\rangle_S=\beta,
\tag{29}
\]

one has

\[
\rho_{H,D}^2
=E-\frac{\beta^2}{\Delta}
=\frac{E}{\Delta}
\left(\Delta-\frac{\beta^2}{E}\right)
=\frac{E\mathfrak D}{\Delta},
\tag{30}
\]

which proves (8)--(9).

For fixed `lambda`, `FD-031` shows that

\[
D(H,Y)
\le
D_\lambda
:=\left\lceil\frac1\lambda\right\rceil-1.
\tag{31}
\]

Define

\[
\delta_\lambda
:=
Z-
\max_{1\le d\le D_\lambda}C_d
>0.
\tag{32}
\]

Since `C_H->Z`, for all sufficiently large `H` in (10),

\[
\Delta=C_H-C_D\ge\frac{\delta_\lambda}{2}.
\tag{33}
\]

Therefore (9) yields the quantitative tradeoff

\[
\boxed{
E\mathfrak D
\ge
\frac{\delta_\lambda}{2Z}
\left(
\left\lfloor\frac H4\right\rfloor
-
\left\lfloor\frac H8\right\rfloor
\right)
\asymp_\lambda H.
}
\tag{34}
\]

On the other hand `FD-031` gives

\[
R_H(a)
\le C_H-\mathfrak D.
\tag{35}
\]

If (11) holds, then `C_H->Z` forces `mathfrak D->0`. Combining this with (34) proves (12).

Equivalently, any independent estimate of the form

\[
E_{H,D}\le H L(H)
\tag{36}
\]

would immediately imply

\[
\mathfrak D\gg_\lambda\frac1{L(H)}.
\tag{37}
\]

In particular, an `O(H)` bound for the physical Schur-tail energy would create a uniform nonzero GCD-duality gap throughout every fixed linear prime-prefix regime. No such estimate is claimed here; (36)--(37) identify exactly what would be sufficient.

## 4. The half-linear test has the same obstruction before endpoint tuning

When `Y>=H/2`, `FD-031` has `D=1` and also gives the alternative decomposition

\[
K_H=
\begin{pmatrix}1&r^T\\r&B\end{pmatrix},
\qquad
r=\left(\frac12,\frac13,\ldots,\frac1H\right)^T,
\tag{38}
\]

with physical tail `y=(M(floor(H/2)),...,M(1))`,

\[
\mathcal E:=y^TBy,
\qquad
b:=r^Ty,
\qquad
s:=r^TB^{-1}r=1-\frac1{C_H}.
\tag{39}
\]

Block inversion shows that the tail of `K_H^{-1}e_1` is a nonzero scalar multiple of `B^{-1}r`. Hence (15) implies

\[
(B^{-1}r)_d=0
\qquad(d\ge2\text{ nonsquarefree}).
\tag{40}
\]

Repeating the terminal-row argument directly in the `B` metric gives

\[
\boxed{
\min_c
(y-cB^{-1}r)^TB(y-cB^{-1}r)
=
\mathcal E-\frac{b^2}{s}
\ge
\frac1Z
\left(
\left\lfloor\frac H4\right\rfloor
-
\left\lfloor\frac H8\right\rfloor
\right).
}
\tag{41}
\]

Thus the first nonnegative term in the exact `FD-031` reciprocal two-defect identity obeys

\[
\boxed{
\mathcal E
\left(s-\frac{b^2}{\mathcal E}\right)
\ge
\frac{s}{Z}
\left(
\left\lfloor\frac H4\right\rfloor
-
\left\lfloor\frac H8\right\rfloor
\right).
}
\tag{42}
\]

So even before the free endpoint `A(H)=M(H)+2k` is tuned, half-linear saturation requires `mathcal E/H->infinity`. Endpoint freedom cannot cancel the terminal nonsquarefree tail mismatch because that mismatch lies in positive Jordan rows to which the endpoint does not contribute.

## 5. Relation to earlier obstructions, prior art, and audit boundary

`FD-025` already proves a universal macroscopic distance from the unrestricted equality ray for a **common source** with a sublinear endpoint, and from it derives the necessity of super-square-root endpoint growth under sparse-horizon saturation. The present statement is not another source-growth theorem. Its different content is that after `FD-031` has discarded **all** residual linear-prefix head constraints and optimized those head coordinates over arbitrary reals, a macroscopic obstruction still survives entirely inside the forced physical Mertens tail. Hence horizon-dependent synthetic sources do not evade the obstruction by choosing enormous head values: if they saturate at linear prime breadth, the escape is transferred to superlinear physical-tail energy.

The inverse formula (14), Jordan factorization (21), and Schur-complement identities are classical matrix/arithmetic ingredients already anchored in `SOURCES.md` through Smith and Haukkanen--Wang--Sillanpää. A targeted prior-art search for GCD-matrix inverse support, Farey--Mertens GCD energy, and Schur-complement extremality found the classical GCD-matrix literature but no additional theorem needed by (7)--(12). No novelty is claimed for the squarefree support of Möbius or for Schur projection by itself; the line-specific delta is the exact support mismatch between the GCD equality ray and the forced terminal Mertens tail after linear-prefix Schur elimination. No new source anchor is therefore required.

The falsification checks are explicit. The argument needs `D<H/2` only so that the selected terminal Jordan rows cannot see a head coordinate; this is automatic eventually for every fixed positive linear breadth. Multiples of four are used because they are certainly nonsquarefree, not because `4` has special Farey meaning. The conclusion concerns `E=y^TSy` (or `mathcal E=y^TBy` in the half-linear specialization), not the complete physical Franel energy. Finally, (12) is only a necessary condition for saturation. Superlinear physical-tail energy does not imply tail alignment, does not construct a saturating prime-prefix source, and does not improve the Franel--Landau exponent or prove RH.
