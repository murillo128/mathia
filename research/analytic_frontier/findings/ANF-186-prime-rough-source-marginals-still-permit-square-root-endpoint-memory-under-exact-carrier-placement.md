# ANF-186 — Prime–rough source marginals still permit square-root endpoint memory under exact-carrier placement

**Status:** `EXACT-DERIVED + SOURCE-ALPHABET-MATCHED-CONTROL + CARRIER-EQUIDISTRIBUTION + MEAN-DIAGONAL-MATCH + ENDPOINT-MEMORY + ARITHMETIC-PLACEMENT-GATE`. `ANF-175` showed that prime-sized atoms at prime-sized density can load the critical endpoint charge on physical width `Theta(sqrt(X log X))`, but that control used only one sign. `ANF-185` then replaced adaptive twist probing by a deterministic critical high-pass and left the actual prime-minus-Ramanujan placement law as the live source gate. The one-point sign law itself does not close that gate.

Let

\[
K=X^{1-2\varepsilon+o(1)},
\qquad 0<\varepsilon<\frac1{16},
\qquad A_0X^2\le U\le B_0X^2,
\]

and keep the Cramér--Granville cutoff

\[
R=\exp((\log X)^{1/10}),
\qquad
B_X:=\frac{P(R)}{\varphi(P(R))},
\qquad
A_X:=\log X-B_X.
\]

The physical residual `r_X=vartheta-Q_R` from `ANF-149` has the two principal coefficient sizes

\[
+A_X\quad\text{on bulk primes},
\qquad
-B_X\quad\text{on }R\text{-rough composites},
\]

up to the negligible variation of `log n` across a square-root block. Since `B_X=(e^\gamma+o(1))\log R`, one has

\[
B_X\to\infty,
\qquad
B_X=o(\log X),
\qquad
A_X=(1-o(1))\log X.
\]

The natural one-point densities that balance these two amplitudes are

\[
d_+:=\frac1{\log X},
\qquad
d_-:=\frac{A_X}{B_X\log X}
=\frac1{B_X}-\frac1{\log X}.
\]

They satisfy the exact identities

\[
A_Xd_+-B_Xd_-=0,
\tag{1}
\]

and

\[
A_X^2d_+ + B_X^2d_-
=A_X
=(1-o(1))\log X.
\tag{2}
\]

Thus they simultaneously encode zero first moment and the correct `asymp log X` diagonal scale.

The new result is that these stronger source marginals are still compatible with the dangerous endpoint mechanism. There exists a deterministic matched control supported in an initial block of length

\[
L_X=\Theta(a_X),
\qquad
a_X:=\sqrt{\delta X\log X},
\]

whose nonzero coefficients use exactly the two source-sized signs `+A_X` and `-B_X` up to the harmless `log(X+j)-log X=o(1)` variation, whose positive and negative densities are `(1+o(1))d_+` and `(1+o(1))d_-`, whose untwisted first moment is `o(L_X)`, whose second moment is `(1+o(1))L_X log X`, and whose local absolute-mass envelope is `O(H+log X)` on every interval of length `H`. Nevertheless its exact distinguished-twist endpoint charge has magnitude `>=a_X`, persists for `Theta(K)` prefixes, and produces bow-scale completion with negligible diagonal.

The only freedom the construction still abuses is decisive: **it places the two source signs after reading the exact logarithmic carrier**. Hence matching the source alphabet, sign densities, mean balance, diagonal variance and local total variation does not solve the bow gate. A successful theorem must constrain the joint arithmetic placement of prime/rough signs relative to the distinguished carrier, or control the deterministic high-pass / signed Fejér statistic directly.

## 1. The two-sign marginal law matches the source mean and diagonal exactly

Recall from `ANF-149` that after discarding prime powers at the bow target scale one may work with

\[
r_X(n)=\vartheta(n)-Q_R(n),
\qquad
Q_R(n)=B_X1_{(n,P(R))=1}.
\tag{3}
\]

For `n=X+j` with `0\le j=O(a_X)`,

\[
\log(X+j)=\log X+O(a_X/X)=\log X+o(1).
\tag{4}
\]

Thus a prime contributes

\[
\log(X+j)-B_X=A_X+o(1),
\tag{5}
\]

whereas an `R`-rough composite contributes `-B_X`. The density `d_-` above is exactly the residual rough density obtained by subtracting the prime density scale from the rough density scale:

\[
\frac1{B_X}-\frac1{\log X}
=\frac{A_X}{B_X\log X}.
\tag{6}
\]

Equations (1)--(2) are therefore not arbitrary moment matching. They are the two-sign one-point law naturally suggested by the prime-versus-rough normal form itself. The construction below realizes these rates on the critical loading block while aligning both signs in one distinguished-twist sector.

## 2. The exact logarithmic carrier equidistributes on every relevant sparse progression

The construction needs one deterministic input that was not used in `ANF-175`: on a block of length `Theta(a_X)`, the exact carrier already visits any fixed angular sector with the expected density along every arithmetic progression whose step is at most logarithmic.

Fix a residue `r`, an integer step `1\le q\le\log X`, and a block length

\[
L\asymp a_X.
\tag{7}
\]

For

\[
0\le m<N,
\qquad
N=\frac{L}{q}+O(1),
\]

put

\[
v_m:=\left(1+\frac{r+qm}{X}\right)^{-iU}.
\tag{8}
\]

Then for every fixed nonzero integer `h`,

\[
\boxed{
\frac1N\sum_{m<N}v_m^h=o(1)
}
\tag{9}
\]

uniformly for `U` in the bow window and for the progression steps used below. Consequently the `v_m` are equidistributed on the unit circle in the triangular-array sense; every fixed arc `I` satisfies

\[
\#\{m<N:v_m\in I\}
=\left(\frac{|I|}{2\pi}+o(1)\right)N.
\tag{10}
\]

To verify (9), write

\[
f(m):=-\frac{hU}{2\pi}
\log\left(1+\frac{r+qm}{X}\right),
\qquad
v_m^h=e(f(m)).
\tag{11}
\]

Since `L=o(X)` and `U\asymp X^2`, its third derivative has fixed sign and satisfies

\[
|f'''(m)|\asymp_h\frac{q^3}{X}
\tag{12}
\]

throughout the block. The classical third-derivative van der Corput estimate, in normalized form, gives when `lambda\asymp Lambda\asymp_h q^3/X`

\[
\frac1N\left|\sum_{m<N}e(f(m))\right|
\ll_h
N^{-1/4}
+\left(\frac{q^3}{X}\right)^{1/6}
+\left(\frac{q^3N^3}{X}\right)^{-1/4}.
\tag{13}
\]

Here

\[
N\asymp\frac{\sqrt{X\log X}}{q},
\]

so, uniformly for `q\le\log X`,

\[
N^{-1/4}=o(1),
\qquad
\left(\frac{q^3}{X}\right)^{1/6}
\le X^{-1/6}(\log X)^{1/2}=o(1),
\tag{14}
\]

and the cancellation in the third term is especially revealing:

\[
\frac{q^3N^3}{X}
\asymp
\frac{L^3}{X}
\asymp
X^{1/2}(\log X)^{3/2}
\longrightarrow\infty.
\tag{15}
\]

Thus (9) follows. Approximation of a fixed arc indicator by upper and lower trigonometric polynomials then gives (10). No Diophantine condition on `U` is required; the cubic variation of the exact logarithmic phase is already large enough across the critical block.

This scale calculation is also useful conceptually: the carrier can be resonant at lower Taylor orders, but on physical width `sqrt(X log X)` its third-order drift is unavoidably macroscopic after summation. That does not itself cancel the endpoint charge, because the source signs can still be placed according to the phase, as the next section shows.

## 3. Two disjoint progressions realize the prime and rough sign densities

Fix once and for all the sector

\[
\mathcal S_+
:=\{e^{i\theta}:|\theta|\le\pi/6\},
\qquad
\mathcal S_-:=-\mathcal S_+.
\tag{16}
\]

Choose even progression steps

\[
q_+
:=2\left\lceil\frac{\log X}{12}\right\rceil,
\tag{17}
\]

and

\[
q_-
:=2\left\lceil
\frac{B_X\log X}{12A_X}
\right\rceil.
\tag{18}
\]

Because `B_X\to\infty` and `B_X=o(log X)`, both satisfy

\[
q_+\to\infty,
\qquad
q_-\to\infty,
\qquad
q_\pm\le\log X
\tag{19}
\]

for all sufficiently large `X`. Use the disjoint candidate progressions

\[
\mathcal P_+:=q_+\mathbb Z_{\ge0},
\qquad
\mathcal P_-:=1+q_-\mathbb Z_{\ge0};
\tag{20}
\]

parity makes them disjoint.

Take the loading interval `0\le j\le L` with

\[
L:=a_X.
\tag{21}
\]

On `\mathcal P_+`, retain exactly those candidates whose normalized carrier

\[
v_j:=\left(1+\frac jX\right)^{-iU}
\tag{22}
\]

lies in `\mathcal S_+`. On `\mathcal P_-`, retain exactly those candidates with `v_j\in\mathcal S_-`. By (10), the retained counts satisfy

\[
N_+
=(1+o(1))\frac{L}{6q_+}
=(1+o(1))\frac{L}{\log X},
\tag{23}
\]

and

\[
N_-
=(1+o(1))\frac{L}{6q_-}
=(1+o(1))\frac{LA_X}{B_X\log X}.
\tag{24}
\]

Define real source amplitudes

\[
c_j:=
\begin{cases}
\log(X+j)-B_X,
&j\in\mathcal P_+,\ v_j\in\mathcal S_+,\\
-B_X,
&j\in\mathcal P_-,\ v_j\in\mathcal S_-,\\
0,&\text{otherwise},
\end{cases}
\tag{25}
\]

for `0\le j\le L`, and put `c_j=0` for `L<j<K`.

The nonzero alphabet in (25) is exactly the prime/rough sign-and-amplitude alphabet of (3), apart from the fact that **the selected sites are not required to be actual primes or actual rough composites**. That distinction is the point of the matched control: we are testing whether the one-point source law alone can rule out endpoint memory.

## 4. The control has zero mean, the correct diagonal scale, and prime-scale local mass

From (4), (23) and (24),

\[
\sum_{j\le L}c_j
=A_XN_+-B_XN_-+o(L)
=o(L).
\tag{26}
\]

Thus the two signs are asymptotically balanced even before inserting the distinguished twist.

The absolute mass is

\[
\begin{aligned}
\sum_{j\le L}|c_j|
&=A_XN_+ + B_XN_- +o(L)\\
&=(2+o(1))\frac{A_X}{\log X}L\\
&=(2+o(1))L.
\end{aligned}
\tag{27}
\]

The square mass is

\[
\begin{aligned}
\sum_{j\le L}|c_j|^2
&=A_X^2N_+ + B_X^2N_- +o(L\log X)\\
&=(1+o(1))L
\left(
\frac{A_X^2}{\log X}
+\frac{A_XB_X}{\log X}
\right)\\
&=(1+o(1))LA_X\\
&=(1+o(1))L\log X.
\end{aligned}
\tag{28}
\]

So the control simultaneously has vanishing first moment at scale `L` and the same leading one-point second-moment scale that feeds the bow diagonal.

It also preserves the local marginal envelope of `ANF-175`. Any interval `J` of offset length `H` meets at most `H/q_++1` positive candidates and `H/q_-+1` negative candidates. Hence

\[
\sum_{j\in J}|c_j|
\ll
A_X\left(\frac{H}{q_+}+1\right)
+B_X\left(\frac{H}{q_-}+1\right)
\ll H+\log X.
\tag{29}
\]

Thus neither large local mass, wrong sign balance nor an inflated diagonal is responsible for what follows.

## 5. The exact twist rotates both source signs into one sector and stores critical charge

Let

\[
b_j:=c_j\left(1+\frac jX\right)^{-iU}=c_jv_j.
\tag{30}
\]

For every positive selected site, `b_j` lies in `\mathcal S_+`. For every negative selected site, `v_j\in\mathcal S_-`, so multiplication by the negative coefficient rotates the contribution by `pi`; again `b_j` lies in `\mathcal S_+`.

Therefore all nonzero twisted contributions have real projection at least `cos(pi/6)=sqrt(3)/2` times their absolute value. The terminal loading charge

\[
Q_X:=\sum_{j\le L}b_j
\tag{31}
\]

satisfies, by (27),

\[
\begin{aligned}
\operatorname{Re}Q_X
&\ge\frac{\sqrt3}{2}
\sum_{j\le L}|c_j|\\
&=(\sqrt3+o(1))L.
\end{aligned}
\tag{32}
\]

With `L=a_X`, this gives for all sufficiently large `X`

\[
\boxed{|Q_X|\ge a_X.}
\tag{33}
\]

Because all later coefficients vanish, every prefix after `L` remembers the same charge. Since

\[
\frac{L}{K}
=\frac{a_X}{K}
\longrightarrow0,
\tag{34}
\]

the left endpoint completion obeys

\[
\boxed{
E_-(b)
:=\sum_{r<K}\left|\sum_{j\le r}b_j\right|^2
\ge(K-L)|Q_X|^2
\gg XK\log X.
}
\tag{35}
\]

The associated diagonal is negligible. From (28),

\[
\Delta_-(b)
\le K\sum_{j<K}|b_j|^2
\ll K a_X\log X
=o(XK\log X).
\tag{36}
\]

Hence the completion is again genuinely off-diagonal and forces the same kind of target-sized dyadic / Fejér scale-slope defect as in `ANF-169`--`ANF-172`.

## 6. Long-range uniformity still cannot see the source-balanced packet

Equation (27) gives a global `l^1` bound

\[
\sum_{j<K}|b_j|=O(a_X).
\tag{37}
\]

Therefore, for every interval `I` and every bounded complex test `|F(j)|\le1`,

\[
\left|\sum_{j\in I}b_jF(j)\right|
\le O(a_X).
\tag{38}
\]

In particular, throughout the current all-interval range

\[
H\ge X^{5/8+\eta},
\]

and for every fixed `A>0`,

\[
\frac{a_X}{H(\log X)^{-A}}
\ll
X^{-1/8-\eta}(\log X)^{A+1/2}
\longrightarrow0.
\tag{39}
\]

Thus the stronger two-sign matched control remains invisible to every bounded-test estimate of size `H log^{-A}X` in the presently available range. Adding source-like mean cancellation and the correct diagonal therefore does not repair the information mismatch isolated in `ANF-175`--`ANF-176`.

There is no contradiction with `ANF-185`. Its deterministic critical high-pass is designed precisely to expose an endpoint-memory packet once the physical transition scale reaches `a_X`; the present construction shows that **one-point source marginals do not imply that the actual arithmetic residual makes that high-pass small**. The remaining task is still to prove such smallness from joint source placement, or to attack the signed Fejér defect directly.

## 7. Evidence boundary and prior-art audit

The carrier-equidistribution input is classical harmonic analysis. A directed prior-art audit found the standard van der Corput derivative-test literature, including modern explicit `d`-th derivative bounds that cover the `d=3` estimate used in (13), as well as the usual Weyl-equidistribution consequence. The Mathia-specific content is not the derivative test. It is the coupling of that deterministic exact-log carrier equidistribution with the prime-minus-Ramanujan two-sign marginal law (1)--(2), producing a control that simultaneously matches source-sized amplitudes, sign densities, mean balance, diagonal scale and local mass while retaining critical endpoint memory.

No external source theorem about primes or rough numbers in `Theta(sqrt(X log X))` intervals is used. In particular, the finding **does not** claim that the actual source can realize (25). The selected positive sites need not be primes and the selected negative sites need not be rough composites; after the loading block the synthetic control is set to zero. These are exactly the freedoms that remain unavailable to the physical source.

Consequently the result is a no-go statement about information content, not a construction of a physical counterexample. Source alphabet, one-point sign density, zero mean, diagonal variance, local total variation, fixed-order uniformity and current long-interval discorrelation can all coexist with bow-scale endpoint memory. What must now be imported is a law tying **where** the prime and rough contributions occur to the exact carrier (or an equivalent nonlocal statistic), not another marginal constraint on their individual sizes.