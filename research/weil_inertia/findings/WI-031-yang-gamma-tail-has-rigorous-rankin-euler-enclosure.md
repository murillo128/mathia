# WI-031 — Yang--Yang's infinite gamma tail has a rigorous Rankin--Euler enclosure

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + PRIOR-ART-REDIRECTION + NEEDS-AUDIT`. This finding does **not** establish the Yang--Yang one-sided fourth-moment theorem and does not change Mathia's current unconditional simple-critical proportion. It closes a narrower proof-engineering gap identified in WI-028/WI-030: the public `tail_bound.py` estimates the uncomputed coefficient tail beyond `DCAP` by doubling the mass in the last computed half-shell. That geometric-ratio extrapolation is unnecessary. The same Ramanujan/Mobius transform has a multiplicative Euler factorization whose absolute Rankin moments converge for every `0 < alpha < 1`, giving a genuine infinite-tail bound after any finite cutoff.

The practical consequence is that the deterministic-tail replay can be made fail-closed without guessing the decay ratio of the last numerical shell. The remaining load-bearing work is still substantial: interval-certify the finite coefficient/integration part and independently prove the zeta-side reduction to the deterministic main/tail object.

## 1. Source boundary

This finding audits the public Yang--Yang repository at

`JoshuaHKU/zeta-0.7947-reproduction@d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8`,

especially:

- `paper.tex`, Proposition `Arc identity`, Lemmas `E3` and `S0`, and the one-sided fourth-moment assembly;
- `scripts/tail_bound.py`, notably `gamma_signed_array`, `_gamma_free_exact`, and `env_total`;
- `scripts/mains_envelope.py`, notably the earlier `gamma_d` helper.

Pinned sources:

- https://github.com/JoshuaHKU/zeta-0.7947-reproduction/blob/d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8/paper.tex
- https://github.com/JoshuaHKU/zeta-0.7947-reproduction/blob/d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8/scripts/tail_bound.py
- https://github.com/JoshuaHKU/zeta-0.7947-reproduction/blob/d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8/scripts/mains_envelope.py

The source already contains the important correction that the generic odd-prime factor must be removed for a special prime `p | 2 b1 b2` whether or not `p | d`; `_gamma_free_exact` and `gamma_signed_array` implement that correction. The older `mains_envelope.py::gamma_d` still has the pre-correction branch structure and must not be used as the reference formula for a certification replay.

The external mathematical ingredients used below are classical: the divisor formula for Ramanujan sums, Mobius inversion, absolute Euler products for multiplicative functions, and the elementary Rankin inequality `1_{d>D} <= (d/D)^alpha`. No novelty is claimed for those tools. The Mathia contribution is their exact application to this particular public tail object and the resulting removal of its heuristic infinite-shell extrapolation.

## 2. Exact local transform

For fixed prime powers `b1,b2`, put

\[
e_i(p)=v_p(b_i).
\]

The Yang--Yang arc coefficient is

\[
\beta_q=\frac{\mu(q_1)\mu(q_2)}{\varphi(q_1)\varphi(q_2)},
\qquad
q_i=\frac{q}{(q,b_i)}.
\tag{1}
\]

Its local factor at `p^a` is therefore

\[
B_p(a)
=\prod_{i=1}^2 h_p\!\left(\max(a-e_i(p),0)\right),
\tag{2}
\]

where

\[
h_p(0)=1,
\qquad
h_p(1)=-\frac1{p-1},
\qquad
h_p(r)=0\quad(r\ge2).
\tag{3}
\]

Using

\[
c_q(j)=\sum_{d\mid(q,j)}d\,\mu(q/d)
\]

in the row sum

\[
r_j(\theta)=\frac{\sin(2\theta j)-\sin(\theta j)}{j}
\]

gives, for every finite `J`, the exact change of variables `j=dk`:

\[
\sum_{j\le J}c_q(j)r_j(\theta)
=
\sum_{d\mid q}\mu(q/d)
S_0\!\left(d\theta;\left\lfloor\frac Jd\right\rfloor\right),
\tag{4}
\]

with

\[
S_0(x;K)=\sum_{k\le K}\frac{\sin(2xk)-\sin(xk)}{k}.
\]

Thus the transformed coefficient is the Mobius difference

\[
\gamma_d=\sum_{e\ge1}\mu(e)\beta_{de},
\tag{5}
\]

and multiplicativity makes its local factor

\[
\boxed{g_p(v)=B_p(v)-B_p(v+1).}
\tag{6}
\]

For all but finitely many odd primes (`p \nmid 2b_1b_2`) this specializes to

\[
g_p(0)=1-\frac1{(p-1)^2}
=\frac{p(p-2)}{(p-1)^2},
\qquad
g_p(1)=\frac1{(p-1)^2},
\tag{7}
\]

and `g_p(v)=0` for `v>=2`. In particular,

\[
\boxed{|g_p(0)|+|g_p(1)|=1.}
\tag{8}
\]

At the finitely many special primes dividing `2b1b2`, (2)--(6) give a finite local table directly. This is exactly the corrected local construction in `tail_bound.py`.

## 3. Full and class pieces

Let

\[
S=S(b_1,b_2)=\{p:p\mid 2b_1b_2\}.
\]

There are two coefficient systems in the source decomposition. The unrestricted transform of (1) is

\[
\gamma_d^{\mathrm{full}}
=\prod_p g_p(v_p(d)),
\tag{9}
\]

where the infinite product is interpreted with the convergent generic factors (7). The `Dbar` class keeps only moduli whose prime factors lie in `S`; its transform is

\[
\gamma_d^{\mathrm{class}}
=\mathbf 1_{\operatorname{supp}(d)\subseteq S}
\prod_{p\in S}g_p(v_p(d)).
\tag{10}
\]

Hence the free coefficient used by the corrected source is exactly

\[
\boxed{
\gamma_d^{\mathrm{free}}
=\gamma_d^{\mathrm{full}}-\gamma_d^{\mathrm{class}}.
}
\tag{11}
\]

This also explains the special-prime normalization correction documented in `tail_bound.py`: the universal twin-prime product contains the generic factor (7) at every odd prime, so for every special odd prime it must be divided out before inserting the special local factor, independently of whether that prime divides `d`.

Now let `P` be the explicit Ramanujan cutoff in the paper (`P=40`). The coefficient of the residual `q>P` piece differs from (11) only by the finite transform of moduli `q<=P`. Such a finite transform is supported on divisors `d<=P`. Therefore

\[
\boxed{
 d>P
 \quad\Longrightarrow\quad
 \gamma_d^{>P}=\gamma_d^{\mathrm{free}}.
}
\tag{12}
\]

Equation (12) is what allows a rigorous bound on the uncomputed `d>DCAP` shell to use the clean Euler product (9)--(11), provided `DCAP>P`.

## 4. Absolute Rankin moments converge for every `alpha<1`

Fix

\[
0<\alpha<1.
\]

Define the finite special-prime moment

\[
A_\alpha(b_1,b_2)
:=
\prod_{p\in S}
\left(
\sum_{v\ge0}p^{\alpha v}|g_p(v)|
\right).
\tag{13}
\]

Each local sum in (13) is finite because (2)--(3) force `g_p(v)=0` for all sufficiently large `v`.

For a generic odd prime, (7) gives

\[
\sum_{v\ge0}p^{\alpha v}|g_p(v)|
=1+\frac{p^\alpha-1}{(p-1)^2}.
\tag{14}
\]

Consequently the generic product

\[
U_{\alpha,S}
:=
\prod_{\substack{p>2\\p\notin S}}
\left(1+\frac{p^\alpha-1}{(p-1)^2}\right)
\tag{15}
\]

converges absolutely, since its logarithm is dominated by

\[
\sum_p O(p^{\alpha-2}),
\]

which converges exactly for `alpha<1`. Therefore Tonelli/Euler-product factorization gives

\[
\sum_{d\ge1}d^\alpha
|\gamma_d^{\mathrm{full}}|
=A_\alpha(b_1,b_2)U_{\alpha,S},
\tag{16}
\]

and, because the class piece has only the special Euler factors,

\[
\sum_{d\ge1}d^\alpha
|\gamma_d^{\mathrm{class}}|
=A_\alpha(b_1,b_2).
\tag{17}
\]

By (11),

\[
\boxed{
\sum_{d\ge1}d^\alpha
|\gamma_d^{\mathrm{free}}|
\le
A_\alpha(b_1,b_2)\bigl(1+U_{\alpha,S}\bigr).
}
\tag{18}
\]

No numerical asymptotic or guessed decay ratio enters (18).

A useful source sanity check is the `alpha=0` generic identity (8): away from the finitely many special primes, the absolute local mass is exactly one. The apparent infinite complexity of the free gamma tail is therefore entirely controlled by a probability-like squarefree Euler product plus finitely many special local replacements.

## 5. Rigorous infinite-cutoff bound

For every `D>P`, (12), (18), and the elementary Rankin inequality give

\[
\begin{aligned}
\sum_{d>D}|\gamma_d^{>P}|
&=\sum_{d>D}|\gamma_d^{\mathrm{free}}|\\
&\le
D^{-\alpha}
\sum_{d>D}d^\alpha|\gamma_d^{\mathrm{free}}|\\
&\le
\boxed{
D^{-\alpha}
A_\alpha(b_1,b_2)
\bigl(1+U_{\alpha,S}\bigr).
}
\end{aligned}
\tag{19}
\]

This is the required genuine infinite-tail theorem.

For certification code it is convenient to bound the omitted-prime product by the universal

\[
U_\alpha
=
\prod_{p>2}
\left(1+\frac{p^\alpha-1}{(p-1)^2}\right),
\qquad
U_{\alpha,S}\le U_\alpha,
\tag{20}
\]

and interval-evaluate either (20) or a finite prefix plus a simple analytic prime tail. For example, at `alpha=1/2`,

\[
\log U_{1/2}
\le
\sum_{p\ge3}p^{-3/2}
<\infty,
\tag{21}
\]

because

\[
\frac{\sqrt p-1}{(p-1)^2}\le p^{-3/2}
\qquad(p\ge3).
\]

Thus even a deliberately crude fully analytic enclosure is immediate; a production replay can optimize `alpha` and evaluate the short Euler prefix with directed intervals.

## 6. What this changes in the public `tail_bound.py`

The current public script computes `|gamma_d^{>P}|` up to `DCAP` and then uses

`2 * sum(ag[DCAP/2 : DCAP])`

as an estimate for all omitted `d>DCAP` mass. That is a plausible numerical model for a roughly inverse-power tail, but it is not a theorem and WI-028 correctly treated it as a certification gap.

Equation (19) gives a direct fail-closed replacement:

1. keep the exact/interval evaluation of `gamma_d^{>P}` for `d<=DCAP`;
2. compute the finite special factor `A_alpha(b1,b2)` from (2)--(6);
3. enclose `U_{alpha,S}` by a directed Euler product plus analytic remainder, or simply by a universal enclosure for `U_alpha`;
4. replace the geometric shell extrapolation by the right side of (19).

The same bound can be inserted into the manuscript's Lemma `E3` because its sawtooth factor is uniformly bounded. If `|S_0|<=C_saw`, the omitted transformed row contribution is at most

\[
C_{\mathrm{saw}}
D^{-\alpha}A_\alpha(1+U_{\alpha,S}),
\tag{22}
\]

before the already-explicit positive geometry/zone integration.

This does **not** certify the reported global number `epsilon_tail <= 0.0111`: the finite `d<=DCAP` contribution and the positive geometry integral still need outward-rounded evaluation, and the full analytic reduction feeding those weights remains to be audited. It does show that no conjectural or empirical decay law is needed for the infinite `d`-tail itself.

## 7. Relation to WI-028 and WI-030

WI-028 reduced the one-sided fourth-moment target to the coarse condition

\[
R(1)<0.0380702829042267\ldots
\]

for any strict improvement over Mathia's current established theorem. WI-030 then evaluated the universal continuum core exactly as

\[
C_{\mathrm{core}}=-\frac1{48},
\]

so, **if** the unreviewed universal-collapse bridge is independently proved, everything outside that core may be as large as

\[
0.0589036162375601\ldots
\]

and still improve the current theorem.

The present finding removes one named source of non-rigorousness from that non-core budget: the `d=DCAP..infinity` extrapolation can be certified by (19). The remaining program is therefore sharper:

\[
\boxed{
\text{universal-collapse / MRT bridge}
\; + \;
\text{finite interval replay}
\; + \;
\text{Rankin--Euler infinite tail}.
}
\]

The difficult part is no longer "guess the infinite coefficient decay". It is to validate the analytic bridge and certify a finite, explicitly bounded computation.

## 8. Prior-art / novelty audit

The Euler-product identity for an absolutely summable multiplicative function and the Rankin cutoff trick are classical. General modern treatments of multiplicative Ramanujan expansions likewise emphasize finite/infinite Euler products and convergence; no novelty is claimed for those principles.

Targeted searches of the pinned Yang--Yang repository found no Rankin bound for the omitted gamma shell and no replacement for the `2 * last-half-shell` estimate. Their own paper already states the exact Ramanujan/Mobius structure from which (6) follows, and `tail_bound.py` contains the corrected special-prime local factors. Accordingly, the right attribution is:

- **literature/source-backed:** arc expansion, beta coefficients, Ramanujan-sum divisor identity, finite-`J` sawtooth transform, corrected special-prime factorization;
- **classical:** Euler products and Rankin tail majorization;
- **exact Mathia deduction:** equations (12), (18), and (19) as a fail-closed replacement for the public infinite-shell extrapolation.

Absence of the same packaged bound in the searched repositories is not a priority claim.

## 9. Falsification tests and boundaries

A certification replay should reject this finding if any of the following fails:

1. derive `g_p(v)=B_p(v)-B_p(v+1)` directly from (1) and the Ramanujan divisor formula and compare it against `_gamma_free_exact` for exhaustive small `(b1,b2,d)` cases;
2. verify that the finite `q<=P` subtraction has transformed support only at `d<=P`, establishing (12);
3. for generic odd primes, verify (7)--(8) exactly;
4. independently sum a large finite prefix of `d^alpha |gamma_free(d)|` and check it remains below the directed enclosure of (18);
5. replace the source's shell extrapolation by (19) and confirm the final interval bound remains below whatever proof-budget threshold is claimed.

The result has deliberately narrow scope. It does not validate Yang--Yang's shifted-correlation transfer, universality collapse, finite quadrature, or global `0.6916` claim, and it does not improve the unconditional zeta proportion by itself.