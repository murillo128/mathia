# WI-098 — Sparse Loewner rank family extends to coprime composite moduli

**Status:** `EXACT-DERIVED + CLASSICAL-IDENTITY + LITERATURE+DERIVED + DECISIVE-NEGATIVE`. This finding does **not** change Mathia's current unconditional simple-critical zero proportion and does not certify or repair the Yang--Yang one-sided fourth-moment candidate. It resolves `CLUE-composite-sparse-loewner-rank-family`: the exact three-term Loewner--Bezout rank mechanism of WI-087 does not require prime moduli. Under the natural primitive-node dimension gate it extends to coprime composite moduli, and an infinite prime-cube subfamily retains the asymptotic one-third residual pairwise rank defect. Thus the macroscopic obstruction isolated in WI-087 is an exact-period/cyclotomic phenomenon rather than a prime-only accident.

Let `m<n<2m` be coprime positive integers satisfying

\[
m\equiv2\pmod 3,
\qquad
n\equiv1\pmod 3,
\tag{1}
\]

and define

\[
a=\frac{2m-n}{3},
\qquad
g=\frac{2n-m}{3},
\qquad
\beta=a+g=\frac{m+n}{3},
\qquad
\delta=\frac{mn+m-n}{3}.
\tag{2}
\]

Assume the primitive-frequency dimension gate

\[
\boxed{\beta\le\min\{\varphi(m),\varphi(n)\}.}
\tag{3}
\]

Then for every `N` with

\[
\operatorname{boundaryDefect}(m,n,N)=\delta,
\]

the finite-window Ramanujan cross Gram from WI-081 satisfies

\[
\boxed{
\operatorname{rank}G_{m,n}^{(N)}=\beta.
}
\tag{4}
\]

The condition is nonvacuous. Coprimality gives `lcm(m,n)=mn`, while

\[
2\delta<mn,
\tag{5}
\]

so already `N=delta` has boundary defect exactly `delta`. In particular

\[
(m,n)=(125,169)
\]

gives

\[
(a,g,\beta,\delta)=(27,71,98,7027),
\qquad
\varphi(125)=100,
\qquad
\varphi(169)=156,
\]

and therefore

\[
\boxed{
\operatorname{rank}G_{125,169}^{(7027)}=98.
}
\tag{6}
\]

More strongly, there are infinitely many coprime composite pairs of this type for which the residual WI-086 defect occupies asymptotically one third of the smaller primitive-frequency space. Choose primes `p<q` with

\[
p\equiv2\pmod3,
\qquad q\equiv1\pmod3,
\qquad q/p\to1,
\]

and set

\[
m=p^3,
\qquad n=q^3.
\tag{7}
\]

For all sufficiently large pairs, (1), `m<n<2m`, and (3) hold. Since

\[
\varphi(p^3)=p^2(p-1),
\]

WI-086 then gives, with `tau` its residual transversality defect,

\[
\frac{\operatorname{rank}G_{m,n}^{(\delta)}}{\varphi(m)}
=\frac{p^3+q^3}{3p^2(p-1)}\longrightarrow\frac23,
\tag{8}
\]

and

\[
\boxed{
\frac{\tau_{m,n}(\delta)}{\varphi(m)}
=1-\frac{p^3+q^3}{3p^2(p-1)}
\longrightarrow\frac13.
}
\tag{9}
\]

So the one-third pairwise obstruction persists along genuinely composite moduli whose primitive dimensions have asymptotic density one inside the modulus.

## 1. The arithmetic package survives with no prime hypothesis

The congruences in (1) make every quantity in (2) integral. Since `m<n<2m`,

\[
0<a<g,
\qquad
g-a=n-m,
\tag{10}
\]

and direct algebra gives

\[
a+\beta=m,
\qquad
\beta+g=n,
\qquad
2\beta=a+n.
\tag{11}
\]

For

\[
P(X)=1+X^a+X^{a+g},
\qquad
Q(X)=1+X^g+X^{a+g},
\tag{12}
\]

these identities imply exactly

\[
\boxed{P(X)-X^aQ(X)=1-X^m,}
\tag{13}
\]

\[
\boxed{P(X)-X^\beta Q(X)=(1+X^a)(1-X^n).}
\tag{14}
\]

The boundary exponent also has the exact decompositions

\[
\delta-a=m\frac{n-1}{3},
\qquad
\delta-\beta=n\frac{m-2}{3}.
\tag{15}
\]

Thus for every primitive `m`-th root `z` and primitive `n`-th root `w`,

\[
z^\delta=z^a,
\qquad
w^\delta=w^\beta.
\tag{16}
\]

Equations (13)--(16) are the complete arithmetic input needed for the same rational interpolation used in WI-087. No primality has entered.

## 2. Denominator regularity only uses exact order

WI-087's prose used the convenient prime-order observation that a three-term unit-modulus zero would force nontrivial cube roots of unity. The Lean formalization already exposes the stronger mechanism in the generic helper `wi087_Q_ne_zero_of_primitive`.

Suppose first that `z` is primitive of exact order `m`. Equation (13) gives

\[
P(z)=z^aQ(z).
\]

If `Q(z)=0`, then `P(z)=0`; subtracting the definitions in (12) gives

\[
z^a=z^g,
\]

hence

\[
z^{g-a}=1.
\]

But

\[
0<g-a=n-m<m
\tag{17}
\]

because `n<2m`, contradicting exact order `m`. Therefore `Q(z)\ne0`.

The identical argument at a primitive `n`-th root uses (14) and

\[
0<g-a=n-m<n
\]

to give `Q(w)\ne0`. Consequently the reduced rational function

\[
R(X)=\frac{P(X)}{Q(X)}
\]

is regular on both primitive node sets and satisfies

\[
\boxed{
R(z)=z^\delta,
\qquad
R(w)=w^\delta.
}
\tag{18}
\]

This is the decisive removal of the apparent prime-only step. The argument needs exact order, not prime order.

## 3. The sparse coefficient matrix is automatically invertible in this residue class

From (10) and (1),

\[
g-a=n-m\equiv2\pmod3.
\tag{19}
\]

Hence `3` does not divide `g-a`. The generic theorem already proved inside `WI081PairwiseRamanujanRank.lean`,

`wi087_coefficientMatrix_mulVec_injective`,

applies to the `beta x beta` coefficient matrix associated with (12) and shows that it is injective. Equivalently, the matrix is nonsingular.

WI-097 gives the exact algebraic classification behind this sufficient gate. If

\[
h=\gcd(a,g-a),
\qquad
L=\frac{g-a}{h},
\]

then the sparse Bezoutian is singular exactly when `3|L`, with nullity `2h`. Since (19) already gives `3\nmid(g-a)`, one necessarily has `3\nmid L`; the present composite family lies on the nonsingular side of the complete WI-097 classification.

Thus there is no hidden composite common-factor phenomenon in this residue package.

## 4. Primitive-node count, not primality, is the remaining rank gate

The primitive `m`-th roots form a set of cardinality `phi(m)`, and similarly for `n`. The generic Vandermonde argument formalized in `WI081PairwiseRamanujanRank.lean` shows that evaluation on any `beta` distinct primitive nodes has full column rank whenever

\[
\beta\le\varphi(m)
\]

and likewise for `n`. This is exactly hypothesis (3).

For primitive node sets `Z_m,Z_n`, the short-boundary cross Gram at length `delta` is, up to invertible diagonal scales, the Loewner matrix

\[
L_{z,w}=\frac{z^\delta-w^\delta}{z-w}.
\tag{20}
\]

By (18), (20) is the rational Loewner matrix of `R=P/Q`. The same coefficient-matrix identity used in WI-087 factors it as

\[
L
=D_m^{-1}V_m B V_n^T D_n^{-1},
\tag{21}
\]

where `B` is the nonsingular `beta x beta` sparse coefficient/Bezout matrix, `V_m,V_n` are primitive-node power-evaluation matrices through degree `beta-1`, and `D_m,D_n` are nonzero diagonal denominator/scaling matrices.

Hypothesis (3) gives full column rank to both evaluation matrices. Therefore

\[
\operatorname{rank}L=\beta.
\tag{22}
\]

WI-081's generic nearest-LCM boundary factorization and shift-phase transport are already formulated for arbitrary distinct positive moduli, not just primes. They preserve rank and convert (22) into (4).

The assembled composite theorem (4) is an exact derivation from those persisted generic lemmas, but it is **not** labelled `FORMAL-CHECKED`: the repository Lean artifact currently packages the final WI-087 theorem only under prime hypotheses and has not yet exposed (4) as a single checked theorem.

## 5. Coprimality makes the target boundary canonical and the concrete witness exact

The conditional statement (4), once `boundaryDefect(m,n,N)=delta` is assumed, does not need coprimality in the Loewner rank calculation itself. Coprimality matters for the canonical realization of that boundary.

Indeed,

\[
\gcd(m,n)=1
\quad\Longrightarrow\quad
\operatorname{lcm}(m,n)=mn.
\]

Also

\[
2\delta<mn
\iff
2m-2n<mn,
\]

which is immediate because `m<n`. Hence `N=delta` lies strictly before the midpoint of one LCM period and has

\[
\operatorname{boundaryDefect}(m,n,\delta)=\delta.
\tag{23}
\]

For `(m,n)=(125,169)`, exact arithmetic gives

\[
a=27,
\quad g=71,
\quad\beta=98,
\quad\delta=7027,
\quad\operatorname{lcm}(125,169)=21125,
\]

and

\[
98\le100=\varphi(125),
\qquad
98\le156=\varphi(169).
\]

The sparse gate is also exact because `g-a=44\equiv2 (mod 3)`. Therefore every factor in (21) has the required rank and (6) follows without a numerical determinant or floating-point rank test.

## 6. Composite prime cubes retain the one-third residual defect

The prime number theorem in arithmetic progressions modulo `3` gives primes in both reduced residue classes inside arbitrarily short fixed relative intervals at sufficiently large scale. As in WI-087, choose sequences

\[
p_k\equiv2\pmod3,
\qquad
q_k\equiv1\pmod3,
\qquad
p_k<q_k,
\qquad
q_k/p_k\to1.
\tag{24}
\]

Set

\[
m_k=p_k^3,
\qquad
n_k=q_k^3.
\]

These are coprime composite moduli and preserve the same residues modulo `3`. Equation (24) gives

\[
\frac{n_k}{m_k}=\left(\frac{q_k}{p_k}\right)^3\to1,
\]

so `n_k<2m_k` eventually.

The dimension gate is also eventually automatic, because

\[
\frac{\beta_k}{\varphi(m_k)}
=\frac{1+(q_k/p_k)^3}{3(1-1/p_k)}\to\frac23,
\tag{25}
\]

and symmetrically

\[
\frac{\beta_k}{\varphi(n_k)}
=\frac{1+(p_k/q_k)^3}{3(1-1/q_k)}\to\frac23.
\tag{26}
\]

Thus (4) applies for all sufficiently large `k`. Moreover `delta_k` is of order `m_kn_k`, while both primitive dimensions are of order `m_k,n_k`; hence

\[
\delta_k>\max\{\varphi(m_k),\varphi(n_k)\}
\]

eventually, placing the family genuinely in WI-086's residual regime. Since `m_k<n_k` and `phi(p^3)=p^2(p-1)` is increasing with `p`, the smaller primitive dimension is `phi(m_k)`. WI-086 therefore gives

\[
\tau_{m_k,n_k}(\delta_k)
=\varphi(m_k)-\beta_k.
\]

Equations (25) and (9) follow. This proves that the asymptotic one-third defect is not tied to prime-dimensional spaces `p-1,q-1`; it survives in composite primitive-frequency spaces of asymptotic density one.

## 7. Prior art and novelty boundary

The load-bearing ingredients are classical or already persisted.

- P. P. Vaidyanathan, **Ramanujan Sums in the Context of Signal Processing—Part I: Fundamentals**, *IEEE Transactions on Signal Processing* 62 (2014), 4145--4157, DOI `10.1109/TSP.2014.2331617`, and Part II, 4158--4172, DOI `10.1109/TSP.2014.2331624`, provide classical general-modulus Ramanujan-subspace and primitive-period/Fourier context. They are already anchored in `research/weil_inertia/SOURCES.md`.
- WI-081 supplies the arbitrary-modulus nearest-LCM boundary factorization and generic primitive-node Vandermonde machinery; `research/weil_inertia/formalization/WI081PairwiseRamanujanRank.lean` kernel-checks those generic components.
- WI-086 supplies the arbitrary-modulus residual transversality invariant `tau` and its exact relation to pairwise rank.
- WI-087 supplies the special three-term Loewner--Bezout interpolation architecture and the prime family from which this clue arose. Its classical rational-interpolation/Bezoutian sources include Antoulas--Anderson and Barnett.
- WI-097 supplies the exact gcd/nullity classification for the sparse coefficient family, with Curgus--Dijksma as theorem-level Bezoutian prior art.

A targeted audit across Ramanujan subspaces, finite-window cross Grams, cyclotomic primitive-node Loewner matrices, sparse trinomial gcds and rational interpolation located these general ingredients but no direct statement of the composite family (1)--(4). That negative search is **not** a priority claim. The durable content here is the exact deduction from established algebra and the persisted Mathia factorization machinery.

## 8. Research consequence

The clue's proposed extension is true, but its main consequence is negative for the broader scalar pairwise-rank route.

The WI-087 defect mechanism is not a peculiarity of prime moduli. Its essential ingredients are:

\[
\boxed{
\text{exact primitive order}
+\text{sparse rational interpolation}
+\text{Bezout nonsingularity}
+\text{enough primitive nodes}.
}
\tag{27}
\]

Prime moduli merely make the dimension gate and the asymptotic packaging especially transparent. The prime-cube family shows that even after moving to composite moduli with nearly full primitive dimension, the residual pairwise rank defect can still occupy asymptotically one third of the smaller block.

This does **not** generalize the prime-specific resonance classifications of WI-088--WI-096 to arbitrary composites, and it does not reopen their scalar stopping rules. It instead strengthens the reason not to expect universal pairwise transversality from modulus compositeness. Any positive continuation relevant to the zeta problem still has to retain information absent from an isolated cross-Gram rank: source coefficients and signs, singular-value magnitude, simultaneous compatibility among several moduli, or source labels erased by the scalar quotient.
