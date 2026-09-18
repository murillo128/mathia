# FD-194 — Geometric square-root Fourier bands have a contractive cumulative inverse

- **Date:** 2026-09-18
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** stable inversion / observation conditioning / sharp threshold
- **Depends on:** FD-117, FD-189, FD-193
- **Classification:** `EXACT-DERIVED + SHARP-STABILITY-THRESHOLD + UNIFORM-L_INFINITY-LEFT-INVERSE`

## Claim

`FD-193` proves that for geometric horizons `H=B^m`, the signed Farey Fourier band

\[
1\le k\le \left\lfloor c\sqrt H\right\rfloor
\]

is exactly injective on formal increment sources if and only if

\[
c\ge\sqrt B.
\]

That result is algebraic: it deliberately leaves conditioning open. The same threshold is in fact a **stable-invertibility threshold** for the exact Fourier normalization used in `FD-117/189`.

Fix an integer `B>=2` and `c>=sqrt(B)`. Write

\[
A(t):=\sum_{n\le t}a(n)
\]

and let

\[
\mathcal F_H^a(k)
=\sum_{d\mid k}d\,A\!\left(\left\lfloor\frac Hd\right\rfloor\right)
\tag{1}
\]

be the signed Farey Fourier coefficient from `FD-117`.

For each `n>=1`, let `H_n` be the least power of `B` with

\[
H_n\ge n(n+1),
\tag{2}
\]

and define the canonical witness

\[
k_n:=\left\lfloor\frac{H_n}{n+1}\right\rfloor+1.
\tag{3}
\]

`FD-193` proves

\[
\left\lfloor\frac{H_n}{k_n}\right\rfloor=n,
\qquad
n+1\le k_n\le Bn,
\qquad
k_n\le\sqrt{BH_n}.
\tag{4}
\]

Hence every divisor of `k_n` lies in the retained band at horizon `H_n`. Divisor Möbius inversion applied to (1) gives the **explicit left inverse**

\[
\boxed{
A(n)
=
\frac1{k_n}
\sum_{d\mid k_n}
\mu\!\left(\frac{k_n}{d}\right)
\mathcal F_{H_n}^a(d).
}
\tag{5}
\]

Now perturb every retained Fourier datum by arbitrary complex noise `eta_H(k)` satisfying

\[
|\eta_H(k)|\le\varepsilon.
\tag{6}
\]

If `\widetilde A(n)` is reconstructed by (5) from

\[
\widetilde{\mathcal F}_H(k)
=\mathcal F_H^a(k)+\eta_H(k),
\]

then

\[
\boxed{
|\widetilde A(n)-A(n)|
\le
\varepsilon\frac{2^{\omega(k_n)}}{k_n}
\le\varepsilon.
}
\tag{7}
\]

Thus the cumulative-source inverse has `l^infinity -> l^infinity` operator norm at most `1`, uniformly in the recovered prefix length, the source, and the geometric horizon.

Recover increments by

\[
\widetilde a(1)=\widetilde A(1),
\qquad
\widetilde a(n)=\widetilde A(n)-\widetilde A(n-1)
\quad(n\ge2).
\tag{8}
\]

Then

\[
\boxed{
\sup_{n\ge1}|\widetilde a(n)-a(n)|\le2\varepsilon.
}
\tag{9}
\]

So the same geometric band that becomes injective at `c=sqrt(B)` already admits a uniformly conditioned source reconstruction in the raw signed-Fourier `l^infinity` norm. There is no intermediate regime in which exact injectivity holds but the canonical inverse is forced to become badly conditioned with prefix length.

The pointwise estimate is substantially stronger than the uniform constant. For every fixed `0<delta<1`,

\[
2^{\omega(m)}\le C_\delta m^\delta,
\tag{10}
\]

and `k_n>=n+1`. Therefore

\[
|\widetilde A(n)-A(n)|
\le
C_\delta\varepsilon n^{-1+\delta},
\tag{11}
\]

and

\[
|\widetilde a(n)-a(n)|
\le
C'_\delta\varepsilon n^{-1+\delta}
\qquad(n\to\infty).
\tag{12}
\]

In this absolute-noise normalization, the canonical high-index reconstruction is therefore not merely stable: its worst-case pointwise noise amplification tends to zero at rate `n^{-1+o(1)}`.

Conversely, if `c<sqrt(B)`, `FD-193` supplies infinitely many exact unsampled cumulative coordinates and distinct formal sources with identical complete band histories. Hence no left inverse exists even at zero noise. Combining the two directions gives the exact stable-invertibility transition

\[
\boxed{
c_*^{\mathrm{stable}}=\sqrt B.
}
\tag{13}
\]

for this observation geometry and norm.

## 1. The divisor transform has an explicitly small inverse row

Fix one horizon `H`. Define

\[
G_H(d):=d\,A\!\left(\left\lfloor\frac Hd\right\rfloor\right).
\tag{14}
\]

Equation (1) is the ordinary divisor zeta transform

\[
\mathcal F_H(k)=\sum_{d\mid k}G_H(d).
\tag{15}
\]

Möbius inversion therefore gives

\[
G_H(k)
=\sum_{d\mid k}
\mu\!\left(\frac kd\right)\mathcal F_H(d),
\tag{16}
\]

or equivalently

\[
A\!\left(\left\lfloor\frac Hk\right\rfloor\right)
=\frac1k
\sum_{d\mid k}
\mu\!\left(\frac kd\right)\mathcal F_H(d).
\tag{17}
\]

The nonzero coefficients in this inverse row are exactly those divisors for which `k/d` is squarefree. Their number is

\[
2^{\omega(k)}.
\tag{18}
\]

Hence the exact `l^infinity` row norm is

\[
\frac{2^{\omega(k)}}k.
\tag{19}
\]

This is at most one. Indeed, if `p_1,...,p_r` are the distinct prime divisors of `k`, then

\[
k\ge p_1\cdots p_r\ge2^r=2^{\omega(k)}.
\tag{20}
\]

No cancellation assumption on the noise is used. The bound holds for adversarial complex perturbations because it is simply the `l^1` norm of the inverse row.

Equation (19) also shows that the conditioning improvement at large quotient index is arithmetic, not an artifact of averaging random noise. The factor `1/k` built into the exact inverse outweighs the growth in the number of squarefree divisor choices.

## 2. The geometric witness makes every required inverse row observable

The inversion in (17) is useful only if every mode `d|k` used by that row is actually retained. This is where the geometry of `FD-193` is load-bearing.

For the canonical pair `(H_n,k_n)` in (2)--(3), `FD-193` proves

\[
\left\lfloor\frac{H_n}{k_n}\right\rfloor=n
\]

and

\[
k_n\le\sqrt{BH_n}.
\]

At `c>=sqrt(B)` the mode `k_n` therefore belongs to the retained band. Since every divisor `d|k_n` satisfies `d<=k_n`, the entire Möbius-inversion row in (5) is present at the **same horizon**. There is no need to combine incompatible normalizations or infer missing modes from another scale.

This proves (5)--(7). It also shows why exact quotient coverage alone was not automatically a stability theorem: one must verify that the divisor closure needed by the inverse comes with each quotient witness. Initial Fourier bands have precisely that downward-closed property.

For a finite prefix `1<=n<=N`, `FD-193` already gives

\[
H_n=O_B(N^2)
\]

and only `O_B(N)` retained Fourier coefficients in total through the largest required geometric horizon. Thus the uniformly stable reconstruction does not require more scalar data than the order-optimal exact reconstruction of `FD-193`.

## 3. Tail conditioning is `n^{-1+o(1)}`

The elementary estimate (10) does not require a maximal-order theorem for `omega`. Fix `delta>0` and let

\[
P_\delta:=2^{1/\delta}.
\]

For every prime `p>=P_delta`,

\[
2\le p^\delta.
\]

The finitely many smaller prime factors contribute only a constant depending on `delta`. Therefore

\[
2^{\omega(m)}
=\prod_{p\mid m}2
\le C_\delta\prod_{p\mid m}p^\delta
\le C_\delta m^\delta.
\tag{21}
\]

Substituting `m=k_n` into (7) and using `k_n>=n+1` gives (11). Applying the same estimate at `n` and `n-1` in (8) gives (12).

This decay should be interpreted only in the stated absolute-noise coordinate system. The raw coefficients in (1) carry the factor `d`; rescaling Fourier modes, using relative error, normalizing by Farey cardinality, or imposing a different data norm changes the conditioning problem. `FD-194` does not claim norm-independent stability.

## 4. Sharpness and matched controls

The lower side of the threshold needs no separate conditioning counterexample. For every

\[
0<c<\sqrt B,
\]

`FD-193` constructs arbitrarily distant cumulative coordinates absent from the complete geometric quotient coverage. `FD-189/190/191` explain how such holes support exact null perturbations in relevant schedules. Therefore the observation operator is noninjective below the threshold, and no deterministic left inverse—bounded or unbounded—can exist on the full formal source class.

At and above the threshold, the proof above constructs a particular bounded left inverse. The transition is therefore genuinely between **nonidentifiability** and **uniformly stable identifiability**, not between nonidentifiability, unstable identifiability, and stable identifiability.

Several stress tests are worth recording explicitly:

- the proof does not use Möbius as the source; it holds for arbitrary formal increments because Möbius appears only as the divisor-incidence inverse kernel;
- it does not assume random, mean-zero, independent, or coherent noise;
- each reconstruction row uses one physical horizon and only retained modes from that horizon;
- the constant `2` in increment recovery is a safe operator-norm bound from differencing two cumulative estimates, not a claim of global sharpness;
- the tail decay in (12) is an absolute-error statement and must not be transported unchanged to normalized or relative Fourier data.

## Representation audit

The result stays entirely inside the exact observation coordinates of `FD-117/189/193`. No full Farey field, hidden source coordinate, prime-extension energy, or extra arithmetic relation is supplied to the inverse.

The only representation change is the exact divisor Möbius inversion already certified by `FD-117`: at a fixed horizon, the initial signed Fourier band and the corresponding divisor-closed quotient samples are related by a triangular incidence transform. The new content is quantitative: its inverse row for quotient `floor(H/k)` has exact `l^1` norm `2^{omega(k)}/k`, and the geometric witnesses of `FD-193` place those rows inside the retained physical band.

The norm is stated explicitly. The data error is the sup norm of **raw signed Fourier coefficients in the project normalization (1)**; the reconstructed quantities are measured first in cumulative-source sup norm and then in increment-source sup norm. No claim is made for probability distributions, normalized Farey energies, `l^2` data, relative noise, or Franel discrepancy.

The generic part is classical divisor-incidence Möbius inversion. The line-specific part is the conjunction of its weighted inverse row with the exact geometric witness geometry from `FD-193`.

## Prior-art and novelty boundary

Ordinary zeta/Möbius transforms on divisor lattices and Ramanujan-sum Fourier representations are classical. The line already anchors Ramanujan's divisor formula in `SOURCES.md`, and `FD-117` is the canonical source for the exact Farey specialization (1). A targeted literature search also found the standard algorithmic literature on fast zeta/Möbius inversion in divisor and semimodular lattices and Ramanujan-Fourier transforms of arithmetic functions. No novelty is claimed for Möbius inversion itself.

The mathematical delta here is narrower: after the sharp geometric coverage constant `sqrt(B)` from `FD-193`, the **same physical witness** exposes a divisor-closed inverse row whose raw-Fourier `l^infinity` norm is at most one, with pointwise norm `2^{omega(k_n)}/k_n=n^{-1+o(1)}`. No source located in the targeted search states this Farey/geometric conditioning consequence or the resulting exact coincidence of injectivity and stable-invertibility thresholds.

No external theorem beyond already-canonical identities is load-bearing, so `SOURCES.md` does not need a new durable anchor.

## Formalization disposition

The result is exact and finite-row, but it does not currently pass the Research Watch fertility gate for a new Lean delegation. The sharp structural boundary `c=sqrt(B)` is already isolated by `FD-193`; the additional proof here reduces directly to divisor Möbius inversion, the elementary count `2^{omega(k)}`, and the inequality `2^{omega(k)}<=k`. Formalizing it would mainly transcribe a short classical incidence-algebra estimate rather than expose a new unresolved kernel/range structure or consequential hypothesis. A later formalization of the `FD-193` observation operator could absorb this stability lemma naturally if that interface becomes a controlled target.

## Research consequence

`FD-193` left open an important possibility: perhaps the exact square-root-base band is only algebraically sufficient, with a catastrophically ill-conditioned inverse that would make the threshold physically fragile. `FD-194` rules out that explanation in the native raw signed-Fourier sup norm.

At `c=sqrt(B)` the information transition is unexpectedly clean. Below it, exact null directions survive. At it, every cumulative source coordinate has a local divisor-closed reconstruction row of norm at most one, and increments are recovered with a uniform factor-two bound. Far out in the source, those row norms even vanish as `n^{-1+o(1)}`.

This does **not** bridge the signed Fourier data to Franel--Landau or to the prime-extension energy of `FD-187/188`; the observational norm is different and the Fourier coefficients themselves are not assumed to satisfy an RH-strength noise estimate. The next useful question is therefore no longer whether geometric square-root recovery is numerically ill-conditioned in these native coordinates, but whether any naturally controlled Farey statistic supplies sufficiently small errors in the exact signed modes needed by this inverse.