# AF-226 — prime-tail proximity marking has an exact logarithmic resolution phase law

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `QUANTITATIVE-FIDELITY`, `NEGATIVE/OBSTRUCTION`, `MARK-COMPLEXITY`, `PRIME-TAIL`, `PHASE-LAW`, `NO-NOVELTY-CLAIM`

## Claim

AF-224 turns a uniformly resolvable marked translation repair into a coloring problem on the source proximity graph. AF-225 shows that at every **fixed** positive source radius, the rational-prime log-log tail needs asymptotically one mark per prime. The moving-radius regime has an exact threshold at scale `1/log Q`.

For `Q >= 3`, let

\[
S_Q:=\{-\log\log p:p\le Q,\ p\text{ prime}\},
\qquad n_Q:=\pi(Q).
\tag{1}
\]

For `r>0`, join two distinct source points when their distance is at most `r`, and write

\[
K_Q(r):=\chi(G_r(S_Q)).
\tag{2}
\]

By AF-225, because `G_r(S_Q)` is a unit interval graph,

\[
K_Q(r)=M_{S_Q}(r),
\tag{3}
\]

where `M_{S_Q}(r)` is the maximal number of source points in an interval of length `r`.

Let `r_Q>0` be any radius sequence and put

\[
c_Q:=r_Q\log Q.
\tag{4}
\]

If

\[
c_Q\longrightarrow c\in[0,\infty],
\tag{5}
\]

with the convention `e^{-\infty}=0`, then

\[
\boxed{
\frac{K_Q(r_Q)}{\pi(Q)}
\longrightarrow
1-e^{-c}.
}
\tag{6}
\]

Thus the proximity-marking problem has three exact asymptotic regimes:

- `r_Q log Q -> 0` if and only if `K_Q(r_Q)=o(pi(Q))`;
- `r_Q log Q -> c in (0,infinity)` gives a positive asymptotic mark fraction `1-e^{-c}`;
- `r_Q log Q -> infinity` if and only if `K_Q(r_Q)~pi(Q)`.

The first equivalence is the sharp residual left open by AF-225. **A growing mark alphabet is genuinely sublinear in source cardinality only if the source-resolution radius collapses faster than `1/log Q`.** Shrinking the radius more slowly still costs a positive fraction, and any radius asymptotically larger than that threshold costs essentially full source identity in alphabet size.

More generally, let a marked representation on `S_Q` use `A_Q` distinct marks, and suppose AF-224 forces different marks whenever two source points are within `r_Q`. Then

\[
|A_Q|\ge K_Q(r_Q).
\tag{7}
\]

Hence, for every fixed `rho in [0,1)`,

\[
|A_Q|\le \rho\,\pi(Q)
\quad\text{eventually}
\tag{8}
\]

forces

\[
\boxed{
\limsup_{Q\to\infty} r_Q\log Q
\le -\log(1-\rho).
}
\tag{9}
\]

In particular, `|A_Q|=o(pi(Q))` forces `r_Q log Q -> 0`.

There is also a direct information interpretation under the uniform distribution on primes up to `Q`. Put

\[
a_Q:=e^{-r_Q},
\qquad
\delta_Q:=\frac{\pi(Q^{a_Q})}{\pi(Q)}.
\tag{10}
\]

The endpoint clique consisting of primes in `(Q^{a_Q},Q]` has distinct marks. Therefore the mark alone identifies the prime with error probability at most `delta_Q`, and

\[
H(P_Q\mid \lambda_Q)
\le h(\delta_Q)+\delta_Q\log \pi(Q^{a_Q}).
\tag{11}
\]

When `r_Q log Q -> c<infinity`,

\[
\delta_Q\to e^{-c},
\tag{12}
\]

so

\[
\liminf_{Q\to\infty}
\frac{H(\lambda_Q)}{\log\pi(Q)}
\ge 1-e^{-c}.
\tag{13}
\]

When `r_Q log Q -> infinity`, `delta_Q->0` and consequently

\[
\frac{H(\lambda_Q)}{\log\pi(Q)}\to1.
\tag{14}
\]

Unlike the fixed-radius case of AF-225, `(14)` is generally a **relative** entropy statement. Arbitrarily slow divergence of `r_Q log Q` need not make the additive entropy deficit `o(1)`.

## Derivation

### 1. Source windows are power intervals in the prime variable

Write

\[
v(p):=-\log\log p.
\tag{15}
\]

A source interval of length `r` corresponds, after reversing the monotone coordinate, to a prime interval with endpoints of the form

\[
[y^{e^{-r}},y].
\tag{16}
\]

Indeed, if the upper source endpoint corresponds to `y`, increasing the source coordinate by `r` multiplies `log y` by `e^{-r}`. Endpoint conventions can alter the prime count by at most one and are asymptotically irrelevant below.

For the cutoff `p<=Q`, every source `r`-window is therefore bounded by a count

\[
\pi(y)-\pi(y^{a})+O(1),
\qquad a=e^{-r},
\qquad y\le Q,
\tag{17}
\]

or, if the untruncated upper endpoint lies beyond `Q`, by the endpoint count

\[
\pi(Q)-\pi(Q^a)+O(1).
\tag{18}
\]

Conversely the endpoint interval `(Q^a,Q]` itself is a valid source clique of diameter at most `r`. Thus `(18)` is always a lower bound for `K_Q(r)` up to the harmless endpoint convention.

### 2. The endpoint clique gives the phase-law lower bound

Assume first that

\[
r_Q\log Q\to c<\infty.
\tag{19}
\]

Then `r_Q->0`, so

\[
a_Q=e^{-r_Q}\to1
\tag{20}
\]

and

\[
(1-a_Q)\log Q\to c.
\tag{21}
\]

The prime number theorem along both arguments gives

\[
\frac{\pi(Q^{a_Q})}{\pi(Q)}
\sim
\frac{Q^{a_Q}/(a_Q\log Q)}{Q/\log Q}
=
\frac{1}{a_Q}
\exp\!\bigl(-(1-a_Q)\log Q\bigr)
\longrightarrow e^{-c}.
\tag{22}
\]

Therefore the endpoint clique gives

\[
\liminf_{Q\to\infty}
\frac{K_Q(r_Q)}{\pi(Q)}
\ge1-e^{-c}.
\tag{23}
\]

If instead `r_Q log Q->infinity`, then

\[
D_Q:=(1-e^{-r_Q})\log Q\to\infty.
\tag{24}
\]

To see this, if `r_Q<=1` then `1-e^{-r_Q}>=r_Q/2`, while any subsequence with `r_Q>1` has `D_Q>=(1-e^{-1})\log Q`.

If `Q^{a_Q}` stays bounded along a subsequence, its prime count is immediately negligible compared with `pi(Q)`. Otherwise the PNT gives

\[
\frac{\pi(Q^{a_Q})}{\pi(Q)}
\sim a_Q^{-1}e^{-D_Q}.
\tag{25}
\]

This tends to zero. If `a_Q>=1/2`, this is immediate from `D_Q->infinity`; if `a_Q<1/2` and `Q^{a_Q}->infinity`, then `a_Q\log Q->infinity`, hence `a_Q^{-1}=O(\log Q)` while `D_Q>=(1/2)\log Q`, again forcing `(25)` to zero. Thus

\[
\frac{K_Q(r_Q)}{\pi(Q)}\to1
\tag{26}
\]

in the infinite-scale regime.

### 3. No interior source window beats the endpoint asymptotically

It remains to prove the matching upper bound when `c<infinity`. For each `Q`, choose a source window attaining `M_{S_Q}(r_Q)`. If its untruncated prime upper endpoint exceeds `Q`, `(18)` already gives the required upper asymptotic. Otherwise write that endpoint as `y_Q<=Q`.

Consider an arbitrary subsequence. Passing to a further subsequence if needed, either `y_Q/Q->0` or

\[
\frac{y_Q}{Q}\to\lambda\in(0,1].
\tag{27}
\]

If `y_Q/Q->0`, then

\[
\frac{\pi(y_Q)}{\pi(Q)}\to0.
\tag{28}
\]

For example, when `y_Q<=Q^{1/2}` this follows directly from the PNT, while for `Q^{1/2}<y_Q=o(Q)` the PNT gives

\[
\frac{\pi(y_Q)}{\pi(Q)}
\sim
\frac{y_Q}{Q}\frac{\log Q}{\log y_Q}
\le (2+o(1))\frac{y_Q}{Q}
\to0.
\tag{29}
\]

Hence such a window has negligible normalized occupancy.

If `(27)` holds with `lambda>0`, then `log y_Q/log Q->1`. The PNT gives

\[
\frac{\pi(y_Q)}{\pi(Q)}\to\lambda,
\tag{30}
\]

while

\[
\frac{\pi(y_Q^{a_Q})}{\pi(y_Q)}
\sim
\frac{1}{a_Q}
\exp\!\bigl(-(1-a_Q)\log y_Q\bigr)
\longrightarrow e^{-c}.
\tag{31}
\]

Therefore

\[
\frac{\pi(y_Q)-\pi(y_Q^{a_Q})}{\pi(Q)}
\longrightarrow
\lambda(1-e^{-c})
\le1-e^{-c}.
\tag{32}
\]

Every subsequential maximizer obeys the same upper bound. Together with `(23)`, this proves `(6)` for finite `c`. The case `c=infinity` was already closed by `(26)`.

A useful point is that no short-interval prime theorem is required for `(6)`. When `c=0`, the local interval may indeed be much shorter than the scales on which the PNT gives an asymptotic prime count. The theorem asks only for its size **relative to all primes below `Q`**. The PNT is sufficient to show that this relative occupancy tends to zero.

### 4. Sublinear and near-full marking are exactly the two sides of the threshold

If `r_Q log Q->0`, equation `(6)` with `c=0` gives

\[
K_Q(r_Q)=o(\pi(Q)).
\tag{33}
\]

Conversely, suppose `K_Q(r_Q)=o(pi(Q))` but `r_Q log Q` does not tend to zero. There is then a subsequence bounded below by some positive constant. Passing again to a subsequence, `r_Q log Q` either converges to a finite positive `c` or diverges to infinity. Equation `(6)` would force the normalized coloring cost to converge respectively to `1-e^{-c}>0` or to `1`, a contradiction. This proves the first equivalence following `(6)`.

The same subsequence argument proves

\[
K_Q(r_Q)\sim\pi(Q)
\quad\Longleftrightarrow\quad
r_Q\log Q\to\infty.
\tag{34}
\]

Now suppose an actual proper marking uses at most `rho pi(Q)` marks as in `(8)`. If `(9)` failed, some subsequence would satisfy

\[
r_Q\log Q\to c> -\log(1-\rho)
\tag{35}
\]

or diverge to infinity. Equation `(6)` would then give

\[
\lim \frac{K_Q(r_Q)}{\pi(Q)}
=1-e^{-c}>\rho
\tag{36}
\]

(or `1`), contradicting `K_Q(r_Q)<=|A_Q|<=rho pi(Q)`. This proves `(9)`.

At the **graph-coloring level**, the threshold is sharp in both directions because AF-225 gives `K_Q=M_{S_Q}` and hence an optimal proper coloring with exactly `K_Q` marks. As already emphasized in AF-225, such a coloring need not lift to a valid analytic marked-translation representation. Equation `(6)` is therefore an exact combinatorial resource law and a necessary lower bound for the full representation, not an existence theorem for that representation.

### 5. The endpoint clique gives the entropy lower bound

Let `P_Q` be uniform on the `n_Q` primes at most `Q`, and let `lambda_Q` be any proper `r_Q`-proximity marking. The endpoint set

\[
C_Q:=\{p:Q^{a_Q}<p\le Q\}
\tag{37}
\]

is a clique, so the mark is injective on `C_Q`. Decode each mark used on `C_Q` to its unique clique prime and define the decoder arbitrarily elsewhere. Its error is at most

\[
\delta_Q=\frac{\pi(Q^{a_Q})}{\pi(Q)}.
\tag{38}
\]

Exactly as in AF-225,

\[
H(P_Q\mid\lambda_Q)
\le h(\delta_Q)+\delta_Q\log\pi(Q^{a_Q}).
\tag{39}
\]

Since `H(P_Q)=log pi(Q)` and the mark is deterministic,

\[
H(\lambda_Q)
\ge
\log\pi(Q)
-h(\delta_Q)
-\delta_Q\log\pi(Q^{a_Q}).
\tag{40}
\]

For finite `c`, `(22)` gives `delta_Q->e^{-c}` and `log pi(Q^{a_Q})/log pi(Q)->1`, proving `(13)`. If `c=infinity`, `delta_Q->0`, and dividing `(40)` by `log pi(Q)` proves `(14)`.

This is deliberately weaker than asserting an exact chromatic-entropy phase law. Minimum-entropy coloring is a separate classical optimization problem, and no equality claim is needed for the fidelity obstruction.

## Translation back to AF-224 fidelity resources

The radius `r_Q` is not an arbitrary coding parameter in AF-224. It is produced by the separation margin, sample continuity, approximation error, and inverse conditioning.

Suppose a cutoff family satisfies AF-224 with hidden source separation `c_{*,Q}>eta_Q`, where

\[
\eta_Q:=\max_a\omega_{a,Q}(2\varepsilon_Q),
\tag{41}
\]

and suppose the common sample coordinate has a local anchored Lipschitz bound

\[
\Omega_{0,Q}(r)\le L_Q r
\tag{42}
\]

on the required scale. Put

\[
\Delta_Q:=c_{*,Q}-\eta_Q>0.
\tag{43}
\]

Whenever `Delta_Q/(2L_Q)` lies inside that local scale, choose

\[
r_Q:=\frac{\Delta_Q}{2L_Q}.
\tag{44}
\]

Then

\[
\Omega_{0,Q}(r_Q)+\eta_Q
\le \frac{\Delta_Q}{2}+\eta_Q
<c_{*,Q},
\tag{45}
\]

so AF-224 forces a proper `r_Q`-proximity marking. Consequently, any marked repair with

\[
|A_Q|=o(\pi(Q))
\tag{46}
\]

must satisfy

\[
\boxed{
\frac{\Delta_Q\log Q}{L_Q}\to0.
}
\tag{47}
\]

This prices the growing-mark escape left open by AF-224/AF-225. A truly sublinear mark cannot coexist with a fixed positive separation/resolution margin and a uniformly controlled sample coordinate. At least one resource must deteriorate at the logarithmic scale: the inverse-resolution defect must approach the desired hidden separation, the sample-coordinate Lipschitz constant must grow faster than the available margin times `log Q`, or the representation must leave the shared-coordinate marked-translation category.

If the mark-specific decoders satisfy a common lower-Lipschitz estimate

\[
d_Z(F_{a,Q}(x),F_{a,Q}(y))
\ge \mu_Q\|x-y\|,
\tag{48}
\]

then AF-224 gives

\[
\eta_Q\le\frac{2\varepsilon_Q}{\mu_Q}.
\tag{49}
\]

Thus, whenever `c_{*,Q}>2\varepsilon_Q/\mu_Q`, the conservative radius

\[
\widetilde r_Q
:=
\frac{c_{*,Q}-2\varepsilon_Q/\mu_Q}{2L_Q}
\tag{50}
\]

also triggers the proximity obstruction. Sublinear marking therefore requires

\[
\boxed{
\frac{\bigl(c_{*,Q}-2\varepsilon_Q/\mu_Q\bigr)_+\log Q}{L_Q}
\to0
}
\tag{51}
\]

along every regime where the positive part lies in the declared local Lipschitz scale.

For fixed positive hidden separation and bounded `L_Q`, `(51)` says that a sublinear mark budget can survive only by driving the error/conditioning ratio to the AF-224 separation threshold at `O(1/log Q)` scale or worse. Conversely, if the error/conditioning margin stays uniformly positive and `L_Q=O(1)`, then `r_Q` stays bounded below and `(6)` forces asymptotically full mark cardinality.

## Exact controls and boundaries

### The theorem is exact for proximity coloring, not for the full marked representation

AF-225 proves that the one-dimensional proximity graph can be colored with exactly `K_Q=M_{S_Q}` marks. It does not construct the analytic maps `Phi`, `Psi`, or the marked decoders required by AF-224. Therefore the upper half of the phase law certifies the cheapest **combinatorial side-information resource**, not the existence of a faithful analytic lift at that cost.

### `1/log Q` is a threshold in the `-log log p` source coordinate

The result is coordinate- and category-specific. A different source coordinate or a mark-dependent sample geometry changes the confusability radius and requires a new audit. The theorem does not declare `1/log Q` to be a universal arithmetic scale.

### The PNT resolves the global mark fraction, not fine short-interval counts

At `r_Q log Q->0`, `(6)` states only that the maximal proximity clique is `o(pi(Q))`. It does not give its exact size. Determining a finer asymptotic for `K_Q(r_Q)` at very small radii can enter genuine short-interval prime-distribution territory and may require stronger arithmetic input.

### Entropy and alphabet size remain distinct resources

Equation `(6)` is an exact asymptotic for minimum alphabet cardinality. Equations `(13)--(14)` are lower bounds on entropy under the uniform prime cutoff, obtained from the endpoint clique. They do not identify the minimum-entropy coloring or prove an exact entropy phase curve.

### Source identity still is not rational-prime specificity

A costly mark can retain source identity without supplying an intrinsic arithmetic mechanism downstream. AF-226 only prices one proposed repair of prime-tail crowding. Any RH-relevant use must still show that the retained side information is canonical, survives the later compression, and distinguishes rational primes from matched controls at the destination category.

## Prior art and novelty assessment

The graph-theoretic and coding ingredients are classical. D. R. Fulkerson and O. A. Gross, **“Incidence Matrices and Interval Graphs,”** *Pacific Journal of Mathematics* **15**(3), 835--855 (1965), DOI `10.2140/pjm.1965.15.835`, is foundational interval-graph prior art. H. S. Witsenhausen, **“The Zero-Error Side Information Problem and Chromatic Numbers,”** *IEEE Transactions on Information Theory* **22**(5), 592--593 (1976), DOI `10.1109/TIT.1976.1055607`, is the classical zero-error coloring bridge. Noga Alon and Alon Orlitsky, **“Source Coding and Graph Entropies,”** *IEEE Transactions on Information Theory* **42**(5), 1329--1339 (1996), DOI `10.1109/18.532875`, supplies the established entropy/coding framework. Minimum-entropy coloring, including interval-graph complexity, is also a mature subject; see Jean Cardinal, Samuel Fiorini, and Gwenaël Joret, **“Minimum Entropy Coloring,”** *Journal of Combinatorial Optimization* **16**(4), 361--377 (2008), DOI `10.1007/s10878-008-9152-2`.

The arithmetic input in `(22)`, `(30)`, and `(31)` is only the classical prime number theorem `pi(x)~x/log x`. No short-interval theorem, RH consequence, or prime-gap conjecture is used.

A targeted prior-art search found the classical interval-graph, zero-error side-information, graph-entropy, and prime-distribution ingredients, but did not locate a source treating the exact moving-radius coloring problem for the transformed rational-prime source `-log log p` or the phase curve `(6)`. **No novelty claim is made from that absence.** The durable Arithmetic Fidelity result is the explicit category-specific synthesis: AF-224's geometric exclusion radius, when evaluated on the rational-prime log-log source, has a precise cardinality transition controlled by `r_Q log Q`, which in turn converts representation margin/conditioning into a quantitative side-information cost.

## Consequence for the research line

AF-225 left shrinking source resolution as the principal escape from its fixed-radius near-full-identity theorem. AF-226 closes that escape at the level needed to price mark cardinality: sublinear side information is possible combinatorially only after the AF-224 exclusion radius falls below the `1/log Q` scale, while any larger scale retains a positive or asymptotically full fraction of source identity.

The remaining translation-category exits are therefore sharper. A proposed repair must now exhibit an explicit favorable law for `Delta_Q/L_Q`, accept a corresponding loss of decoder conditioning/error, make the sample geometry mark dependent, or leave the translation-difference category. Simply allowing the mark alphabet to grow no longer avoids a quantitative accounting of how much of the prime source it carries.