# FD-031 — linear prime-prefix relaxations have an exact Mertens-tail angle defect

**Status:** `EXACT-DERIVED + SCHUR-COMPLEMENT + LINEAR-PRIME-BREADTH + PHYSICAL-MERTENS-TAIL + SATURATION-OBSTRUCTION + FINITE-DIMENSIONAL-REDUCTION`.

`FD-030` shows that exact Möbius ancestry through every prime below any unbounded cutoff `Y_H=o(H)` still permits horizon-dependent saturation of the sharp `FD-003` GCD-duality constant. It leaves the first genuinely different breadth regime at `Y_H` comparable with `H`. `FD-029` already gives the finite-scale information boundary there: once `Y` is a positive fraction of `H`, all but finitely many leading horizon coordinates are forced to equal the physical Mertens staircase.

The remaining relaxation can be solved exactly at the level of quadratic geometry. The result is a new obstruction specific to the linear-breadth regime: **after the finitely many still-free leading coordinates are optimized away, saturation is possible only if the forced physical Mertens tail becomes projectively aligned with one distinguished Schur-complement direction.** Endpoint or low-coordinate doping cannot repair a persistent tail-angle defect.

More precisely, fix integers

\[
1\le Y<H
\]

and let `a_1,...,a_H` obey the squarefree ternary conditions and the complete prime-prefix ancestry law of `FD-029` through `Y`. Put

\[
A(x)=\sum_{n\le x}a_n,
\qquad
m_d=A\!\left(\left\lfloor\frac Hd\right\rfloor\right),
\qquad
K_H(d,e)=\frac{\gcd(d,e)^2}{de},
\tag{1}
\]

and define

\[
D=D(H,Y):=\left\lfloor\frac{H}{Y+1}\right\rfloor.
\tag{2}
\]

Then `D>=1`, and every coordinate with `d>D` is already physical:

\[
\boxed{
m_d=M\!\left(\left\lfloor\frac Hd\right\rfloor\right)
\qquad(d>D).}
\tag{3}
\]

Write the block decomposition

\[
K_H=
\begin{pmatrix}
K_D&P\\
P^T&B
\end{pmatrix},
\qquad
m=\binom{x}{y},
\tag{4}
\]

where `x in R^D` contains the possibly nonphysical leading coordinates and

\[
y_d=M\!\left(\left\lfloor\frac Hd\right\rfloor\right),
\qquad D<d\le H,
\tag{5}
\]

is the forced Mertens tail. Let

\[
S:=B-P^TK_D^{-1}P,
\qquad
E:=y^TSy,
\tag{6}
\]

\[
\beta:=e_1^TK_D^{-1}Py,
\qquad
C_D:=(K_D^{-1})_{11},
\qquad
C_H:=(K_H^{-1})_{11}.
\tag{7}
\]

The matrices `K_D` and `S` are positive definite and `y` is nonzero because its last coordinate is `M(1)=1`; hence `E>0`. If

\[
R_H(a):=\frac{A(H)^2}{m^TK_Hm}
\tag{8}
\]

for a nonzero endpoint, then every admissible source satisfies the exact relaxation bound

\[
\boxed{
R_H(a)\le
\widehat R_{H,D}
:=C_D+\frac{\beta^2}{E}
\le C_H.
}
\tag{9}
\]

Both inequalities have a precise geometric meaning. Put

\[
w:=P^TK_D^{-1}e_1,
\qquad
\Delta_{H,D}:=C_H-C_D.
\tag{10}
\]

Block inversion gives

\[
\boxed{
\Delta_{H,D}=w^TS^{-1}w,
}
\tag{11}
\]

while `beta=w^Ty`. Therefore Cauchy--Schwarz in the `S` metric yields

\[
\frac{\beta^2}{E}\le\Delta_{H,D}.
\tag{12}
\]

Define the **physical tail defect**

\[
\boxed{
\mathfrak D_{H,D}
:=\Delta_{H,D}-\frac{\beta^2}{E}\ge0.
}
\tag{13}
\]

Then (9) is equivalently

\[
\boxed{
\widehat R_{H,D}=C_H-\mathfrak D_{H,D}.
}
\tag{14}
\]

Whenever `Delta_(H,D)>0`, let `theta_(H,D)` be the projective angle in the `S` inner product between the physical tail `y` and the distinguished vector `S^(-1)w`. Since

\[
\|y\|_S^2=E,
\qquad
\|S^{-1}w\|_S^2=\Delta_{H,D},
\qquad
\langle y,S^{-1}w\rangle_S=\beta,
\tag{15}
\]

one has the exact angle formula

\[
\boxed{
\mathfrak D_{H,D}
=\Delta_{H,D}\sin^2\theta_{H,D}.
}
\tag{16}
\]

Thus the only way the real relaxation with a fixed physical tail can recover the unrestricted coordinate constant is for that tail to lie on the unique extremal projective direction after the finitely many free coordinates have been Schur-eliminated.

## 1. The prime prefix freezes the whole tail at linear breadth

`FD-029` proves the exact prefix identity

\[
A(x)=M(x)\qquad(1\le x\le Y).
\tag{17}
\]

If `d>D`, then by (2)

\[
d>\frac{H}{Y+1},
\]

so

\[
\left\lfloor\frac Hd\right\rfloor\le Y.
\tag{18}
\]

Equation (17) therefore gives (3). No estimate for `M`, distribution of primes, or asymptotic argument is used.

This is the sharp coordinate count for the present purpose: the only horizon entries that can possibly differ from the physical Mertens vector are those for which `floor(H/d)>Y`, exactly the indices `d<=D`. The arithmetic constraints among those first `D` values may be much stronger than arbitrary real freedom. Replacing them by arbitrary `x in R^D` is therefore a relaxation, so any upper bound obtained after that replacement remains valid for the actual prime-prefix class.

If `Y>=lambda H` for a fixed `0<lambda<1`, then

\[
D<\frac1\lambda,
\qquad
D\le \left\lceil\frac1\lambda\right\rceil-1.
\tag{19}
\]

Hence a positive linear prime breadth leaves only a **uniformly bounded-dimensional** synthetic head and a growing physical tail.

## 2. Exact optimization over every remaining synthetic head

For arbitrary `x in R^D`, complete the square in (4):

\[
\begin{aligned}
m^TK_Hm
&=x^TK_Dx+2x^TPy+y^TBy\\
&=(x+K_D^{-1}Py)^TK_D(x+K_D^{-1}Py)+y^TSy.
\end{aligned}
\tag{20}
\]

Set

\[
z=x+K_D^{-1}Py,
\qquad
u=z_1.
\tag{21}
\]

Because the first component of `K_D^(-1)Py` is `beta`, the endpoint is

\[
x_1=\nu-\beta.
\tag{22}
\]

For fixed `nu`, the sharp `FD-003` coordinate inequality in dimension `D` gives

\[
z^TK_Dz\ge\frac{\nu^2}{C_D},
\tag{23}
\]

with equality on the `K_D` equality ray. Consequently

\[
\frac{x_1^2}{m^TK_Hm}
\le
\frac{(\nu-\beta)^2}{\nu^2/C_D+E}.
\tag{24}
\]

The right side has an exact one-variable supremum. Weighted Cauchy--Schwarz gives

\[
(\nu-\beta)^2
\le
\left(\frac{\nu^2}{C_D}+E\right)
\left(C_D+\frac{\beta^2}{E}\right),
\tag{25}
\]

and the constant is sharp as a supremum. If `beta!=0`, equality occurs at a finite `nu`; if `beta=0`, the value `C_D` is approached as `|nu|->infinity`. This proves the first inequality in (9) and identifies the best possible quotient after **all** residual head constraints have been discarded.

The second inequality is not an additional estimate. The standard block inverse formula gives

\[
(K_H^{-1})_{1,1}
=(K_D^{-1})_{1,1}
+e_1^TK_D^{-1}P
S^{-1}P^TK_D^{-1}e_1,
\tag{26}
\]

which is exactly (11). Since `beta=w^Ty`, Cauchy--Schwarz in the positive `S` metric gives

\[
\beta^2
\le
(y^TSy)(w^TS^{-1}w)
=E\Delta_{H,D},
\tag{27}
\]

proving (12)--(16).

The important point is where the loss now lives. It is no longer in the unknown synthetic values `A(H),A(floor(H/2)),...` themselves: those have been optimized away. The entire difference between the best linear-prefix relaxation and unrestricted `FD-003` saturation is the projective mismatch of the **actual Mertens tail** with one explicit Schur-complement direction.

## 3. Any fixed positive linear breadth forces tail alignment under saturation

Let `Z=zeta(2)`. `FD-003` gives

\[
C_H\longrightarrow Z.
\tag{28}
\]

Fix `0<lambda<1` and suppose there are horizons `H_j->infinity`, cutoffs

\[
Y_j\ge\lambda H_j,
\qquad
Y_j<H_j,
\tag{29}
\]

and admissible horizon-dependent prime-prefix sources for which

\[
R_{H_j}(a^{(j)})\longrightarrow Z.
\tag{30}
\]

By (19), the integers `D_j=D(H_j,Y_j)` range over only finitely many values. For every fixed finite `D`, `C_D<Z`; hence

\[
\delta_\lambda
:=Z-
\max_{1\le D\le\lceil1/\lambda\rceil-1}C_D
>0.
\tag{31}
\]

For all sufficiently large `j`, therefore,

\[
\Delta_{H_j,D_j}=C_{H_j}-C_{D_j}\ge\frac{\delta_\lambda}{2}.
\tag{32}
\]

Since

\[
R_{H_j}\le\widehat R_{H_j,D_j}\le C_{H_j}	o Z,
\]

assumption (30) forces

\[
\boxed{
\mathfrak D_{H_j,D_j}\longrightarrow0,
\qquad
\sin^2\theta_{H_j,D_j}\longrightarrow0.
}
\tag{33}
\]

This is the qualitative transition that the sublinear construction in `FD-030` could avoid. At `Y_H=o(H)`, an unbounded reservoir of free prime quotient shells can synthesize larger and larger portions of the GCD equality ray. At `Y_H>=lambda H`, only boundedly many head coordinates remain synthetic. If saturation still occurs, the growing part of the vector is no longer engineerable: the **physical Mertens tail itself must converge projectively to the corresponding extremal Schur direction**.

Conversely, any theorem giving a fixed angular separation

\[
\sin^2\theta_{H,D(H,Y)}\ge\varepsilon_\lambda>0
\tag{34}
\]

through all sufficiently large horizons with `Y>=lambda H` would immediately give a nonvanishing gap for this whole linear-prefix relaxation. Such a theorem would be genuine arithmetic input about the Mertens tail; it is not supplied here.

## 4. At half-linear breadth the endpoint and tail deficits separate completely

The case `Y>=H/2` makes the geometry especially transparent. For `Y<H`, equation (2) gives `D=1`, agreeing with the endpoint-doping classification in `FD-029`: every coordinate `d>=2` is physical and only `A(H)` may vary.

Write

\[
r=\left(\frac12,\frac13,\ldots,\frac1H\right)^T,
\qquad
K_H=
\begin{pmatrix}1&r^T\\r&B\end{pmatrix},
\tag{35}
\]

and let

\[
y_d=M\!\left(\left\lfloor\frac Hd\right\rfloor\right)\quad(d\ge2),
\qquad
\mathcal E=y^TBy,
\qquad
b=r^Ty,
\tag{36}
\]

\[
s=r^TB^{-1}r=1-\frac1{C_H}.
\tag{37}
\]

For any admissible nonzero endpoint `x=A(H)=M(H)+2k`, `FD-029` gives

\[
R_H(x)=
\frac{x^2}{x^2+2bx+\mathcal E}.
\tag{38}
\]

Completing the square in `1/x` yields the exact two-defect identity

\[
\boxed{
\frac1{R_H(x)}-\frac1{C_H}
=
\left(s-\frac{b^2}{\mathcal E}\right)
+
\mathcal E
\left(\frac1x+\frac b{\mathcal E}\right)^2.
}
\tag{39}
\]

Both terms are nonnegative. The first is the physical Mertens-tail angle defect in the `B` metric; the second is the endpoint-reachability defect. Thus even perfect choice of the free prime signs cannot hide a bad tail angle, while perfect tail alignment is still not sufficient unless the discrete endpoint progression can approach the required optimizer. If `x=0`, then `R_H=0` and saturation is already impossible.

Equation (39) is stronger than merely writing the one-dimensional family in `FD-029`: it identifies exactly and additively where every failure to saturate the unrestricted coordinate constant comes from.

## 5. Consequence and prior-art boundary

This result does **not** prove a uniform linear-prefix gap, an improved Franel exponent, a new Mertens estimate, or RH. It instead turns the open linear-breadth control problem left by `FD-030` into a sharply defined arithmetic target. A horizon-dependent synthetic source satisfying ancestry through a positive fraction of all prime directions can saturate only when a completely source-independent object — the physical Mertens tail (5) — is already nearly extremal in the explicit Schur geometry (6), and in the half-linear regime its remaining endpoint must also satisfy the exact tuning condition in (39).

The block Schur-complement formula, weighted Cauchy--Schwarz optimization, and projective-angle interpretation are standard finite-dimensional linear algebra. The GCD-matrix factorization and sharp coordinate constant are already anchored in `FD-003` through the classical Smith/meet-matrix literature. `FD-029` supplies the exact prime-prefix-to-physical-tail bridge. No novelty is claimed for Schur complements or constrained Rayleigh quotients in isolation; the line-specific delta is the exact combination showing where the first linear prime-breadth regime differs from the `FD-030` sublinear saturation construction.

A targeted prior-art search around Farey discrepancy, Mertens GCD matrices, and Schur-complement extremality did not identify an external theorem needed for the derivation. The proof above is finite and self-contained once `FD-003` and `FD-029` are admitted, so `SOURCES.md` does not require a new load-bearing anchor.

The decisive falsification checks are explicit. The tail begins at `D+1`, not at an approximate index `H/Y`; (2) is chosen so that `floor(H/d)<=Y` holds exactly. The leading `D` coordinates are deliberately relaxed to arbitrary reals, so (9) is an upper bound for the arithmetic class rather than a realizability claim. A small angle defect is only a necessary condition for saturation; it does not construct admissible head values. Finally, a nonvanishing constant gap from `zeta(2)` would still be a constant-level separation of the GCD-duality relaxation and would not by itself improve the RH-critical exponent.