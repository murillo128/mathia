# FD-027 — finite-prime Möbius ancestry still allows sparse GCD-duality saturation

**Status:** `EXACT-DERIVED + COMMON-SOURCE-CONSTRUCTION + EXACT-SQUAREFREE-TERNARY-INCREMENTS + FINITE-PRIME-MOBIUS-ANCESTRY + POWER-ENVELOPE-CONTROL + RH-SCALE-DIAGONAL-CONTROL + SPARSE-HORIZON-SATURATION + NEGATIVE/OBSTRUCTION`.

`FD-026` shows that one common source with the exact Möbius zero set and exact unit amplitudes on every squarefree increment can still approach the sharp Franel--Mertens GCD-duality constant on sufficiently sparse horizons, even while satisfying every `1/2+epsilon` cumulative growth envelope. Its remaining freedom is the choice of squarefree signs. The next natural restriction is to impose genuine pieces of the Möbius multiplicative sign law rather than another endpoint norm.

Any **fixed finite set of prime directions is still insufficient**.

Let `P` be a fixed finite set of primes and put

\[
Q:=\prod_{p\in P}p,
\qquad
Z:=\zeta(2).
\tag{1}
\]

For an increment sequence `a=(a_n)`, write

\[
A(x):=\sum_{n\le x}a_n,
\qquad
m_d^{(H)}:=A\!\left(\left\lfloor\frac Hd\right\rfloor\right),
\tag{2}
\]

and retain the line's GCD kernel

\[
K_H(d,e):=\frac{\gcd(d,e)^2}{de},
\qquad
E_H:=(m^{(H)})^TK_Hm^{(H)},
\qquad
R_H:=\frac{A(H)^2}{E_H},
\tag{3}
\]

with `R_H:=0` when the horizon vector vanishes.

Then, for every fixed `alpha>1/2` and every increasing integer sequence

\[
H_0<H_1<\cdots,
\qquad
\frac{H_j}{H_{j-1}}\longrightarrow\infty,
\tag{4}
\]

there is one infinite sequence `a` such that

\[
a_1=1,\qquad
a_n=0\ \text{if }n\text{ is nonsquarefree},\qquad
a_n\in\{-1,+1\}\ \text{if }n\text{ is squarefree},
\tag{5}
\]

and, simultaneously for every `p in P`,

\[
\boxed{
a_{pn}=-a_n
\qquad\text{whenever }p\nmid n.
}
\tag{6}
\]

(The nonsquarefree cases in (6) are `0=0`; on squarefree inputs this is exactly the Möbius sign rule in the fixed prime direction `p`.) The same source satisfies

\[
|A(n)|\ll_{P,\alpha}n^\alpha
\tag{7}
\]

and

\[
\boxed{
R_{H_j}\longrightarrow Z.
}
\tag{8}
\]

There is also the same RH-scale diagonal strengthening as in `FD-026`: for every fixed finite `P`, one can choose a sufficiently sparse horizon sequence and one source satisfying (5)--(6) such that

\[
\boxed{
A(n)=O_{P,\varepsilon}\!\left(n^{1/2+\varepsilon}\right)
\quad\text{for every }\varepsilon>0,
\qquad
R_{H_j}\longrightarrow Z.
}
\tag{9}
\]

Thus the obstruction in `FD-026` survives not merely free squarefree signs but **any fixed finite amount of exact prime-by-prime Möbius ancestry**. A source-side argument that separates the physical Mertens staircase from sparse GCD near-extremizers must use prime breadth growing with scale, a genuinely global multiplicative/divisor constraint, or information retained before the Farey data collapse to this cumulative staircase. This is a negative classification of a relaxation; it is not an estimate for the true Möbius function and does not improve the Franel--Landau exponent.

## 1. Factor out finitely many prime signs

Let

\[
\mathcal C_P
:=
\{m\ge1:m\text{ is squarefree and }(m,Q)=1\}.
\tag{10}
\]

Choose signs `b_m in {-1,+1}` on `\mathcal C_P`, with `b_1=1`, and set

\[
B(x):=\sum_{\substack{m\le x\\m\in\mathcal C_P}} b_m.
\tag{11}
\]

Every squarefree `n` has a unique factorization

\[
n=q\,m,
\qquad
q\mid Q,\quad m\in\mathcal C_P.
\tag{12}
\]

Define

\[
a_n=
\begin{cases}
\mu(q)b_m,& n=qm\text{ as in (12)},\\
0,&n\text{ nonsquarefree}.
\end{cases}
\tag{13}
\]

This gives (5). If `p in P` and `p\nmid n`, multiplication by `p` toggles exactly one factor in `q`, so (6) follows. Conversely, all freedom of the construction is now concentrated in the core signs `b_m`.

Summing (13) by the divisor `q` gives the exact finite-difference identity

\[
\boxed{
A(x)=\sum_{q\mid Q}\mu(q)\,
B\!\left(\left\lfloor\frac{x}{q}\right\rfloor\right).
}
\tag{14}
\]

At a horizon `H`, write

\[
q_d:=\left\lfloor\frac Hd\right\rfloor.
\tag{15}
\]

Nested floors satisfy

\[
\left\lfloor\frac{q_d}{q}\right\rfloor
=
\left\lfloor\frac{H}{qd}\right\rfloor
=q_{qd},
\tag{16}
\]

hence

\[
\boxed{
A(q_d)=\sum_{q\mid Q}\mu(q)B(q_{qd}).
}
\tag{17}
\]

Equation (17) is the load-bearing point. Imposing finitely many exact prime-sign relations does not destroy endpoint interpolation; it replaces direct interpolation of `A(q_d)` by a finite triangular difference problem for the core cumulative function `B`.

## 2. The core still has enough local sign capacity

Let

\[
\mathsf Q_P(x):=\#\{m\le x:m\in\mathcal C_P\}.
\tag{18}
\]

Elementary squarefree and coprimality inclusion-exclusion gives

\[
\boxed{
\mathsf Q_P(x)=c_Px+O_P(\sqrt x),
\qquad
c_P=
\frac1{\zeta(2)}
\prod_{p\in P}\frac{p}{p+1}>0.
}
\tag{19}
\]

For completeness, first restrict the squarefree indicator to integers coprime to `Q`, then expand it. This gives

\[
\mathsf Q_P(x)
=
\sum_{\substack{r\le\sqrt x\\(r,Q)=1}}
\mu(r)
\sum_{s\mid Q}\mu(s)
\left\lfloor\frac{x}{r^2s}\right\rfloor.
\tag{20}
\]

The floor errors total `O_P(sqrt x)`, while the main Euler product is

\[
\left(\sum_{\substack{r\ge1\\(r,Q)=1}}\frac{\mu(r)}{r^2}\right)
\left(\sum_{s\mid Q}\frac{\mu(s)}s\right)
=
\frac1{\zeta(2)}
\prod_{p\mid Q}\frac{p}{p+1}.
\tag{21}
\]

For the hyperbola interval

\[
I_d:=(q_{d+1},q_d]\cap\mathbb Z
\tag{22}
\]

let `S_{P,d}` count its core points. From (19),

\[
S_{P,d}
=
c_P|I_d|+O_P(\sqrt{q_d}),
\tag{23}
\]

so whenever `R=R(H)` obeys

\[
R\to\infty,
\qquad
\frac{R^3}{H}\to0,
\tag{24}
\]

one has, uniformly for `1<=d<=QR`,

\[
\boxed{
S_{P,d}\gg_P \frac{H}{d^2}.
}
\tag{25}
\]

The fixed factor `Q` is harmless in (24).

There is also an exact parity criterion. Any assignment of core signs satisfies

\[
B(x)\equiv\mathsf Q_P(x)\pmod2.
\tag{26}
\]

Conversely, if an interval contains `S` core integers, every endpoint change `Delta` with `|Delta|<=S` and `Delta congruent S (mod 2)` is realizable by choosing the appropriate numbers of `+1` and `-1` core signs. Those signs can be ordered so that intermediate partial sums remain between the prescribed endpoint values up to a unit overshoot.

## 3. A finite triangular inversion preserves the equality prefix

Let

\[
\nu^{(R)}:=K_R^{-1}e_1,
\qquad
C_R:=\nu^{(R)}_1.
\tag{27}
\]

`FD-003` gives `C_R -> Z`, and `FD-024` gives the uniform bound

\[
|\nu_d^{(R)}|\le\frac{Z^2}{d}.
\tag{28}
\]

Fix first an exponent `gamma` with

\[
\frac12<\gamma<\min\{\alpha,1\}
\tag{29}
\]

when `alpha<1`, and choose any `gamma in (1/2,1)` when `alpha>=1`.
Choose

\[
0<\beta<\min\left\{1-\gamma,\frac13\right\},
\tag{30}
\]

and on a sufficiently late stage of (4), with `rho=H/H_prev`, put

\[
R:=
\left\lfloor
\min\left\{H^\beta,\frac{\rho}{16Q}\right\}
\right\rfloor,
\qquad
t:=\frac{H^\gamma}{64Z^2}.
\tag{31}
\]

Then

\[
R\to\infty,\qquad
R^3/H\to0,\qquad
H^{\gamma-1}R\to0,
\qquad
q_{QR}>H_{\rm prev}.
\tag{32}
\]

For `1<=d<=R`, choose an integer `y_d` of the forced squarefree parity such that

\[
y_d\equiv \mathsf Q(q_d)\pmod2,
\qquad
|y_d-t\nu_d^{(R)}|\le1,
\tag{33}
\]

where `\mathsf Q(x)` is the number of all squarefree integers up to `x`.
We want

\[
A(q_d)=y_d.
\tag{34}
\]

Write `z_d:=B(q_d)`. For the boundary indices

\[
R<d\le QR
\tag{35}
\]

first choose `z_d in {0,1}` with

\[
z_d\equiv\mathsf Q_P(q_d)\pmod2.
\tag{36}
\]

Now define `z_d` for `d=R,R-1,...,1` by the triangular recurrence

\[
\boxed{
z_d
=
y_d-
\sum_{\substack{q\mid Q\\q>1}}
\mu(q)z_{qd}.
}
\tag{37}
\]

Every index on the right is larger than `d` and at most `QR`, so this is well-defined. Equation (37) is exactly (17), hence (34) holds.

The parity also closes exactly. Unique decomposition (12) implies

\[
\mathsf Q(x)
=
\sum_{q\mid Q}
\mathsf Q_P\!\left(\left\lfloor\frac{x}{q}\right\rfloor\right).
\tag{38}
\]

Using (16), (33), and the fact that `mu(q)` is odd for every `q|Q`, induction in (37) gives

\[
\boxed{
z_d\equiv\mathsf Q_P(q_d)\pmod2
\qquad(1\le d\le QR).
}
\tag{39}
\]

Thus all prescribed core endpoints have exactly the parity required by actual `+-1` core signs.

It remains to check size. Let `T_p` denote the dilation operator `(T_pz)_d=z_{pd}`. The left side of (17) is

\[
\prod_{p\in P}(I-T_p)z.
\tag{40}
\]

With zero boundary, its inverse is the positive semigroup series

\[
\prod_{p\in P}(I-T_p)^{-1}
=
\sum_{s\in\langle P\rangle}T_s,
\tag{41}
\]

where `\langle P\rangle` is the multiplicative semigroup generated by `P`. Since

\[
\sum_{s\in\langle P\rangle}\frac1s
=
\prod_{p\in P}(1-p^{-1})^{-1}<\infty,
\tag{42}
\]

(28), (33), and (41) give the zero-boundary estimate

\[
|z_d|
\ll_P \frac{t}{d}+(1+\log R)^{|P|}.
\tag{43}
\]

The actual `0/1` boundary changes this by at most another `O_P((1+log R)^{|P|})`. One way to see this without a stability assumption is to extend the boundary correction by zero beyond `QR`, apply (40), and then invert with (41): only semigroup multiples in the fixed multiplicative annulus `R<sd<=QR` contribute, each with bounded finite-difference amplitude. Hence

\[
\boxed{
|z_d|
\ll_P \frac{t}{d}+(1+\log R)^{|P|}
\qquad(d\le R),
}
\tag{44}
\]

while `|z_d|<=1` for `R<d<=QR`.

Therefore the endpoint change across `I_d` is

\[
|z_d-z_{d+1}|
\ll_P
\frac{H^\gamma}{d}+(1+\log R)^{|P|}
\qquad(d\le R),
\tag{45}
\]

and is at most `1` when `R<d<QR`. By (25),

\[
\frac{H^\gamma/d}{H/d^2}
=
H^{\gamma-1}d
\le H^{\gamma-1}R=o(1),
\tag{46}
\]

and the polylogarithmic term is also negligible. Thus every endpoint change is realizable on the actual core points of `I_d`.

The bridge `(H_prev,q_{QR}]` is fresh by (32). Its core density is positive by (19), while the inherited endpoint is `O(H_prev^gamma)` and `gamma<1`, so it can first move the old value to the required parity-compatible `z_{QR} in {0,1}` and use balanced pairs for the remaining core points. Inductively, all core signs are assigned exactly once.

The bounded-overshoot ordering, (44), and `n asymp H/d` on `I_d` give

\[
|B(n)|\ll_{P,\gamma}n^\gamma.
\tag{47}
\]

Equation (14) then yields

\[
\boxed{
|A(n)|\ll_{P,\gamma}n^\gamma,
}
\tag{48}
\]

which implies (7).

## 4. The GCD energy sees the same equality ray

At a stage horizon `H`, embed `nu^(R)` into the first `R` coordinates of `\mathbb R^H` by zeros. Equations (33)--(34) give

\[
m^{(H)}=t\widetilde\nu+e,
\tag{49}
\]

where

\[
|e_d|\le1\quad(d\le R),
\qquad
|e_d|\ll_{P,\gamma}(H/d)^\gamma\quad(d>R).
\tag{50}
\]

The prefix rounding estimate from `FD-007`/`FD-026` gives

\[
\|e_{\le R}\|_{K_H}=O(\sqrt R).
\tag{51}
\]

The weighted GCD tail estimate of `FD-024`, valid for every `gamma>1/2`, gives

\[
\|e_{>R}\|_{K_H}^2
\ll_{P,\gamma}
H^{2\gamma}R^{1-2\gamma}.
\tag{52}
\]

Since `t asymp H^gamma` and `R->infinity`,

\[
\boxed{
\frac{\|e\|_{K_H}}{t}
\ll_{P,\gamma}
\frac{\sqrt R}{H^\gamma}
+
R^{1/2-\gamma}
\longrightarrow0.
}
\tag{53}
\]

The top-left block of `K_H` is `K_R`, so

\[
\|\widetilde\nu\|_{K_H}^2=C_R.
\tag{54}
\]

Also `A(H)=y_1=tC_R+O(1)`. Cauchy--Schwarz in the `K_H` inner product therefore gives

\[
E_H=t^2(C_R+o(1)),
\qquad
R_H=C_R+o(1)\longrightarrow Z.
\tag{55}
\]

This proves (8). Notice that the prime-sign relations are exact at every integer, not merely at the retained horizons; the only sparsity is in where the GCD-duality near-extremality is requested.

## 5. The all-`1/2+epsilon` diagonal survives as well

Fix `P` and suppose the core signs have been assigned through `H_*`. Put

\[
B_*:=\max_{n\le H_*}|B(n)|.
\tag{56}
\]

At stage `j`, choose a new horizon `H` so large that, with

\[
R:=\lfloor H^{1/5}\rfloor,
\qquad
L(H):=\exp(\sqrt{\log H}),
\tag{57}
\]

one has

\[
q_{QR}>H_*,
\qquad
L(H)\ge j(B_*+2).
\tag{58}
\]

Set

\[
t:=\frac{\sqrt H\,L(H)}{64Z^2}.
\tag{59}
\]

The same triangular parity construction applies. For `d<=R`, (44) now gives

\[
|z_d|
\ll_P \frac{\sqrt H\,L(H)}d+(1+\log H)^{|P|}.
\tag{60}
\]

All intervals through `QR` have `gg_P H/d^2` core points, and at the smallest relevant scale this is `gg_P H^(3/5)`. The required endpoint changes are `H^(1/2+o(1))`, so the sign assignments remain feasible.

For every tail coordinate `d>R`, the sampled source point satisfies

\[
\left\lfloor\frac Hd\right\rfloor\le q_{R+1}.
\tag{61}
\]

Between `q_{QR}` and `q_{R+1}`, the auxiliary endpoints from `R<d<=QR` are all `0/1`, and their interval signs may be ordered with unit overshoot. Below `q_{QR}`, the bridge and the inherited source are bounded by `B_*+2`. Therefore

\[
|B(x)|\le B_*+2
\qquad(x\le q_{R+1})
\tag{62}
\]

after enlarging the harmless constant once, and (14) gives

\[
|A(x)|\ll_P B_*+1
\qquad(x\le q_{R+1}).
\tag{63}
\]

Using the full-tail estimate `1^T K_H 1 << H` from `FD-026`,

\[
\|e_{>R}\|_{K_H}
\ll_P(B_*+1)\sqrt H.
\tag{64}
\]

Consequently

\[
\frac{\|e\|_{K_H}}t
\ll_P
\frac{B_*+1}{L(H)}
+
\frac{\sqrt R}{\sqrt H\,L(H)}
=
O_P(1/j)+o(1),
\tag{65}
\]

and the same equality-ray calculation gives `R_H->Z`.

Finally, on the planted region `d<=R`, every `n in I_d` satisfies `n gg H/d`, while (60) gives the pointwise bound

\[
|B(n)|
\ll_P
\sqrt n\,\exp(2\sqrt{\log n})
\tag{66}
\]

for all sufficiently large stages; the auxiliary region and bridge do not create larger excursions. Hence, by (14),

\[
\boxed{
|A(n)|
\ll_P
\sqrt n\,\exp(2\sqrt{\log n}).
}
\tag{67}
\]

Since `exp(2sqrt(log n))=O_epsilon(n^epsilon)` for every `epsilon>0`, equation (9) follows.

## 6. Prior-art boundary, stress tests, and consequence

The fixed-prime relation (6) is a genuine fragment of Möbius multiplicativity, not a new arithmetic identity. The neighboring literature on squarefree-supported multiplicative signs is substantially stronger in a different direction. Marco Aymone, *A note on multiplicative functions resembling the Möbius function*, J. Number Theory **212** (2020), 113--121, constructs multiplicative squarefree-supported functions with small partial sums. Aymone, *The Erdős discrepancy problem over the squarefree and cubefree integers*, Mathematika **68** (2022), 51--73, DOI `10.1112/mtk.12117`, studies `mu^2 g` with `g` completely multiplicative and proves unboundedness phenomena. Those hypotheses couple all prime directions. The present construction deliberately keeps only an arbitrary **fixed finite** set of exact prime relations and asks a different Farey--Mertens GCD-extremal question. These papers are prior-art boundaries, not inputs to the proof, so no new load-bearing source entry is required in `SOURCES.md`.

The main internal checks are exact. Equation (16) prevents a floor-rounding error from entering the prime-dilation identities. Equation (38) proves that the triangular target system has the parity of actual core signs, rather than only a real solution. The core density (19) is positive for every fixed `P`; the constants may deteriorate with `P`, which is precisely why no growing-prime statement is claimed. The energy estimate uses the complete inherited tail, not just the planted coordinates.

There is no conflict with `FD-015`: that finding says a common source cannot nearly saturate at both `H` and certain fixed squarefree dilates `qH`. The source constructed here is required to saturate only the prescribed supermultiplicatively separated horizons; it makes no claim that `pH_j` is also a saturating horizon. Likewise, (9) does not prove an endpoint `O(sqrt n)` bound and does not identify the synthetic source with Möbius.

A falsification of this result would require a failure of one of four explicit mechanisms: the core decomposition/parity identities (14),(38); the triangular endpoint inversion (37); the capacity estimate (25),(45); or the inherited-tail estimate (52)/(64). A theorem using a number of prime relations that grows with the horizon lies outside the claim and is not obstructed here.

The durable boundary is therefore sharper than `FD-026`:

\[
\boxed{
\text{fixed finite prime breadth}
\quad\text{does not coerce a sparse GCD-duality deficit.}
}
\tag{68}
\]

The remaining cumulative route must exploit arithmetic compatibility whose breadth itself grows with scale, or a genuinely global divisor or multiplicative law. This narrows where Möbius-specific rigidity can first enter without pretending that the obstruction itself advances RH.
