# MC-162 — Absolute commutator decoder stability collapses to same-exponent Mertens equivalence

**Status:** `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `BOUNDARY/CONDITIONAL-GAIN`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

The explicit absolute-contraction certificates left open in `MC-160` and `MC-161` do not define an intermediate power-cancellation scale. Whenever one of those certificates holds at exponent `theta>0`, the corresponding transformed summatory bound at exponent `theta` is **equivalent at the same exponent** to the Mertens bound

\[
M(x)=O(x^\theta).
\]

Moreover, the same contraction inequality automatically forces the associated Dirichlet transfer factor to be zero-free in `Re(s)>=theta`. Thus, inside these linear prime-commutator families, absolute decoder stability is stronger than the analytic nonmasking condition isolated in `MC-008`.

This does not prove that a transformed source estimate is useless: an equivalent statement can still admit a different proof. It does prove that the explicit `eta<1` route cannot by itself supply a strictly weaker power-scale theorem. Any gain must come from an **independent source-side proof mechanism** for the transformed statistic, or from signed arithmetic inverse control genuinely stronger than the absolute contraction estimate.

## 1. Tail-centered readouts are bounded forward on exactly the same power space

Use the tail-centered notation of `MC-161`. For prime weights `w=(w_p)`,

\[
f_w(n)=\mu(n)\sum_{p\mid n}w_p,
\qquad
F_w(x)=\sum_{n\le x}f_w(n),
\]

and the exact prime-power identity is

\[
F_w(x)=-\sum_p w_p\sum_{j\ge1}M(x/p^j).
\tag{1}
\]

Fix `theta>0` and define

\[
B_\theta(w):=\sum_p\frac{|w_p|}{p^\theta-1}.
\tag{2}
\]

If `B_theta(w)<infinity` and `M(x)=O(x^theta)`, then (1) gives immediately

\[
|F_w(x)|
\le Cx^\theta
\sum_p|w_p|\sum_{j\ge1}p^{-j\theta}
=C B_\theta(w)x^\theta.
\tag{3}
\]

Hence

\[
M(x)=O(x^\theta)
\quad\Longrightarrow\quad
F_w(x)=O(x^\theta).
\tag{4}
\]

Now suppose `w` is nonzero, let `q` be its least active prime, and use the sufficient inverse factor from `MC-161`,

\[
\eta_{\theta,q}(w)
=
\frac1{|w_q|}
\left[
\frac{|w_q|}{q^\theta-1}
+q^\theta\sum_{p>q}\frac{|w_p|}{p^\theta-1}
\right].
\tag{5}
\]

If `eta_(theta,q)(w)<1`, then `B_theta(w)<infinity`, and the lower-triangular induction of `MC-161` gives the reverse implication

\[
F_w(x)=O(x^\theta)
\quad\Longrightarrow\quad
M(x)=O(x^\theta).
\tag{6}
\]

Combining (4) and (6),

\[
\boxed{
\eta_{\theta,q}(w)<1
\quad\Longrightarrow\quad
F_w(x)=O(x^\theta)
\iff
M(x)=O(x^\theta).
}
\tag{7}
\]

The same statement holds with the usual harmless change of constants for real `x>=1`. No analytic continuation or zero-free hypothesis enters this equivalence.

A first structural consequence is already visible in (5): its self-prime term forces

\[
q^\theta>2.
\tag{8}
\]

Thus at a near-critical exponent, a centered absolute contraction cannot even begin at an arbitrarily small active prime.

## 2. The raw `ell^1` commutator family has the same equivalence

For `a=(a_p) in ell^1(P)` use the notation of `MC-160`,

\[
A=\sum_p a_p,
\qquad
T_a(x)
=-2A M(x)-\sum_p a_p\sum_{j\ge1}M(x/p^j).
\tag{9}
\]

Put

\[
B_\theta(a)=\sum_p\frac{|a_p|}{p^\theta-1}.
\tag{10}
\]

Since `a in ell^1`, this is finite for every `theta>0`. From (9),

\[
M(x)=O(x^\theta)
\Longrightarrow
T_a(x)=O(x^\theta).
\tag{11}
\]

If `A!=0`, the sufficient inverse contraction in `MC-160` is

\[
\eta_\theta(a)
=\frac{B_\theta(a)}{2|A|}<1.
\tag{12}
\]

Under (12), the reverse induction gives `T_a(x)=O(x^theta) => M(x)=O(x^theta)`, and therefore

\[
\boxed{
\eta_\theta(a)<1
\quad\Longrightarrow\quad
T_a(x)=O(x^\theta)
\iff
M(x)=O(x^\theta).
}
\tag{13}
\]

If `A=0`, let `q` be the least active prime. The corresponding factor is

\[
\eta_{\theta,q}(a)
=
\frac1{|a_q|}
\left[
\frac{|a_q|}{q^\theta-1}
+q^\theta\sum_{p>q}\frac{|a_p|}{p^\theta-1}
\right].
\tag{14}
\]

The same forward estimate plus the `MC-160` triangular inverse gives

\[
\boxed{
A=0,\ \eta_{\theta,q}(a)<1
\quad\Longrightarrow\quad
T_a(x)=O(x^\theta)
\iff
M(x)=O(x^\theta).
}
\tag{15}
\]

Thus the absolute stability certificate never yields only a one-way same-exponent improvement in these families: once it is strong enough to transfer a source bound back to Mertens, the forward prime-power transform is already bounded at that same exponent.

## 3. Absolute contraction also forces analytic nonmasking

The same inequalities have a second interpretation. Define, whenever the series converges,

\[
K_w(s)=\sum_p\frac{w_p}{p^s-1}.
\tag{16}
\]

For the centered coefficients, the Dirichlet-series identity in the half-plane of absolute convergence is

\[
\sum_{n\ge1}\frac{f_w(n)}{n^s}
=-\frac{K_w(s)}{\zeta(s)}.
\tag{17}
\]

If `eta_(theta,q)(w)<1`, write

\[
R_\theta=\sum_{p>q}\frac{|w_p|}{p^\theta-1}.
\]

Equation (5) implies

\[
R_\theta
<
|w_q|\frac{q^\theta-2}{q^\theta(q^\theta-1)}
<
\frac{|w_q|}{q^\theta+1}.
\tag{18}
\]

For `sigma=Re(s)>=theta`,

\[
\sum_{p>q}\frac{|w_p|}{|p^s-1|}
\le
\sum_{p>q}\frac{|w_p|}{p^\sigma-1}
\le
q^{\theta-\sigma}R_\theta,
\tag{19}
\]

where `p^sigma-1 >= p^(sigma-theta)(p^theta-1)` was used. On the other hand,

\[
\left|\frac{w_q}{q^s-1}\right|
\ge
\frac{|w_q|}{q^\sigma+1}.
\tag{20}
\]

Since

\[
\frac{q^{\theta-\sigma}}{q^\theta+1}
\le
\frac1{q^\sigma+1},
\tag{21}
\]

(18)–(21) show that the least-prime term strictly dominates the complete tail. Therefore

\[
\boxed{K_w(s)\ne0\qquad (\operatorname{Re}s\ge\theta).}
\tag{22}
\]

For the raw family with `A!=0`, put `K_a(s)=sum_p a_p/(p^s-1)`. Condition (12) gives directly

\[
|K_a(s)|
\le B_\theta(a)
<2|A|,
\qquad \operatorname{Re}s\ge\theta,
\]

so

\[
\boxed{2A+K_a(s)\ne0\qquad (\operatorname{Re}s\ge\theta).}
\tag{23}
\]

When `A=0`, the least-prime argument (18)–(22) applies verbatim to `a`.

The pointwise raw coefficient Dirichlet series satisfies

\[
\sum_{n\ge1}\frac{c_a(n)}{n^s}
=-\frac{2A+K_a(s)}{\zeta(s)}
\tag{24}
\]

initially for `Re(s)>1`. Hence the explicit contraction certificates automatically rule out transfer-factor zeros throughout the half-plane on which they operate. In the terminology of `MC-008`, **absolute inverse stability implies analytic nonmasking** for these commutator kernels.

The converse is false in general. `MC-008` already supplies an explicit small-prime comparator whose transfer factor is nonmasking in the right critical strip even though its absolute inverse coefficients are unstable below exponent one. Nonmasking is therefore the weaker analytic information-preservation condition.

## 4. What this does and does not close

The accepted decoder-stability clue asks for a transformed statistic with both a source-side estimate and a controlled inverse. Equations (7), (13), and (15) sharpen what such a success would mean. If the control is exactly one of the absolute `eta<1` certificates above, then an estimate

\[
F_w(x)=O(x^\theta)
\quad\text{or}\quad
T_a(x)=O(x^\theta)
\]

is already an equivalent formulation of the Mertens power bound at exponent `theta`. The contraction itself supplies no intermediate exponent and no independent arithmetic saving.

This is a **classification, not a circularity objection**. An equivalent transformed statement may still be easier to prove because its coefficients, positivity, factorization, or another source-side structure admits tools unavailable for `M` directly. A future scalar candidate is therefore still meaningful if it comes with a genuinely independent theorem for the transformed source. What no longer counts as progress is presenting `eta<1` alone as the quantitative advantage.

The remaining scalar escape is also sharper. One may seek a signed Möbius-specific inverse-tail estimate that succeeds even when the absolute `eta` diverges or exceeds one. Such a theorem would use relations among the actual lower-scale values of `M`, rather than generic weighted-sup contraction, and is not ruled out here. `MC-161`'s unit charge shows why this distinction matters: its source is independently tractable, but its absolute inverse is maximally unstable in every sublinear power space.

## Prior art and novelty assessment

Weighted convolution algebras, Wiener-type inversion principles, Tauberian transfer, and Dirichlet-series nonvanishing are classical subjects. Jung and Lemke Oliver (`MC-S7`) explicitly study convolution/pretentious conditions that transfer power cancellation, while Venturini (`MC-S17`) gives an adjacent theorem in which analyticity of an auxiliary multiplicative Dirichlet series forces a zeta zero-free half-plane. `MC-008` already established the line-local zero-mask criterion relevant here.

A targeted literature search for the exact prime-commutator transforms and constants (5), (12), and (14), and for the implication from those particular contraction constants to the transfer-factor dominance (22)–(23), did not locate a matching published theorem. No novelty is inferred from that absence. The present result is an elementary consequence of the already persisted commutator identities plus absolute convergence and a least-prime dominance estimate, and is recorded with **no novelty claim**.

## Boundaries and falsification tests

- The theorem concerns the explicit **absolute** contraction certificates from `MC-160` and `MC-161`. Their failure does not imply that exponent transfer is impossible.
- Same-exponent equivalence is a mathematical implication, not a claim that the two statements have identical proof complexity.
- The nonmasking statement concerns the transfer factors generated by these exact prime-power kernels. It does not classify arbitrary nonlinear, noncommutative, or singular infinite-prime readouts.
- The centered least-prime proof requires `eta_(theta,q)<1`, which itself forces `q^theta>2`; there is no hidden use of RH or of a zeta zero-free region.
- The Dirichlet-series identities are invoked initially only where their Euler/Dirichlet manipulations converge absolutely. The zero-free conclusion for the transfer factor is proved directly from (18)–(23), not by assuming continuation of `1/zeta`.
- A counterexample to any forward identity (1) or (9), to the previously derived inverse recursions, or to the dominance inequalities (18)–(23) would refute the corresponding part.

## Consequence for the line

The scalar commutator frontier now has three clean regimes. Pure magnitude readouts are cancellation-blind; signed linear readouts are Mertens-complete; and the explicit absolute stability certificates, when they hold, make their power bounds same-exponent equivalent to Mertens while automatically guaranteeing analytic nonmasking.

The useful unresolved question is therefore not whether one can tune another `eta<1` weight. It is whether a fixed transformed input has an **independently provable source theorem** that exploits genuinely different structure, or whether signed arithmetic cancellation in an otherwise unstable inverse can be controlled without already assuming the target. If neither occurs, scalarization has no remaining quantitative advantage and the line should move to the genuinely relational/non-scalar carriers identified by the local synthesis.