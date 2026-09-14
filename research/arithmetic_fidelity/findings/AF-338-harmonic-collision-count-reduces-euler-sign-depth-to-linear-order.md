# AF-338 — harmonic collision counting reduces finite Euler sign depth from quadratic to linear order

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `FINITE-ORDER-POSITIVE-GATE`, `SOURCE-COMPLEXITY-GATE`, `QUANTITATIVE-RECOVERY`, `ARITHMETIC-TAIL`, `NO-NOVELTY-CLAIM`

## Claim

[[research/arithmetic_fidelity/findings/AF-337-deep-half-plane-harmonic-tail-restores-finite-euler-sign-regularity|AF-337]] proves that every fixed sign order of the full Euler-log sampling matrix is eventually recovered on escaping integer windows once the left sample depth satisfies

\[
\sigma>(h+1)\binom r2.
\]

That quadratic threshold is not intrinsic to the harmonic tail. It comes from bounding every non-first-harmonic generalized Vandermonde determinant by a constant and thereby discarding the fact that most of its source-column collisions are inherited from the first harmonic.

Keeping those collisions gives a much stronger uniform theorem.

Let

\[
E_s(q):=-\log(1-q^{-s})
       =\sum_{m\ge1}\frac{q^{-ms}}m,
\qquad s>0,
\]

fix

\[
r\ge1,\qquad h>0,\qquad A>1,
\]

and form

\[
M_{ij}=E_{\sigma+(i-1)h}(q_j),
\qquad i=1,\ldots,r,
\]

on any finite increasing integer set

\[
P\le q_1<\cdots<q_N\le AP.
\]

If

\[
\boxed{\sigma>r-1,}
\tag{1}
\]

then there exists

\[
P_0=P_0(r,h,A,\sigma)
\]

such that for every `P>=P_0`, the matrix `M` is strictly sign-regular through order `r` with checkerboard signature

\[
\boxed{\varepsilon_k=(-1)^{\binom k2}.}
\tag{2}
\]

More quantitatively, put

\[
\Delta:=\sigma-(r-1)>0.
\tag{3}
\]

For every `k x k` minor, every selected increasing row set `I`, and every selected increasing column set `J`, let `D_{I,J}` be the full-Euler determinant and `D^{(1)}_{I,J}` the determinant obtained by keeping only the first Dirichlet harmonic `q^{-s}` in every column. There is a constant

\[
C=C(r,h,A,\sigma)>0
\]

such that, uniformly over all such minors and all allowed integer source sets,

\[
\boxed{
\left|
\frac{D_{I,J}-D^{(1)}_{I,J}}
     {D^{(1)}_{I,J}}
\right|
\le C P^{-\Delta}
}
\tag{4}
\]

for all sufficiently large `P`.

Thus the full Euler-log matrix inherits the first-harmonic sign pattern once `P` is large, with a **linear** sufficient sampling-depth budget in the requested order:

\[
\boxed{
\text{sign order }r
\quad\Longrightarrow\quad
\sigma>r-1.
}
\tag{5}
\]

The dependence on the sample spacing `h` disappears from the exponent threshold. It remains only in the constants and in how large `P_0` must be.

As in AF-337, the theorem is not prime-specific: primes, composites, and mixed integer controls inside the same multiplicative window all satisfy it. Its value is therefore as a source-complexity transport theorem, not as a rational-prime discriminator by itself.

## Derivation

### 1. Normalize an arbitrary row minor against its first harmonic

Take a `k x k` minor with row indices

\[
1\le i_1<\cdots<i_k\le r
\]

and selected source norms

\[
P\le q_1<\cdots<q_k\le AP.
\]

Write

\[
\sigma_I:=\sigma+(i_1-1)h,
\qquad
n_a:=i_a-i_1,
\]

so

\[
0=n_1<n_2<\cdots<n_k\le r-1.
\tag{6}
\]

Set

\[
y_j:=q_j^{-h}.
\tag{7}
\]

The first-harmonic determinant is

\[
D^{(1)}_{I,J}
=
\left(\prod_{j=1}^k q_j^{-\sigma_I}\right)
A_n(y),
\tag{8}
\]

where

\[
A_n(y):=\det[y_j^{n_a}]_{a,j=1}^k.
\tag{9}
\]

Because `q_1<...<q_k`, the nodes satisfy `y_1>...>y_k>0`; hence

\[
\operatorname{sgn} A_n(y)=(-1)^{\binom k2}.
\tag{10}
\]

For a harmonic tuple

\[
m=(m_1,\ldots,m_k)\in\mathbb N^k,
\]

put

\[
z_j:=y_j^{m_j},
\qquad
u_j:=m_j-1,
\qquad
S(m):=\sum_{j=1}^k\nu_j.
\tag{11}
\]

Columnwise expansion of the absolutely convergent Euler logarithm gives

\[
D_{I,J}
=
\sum_{m\in\mathbb N^k}
\left(\prod_{j=1}^k\frac{q_j^{-m_j\sigma_I}}{m_j}\right)
A_n(z).
\tag{12}
\]

The tuple `m=(1,...,1)` is exactly `(8)`. Therefore each non-first-harmonic tuple contributes, relative to the first harmonic,

\[
R_m
:=
\left(\prod_{j=1}^k\frac{q_j^{-\nu_j\sigma_I}}{m_j}\right)
\frac{|A_n(z)|}{|A_n(y)|}.
\tag{13}
\]

The problem is to sum `R_m` without throwing away the collision geometry of `A_n(z)`.

### 2. The Schur factor does not create a positive power of `P`

Let

\[
d:=\sum_{a=1}^k n_a-\binom k2\ge0.
\tag{14}
\]

The generalized Vandermonde factorization gives, after taking absolute values,

\[
|A_n(x)|
=
\prod_{a<b}|x_a-x_b|\,s_\lambda(x_1,\ldots,x_k),
\tag{15}
\]

for a partition `lambda` of degree `d`. The Schur polynomial has nonnegative integer coefficients and is homogeneous of degree `d`.

Let

\[
m_*:=\min_jm_j.
\]

Since every `q_j` lies in `[P,AP]`, we have

\[
(AP)^{-h}\le y_j\le P^{-h},
\qquad
0<z_j\le P^{-hm_*}.
\tag{16}
\]

Hence

\[
s_\lambda(z)
\le
s_\lambda(1,\ldots,1)P^{-hm_*d},
\tag{17}
\]

while positivity of the Schur coefficients gives

\[
s_\lambda(y)
\ge
(AP)^{-hd}.
\tag{18}
\]

Therefore

\[
\boxed{
\frac{s_\lambda(z)}{s_\lambda(y)}
\le
C_{I,A,h}\,P^{-h(m_*-1)d}
\le C_{I,A,h}.
}
\tag{19}
\]

So arbitrary row gaps do not cost an additional positive power of `P`. The row-shape factor that produced part of AF-337's coarse exponent is harmless for the relative harmonic comparison.

### 3. Equal harmonic labels preserve pairwise collision factors

Consider one pair of columns `a<b`.

If

\[
m_a=m_b=m,
\]

then

\[
\frac{|y_a^m-y_b^m|}{|y_a-y_b|}
=
\sum_{\ell=0}^{m-1}y_a^{m-1-\ell}y_b^\ell
\le
mP^{-h(m-1)}
\le m.
\tag{20}
\]

Thus an equal harmonic label preserves the first-harmonic pairwise zero `y_a-y_b`; it does **not** spend the inverse source-gap factor that AF-337 paid when it bounded the whole determinant independently.

If instead

\[
m_a\ne m_b,
\]

then

\[
|y_a^{m_a}-y_b^{m_b}|
\le
2P^{-h\min(m_a,m_b)}.
\tag{21}
\]

The mean-value theorem and integer spacing give

\[
|y_a-y_b|
=q_a^{-h}-q_b^{-h}
\ge
h(AP)^{-(h+1)}(q_b-q_a),
\tag{22}
\]

so

\[
\frac{|y_a^{m_a}-y_b^{m_b}|}{|y_a-y_b|}
\le
C_{h,A}
\frac{P^{1-h(\min(m_a,m_b)-1)}}{q_b-q_a}
\le
C_{h,A}P.
\tag{23}
\]

A pair pays at most one positive power of `P` **only when the two columns carry different harmonic labels**.

Let

\[
X(m):=\#\{a<b:m_a\ne m_b\}
\tag{24}
\]

be the number of such cross-harmonic pairs. Combining `(15)`, `(19)`, `(20)`, and `(23)`, and absorbing the finitely many row shapes into one constant, gives

\[
\boxed{
\frac{|A_n(z)|}{|A_n(y)|}
\le
C_{r,h,A}\,
(\max_jm_j)^{\binom k2}
P^{X(m)}.
}
\tag{25}
\]

This deliberately drops several favorable negative powers of `P`; only the possible collision loss matters for a uniform sufficient theorem.

### 4. Cross-harmonic collision loss is bounded by the extra-harmonic budget

Let

\[
J:=\{j:m_j>1\},
\qquad t:=|J|.
\]

If `m` is not the all-ones tuple then `t>=1`. Every unequal-harmonic pair has at least one endpoint in `J`, hence

\[
X(m)
\le
t(k-t)+\binom t2
=kt-\frac{t(t+1)}2
\le t(k-1).
\tag{26}
\]

But

\[
S(m)=\sum_j(m_j-1)\ge t,
\tag{27}
\]

so

\[
\boxed{X(m)\le(k-1)S(m).}
\tag{28}
\]

This is the decisive exponent balance. Each unit of extra Euler-harmonic order pays one factor `q^{-sigma_I}`, while it can destroy at most `k-1` first-harmonic pairwise collision factors.

Substituting `(25)` and `(28)` into `(13)` and dropping the helpful factors `1/m_j` yields

\[
R_m
\le
C_{r,h,A}
(\max_jm_j)^{\binom k2}
P^{-[\sigma_I-(k-1)]S(m)}.
\tag{29}
\]

### 5. The complete harmonic tail is a geometric-polynomial remainder

Put

\[
\delta_{I,k}:=\sigma_I-(k-1).
\tag{30}
\]

Under `(1)`, for every selected row set and every `k<=r`,

\[
\delta_{I,k}
\ge
\sigma-(r-1)
=\Delta>0.
\tag{31}
\]

For fixed total excess `S>=1`, the number of tuples `(m_1,...,m_k)` with `S(m)=S` is

\[
\binom{S+k-1}{k-1},
\]

and `max_jm_j<=S+1`. Therefore `(29)` gives

\[
\sum_{m\ne(1,\ldots,1)}R_m
\le
C_{r,h,A}
\sum_{S\ge1}
(S+1)^{\binom r2}
\binom{S+r-1}{r-1}
P^{-\Delta S}.
\tag{32}
\]

For fixed `r` and `Delta>0`, the polynomially weighted geometric series on the right is

\[
O(P^{-\Delta})
\qquad(P\to\infty).
\tag{33}
\]

The constants are uniform over the finitely many possible row shapes and over every increasing integer source set in `[P,AP]`. Equations `(13)` and `(32)` therefore prove `(4)`.

For sufficiently large `P`, the right side of `(4)` is strictly below `1`. Every full-Euler minor then has the sign of its first-harmonic generalized Vandermonde minor, proving `(2)`.

## Consequence for bounded source sign complexity

Strict sign regularity through order `r` gives the same oscillation/nullspace consequence used in [[research/arithmetic_fidelity/findings/AF-216-ordered-sign-complexity-caps-moment-and-dirichlet-cancellation|AF-216]] and AF-337. Once `P>=P_0`, a nonzero signed source supported on the selected integer or prime norms and having at most `r-1` ordered sign changes cannot annihilate all `r` full-Euler samples

\[
\sigma,\ \sigma+h,\ \ldots,\ \sigma+(r-1)h.
\tag{34}
\]

The cost of transferring a source sign budget of order `r` to the full Euler logarithm is therefore no longer the quadratic depth from AF-337. A linear sufficient depth `sigma>r-1` is enough.

## Relation to AF-337 and the live frontier

AF-337's theorem remains correct, including its exact finite-instance gate. AF-338 strengthens only the uniform tail comparison. The earlier proof compared a first-harmonic generalized Vandermonde of size roughly `P^{-Theta(r^2)}` with a higher-harmonic determinant bounded independently of source collisions. The present proof instead compares the higher-harmonic generalized Vandermonde **pair by pair** with the first one.

The resulting resource is not the total number of Vandermonde pairs but the number `X(m)` whose harmonic labels disagree. Since `X(m)` is at most `(k-1)` times the total extra-harmonic order, the exponent budget becomes linear.

This materially changes the remaining obstruction. The source-sign route does not inherently require a quadratic excursion into the half-plane. It still requires `sigma` to grow with the desired sign order, and for every nontrivial `r>=2` the theorem remains entirely inside the absolute-convergence region. The RH-facing problem therefore remains:

- force a natural prime-derived signed discrepancy to have a sufficiently small ordered sign budget; and
- transport the resulting finite-order certificate toward a zero-sensitive observation without losing the destination signal.

AF-338 makes that transport bill substantially cheaper but does not remove it.

## Exact controls and boundaries

### The theorem remains non-prime-specific

Only positivity of the norms, a fixed multiplicative window, and integer spacing enter the uniform proof. Rational primes satisfy those hypotheses, but so do matched composite and mixed-integer controls. Nothing here distinguishes primality.

### Integer spacing is the source of the one-power cross-harmonic loss

The estimate `(22)` turns a missing transformed-node collision factor into at most one power of `P`. A source family with smaller physical gaps would require its own spacing exponent. Thus `(1)` is not a universal theorem for arbitrary dense real source clouds.

### The multiplicative window remains essential for this uniform statement

The constants in `(19)`, `(22)`, and `(25)` use `q_j/P` bounded above and below. Without `q_j<=AP`, one must retain the actual source-scale ratios rather than a single power of `P`.

### The threshold `sigma>r-1` is sufficient, not claimed sharp

The proof takes absolute values over all higher-harmonic tuples and then bounds every unequal-harmonic pair by the worst possible one-power loss. It does not exploit cancellation among harmonic tuples, the favorable factors in `(20)` and `(23)`, or special source spacing. [[research/arithmetic_fidelity/findings/AF-218-full-euler-log-is-strictly-sign-regular-of-order-two|AF-218]] and [[research/arithmetic_fidelity/findings/AF-219-full-euler-log-is-strictly-sign-regular-of-order-three|AF-219]] already show that low orders can perform much better globally.

No claim is made that `r-1` is the optimal asymptotic threshold.

### Exact detection is not stable inversion

Equation `(4)` controls determinants relative to their first-harmonic values and therefore proves exact sign regularity. It does not provide a source-norm recovery bound uniform in arbitrary coefficient dynamic range, support size, or perturbations. Zero-error fidelity and conditioning remain separate currencies.

### The theorem does not enter the critical strip

For `r>=2`, condition `(1)` implies `sigma>1`. The proof uses the absolutely convergent Euler-log expansion and does not invoke analytic continuation or zero information. The improvement is in the **cost of preserving a source discriminator**, not in crossing the analytic-continuation boundary.

## Prior art and novelty assessment

No novelty claim is made for the constituent mathematics.

- Karlin's classical total-positivity theory supplies sign regularity, oscillation, and variation-diminishing/nullspace consequences.
- Generalized Vandermonde determinants, their Schur factorization, and total positivity are classical. Demmel and Koev, **“The Accurate and Efficient Solution of a Totally Positive Generalized Vandermonde Linear System,”** *SIAM Journal on Matrix Analysis and Applications* 27(1), 142–152 (2005), DOI `10.1137/S0895479804440335`, is a modern reference for the generalized-Vandermonde/Schur/total-positivity connection.
- P. Díaz and E. Mainar, **“Total positivity of analytic bases through symmetric functions,”** *Revista de la Real Academia de Ciencias Exactas, Físicas y Naturales. Serie A. Matemáticas* 120, article 70 (2026), DOI `10.1007/s13398-026-01865-x`, gives recent systematic prior art for Schur-function expansions of analytic collocation minors and sufficient total-positivity criteria. Its analytic-basis framework is structurally adjacent, but the searched result does not supply the Euler-log harmonic-label comparison or the threshold `(1)`.
- The Euler logarithm expansion and first-prime-power/higher-prime-power separation are classical.

The derived contribution here is the specific **relative collision accounting** `(20)`--`(28)` for Euler harmonics on escaping multiplicative integer windows. A targeted literature search did not identify this exact Euler-log theorem, but the result is recorded as a derived Mathia specialization rather than a novelty claim.

## Consequence for Arithmetic Fidelity

AF-337 identified three currencies: requested sign order, source-column collision, and harmonic suppression depth. AF-338 sharpens their exchange rate.

A higher Euler harmonic does not erase all first-harmonic collision structure. Equal harmonic labels carry the same pairwise collision factor forward; only cross-harmonic pairs can spend it. The number of such losses is controlled linearly by the amount of extra harmonic mass.

That gives a reusable fidelity principle beyond this kernel:

> When a perturbation is indexed columnwise, determinant stability should be priced by the **number of pairwise collision factors actually broken by the perturbation**, not by the full determinant collision order.

For the present RH-facing route, this removes the quadratic depth artifact and leaves the genuinely arithmetic bottleneck exposed: obtain a natural low-sign-complexity prime discrepancy and transport its finite-order certificate to observations that still retain zero-sensitive content.