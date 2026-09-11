# MC-228 — The first-shell selected residues contain a polynomial CRT common mode with a `c=1/4` separate-control boundary

**Status:** `EXACT-DERIVED`, `FRONTIER-REFINEMENT`, `NEGATIVE/OBSTRUCTION`, `MATCHED-CONTROL`, `CLASSICAL-MECHANISM`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Continue with the active first square-defect shell from `MC-221`--`MC-227`. Fix

\[
0<c<\frac12,
\qquad
y=c\log X,
\qquad
P=\prod_{p\le y}p,
\qquad
T=X-P,
\]

and let

\[
\mathcal D_y:=\{d:\ y<d\le2y,\ d\text{ prime}\}.
\]

For each `d\in\mathcal D_y`, write the rough source-selected support

\[
\mathcal R_d
:=
\{n\le T:(n,P)=1,\ n\equiv-P\pmod{d^2}\},
\tag{1}
\]

so that the first-shell Möbius coordinate is

\[
A_d(T)=\sum_{n\in\mathcal R_d}\mu(n).
\tag{2}
\]

Define the full-shell square product

\[
Q_y:=\prod_{d\in\mathcal D_y}d^2.
\tag{3}
\]

The source prescription in `(1)` forces a large deterministic overlap that is invisible if the square moduli are treated as unrelated averaging coordinates. For all sufficiently large `X`,

\[
\boxed{
\bigcap_{d\in\mathcal D_y}\mathcal R_d
=
\left\{
 kQ_y-P:
 1\le k\le\left\lfloor\frac X{Q_y}\right\rfloor,
\ (k,P)=1
\right\}.
}
\tag{4}
\]

The prime number theorem in Chebyshev-`theta` form gives

\[
\log P=\vartheta(y)=y+o(y),
\qquad
\log Q_y
=2(\vartheta(2y)-\vartheta(y))
=2y+o(y),
\tag{5}
\]

hence

\[
P=X^{c+o(1)},
\qquad
Q_y=X^{2c+o(1)},
\qquad
K_y:=\left\lfloor\frac X{Q_y}\right\rfloor
=X^{1-2c+o(1)}.
\tag{6}
\]

In particular `P<Q_y<X` for every fixed `0<c<1/2` and all sufficiently large `X`, so `(4)` contains polynomially many candidate inputs. Exact inclusion-exclusion in the `k`-variable and Mertens' product theorem give

\[
\boxed{
\left|\bigcap_{d\in\mathcal D_y}\mathcal R_d\right|
=
\left(e^{-\gamma}+o(1)\right)
\frac{X}{Q_y\log y}
=
\frac{X^{1-2c+o(1)}}{\log y}.
}
\tag{7}
\]

This is not merely an overlap of rough supports caused by square-full values. In the entire supercritical separate-control regime `0<c<1/4`, almost all points in `(4)` are square-free:

\[
\boxed{
\#\left\{
n\in\bigcap_{d\in\mathcal D_y}\mathcal R_d:
\mu^2(n)=1
\right\}
=
\left(e^{-\gamma}+o(1)\right)
\frac{X}{Q_y\log y}.
}
\tag{8}
\]

Thus the common mode contains `X^{1-2c+o(1)}` genuinely nonzero Möbius signs when `c<1/4`.

Now isolate their signed sum

\[
C_y(X)
:=
\sum_{n\in\cap_{d\in\mathcal D_y}\mathcal R_d}\mu(n).
\tag{9}
\]

Every shell coordinate has the exact decomposition

\[
A_d(T)=C_y(X)+B_d(X),
\tag{10}
\]

where `B_d` sums the points of `\mathcal R_d` outside the full-shell intersection. Let

\[
H_y:=\sum_{d\in\mathcal D_y}d.
\tag{11}
\]

The prime number theorem gives

\[
H_y=\left(\frac32+o(1)\right)\frac{y^2}{\log y}=X^{o(1)}.
\tag{12}
\]

If a proof controls the common component separately, its contribution to the weighted shell norm is

\[
H_y|C_y|^2.
\tag{13}
\]

The support-only estimate from `(7)` yields

\[
\boxed{
H_y|C_y|^2
\le
X^{2-4c+o(1)}.
}
\tag{14}
\]

Therefore the full-shell common mode has a sharp **power-budget transition at `c=1/4`** for separate control:

\[
\boxed{
c\ge\frac14
\quad\Longrightarrow\quad
H_y|C_y|^2\le X^{1+o(1)}
\text{ trivially from support size.}
}
\tag{15}
\]

For `0<c<1/4`, the same support-only route is super-diagonal by the fixed power `X^{1-4c+o(1)}`. Using `(8)`, this cannot be blamed on most common points having Möbius value zero. To place the common component itself at the target scale one would need

\[
|C_y(X)|\le X^{1/2+o(1)},
\tag{16}
\]

or, relative to the nonzero common population,

\[
\frac{|C_y(X)|}
{\#\{n\in\cap_d\mathcal R_d:\mu^2(n)=1\}}
\le
X^{-1/2+2c+o(1)}.
\tag{17}
\]

This does **not** prove that `(16)` is necessary for the full energy

\[
W_y(X)=\sum_{d\in\mathcal D_y}d|A_d(T)|^2,
\]

because the residual terms `B_d` in `(10)` may anti-align with the common component. The exact conclusion is narrower: a proof that takes absolute values, orthogonalizes supports, or estimates the CRT-common block independently pays the phase boundary `(14)`. Below `c=1/4`, avoiding signed cancellation in `C_y` requires using coherent interference between the common block and the residual source geometry.

This identifies an explicit piece of the source coupling that `MC-224`--`MC-227` said generic norm and fiberwise estimates erase. The square moduli are not merely a sparse family of unrelated progression tests: the distinguished residues selected by `n+P=d^2m` share one polynomial-size arithmetic progression across **every** modulus in the first shell.

No estimate `(16)`, no improvement of `W_y`, no improved Mertens bound, and no consequence for the zeta zero set is proved here.

## 1. Exact CRT description of the common source block

The moduli `d^2`, `d\in\mathcal D_y`, are pairwise coprime. If `n` belongs to every `\mathcal R_d`, then

\[
n\equiv-P\pmod{d^2}
\qquad(d\in\mathcal D_y).
\]

By the Chinese remainder theorem this is equivalent to

\[
n\equiv-P\pmod{Q_y}.
\tag{18}
\]

Hence

\[
n=kQ_y-P
\tag{19}
\]

for some integer `k`. Since `n\le T=X-P`, equation `(19)` gives exactly

\[
1\le k\le K_y=\left\lfloor\frac X{Q_y}\right\rfloor
\tag{20}
\]

once `Q_y>P`, which follows from `(5)`.

The primorial roughness condition also transfers exactly. Every prime factor of `P` is at most `y`, while every prime factor of `Q_y` lies in `(y,2y]`; therefore

\[
(Q_y,P)=1.
\tag{21}
\]

Reducing `(19)` modulo any prime `p\mid P` gives

\[
n\equiv kQ_y\pmod p.
\]

Since `Q_y` is a unit modulo `p`,

\[
(n,P)=1
\iff
(k,P)=1.
\tag{22}
\]

Equations `(18)`--`(22)` prove the exact set identity `(4)`. The overlap is therefore forced by the original lifted source relation rather than by an averaging inequality or a probabilistic collision calculation.

## 2. The common rough support has polynomial cardinality

Using `(4)`, inclusion-exclusion over the square-free divisors of the primorial gives

\[
\#\{k\le K_y:(k,P)=1\}
=
\sum_{r\mid P}\mu(r)\left\lfloor\frac{K_y}{r}\right\rfloor
=
K_y\frac{\varphi(P)}P+O(\tau(P)).
\tag{23}
\]

At `y=c\log X`,

\[
\tau(P)=2^{\pi(y)}=X^{o(1)},
\tag{24}
\]

whereas `K_y=X^{1-2c+o(1)}` has a fixed positive power for every `c<1/2`. Mertens' product theorem gives

\[
\frac{\varphi(P)}P
=
\prod_{p\le y}\left(1-\frac1p\right)
\sim\frac{e^{-\gamma}}{\log y}.
\tag{25}
\]

Substitution into `(23)` proves `(7)`.

The product scale `(6)` is equally elementary. Writing `\vartheta(x)=\sum_{p\le x}\log p`, one has

\[
\log Q_y
=2\sum_{y<d\le2y\atop d\text{ prime}}\log d
=2(\vartheta(2y)-\vartheta(y)),
\]

and the prime number theorem `\vartheta(x)\sim x` gives `(5)`--`(6)`.

## 3. Below `c=1/4`, almost every common rough point is square-free

Let

\[
n_k=kQ_y-P,
\qquad
1\le k\le K_y,
\qquad
(k,P)=1.
\]

If `n_k` is not square-free, then `p^2\mid n_k` for some prime `p>y`, because `(n_k,P)=1`. A shell prime `p\in\mathcal D_y` is impossible: by construction

\[
n_k\equiv-P\not\equiv0\pmod p.
\tag{26}
\]

For every remaining prime `p>y`, one has `(p,Q_y)=1`, so

\[
kQ_y\equiv P\pmod{p^2}
\tag{27}
\]

selects exactly one residue class of `k` modulo `p^2`. Therefore the number of common rough points with a square prime divisor is at most

\[
\sum_{y<p\le\sqrt X\atop p\notin\mathcal D_y}
\left(\frac{K_y}{p^2}+1\right)
\ll
\frac{K_y}{y}+\frac{\sqrt X}{\log X}.
\tag{28}
\]

For every fixed `c<1/4`,

\[
K_y=X^{1-2c+o(1)}=X^{1/2+\delta+o(1)}
\]

for some fixed `\delta>0`. Both terms in `(28)` are therefore

\[
o\!\left(\frac{K_y}{\log y}\right).
\tag{29}
\]

Combining `(7)`, `(28)` and `(29)` proves `(8)`.

The endpoint `c=1/4` is deliberately excluded from `(8)`: the elementary `+1` sum in `(28)` is too crude to give the same uniform asymptotic from only `Q_y=X^{1/2+o(1)}`. This does not affect the energy boundary `(15)`, which uses the rough support only and remains valid at `c=1/4`.

## 4. Separate-control energy has a `c=1/4` transition

Partial summation with the prime number theorem gives `(12)`. Since `|\mu(n)|\le1`, equation `(7)` implies

\[
|C_y(X)|
\le
\left|\bigcap_d\mathcal R_d\right|
=X^{1-2c+o(1)}.
\tag{30}
\]

Multiplying the square of `(30)` by `H_y=X^{o(1)}` proves `(14)`. The exponent equals `1` exactly when

\[
2-4c=1,
\]

that is `c=1/4`, proving `(15)`.

For `c<1/4`, `(8)` says the common block contains the same first-order number of nonzero signs as rough points. If the common component is estimated separately, the diagonal shell target asks for `(16)`, and division by `(8)` gives `(17)`.

There is a useful matched-control calibration. Give every rational prime an independent Rademacher sign `\xi_p` and define on square-free integers

\[
f_\xi(n)=\mu^2(n)\prod_{p\mid n}\xi_p.
\tag{31}
\]

For distinct square-free integers, the corresponding prime-support characters are orthogonal. Hence for the common sum

\[
C_y^\xi
:=
\sum_{n\in\cap_d\mathcal R_d}f_\xi(n),
\]

one has exactly

\[
\mathbb E_\xi|C_y^\xi|^2
=
\#\{n\in\cap_d\mathcal R_d:\mu^2(n)=1\}.
\tag{32}
\]

When `c<1/4`, `(8)` therefore gives

\[
H_y\,\mathbb E|C_y^\xi|^2
=X^{1-2c+o(1)},
\tag{33}
\]

comfortably below the target `X^{1+o(1)}`. The common-incidence geometry itself is thus not a probabilistic power obstruction. The unresolved issue is deterministic parity coherence at the all-minus Möbius prime-sign point, or cancellation of that common point against the residual vectors in `(10)`.

## 5. Relation to the current first-shell frontier

`MC-216` proves that the selected residues `-P mod d^2` form a coherent inverse-limit point and that their explicit Dirichlet-character phases can be removed by one global unit-group gauge. The present result concerns structure that survives that gauge: **the integer lifts of those coherent residues have a literal simultaneous intersection of polynomial size.** It is therefore not a contradiction to the gauge no-go; it is an example of the non-equivariant integer-incidence information that `MC-216` left alive.

`MC-224` shows that coefficient-uniform square-modulus large sieve estimates forget the source-selected direction and remain one full power above the first-shell target. `MC-227` shows that Möbius-specific BDH, even with arbitrary fixed logarithmic saving, still loses the power budget when the smooth-semigroup fibers are estimated independently. Equation `(4)` now identifies one exact cross-modulus coupling that those norm interfaces do not record: a polynomial family of integer inputs is copied with the same Möbius sign into every shell coordinate.

This also separates the present `c=1/4` boundary from the `c=1/3` boundary in `MC-212`. The latter is a Mertens-completeness threshold for **scale-uniform separate control of the principal character energy**. The present threshold is only the support budget for the **full-shell CRT common block**. In particular, throughout the nonempty window

\[
\frac14\le c\le\frac13,
\tag{34}
\]

the full-shell common block is already harmless at target power by the trivial estimate `(15)`, while `MC-212` says a scale-uniform diagonal bound for the principal energy would still be RH-level information. Hence the hard principal/transverse obstruction cannot be explained solely by this all-moduli common support.

The remaining source-coupled target is correspondingly sharper. A useful argument must control partially shared incidence, deterministic parity, or principal/residual anti-alignment beyond the single CRT-common block; simply observing that the selected moduli have common integer lifts is not enough.

## 6. Prior art and novelty boundary

The Chinese remainder theorem, the prime number theorem, Mertens' product theorem, and the elementary square-divisor union bound in `(28)` are classical. No novelty is claimed for any of these ingredients or for the fact that compatible congruences combine into one progression.

Recent and classical large-sieve work for square moduli studies spacing, exponential sums, modular square roots, additive energies, and coefficient-uniform family norms. That literature is an important prior-art boundary for `MC-224`, but it does not change the elementary identity `(4)`: the overlap here is created by the **same inhomogeneous source residue `-P` being imposed at every shell modulus**, not by an unexpectedly close pair of rational frequencies. A targeted search found no reason to promote the CRT mechanism itself as a new theorem.

The durable line-specific delta is the exact composition with the current first-shell scale: the full selected-modulus family collapses on one common progression of modulus `Q_y=X^{2c+o(1)}`, that progression contains polynomially many rough inputs and, for `c<1/4`, asymptotically the same number of square-free inputs, while its support-only separate-control energy crosses the diagonal power precisely at `c=1/4`.

## 7. Boundaries and falsification tests

- The exact identity `(4)` concerns the rough selected sets `\mathcal R_d`. The square-free asymptotic `(8)` is proved here only for fixed `c<1/4`; it must not be extrapolated to `c\ge1/4` from this argument.
- Equation `(14)` is an **upper budget for a separately controlled component**, not a lower bound for the actual shell energy. The residual `B_d` terms may cancel `C_y` strongly.
- The existence of a large common support does not imply large deterministic Möbius bias. The matched random multiplicative ensemble in `(32)`--`(33)` has the same support geometry and lies below the target power in mean square.
- The threshold `c=1/4` is specific to the full-shell common block and the weight `d` in `W_y`. It is not the principal-energy `c=1/3` threshold of `MC-212` and is not asserted to be an RH phase transition.
- The proof uses all prime root moduli in `(y,2y]`. A partial shell has a different product modulus and must be recalibrated from its own `\sum\log d`.
- `Q_y` is a modulus in the integer-lift description, not a new Euler product or zeta surrogate. No analytic continuation or zero-free region is imported.
- A future theorem may exploit the common block constructively rather than treat it as an error. This finding rules out only source-coupling arguments that implicitly assume the selected progression coordinates are independent or whose separate-control budget ignores the common CRT mode.

The exact claim is falsified if simultaneous membership in all `\mathcal R_d` is not equivalent to `(18)`--`(22)`. The scale claims are falsified if `\log Q_y\ne2y+o(y)`, the inclusion-exclusion error in `(23)` is not negligible for fixed `c<1/2`, or the square-full contamination bound `(28)` is not lower order than `(7)` for fixed `c<1/4`.

## Consequence for the live frontier

The first-shell source coupling is now more concrete. Besides the character-phase and semigroup-fiber descriptions, the selected residues possess a literal CRT common mode: `X^{1-2c+o(1)}` input locations feed every square-modulus coordinate simultaneously. For `c\ge1/4` this all-moduli overlap is harmless by cardinality alone; for `c<1/4` a separate-control proof needs fixed-power deterministic parity cancellation in the common progression or must preserve its interference with the residual coordinates.

The useful next question is therefore not whether the shell moduli overlap — they do, exactly and substantially — but whether **partially shared source blocks and their Möbius parity admit an orthogonal or martingale-like decomposition that gains power before absolute values are taken**. Any such decomposition must keep the integer lift `n+P=d^2m`; replacing it by generic square-modulus spacing returns to the obstruction already quantified in `MC-224` and `MC-227`.