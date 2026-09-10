# FD-032 — squarefree equality-ray support forces linear Schur-tail distance

**Status:** `EXACT-DERIVED + EQUALITY-RAY-SUPPORT + LINEAR-PRIME-BREADTH + SCHUR-DISTANCE-LOWER-BOUND + SATURATION-ESCAPE-CLASSIFICATION`.

`FD-031` reduces every linear prime-prefix relaxation to a physical Mertens tail plus only finitely many synthetic head coordinates. Its remaining obstruction is projective: after Schur-eliminating the synthetic head, saturation of the sharp `FD-003` GCD-duality constant can occur only if that physical tail approaches one distinguished equality direction in the Schur metric.

There is an exact support mismatch hidden inside that direction. The `FD-003` equality vector `K_H^{-1}e_1` vanishes at every nonsquarefree coordinate, whereas the forced physical Mertens tail is identically `M(1)=1` on the terminal interval `H/2<d<=H`. Consequently the tail cannot become absolutely close to the extremal ray: **its squared Schur distance from that ray is always at least linear in `H`**, independently of every synthetic head choice.

Retain the `FD-031` notation

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

Whenever `Delta>0`, define

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

Since

\[
\rho_{H,D}^2
=
\frac{E\mathfrak D}{\Delta},
\tag{8}
\]

this gives the exact energy-defect tradeoff

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

Thus the angle defect from `FD-031` can become small only by diluting a compulsory macroscopic transverse component inside an increasingly large physical-tail norm.

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

No growth assumption is made on the synthetic source, its endpoint, or the finitely many Schur-eliminated head coordinates. The object forced to become superlinear is the **source-independent physical Mertens tail energy** selected by linear prime-prefix breadth.

## 1. The unrestricted equality vector is exactly squarefree-supported

Let

\[
u^{(H)}:=K_H^{-1}e_1.
\tag{13}
\]

Here the displayed symbol is the Latin vector `u`, not a new arithmetic function. The inverse factorization already derived in `FD-003` gives, for every `1<=d<=H`,

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

For squarefree `d`, writing `k=d\ell` gives the explicit companion formula

\[
u_d^{(H)}
=
\frac{d\mu(d)}{J_2(d)}
\sum_{\substack{\ell\le H/d\\(\ell,d)=1}}
\frac{\mu(\ell)^2}{J_2(\ell)}.
\tag{16}
\]

Only the exact zero set (15) is needed below. Block inversion of (1) identifies the tail of the same vector:

\[
u^{(H)}_{D+1:H}=-S^{-1}w=-t.
\tag{17}
\]

Therefore

\[
\boxed{
D<d\le H,\ \mu(d)=0
\quad\Longrightarrow\quad
t_d=0.
}
\tag{18}
\]

The distinguished Schur direction literally has no coordinate support on nonsquarefree tail indices.

## 2. Multiples of four create a macroscopic transverse tail

For every

\[
\frac H2<d\le H,
\tag{19}
\]

one has `floor(H/d)=1`, so the physical tail satisfies

\[
\boxed{y_d=M(1)=1.}
\tag{20}
\]

The exact `FD-003` Jordan decomposition is

\[
q^TK_Hq
=
\sum_{r\le H}J_2(r)
\left(
\sum_{\substack{d\le H\\r\mid d}}
\frac{q_d}{d}
\right)^2
\tag{21}
\]

for every full vector `q`. The Schur complement also has the variational identity

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

Now take

\[
\mathcal R_H
:=
\left\{r:\frac H2<r\le H,\ 4\mid r\right\}.
\tag{23}
\]

Every `r in R_H` is nonsquarefree. If `D<H/2`, then `r>D`, so no head coordinate can enter its divisor-incidence row. Since `2r>H`, the only tail coordinate divisible by `r` is `d=r` itself.

For any scalar `c`, put `z=y-ct`. Equations (18) and (20) give

\[
z_r=1
\qquad(r\in\mathcal R_H).
\tag{24}
\]

Hence every possible Schur-minimizing head still leaves the fixed positive Jordan contributions

\[
(y-ct)^TS(y-ct)
\ge
\sum_{r\in\mathcal R_H}\frac{J_2(r)}{r^2}.
\tag{25}
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
\tag{26}
\]

Finally,

\[
|\mathcal R_H|
=
\left\lfloor\frac H4\right\rfloor
-
\left\lfloor\frac H8\right\rfloor.
\tag{27}
\]

Taking the minimum over `c` proves (7). No estimate for `M(x)` at growing `x` enters: only `M(1)=1`, exact squarefree support of the equality ray, and positivity of the Jordan rows are used. Multiples of four are deliberately conservative; they provide a deterministic positive-density nonsquarefree subset with an exact count.

## 3. Linear-prefix saturation can escape only through superlinear tail energy

Since

\[
\|y\|_S^2=E,
\qquad
\|t\|_S^2=\Delta,
\qquad
\langle y,t\rangle_S=\beta,
\tag{28}
\]

the projection formula gives

\[
\rho_{H,D}^2
=E-\frac{\beta^2}{\Delta}
=
\frac{E}{\Delta}
\left(\Delta-\frac{\beta^2}{E}\right)
=
\frac{E\mathfrak D}{\Delta},
\tag{29}
\]

proving (8)--(9).

For fixed `lambda`, `FD-031` gives

\[
D(H,Y)
\le
D_\lambda
:=\left\lceil\frac1\lambda\right\rceil-1.
\tag{30}
\]

Define

\[
\delta_\lambda
:=
Z-
\max_{1\le d\le D_\lambda}C_d
>0.
\tag{31}
\]

Since `C_H->Z`, for all sufficiently large `H` in (10),

\[
\Delta=C_H-C_D\ge\frac{\delta_\lambda}{2}.
\tag{32}
\]

Therefore

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
\tag{33}
\]

`FD-031` also gives

\[
R_H(a)\le C_H-\mathfrak D.
\tag{34}
\]

Thus `R_H(a)->Z` forces `mathfrak D->0`, and (33) forces (12).

More generally, an independent estimate

\[
E_{H,D}\le H L(H)
\tag{35}
\]

would imply

\[
\mathfrak D\gg_\lambda\frac1{L(H)}.
\tag{36}
\]

In particular, an `O(H)` bound for the physical Schur-tail energy would create a uniform nonzero GCD-duality gap throughout every fixed linear prime-prefix regime. No such estimate is claimed here; (35)--(36) identify exactly what would suffice.

## 4. The half-linear test has the same obstruction before endpoint tuning

When `Y>=H/2`, `FD-031` has `D=1` and writes

\[
K_H=
\begin{pmatrix}1&r^T\\r&B\end{pmatrix},
\qquad
r=\left(\frac12,\frac13,\ldots,\frac1H\right)^T.
\tag{37}
\]

For the physical tail `y=(M(floor(H/2)),...,M(1))`, put

\[
\mathcal E:=y^TBy,
\qquad
b:=r^Ty,
\qquad
s:=r^TB^{-1}r=1-\frac1{C_H}.
\tag{38}
\]

Block inversion shows that the tail of `K_H^{-1}e_1` is a nonzero scalar multiple of `B^{-1}r`. Therefore (15) implies

\[
(B^{-1}r)_d=0
\qquad(d\ge2\text{ nonsquarefree}).
\tag{39}
\]

The same terminal-row argument in the `B` metric gives

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
\tag{40}
\]

Thus the first nonnegative term in the exact `FD-031` reciprocal two-defect identity satisfies

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
\tag{41}
\]

So even before the free endpoint `A(H)=M(H)+2k` is tuned, half-linear saturation requires `mathcal E/H->infinity`. Endpoint freedom cannot cancel the terminal nonsquarefree mismatch because those positive Jordan rows do not see the endpoint.

## 5. Relation to earlier obstructions, prior art, and audit boundary

`FD-025` proves a universal macroscopic distance from the unrestricted equality ray for a **common source** with a sublinear endpoint, and from it derives the necessity of super-square-root endpoint growth under sparse-horizon saturation. The present statement is different: after `FD-031` has discarded **all** residual linear-prefix head constraints and optimized those head coordinates over arbitrary reals, a macroscopic obstruction still survives entirely inside the forced physical Mertens tail. Horizon-dependent synthetic sources therefore cannot evade it merely by choosing enormous head values; saturation transfers the escape to superlinear physical-tail energy.

The inverse formula (14), Jordan factorization (21), and Schur-complement identities are classical ingredients already anchored in `SOURCES.md` through Smith and Haukkanen--Wang--Sillanpää. A targeted prior-art search for GCD-matrix inverse support, Farey--Mertens GCD energy, and Schur-complement extremality found the classical GCD-matrix literature but no additional theorem required by (7)--(12). No novelty is claimed for Möbius squarefree support or Schur projection in isolation; the line-specific delta is their exact splice with the forced terminal Mertens tail after linear-prefix Schur elimination. No new source anchor is required.

The falsification checks are explicit. The argument needs `D<H/2` only so the selected terminal Jordan rows cannot see a head coordinate; this is automatic eventually for every fixed positive linear breadth. Multiples of four are used because they are certainly nonsquarefree, not because `4` has special Farey meaning. The conclusion concerns `E=y^TSy` (or `mathcal E=y^TBy` in the half-linear specialization), not the complete physical Franel energy. Finally, (12) is only a necessary condition for saturation: superlinear physical-tail energy does not imply tail alignment, construct a saturating source, improve the Franel--Landau exponent, or prove RH.
